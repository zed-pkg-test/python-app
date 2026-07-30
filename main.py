"""python_lib is sourced via zed (into .vendor/.zed, put on the import path by
the python adapter); everything else would come from pip."""

import sys

from python_lib import greet


def main() -> int:
    msg = greet("python-app")
    print(msg)
    if "from zed-pkg-test/python-lib" not in msg:
        print("FAIL: zed-sourced dependency did not resolve", file=sys.stderr)
        return 1
    print("OK: zed-sourced dep resolved alongside pip")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
