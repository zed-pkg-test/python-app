"""Both dependencies are installed by Zed into the project-local vendor tree."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

from polyglot_lib import greet


def main() -> int:
    message = greet("python-app")
    print(message)
    if message != "hello python-app from polyglot-lib/python":
        print("FAIL: Python polyglot slice did not resolve", file=sys.stderr)
        return 1

    schema_path = os.environ.get("ZED_SHARED_SCHEMA_PATH")
    if not schema_path:
        print("FAIL: ZED_SHARED_SCHEMA_PATH is required", file=sys.stderr)
        return 1
    schema = json.loads(Path(schema_path).read_text(encoding="utf-8"))
    if schema.get("title") != "JobEnvelope":
        print("FAIL: shared schema package did not resolve", file=sys.stderr)
        return 1

    print("OK: both Zed source packages resolved")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
