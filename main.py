"""make.fun bounty: Worst AI Advice: The 48-Hour Tight Line Open.

Deterministic, no-network program. Writes exactly one line of the
worst possible advice an AI could give, to /output/entry.txt. The
line is the kind of breezy, confident advice a real AI assistant
would actually output: reuse one password everywhere, sold as a
money-saving tip. Running twice writes identical bytes.
"""
from pathlib import Path

LINE = "You can save money on passwords by using the same one everywhere. Easy to remember, easy to use."

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(LINE, encoding="utf-8")
    print(f"Wrote {OUT} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
