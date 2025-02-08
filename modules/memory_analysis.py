#!/usr/bin/env python3
import psutil

def list_running_processes():
    """List running processes"""
    for process in psutil.process_iter(attrs=["pid", "name", "username"]):
        print(process.info)

if __name__ == "__main__":
    list_running_processes();

