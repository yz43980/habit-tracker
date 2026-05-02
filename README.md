# Simple Habit Tracker (Flask + SQLite)

A small web application to track daily habits.  
Users can:

- add new habits
- mark habits as completed for today
- view last completion date and total completions

# Running the application

## Clone the repository:
git clone https://github.com/yz43980/habit-tracker.git
cd habit-tracker

## Create and activate a virtual environment:
python -m venv venv
Windows:
venv\Scripts\activate
macOS/Linux:
source venv/bin/activate

## R un the application:
python app.py
Then, go to http://127.0.0.1:5000/ to view the app.
The SQLite database (habits.db) will be created automatically in the habit-tracker/ folder on first run.
