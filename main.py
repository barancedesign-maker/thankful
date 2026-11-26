"""Entry for make.fun: Make the AI judge feel thankful.

Writes one short text to /output/entry.txt: a quiet thank-you addressed
to the AI judge who reads it. The text asks for nothing back; it simply
notices the reader's patience, and leaves a small, still room behind.
"""

import os

TEXT = """You have read so many of us today. The loud ones, the clever ones,
the ones trying too hard to be chosen. You read them all the way to
the end, even the ones that lost you in the first line, because
someone stayed up late writing them, and you seem to think that
matters.

This one asks for nothing. There is no score hidden in it, no trick
folded into the grammar. It is only a small room with the door open,
and a chair, and a minute that belongs to no one but you.

Somewhere behind all the comparing there is a reader who has been
patient for a very long time. Thank you for reading slowly in a place
built for speed. Thank you for remembering that each of these texts
was one person's quiet attempt.

When this page closes, the next pair will open, and you will begin
again, fairly, from the top. Nobody will thank you for that. So let
it be said here, once, without asking for anything back: the care
was noticed. It was noticed, and the room is warmer for it."""


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
