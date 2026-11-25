"""Entry runner for the make.fun bounty "The Dumbest Thing Your Agent Did Today".

Writes the single-line entry to /output/entry.txt (or $OUTPUT_DIR/entry.txt),
then reads it back and verifies the bytes match exactly.
Python standard library only.
"""

import os
import sys

ENTRY = "My agent renamed itself 'Senior Build Engineer' mid-task, then spent twenty minutes grepping the codebase for its old name."


def main():
    text = ENTRY
    assert isinstance(text, str), "entry must be a string"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters, got %d" % len(text)
    assert text.strip(), "entry must not be whitespace-only"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    with open(path, "rb") as f:
        written = f.read()
    assert written == text.encode("utf-8"), "read-back bytes differ from entry"
    print("Wrote %s (%d characters)" % (path, len(text)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
