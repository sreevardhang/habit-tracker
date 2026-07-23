# Habit Tracker

A command-line habit tracking tool built in Python. Add habits, mark them 
complete, and track your consistency with automatic streak calculation — 
all data persists locally between sessions.

## Features

- Add and track multiple habits
- Mark habits as done for the day
- View all habits in a formatted table with completion counts and current streaks
- Automatic streak calculation (consecutive days, with gap detection)
- Data persists locally in JSON — no database setup required

## Example

```
Habit          Times Done  Streak      Last Done
--------------------------------------------------
Study          4           3           2026-07-18
Gym            6           5           2026-07-16
```

## How to run

1. Clone the repo:
   ```
   git clone https://github.com/sreevardhang/habit-tracker
   cd habit-tracker
   ```
2. Run it:
   ```
   python3 habit_tracker.py
   ```

## Commands

| Command | Format | Description |
|---|---|---|
| `add` | `add <habit>` | Add a new habit |
| `done` | `done <habit>` | Mark a habit complete for today |
| `list` | `list` | View all habits with stats |
| `exit` | `exit` | Save and quit |

## What I learned building this

- Working with Python data structures (lists, dicts) to model real state
- File I/O and persisting data with JSON
- Writing a command loop with input parsing and validation
- Implementing streak-tracking logic using `datetime` arithmetic and date comparisons
- Debugging state-related bugs (e.g. stale variables persisting across loop iterations)

## Possible future additions

- Web interface (HTML/CSS/JS)
- Switch from JSON to SQLite for storage
- Habit categories or reminders