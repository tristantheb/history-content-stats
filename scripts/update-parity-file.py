#!/usr/bin/env python3
"""
Update parity file with new lines from en-us or removed lines.
Usage: python scripts/update-parity-file.py
"""
DEFAULT_HISTORY_PATH = "history/logs-en-us.csv"
DEFAULT_PARITY_PATH = "statistics/parity-{}.csv"
SECONDARY_LOCALES = ["de", "es", "fr", "ja", "pt-br", "ko", "ru", "zh-cn", "zh-tw"]


def main() -> None:
  with open(DEFAULT_HISTORY_PATH, "r", encoding="utf-8") as file:
    history_data = file.read()

  history_lines = history_data.splitlines()[1:]
  history_paths: list[str] = []
  for history_line in history_lines:
    parts = history_line.split(",", 1)
    history_paths.append(parts[0])

  for locale in SECONDARY_LOCALES:
    parity_path = DEFAULT_PARITY_PATH.format(locale)
    with open(parity_path, "r+", encoding="utf-8") as file:
      file.readline()
      body_offset = file.tell()
      parity_body = file.read()
      parity_lines = parity_body.splitlines()

      parity_map: dict[str, str] = {}
      for parity_line in parity_lines:
        parts = parity_line.split(",", 1)
        path = parts[0]
        parity = ""
        if len(parts) > 1:
          parity = parts[1]
        if path not in parity_map:
          parity_map[path] = parity

      file.seek(body_offset)
      for path in history_paths:
        parity = "null"
        if path in parity_map:
          parity = parity_map[path]
        file.write(path + "," + parity + "\n")
      file.truncate()

    print(f"::notice::Parity file for locale {locale} has been updated.")
  exit(0)


if __name__ == "__main__":
  raise SystemExit(main())
