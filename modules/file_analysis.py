#!/usr/bin/env python3
import os
import hashlib

def list_hidden_files(directory="."):
    """List hidden files in a directory"""
    hidden_files = [f for f in os.listdir(directory) if f.startswith('.')]
    return hidden_files

def compute_file_hash(file_path, algorithm="sha256"):
    """Compute hash of a file using SHA256"""
    hasher = hashlib.new(algorithm)
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()

if __name__ == "__main__":
    print("Hidden files:", list_hidden_files())
