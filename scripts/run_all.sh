#!/bin/bash
echo "Running eyERED forensic analysis..."
python3 modules/file_analysis.py
python3 modules/memory_analysis.py
python3 modules/network_analysis.py
python3 modules/log_analysis.py

