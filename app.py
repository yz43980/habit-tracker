from flask import Flask, render_template, request, redirect, url_for
from services import HabitService

app = Flask(__name__)
habit_service = HabitService()

@app.route("/")
def index():
    habits = habit_service.get_all_habits()
    return render_template("index.html", habits=habits)

@app.route("/add", methods=["GET", "POST"])
def add_habit():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        description = request.form.get("description", "").strip()
        if name:
            habit_service.create_habit(name, description)
            return redirect(url_for("index"))
    return render_template("add_habit.html")

@app.route("/complete/<int:habit_id>", methods=["POST"])
def complete_habit(habit_id):
    habit_service.mark_completed_today(habit_id)
    return redirect(url_for("index"))

@app.route("/delete/<int:habit_id>", methods=["POST"])
def delete_habit(habit_id):
    habit_service.delete_habit(habit_id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
