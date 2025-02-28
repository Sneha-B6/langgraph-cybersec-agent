import datetime
import os

class Logger:
    def __init__(self, log_file="logs.txt"):
        self.log_file = log_file

        # Ensure the log file exists
        if not os.path.exists(self.log_file):
            with open(self.log_file, "w") as f:
                f.write("Log file created.\n")

    def log(self, message):
        """Logs a message with a timestamp."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        print(log_entry)

        with open(self.log_file, "a") as f:
            f.write(log_entry + "\n")

def generate_report():
    """Reads logs and returns the report."""
    try:
        with open("logs.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        return "No logs available."
