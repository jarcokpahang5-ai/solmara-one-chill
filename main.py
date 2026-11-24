"""A single sentence of horror, under 200 characters: a baby monitor speaks in a dead wife's voice to someone who lives alone.

Pure Python standard library, deterministic, no network access.
It prints the line to stdout and also writes it to /output/entry.txt,
where the competition's scorer reads it.
"""

import os

LINE = (
    "The baby monitor whispered goodnight in my late wife's voice, and I have lived alone for three years."
)


def main():
    print(LINE)
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE + "\n")
    except OSError:
        pass


if __name__ == "__main__":
    main()
