#!/usr/bin/env python3
"""
Update parity file with new lines from en-us or removed lines.
Usage: python scripts/update-parity-file.py
"""
DEFAULT_HISTORY_PATH = "history/logs-en-us.csv"
DEFAULT_PARITY_PATH = "statistics/parity-{}.csv"
SECONDARY_LOCALES = ["de", "es", "fr", "ja", "pt-br", "ko", "ru", "zh-cn", "zh-tw"]


def main() -> None:
  with open(DEFAULT_HISTORY_PATH, "r", encoding="utf-8") as f:
    history_data = f.read()
    history_lines = history_data.splitlines()[1:]
  for locale in SECONDARY_LOCALES:
    with open(DEFAULT_PARITY_PATH.format(locale), "r+", encoding="utf-8") as f:
      parity_lines = f.read().splitlines()
      parity_dict = {line.split(",")[0]: line.split(",")[1] for line in parity_lines[1:]}
      for line in history_lines:
        path_line = line.split(",")[0]
        if path_line not in parity_dict:
          parity_dict[path_line] = "null"

      f.seek(0)
      f.write(parity_lines[0] + "\n")
      for path, parity in parity_dict.items():
        f.write(f"{path},{parity}\n")

    print(f"::notice::Parity file for locale {locale} has been updated.")
    exit(0)


if __name__ == "__main__":
  raise SystemExit(main())
