# eyERED
eyERED is an open-source command-line tool for forensic analysis on Linux systems. Built with Python and Bash, it helps security analysts, incident responders, and forensic investigators detect anomalies and collect evidence efficiently.

Features:
File integrity checks (hidden files, recent changes, hash verification)

Process and memory analysis (running processes, memory dumps)

Network monitoring (open ports, active connections)

Log analysis (failed logins, system activity tracking)

Modular and extensible design for easy customization


Installation
1. Clone the Repository
git clone https://github.com/JEsegu/eyERED.git
cd eyERED

2. Install Dependencies
pip install -r requirements.txt

3. Make Scripts Executable
chmod +x scripts/run_all.sh
Usage
Run All Forensic Modules

To perform a full system analysis:
./scripts/run_all.sh

Run Individual Modules
File Analysis
Detect hidden files and compute file hashes
python3 modules/file_analysis.py

Memory Analysis
List running processes
python3 modules/memory_analysis.py

Network Analysis
Check open ports and active connections:
python3 modules/network_analysis.py

Log Analysis
Detect failed logins:
python3 modules/log_analysis.py

Example Output
Example of detecting hidden files:
Hidden files: ['.bash_history', '.ssh']
Example of detecting failed logins:
Failed password for root from 192.168.1.10 port 54544 ssh2


Contribution
We welcome contributions!

Fork the repository.
Create a new branch.
Commit changes and push.
Open a Pull Request (PR).
License
This project is licensed under the MIT License.

