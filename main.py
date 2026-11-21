from pathlib import Path


POEM = (
    "You pick the stairs. I'll take the low end.\n"
    "If either says down, down it goes.\n"
    "\n"
    "Halfway up you say down so softly\n"
    "I could have kept climbing.\n"
    "\n"
    "I bend. The glass ticks against stone.\n"
    "Through it I watch your thumb\n"
    "uncurl, then go pink again."
)


def main() -> None:
    target = Path("/output/entry.txt")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(POEM, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
