import json
import logging
from datetime import datetime

class LogEntry:
  def __init__(self, level, log_string, timestamp, source):
    self.level = level
    self.log_string = log_string
    self.timestamp = timestamp
    self.source = source

def write_log(log_file, log_entry):
  try:
    with open(log_file, "a") as f:
      f.write(json.dumps(log_entry.__dict__) + "\n")
  except Exception as e:
    logging.error(f"Error writing log to {log_file}: {str(e)}")

def main():
  # Load configuration (replace with actual configuration loading logic)
  config = {
      "api1": {"log_file": "log1.log", "default_level": "info"},
      "api2": {"log_file": "log2.log", "default_level": "error"},
  }

  # Configure logging
  logging.basicConfig(filename="error.log", level=logging.ERROR)

  # Sample API calls (replace with actual API integration)
  log_entry1 = LogEntry("info", "Data processing successful.", datetime.utcnow().isoformat(), "api1")
  write_log(config["api1"]["log_file"], log_entry1)

  log_entry2 = LogEntry("error", "Failed to connect to database.", datetime.utcnow().isoformat(), "api2")
  write_log(config["api2"]["log_file"], log_entry2)

if __name__ == "__main__":
  main()