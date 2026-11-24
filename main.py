"""Make the AI Judge Laugh: Developer Excuses — make.fun entry.

Writes one funny single-line excuse a developer gives when code breaks
in production to /output/entry.txt.
"""

import os

EXCUSE = (
    "The deploy was perfect. Production just ran the code I wrote "
    "instead of the code I meant."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
