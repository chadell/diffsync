#!/usr/bin/env python
"""Main executable for DiffSync "example2"."""
import sys
import argparse
import pprint

from diffsync import Diff
from diffsync.logging import enable_console_logging

from local_adapter import LocalAdapter
from nautobot_adapter import NautobotAdapter


def main():
    """Demonstrate DiffSync behavior using the example backends provided."""
    parser = argparse.ArgumentParser("example1")
    parser.add_argument("--verbosity", "-v", default=0, action="count")
    parser.add_argument("--diff", action="store_true")
    parser.add_argument("--sync", action="store_true")
    args = parser.parse_args()
    enable_console_logging(verbosity=args.verbosity)

    if not args.sync and not args.diff:
        sys.exit("please select --diff or --sync")

    print("Initializing and loading Local Data ...")
    local = LocalAdapter()
    local.load()
    # print(local.str())

    print("Initializing and loading Nautobot Data ...")
    nautobot = NautobotAdapter()
    nautobot.load()
    # print(nautobot.str())

    if args.diff:
        print("Calculating the Diff between the local adapter and Nautobot ...")
        diff = nautobot.diff_from(local)
        print(diff.str())

    elif args.sync:
        print("Updating the list of countries in Nautobot ...")
        nautobot.sync_from(local)


if __name__ == "__main__":
    main()