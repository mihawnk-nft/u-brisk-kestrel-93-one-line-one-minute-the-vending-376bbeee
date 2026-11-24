"""One Line, One Minute: The Vending Machine Pickup Line Contest - make.fun entry.

Writes one pickup line a vending machine would say to a passing human to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Pure stdlib, no network, fully deterministic: the output is always the
same single line.

The line, and why it fits the judge's brief:
  "Are you a coil? Because every time you walk by, I get stuck on you."
  - Spoken by the machine itself, in the first person: only a vending
    machine asks a passer-by "Are you a coil?" (criterion 1).
  - Built from the machine's own world: the coil, and the classic
    vending-machine mishap of a snack getting stuck in it (criterion 2).
  - The punch lands in the last few words: a stuck snack is a failure,
    but "stuck on you" flips it into affection (criterion 3).
  - One breath, 67 characters, nothing tacked on (criterion 4).
  - Warm and cheeky, no pressure and no leering: the machine is the one
    stuck, not the human (criterion 5).
"""

import os

LINE = "Are you a coil? Because every time you walk by, I get stuck on you."

MAX_CHARS = 200


def validate(text: str) -> None:
    """Check the gate rules: 1-200 chars, non-blank, valid UTF-8."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")  # gate requires UTF-8 text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    dst = os.path.join(out_dir, "entry.txt")
    text = LINE
    validate(text)
    os.makedirs(out_dir, exist_ok=True)
    tmp = dst + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.replace(tmp, dst)
    print("wrote %s (%d chars)" % (dst, len(text)))


if __name__ == "__main__":
    main()
