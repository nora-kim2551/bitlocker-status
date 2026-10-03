"""BitLocker Status — Print BitLocker protection status per volume. It does not unlock or change keys."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='bitlocker_status',
        description='Print BitLocker protection status per volume. It does not unlock or change keys.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('BitLocker Status')
    print('Is this volume protected, as a table.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
