import sys
import os
from datetime import datetime

LOG_FILE = "logs.txt"

class Logger:
    def __init__(self):
        self.terminal = sys.__stdout__
        self.file = open(LOG_FILE, "a", encoding="utf-8")

    def write(self, message):
        self.terminal.write(message)
        self.file.write(message)
        self.file.flush()

    def flush(self):
        self.terminal.flush()
        self.file.flush()

def start_log():
    now = datetime.now()

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write("\n" + "=" * 80 + "\n")
        f.write(f"DATE       : {now:%Y-%m-%d}\n")
        f.write(f"TIME       : {now:%H:%M:%S}\n")
        f.write(f"PYTHON FILE: {os.path.basename(sys.argv[0])}\n")
        f.write("=" * 80 + "\n\n")

sys.stdout = Logger()
sys.stderr = sys.stdout

start_log()