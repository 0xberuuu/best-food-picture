"""Copy the entry image to the output directory.

The entry image lives beside this program in the repository. The grader
runs this program twice and both runs must write identical bytes, so this
is a plain byte-for-byte copy with no randomness and no network access.
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    if not os.path.isfile(source):
        print("entry.png not found beside main.py", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    if os.path.getsize(target) != os.path.getsize(source):
        print("copied size does not match source", file=sys.stderr)
        return 1
    print("wrote %d bytes to %s" % (os.path.getsize(target), target))
    return 0


if __name__ == "__main__":
    sys.exit(main())
