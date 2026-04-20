#!/usr/bin/env python3
"""
Analyze the sha parity between the translated file and the english file.
Usage: python scripts/check-parity.py [line_changed] [locale]
"""
import sys
import subprocess
from typing import List, Optional

DEFAULT_LOCALE_HISTORY_PATH = "history/logs-{}.csv"
DEFAULT_PARITY_PATH = "statistics/parity-{}.csv"
DEFAULT_GIT_PATH = "./files/en-us/"
DEFAULT_GIT_REPO = "./content"
PRIMARY_LOCALE = "en-us"
SECONDARY_LOCALES = ["de", "es", "fr", "ja", "pt-br", "ko", "ru", "zh-cn", "zh-tw"]


def _check_page_parity(path_line: str, locale: str|None = None) -> int|None:
  # Read locale file if we use english (locale set to search)
  loc_line = None
  if locale is not None:
    with open(DEFAULT_LOCALE_HISTORY_PATH.format(locale), "r", encoding="utf-8") as loc_f:
      loc_data = loc_f.read()
      loc_line = next((line for line in loc_data.splitlines()[1:] if line.startswith(path_line.split(",")[0] + ",")), None)
    if loc_line is None:
      print(f"::warning::No corresponding line found in locale {locale} for {path_line.split(',')[0]}.")
      return None

  splited_line = path_line.split(",")
  file_path = splited_line[0]
  # If we are in a locale file, the splited li contain the SHA of the locale.
  # Else, we have searched the locale.
  line_sha = splited_line[1] if locale is None \
    else loc_line.split(",")[1] if loc_line is not None \
    else None

  if line_sha is None or line_sha == "no_hash_commit":
    return None

  search_path = DEFAULT_GIT_PATH + file_path + "/index.md"
  args = ["rev-list", "--count", f"{line_sha}..HEAD", "--", search_path]
  completed_process = subprocess.run(["git", "-C", DEFAULT_GIT_REPO, *args], capture_output=True, text=True)

  if completed_process.returncode != 0:
    print(f"::error::Failed to execute git command: {completed_process.stderr.strip()}")
    exit(1)

  return int(completed_process.stdout.strip())


def _update_locale(line_changed: str, locale: str, parity_count: int|None) -> None:
  path_line = line_changed.split(",")[0]

  try:
    with open(DEFAULT_PARITY_PATH.format(locale), "r+") as f:
      lines = f.readlines()
      for i, line in enumerate(lines):
        if line.startswith(path_line + ","):
          lines[i] = f"{path_line},{parity_count if parity_count is not None else 'null'}\n"
          f.seek(0)
          f.writelines(lines)
          f.truncate()
          break
  except Exception as e:
    print(f"::error::Failed to update file with for {path_line} in locale {locale}: {e}")
    exit(1)


def main(args: Optional[List[str]] = None) -> None:
  if args is None:
    exit(1)

  # Setting up named args
  line_changed = args[0]
  locale = args[1]
  parity_count = None

  if (locale == PRIMARY_LOCALE):
    # When we are in the english file, we check parity for all locales.
    for sec_locale in SECONDARY_LOCALES:
      parity_count = _check_page_parity(line_changed, sec_locale)
      _update_locale(line_changed, sec_locale, parity_count)
  elif (locale in SECONDARY_LOCALES):
    # For a locale with a change, we only check it's parity.
    parity_count = _check_page_parity(line_changed)
    _update_locale(line_changed, locale, parity_count)
  else:
    print(f"::error::Locale {locale} is not supported.")
    exit(1)

  print(f"::notice::Checked parity for file: {line_changed.split(',')[0]} (locale: {locale}).")
  exit(0)


if __name__ == "__main__":
  raise SystemExit(main(sys.argv[1:]))
