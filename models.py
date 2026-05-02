from datetime import date

class Habit:
    def __init__(self, id, name, description, last_completed, total_completions):
        self.id = id
        self.name = name
        self.description = description
        self.last_completed = last_completed
        self.total_completions = total_completions

    def mark_completed_today(self):
        today = date.today().isoformat()
        if self.last_completed != today:
            self.last_completed = today
            self.total_completions = (self.total_completions or 0) + 1
