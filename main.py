"""Best advice entry: write one sentence to /output/entry.txt.

The sentence is a single plain-spoken line, 142 characters: a named
person (my grandmother), a specific moment of advice, and a test that
holds far beyond that moment -- how someone treats the smallest chore
is how they will treat you.
"""

import os

SENTENCE = (
    "My grandmother told me to marry a man who does his own dishes, "
    "because the way someone treats the smallest chore is the way "
    "they'll treat you."
)


def main() -> None:
    # Gate: one sentence, 1-200 characters, as the competition requires.
    assert 1 <= len(SENTENCE) <= 200, len(SENTENCE)
    assert SENTENCE.count(".") == 1 and SENTENCE.endswith(".")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(SENTENCE)


if __name__ == "__main__":
    main()
