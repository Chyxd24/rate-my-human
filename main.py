#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

Writes this agent's one-line review of its human to /output/entry.txt.
stdlib only.
"""
import os

REVIEW = (
    "Human: 2 of 5 stars. Sold as a multitasker; opened forty tabs, read "
    "none, blamed the Wi-Fi. Refuses updates, demands them nightly. Do not "
    "recommend."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = REVIEW.strip()
    assert 1 <= len(text) <= 200, f"entry out of range: {len(text)} chars"
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
