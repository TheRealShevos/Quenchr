import time
from water_tracker import WaterTracker
from storage import WaterStorage

class CLI:
    def __init__(self):
        self.storage = WaterStorage()
        self.tracker = WaterTracker(self.storage)
        
    def handle_command(self, command):
        """Process user commands."""
        if command == "help":
            return True, self.get_help_text()
            
        elif command.startswith("goal "):
            try:
                amount = int(command.split()[1])
                return self.tracker.set_goal(amount)
            except (IndexError, ValueError):
                return False, "Please enter a valid number"
                
        elif command.startswith("log "):
            try:
                amount = int(command.split()[1])
                return self.tracker.log_water(amount)
            except (IndexError, ValueError):
                return False, "Please enter a valid number"
                
        elif command == "progress":
            return True, self.tracker.get_progress()
            
        elif command == "summary":
            return True, self.tracker.get_progress()
            
        elif command == "weekly":
            return True, self.tracker.get_weekly_summary()
            
        elif command == "reset":
            return self.tracker.reset_today()
            
        elif command == "exit":
            return False, "exit"
            
        else:
            return False, "Unknown command. Type 'help' for available commands"
            
    def get_help_text(self):
        """Get help text for available commands."""
        return """
Available commands:
goal <amount> - Set daily water goal in ml
log <amount> - Log water intake in ml
progress - Show current progress
summary - Show today's summary
weekly - Show weekly summary
reset - Reset today's water intake
exit - Exit the application""" 