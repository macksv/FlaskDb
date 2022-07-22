""" This flask program simulates a simple database for storing Reminders """

from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from setup import app, db
#import models.models
from models.models import Reminder


#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///FlaskAppDB.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db = SQLAlchemy(app)


@app.route("/", methods=["GET", "POST"])
def index():
    #from models.models import Reminder
    if request.method == "POST":
        task_content = request.form["content"]
        new_task = Reminder(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except Exception:
            return "There was an issue adding your task"

    else:
        tasks = Reminder.query.order_by(
            Reminder.date_created).all()
        return render_template("index.html", tasks=tasks)


@app.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    #from models.models import Reminder
    task_to_delete = Reminder.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect("/")
    except Exception as e:
        return f"There was a problem deleting this task ! {e}"


@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    #from models.models import Reminder
    task_to_update = Reminder.query.get_or_404(id)

    if request.method == "POST":
        task_to_update.content = request.form["content"]

        try:
            # db.session.update(task_to_update)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            return f"There was an issue updating this task ! {e}"
    else:
        return render_template("update.html", task=task_to_update)


if __name__ == "__main__":
    #    app.run(debug=True)
    # Heroku will set the PORT env variable for web traffic
    port = os.environ.get("PORT", 5000)
    app.run(debug=False, host="0.0.0.0", port=port)
