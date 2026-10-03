"""Log Rotate Local — Rotate a log file by size and keep N dated copies."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='log_rotate_local',
        description='Rotate a log file by size and keep N dated copies.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Log Rotate Local')
    print("Poor-man's logrotate for a Windows service log.")
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
