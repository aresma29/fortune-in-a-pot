"""Fortune in a Pot — print the fortune stored in entry.txt."""
from pathlib import Path


def main() -> int:
    # Resolve entry.txt relative to this script, not the working directory.
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    text = entry_path.read_text(encoding="utf-8").rstrip("\n")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
