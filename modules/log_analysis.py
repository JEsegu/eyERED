#!/usr/bin/env python3
import re

def check_failed_logins(log_file="/var/log/auth.log"):
    """Check for failed login attempts"""
    try:
        with open(log_file, "r") as f:
            for line in f:
                if "Failed password" in line:
                    print(line.strip())
    except FileNotFoundError:
        print("Log file not found. Try running as root.")

if __name__ == "__main__":
    check_failed_logins();

