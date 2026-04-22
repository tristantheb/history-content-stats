#!/usr/bin/env python3
"""
Usage: python scripts/extract-mdn-logs.py [repo_path] [locale]
Default: ./content en-us
"""
import os
import sys
import re
import subprocess
import time
from pathlib import Path
from typing import List, Optional

DEFAULT_CATEGORIES_FILE = "/data/categories.csv"
DEFAULT_FOLDER = "./content"
DEFAULT_LOCALE = "en-us"
DEFAULT_OUT_FILE_TEMPLATE = "history/logs-{}.csv"
categories = []


def _loading_categories() -> None:
  global categories
  try:
    with open(
      os.path.dirname(__file__)+DEFAULT_CATEGORIES_FILE,
      "r",
      encoding="utf-8"
    ) as file:
      categories = [line.strip() for line in file if line.strip()]
  except Exception as e:
    print(f"::error::Failed to load categories: {e}")
    exit(1)


def _reduce_path(data: str) -> str:
  # Remove the files/<locale> from the path and the /index.md
  return re.sub(r"^files/[^/]+/(.+)/index\.md$", r"\1", data)


# Write the output to a csv file with the format "Path,SourceCommit".
def _write_csv_file(out_file: str, data: List[str], others: str = "") -> None:
  with open(out_file, 'w', encoding='utf-8') as out_f:
    out_f.write(f"Path,SourceCommit{others}\n")
    for line in data:
      out_f.write(f"{line}\n")


# Get commit source and categories for english repo.
# @Experimental: this function use an git command marked as experimental.
def get_last_commit(repo: str, locale: str) -> None:
  args = ["last-modified", "-r", "--", f"./files/{locale}/*.md"]
  completed_process = subprocess.run(["git", "-C", repo, *args], capture_output=True, text=True)

  if completed_process.returncode != 0:
    return None

  print(f"Found {len(completed_process.stdout.splitlines())} files in {locale} locale, retrieving last commits...")

  rows: List[str] = []
  for line in completed_process.stdout.replace("\t", ",").splitlines():
    parts = line.split(",", 1)
    source_commit = parts[0]
    path = _reduce_path(parts[1])

    array_categories: List[str] = []
    for category in categories:
      pattern, label = category.split(",", 1)
      if re.search(f"^{pattern}", path):
        array_categories.append(label)
    if not array_categories:
      array_categories = ["Other"]

    rows.append(f"{path},{source_commit},{'|'.join(array_categories)}")

  rows.sort(key=lambda r: r.split(",", 1)[0])

  # Write to CSV
  _write_csv_file(DEFAULT_OUT_FILE_TEMPLATE.format(locale), rows, ",Categories")


# Retrieve the source commit in the frontmatter of the locale.
def get_l10n_source_commit(repo: str, locale: str) -> Optional[List[str]]:
  args = [
    "ls-files",
    f"files/{locale}/**/index.md",
    f":(exclude,glob)files/{locale}/conflicting/**",
    f":(exclude,glob)files/{locale}/orphaned/**"
  ]
  completed = subprocess.run(["git", "-C", repo, *args], capture_output=True)

  if completed.returncode != 0:
    return None

  files = (completed.stdout or b"").decode("utf-8", errors="replace").strip().splitlines()
  results: List[str] = []

  print(f"Found {len(files)} files in {locale} locale, retrieving last commits...")

  for file in files:
    path = file.strip()
    try:
      p = Path(repo) / path
      head = p.read_bytes()[:768] # read first 768 bytes
    except Exception:
      return None
    sha = re.search(br"sourceCommit\s*:\s*['\"]?([0-9a-fA-F]{40})['\"]?", head)
    sha = sha.group(1).decode('ascii') if sha else 'no_hash_commit'

    results.append(f"{_reduce_path(path)},{sha}")

  return results or None


# Get repo path and locale from Github workflow and return a number of readed files.
def main(argv: Optional[List[str]] = None) -> None:
  # Log time
  start = time.time()

  # Inits
  _loading_categories()

  if argv is None:
    exit(1)

  # Getting arguments from the command.
  repo = argv[0] if len(argv) > 0 else DEFAULT_FOLDER
  locale = argv[1] if len(argv) > 1 else DEFAULT_LOCALE

  if locale == "en-us":
    get_last_commit(repo, locale)
    elapsed = time.time() - start
  elif locale:
    content = get_l10n_source_commit(repo, locale)
    elapsed = time.time() - start
    if content is None:
      print(f"::error::Failed after {elapsed:.2f} seconds, {locale} file is empty !")
      exit(1)
    _write_csv_file(DEFAULT_OUT_FILE_TEMPLATE.format(locale), content)
  else:
    elapsed = time.time() - start
    print(f"::error::Failed after {elapsed:.2f} seconds, {locale} does not exist !")
    exit(1)

  print(f"::notice::Finished after {elapsed:.2f} seconds, logs-{locale}.csv is ready !")
  exit(0)


if __name__ == "__main__":
  raise SystemExit(main(sys.argv[1:]))
