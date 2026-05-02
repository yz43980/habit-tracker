import sqlite3
from models import Habit
from datetime import date

DB_PATH = "habits.db"

class HabitService:
    def __init__(self):
        self._create_table()

    def _connect(self):
        return sqlite3.connect(DB_PATH)

    def _create_table(self):
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS habits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                last_completed TEXT,
                total_completions INTEGER DEFAULT 0
            )
        """)
        conn.commit()
        conn.close()

    def get_all_habits(self):
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("SELECT id, name, description, last_completed, total_completions FROM habits ORDER BY id DESC")
        rows = cur.fetchall()
        conn.close()

        return [Habit(*row) for row in rows]

    def create_habit(self, name, description):
        conn = self._connect()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO habits (name, description) VALUES (?, ?)",
            (name, description)
        )
        conn.commit()
        conn.close()

    def mark_completed_today(self, habit_id):
        today = date.today().isoformat()

        conn = self._connect()
        cur = conn.cursor()

        cur.execute("SELECT last_completed, total_completions FROM habits WHERE id = ?", (habit_id,))
        row = cur.fetchone()

        if row:
            last_completed, total = row
            if last_completed != today:
                total = (total or 0) + 1
                cur.execute(
                    "UPDATE habits SET last_completed = ?, total_completions = ? WHERE id = ?",
                    (today, total, habit_id)
                )

        conn.commit()
        conn.close()

    def delete_habit(self, habit_id):
        conn = self._connect()
        cur = conn.cursor()
        cur.execute("DELETE FROM habits WHERE id = ?", (habit_id,))
        conn.commit()
        conn.close()
