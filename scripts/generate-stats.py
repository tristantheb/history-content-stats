#!/usr/bin/env python3
"""
Usage: python .github/scripts/generate-stats.py [locale]
"""
import time
import sys
from datetime import date

DEFAULT_ENGLISH_CSV = "history/logs-en-us.csv"
DEFAULT_LOCALE_CSV = "history/logs-{}.csv"
DEFAULT_OUT_FILE_TEMPLATE = "statistics/stats-{}.csv"


def _get_stats_from_locale(lang: str) -> str:
  # Getting the CSV content from locale and en-us from this repo
  try:
    with open(DEFAULT_ENGLISH_CSV, "r", encoding="utf-8") as en_f:
      en_data = en_f.read()
    with open(DEFAULT_LOCALE_CSV.format(lang), "r", encoding="utf-8") as loc_f:
      loc_data = loc_f.read()
  except Exception as e:
    print(f"::error::Failed to load CSV files: {e}")
    exit(1)

  # Getting path of Path,SourceCommit from en-us CSV
  paths: list[str] = []
  for line in en_data.splitlines()[1:]:
    parts = line.split(",")
    if len(parts) >= 2:
      paths.append(parts[0])

  # Compate data from en-us and locale to compare CommitHash of each path from Path,SourceCommit
  updated = 0
  outdated = 0
  untranslated = 0
  total = loc_data.splitlines()[1:].__len__()
  for path in paths:
    en_commit = next((line.split(",")[1] for line in en_data.splitlines()[1:] if line.split(",")[0] == path), None)
    loc_commit = next((line.split(",")[1] for line in loc_data.splitlines()[1:] if line.split(",")[0] == path), None)
    if loc_commit is None:
      untranslated += 1
    elif en_commit == loc_commit:
      updated += 1
    elif loc_commit == "no_hash_commit":
      outdated += 1
    else:
      outdated += 1

  # No commit,Has hash,File not translated,Total translated
  return f"{outdated},{updated},{untranslated},{total}"


def main(args: list[str]) -> None:
  # Log time
  start = time.time()

  if len(args) != 1:
    print("::error::Usage: generate-stats.py <locale>")
    exit(1)

  locale = args[0]
  stats = _get_stats_from_locale(locale)

  # Get date as YYYY-MM-DD
  date_str = date.today().strftime("%Y-%m-%d")

  # Add the stats to an existing CSV file
  out_file = DEFAULT_OUT_FILE_TEMPLATE.format(locale)
  try:
    with open(out_file, "a", encoding="utf-8") as f:
      f.write(f"{date_str},{stats}\n")
  except Exception as e:
    elapsed = time.time() - start
    print(f"::error::Failed after {elapsed:.2f} seconds, to write {e} !")
    exit(1)

  elapsed = time.time() - start
  print(f"::notice::Finished after {elapsed:.2f} seconds, logs-{locale}.csv is ready !")
  exit(0)


if __name__ == "__main__":
  raise SystemExit(main(sys.argv[1:]))
