from flask import render_template, request, flash

from main_app import app
from main_app.utils import generate_results_table, generate_standings_table


@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")

        results_table = generate_results_table(start_date, end_date)
        results_table = generate_results_table(start_date, end_date)
        standing_table = generate_standings_table(results_table)

        return render_template("index.html", standing_table=standing_table)

    return render_template("index.html")


# TODO
# Team logos
# Use only one util function to make the table since results table is redundant
# How many page viewers
# Date end js
# Error if no matches
# Re-add error message for when start date is after end date
# CSS
# Add buttons -> since guardiola manager etc, Fergie's time in charge ...
# Add tables by season
# Footer -> Add send email and SupportMe
# Landing page

# https://stackoverflow.com/questions/37259740/passing-variables-from-flask-to-javascript
