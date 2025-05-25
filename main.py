from cli import CLI

def show_progress(data):
    """Display progress with visual bar."""
    filled = int(data["percentage"] / 10)
    progress_bar = "💧" * filled + "⬜" * (10 - filled)
    
    print(f"\n📊 Progress: {data['percentage']:.1f}%")
    print(f"Progress: [{progress_bar}]")
    print(f"Total: {data['total']}ml / {data['goal']}ml")

def show_summary(data):
    """Display today's summary."""
    print("\n📝 Today's Summary")
    print(f"Total Intake: {data['total']}ml")
    print(f"Daily Goal: {data['goal']}ml")
    print(f"Progress: {data['percentage']:.1f}%")
    print(f"Goal Status: {'✅ Achieved!' if data['total'] >= data['goal'] else '❌ Not yet'}")

def show_weekly_summary(data):
    """Display weekly summary."""
    if not data:
        print("No weekly data available yet.")
        return
        
    print("\n📅 Weekly Summary")
    for date, total in data["daily_totals"]:
        print(f"{date}: {total}ml")
    print(f"\nAverage daily intake: {data['average']:.1f}ml")

def main():
    cli = CLI()
    
    print("🚀 Welcome to Quenchr - Your Personal Hydration Assistant!")
    print("Type 'help' for available commands")
    
    while True:
        command = input("\nEnter command: ").strip().lower()
        success, result = cli.handle_command(command)
        
        if not success:
            if result == "exit":
                print("👋 Thank you for using Quenchr!")
                break
            print(f"❌ {result}")
            continue
            
        if command == "help":
            print(result)
        elif command == "progress":
            show_progress(result)
        elif command == "summary":
            show_summary(result)
        elif command == "weekly":
            show_weekly_summary(result)
        elif command.startswith("log "):
            print(f"✅ {result}")
            show_progress(cli.tracker.get_progress())
        elif command.startswith("goal "):
            print(f"✅ {result}")
        elif command == "reset":
            print(f"✅ {result}")
            show_progress(cli.tracker.get_progress())

if __name__ == "__main__":
    main() 