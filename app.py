from flask import Flask, render_template, request, session, redirect
import os
import resend

# Config
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev-key")

resend.api_key = os.getenv("RESEND_API_KEY")

@app.route("/send-email", methods=["POST"])
def send_email():

    email = request.form["email"]

    branch = session.get("branch")

    if branch == "gift":

        message = f"""
🎁 Birthday Surprise Results

Preference: Gift
Gift Style: {session.get('gift_style')}
Motivation: {session.get('motivation')}
Category: {session.get('category')}
"""

    elif branch == "experience":

        message = f"""
🎁 Birthday Surprise Results

Preference: Experience
Experience Type: {session.get('experience_type')}
Who with: {session.get('who_with')}
"""

    else:
        message = "No results found."

    resend.Emails.send({
        "from": "Birthday Surprise Helper <onboarding@resend.dev>",
        "to": email,
        "subject": "Your Gift Quiz Results 🎁",
        "text": message
    })

    return redirect("/results")


#Welcome
@app.route("/")
def opening():
    return render_template("opening.html")

#Home
@app.route("/home")
def home():
    session.clear()
    return render_template("home.html")


#Branch selection

@app.route("/branch", methods=["POST"])
def branch():

    choice = request.form["choice"]
    session["branch"] = choice

    if choice ==  "gift":
        return redirect("/gift-q1")

    return redirect("/experience-q1")

#Gift Q1
@app.route("/gift-q1", methods=["GET", "POST"])
def gift_q1():

    if request.method == "POST":
        session["gift_style"] = request.form["gift_style"]
        return redirect("/gift-q2")

    return render_template("gift-q1.html")

#Gift Q2
@app.route("/gift-q2", methods=["GET", "POST"])
def gift_q2():

    if request.method == "POST":
        session["motivation"] = request.form["motivation"]
        return redirect("/gift-q3")

    return render_template("gift-q2.html")
#Gift Q3
@app.route("/gift-q3", methods=["GET", "POST"])
def gift_q3():

    if request.method == "POST":
        session["category"] = request.form["category"]
        return redirect("/gift-q4")

    return render_template("gift-q3.html")

#Gift Q4
@app.route("/gift-q4", methods=["GET", "POST"])
def gift_q4():

    if request.method == "POST":
        session["category"] = request.form["category"]
        return redirect("/results")

    return render_template("gift-q4.html")

# Experience Q1
@app.route("/experience-q1", methods=["GET", "POST"])
def experience_q1():

    if request.method == "POST":
        session["experience_type"] = request.form["experience_type"]
        return redirect("/experience-q2")

    return render_template("experience-q1.html")

# Experience Q2

@app.route("/experience-q2", methods=["GET", "POST"])
def experience_q2():

    if request.method == "POST":
        session["who_with"] = request.form["who_with"]
        return redirect("/experience-q3")

    return render_template("experience-q2.html")

@app.route("/experience-q3", methods=["GET", "POST"])
def experience_q3():

    if request.method == "POST":
        session["who_with"] = request.form["who_with"]
        return redirect("/results")

    return render_template("experience-q3.html")

# Results

@app.route("/results")
def results():

    profile = {}

    if session["branch"] == "gift":

        profile["preference"] = "Gift"

        profile["gift_style"] = (
            "One larger gift"
            if session["gift_style"] == "big"
            else "Multiple smaller gifts"
        )

        profile["motivation"] = session["motivation"].capitalize()
        profile["category"] = session["category"].capitalize()

    if session["branch"] == "experience":
        profile["preference"] = "Experience"

        profile["experience_type"] = session["experience_type"].capitalize()
        profile["who_with"] = session["who_with"].capitalize()

    return render_template(
        "results.html",
        profile=profile
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)



