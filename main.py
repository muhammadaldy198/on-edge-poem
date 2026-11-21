from pathlib import Path


POEM = (
    "You pick the stairs. I'll take the low end.\n"
    "We agree: either of us can call down.\n"
    "\n"
    "Halfway up, you say:\n"
    "Down.\n"
    "We set the pane on edge.\n"
    "Through the glass I watch your thumb\n"
    "uncurl, then go pink again."
)


def main() -> None:
    target = Path("/output/entry.txt")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(POEM, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
