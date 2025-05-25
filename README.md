# Quenchr

A personal hydration tracking application that helps you maintain your daily water intake goals.

## Features

- Set daily water intake goals
- Log water consumption
- Track progress with visual indicators
- View daily and weekly summaries
- Reset daily tracking
- Persistent data storage

## Installation

1. Make sure you have Python 3.8 or higher installed
2. Install Poetry (if not already installed):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```
3. Clone this repository
4. Install dependencies:
   ```bash
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
   - `goal <amount>` - Set daily water goal in ml
   - `log <amount>` - Log water intake in ml
   - `progress` - Show current progress
   - `summary` - Show today's summary
   - `weekly` - Show weekly summary
   - `reset` - Reset today's water intake
   - `exit` - Exit the application

## Data Storage

Your water intake data is stored in `water_log.txt` in the following format:
```json
{"timestamp": "YYYY-MM-DDTHH:MM:SS", "amount": 200}
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details. 