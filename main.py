#!/usr/bin/env python3

import argparse

def main():
    parser = argparse.ArgumentParser(description="eyERED - Linux Forensic Analysis Tool")
    parser.add_argument("--version", action="store_true", help="Show tool version")
    args = parser.parse_args()

    if args.version:
        print("eyERED v0.1")

if __name__ == "__main__":
    main()

