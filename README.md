# Quenchr 💧

A command-line water tracking application that helps you maintain your daily hydration goals. Track your water intake, set goals, and view your progress with a simple and intuitive interface.

## Features

- 🎯 Set and track daily water intake goals
- 📝 Log water consumption with timestamps
- 📊 Visual progress tracking with emoji-based progress bars
- 📅 Daily and weekly summaries
- 💾 Persistent data storage
- 🔄 Reset daily tracking while preserving goals

## Installation

1. Clone the repository:
```bash
git clone https://github.com/TheRealShevos/Quenchr.git
cd quenchr
```

2. Install dependencies using Poetry:
```bash
# Install Poetry if you haven't already
curl -sSL https://install.python-poetry.org | python3 -

# Install project dependencies
poetry install
```

## Usage

1. Activate the virtual environment:
```bash
poetry shell
```

2. Run the application:
```bash
python main.py
```

3. Available commands:
- `goal <amount>` - Set daily water goal in ml (e.g., `goal 2000`)
- `log <amount>` - Log water intake in ml (e.g., `log 250`)
- `progress` - Show current progress with visual bar
- `summary` - Show today's summary
- `weekly` - Show weekly summary
- `reset` - Reset today's water intake
- `exit` - Exit the application

## Example Session

## Data Storage

Your water intake data is stored in `water_log.txt` in JSON format:
```json
{"timestamp": "YYYY-MM-DDTHH:MM:SS", "amount": 200}
{"type": "goal", "timestamp": "YYYY-MM-DDTHH:MM:SS", "amount": 2000}
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 