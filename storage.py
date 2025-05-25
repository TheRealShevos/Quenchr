import json
import os
from datetime import datetime

class WaterStorage:
    def __init__(self, log_file="water_log.txt"):
        self.log_file = os.path.abspath(log_file)  # Get absolute path
        print(f"Log file path: {self.log_file}")  # Debug print
        # Create file if it doesn't exist
        if not os.path.exists(self.log_file):
            try:
                with open(self.log_file, 'w') as f:
                    pass
                print(f"Created new log file at {self.log_file}")  # Debug print
            except Exception as e:
                print(f"Error creating log file: {e}")  # Debug print
        
    def save_entry(self, entry):
        """Save a log entry to file."""
        try:
            print(f"Attempting to save entry: {entry}")  # Debug print
            with open(self.log_file, 'a') as f:
                f.write(json.dumps(entry) + "\n")
                f.flush()  # Force write to disk
            print(f"Successfully saved entry to {self.log_file}")  # Debug print
            return True
        except Exception as e:
            print(f"Error saving entry: {e}")  # Debug print
            return False
            
    def load_today_entries(self):
        """Load today's entries from file."""
        if not os.path.exists(self.log_file):
            print(f"Log file does not exist: {self.log_file}")  # Debug print
            return []
            
        today = datetime.now().date().isoformat()
        entries = []
        
        try:
            with open(self.log_file, 'r') as f:
                for line in f:
                    if not line.strip():
                        continue
                    data = json.loads(line)
                    if data["timestamp"].startswith(today):
                        entries.append(data)
            print(f"Loaded {len(entries)} entries for today")  # Debug print
        except Exception as e:
            print(f"Error loading entries: {e}")  # Debug print
            pass
            
        return entries
        
    def get_weekly_data(self):
        """Get water intake data for the last 7 days."""
        if not os.path.exists(self.log_file):
            return {}
            
        daily_totals = {}
        try:
            with open(self.log_file, 'r') as f:
                for line in f:
                    if not line.strip():
                        continue
                    data = json.loads(line)
                    date = data["timestamp"].split("T")[0]
                    daily_totals[date] = daily_totals.get(date, 0) + data["amount"]
        except Exception as e:
            print(f"Error getting weekly data: {e}")  # Debug print
            pass
            
        return daily_totals

    def reset_today_entries(self):
        """Reset today's entries in the file."""
        if not os.path.exists(self.log_file):
            return True
            
        today = datetime.now().date().isoformat()
        try:
            # Read all entries
            with open(self.log_file, 'r') as f:
                lines = f.readlines()
            
            # Write back all entries except today's
            with open(self.log_file, 'w') as f:
                for line in lines:
                    if not line.strip():
                        continue
                    data = json.loads(line)
                    if not data["timestamp"].startswith(today):
                        f.write(line)
                f.flush()  # Force write to disk
            print(f"Successfully reset today's entries")  # Debug print
            return True
        except Exception as e:
            print(f"Error resetting entries: {e}")  # Debug print
            return False

    def save_goal(self, goal):
        """Save the daily goal to file."""
        try:
            goal_entry = {
                "type": "goal",
                "timestamp": datetime.now().isoformat(),
                "amount": goal
            }
            print(f"Attempting to save goal: {goal_entry}")  # Debug print
            with open(self.log_file, 'a') as f:
                f.write(json.dumps(goal_entry) + "\n")
                f.flush()  # Force write to disk
            print(f"Successfully saved goal to {self.log_file}")  # Debug print
            return True
        except Exception as e:
            print(f"Error saving goal: {e}")  # Debug print
            return False

    def load_latest_goal(self):
        """Load the most recent goal from file."""
        if not os.path.exists(self.log_file):
            print(f"Log file does not exist, using default goal")  # Debug print
            return 2000  # Default goal
        
        try:
            with open(self.log_file, 'r') as f:
                lines = f.readlines()
            
            # Find the most recent goal entry
            for line in reversed(lines):
                if not line.strip():
                    continue
                data = json.loads(line)
                if data.get("type") == "goal":
                    print(f"Found goal: {data['amount']}")  # Debug print
                    return data["amount"]
            print("No goal found in file, using default")  # Debug print
        except Exception as e:
            print(f"Error loading goal: {e}")  # Debug print
            pass
        
        return 2000  # Default goal if no goal found 