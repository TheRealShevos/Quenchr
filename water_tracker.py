from datetime import datetime

class WaterTracker:
    def __init__(self, storage):
        self.storage = storage
        self.daily_goal = self.storage.load_latest_goal()  # Load saved goal
        self.today_logs = []
        self.load_today_logs()
        
    def set_goal(self, goal):
        """Set the daily water intake goal."""
        if goal <= 0:
            return False, "Goal must be greater than 0"
        self.daily_goal = goal
        if not self.storage.save_goal(goal):
            return False, "Error saving goal to file"
        return True, f"Daily goal set to {goal}ml"
        
    def log_water(self, amount):
        """Log water intake with timestamp."""
        if amount <= 0:
            return False, "Amount must be greater than 0"
            
        entry = {
            "timestamp": datetime.now().isoformat(),
            "amount": amount
        }
        self.today_logs.append(entry)
        
        if not self.storage.save_entry(entry):
            return False, "Error saving to log file"
            
        return True, "Water intake logged successfully"
        
    def get_progress(self):
        """Get current progress data."""
        total = sum(log["amount"] for log in self.today_logs)
        percentage = (total / self.daily_goal) * 100
        return {
            "total": total,
            "goal": self.daily_goal,
            "percentage": percentage
        }
        
    def get_weekly_summary(self):
        """Get weekly summary data."""
        daily_totals = self.storage.get_weekly_data()
        last_7_days = sorted(daily_totals.items(), reverse=True)[:7]
        
        if not last_7_days:
            return None
            
        avg = sum(total for _, total in last_7_days) / len(last_7_days)
        return {
            "daily_totals": last_7_days,
            "average": avg
        }
        
    def reset_today(self):
        """Reset today's water intake counter."""
        if not self.storage.reset_today_entries():
            return False, "Error resetting today's entries"
        self.today_logs = []
        return True, "Today's water intake has been reset"
        
    def load_today_logs(self):
        """Load today's logs from storage."""
        self.today_logs = self.storage.load_today_entries() 