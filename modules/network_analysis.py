#!/usr/bin/env python3
import psutil

def list_open_ports():
    """List open network ports"""
    for conn in psutil.net_connections(kind="inet"):
        if conn.status == "LISTEN":
            print(f"Port {conn.laddr.port} is open on {conn.laddr.ip}")

if __name__ == "__main__":
    list_open_ports();
