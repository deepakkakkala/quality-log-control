import json

def search_logs(log_file, filters):
  matches = []
  with open(log_file, "r") as f:
    for line in f:
      log_entry = json.loads(line.strip())
      match = True
      for key, value in filters.items():
        if getattr(log_entry, key) != value:
          match = False
          break
      if match:
        matches.append(log_entry)
  return matches

def main():
  # Parse user input (replace with actual CLI parsing)
  filters = {
      "level": "error",
  }

  # Search logs
  logs = search_logs("log1.log", filters)
  for log in logs:
    print(f"Level: {log['level']}, Message: {log['log_string']}, Source: {log['source']}")

if __name__ == "__main__":
  main()
