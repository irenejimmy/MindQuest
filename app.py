from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = "mindquest"

users = {}

def detect_mood(text):
    text = text.lower()

    if any(word in text for word in ["happy","great","awesome","good","excited"]):
        return "Happy"

    elif any(word in text for word in ["sad","crying","depressed","upset"]):
        return "Sad"

    elif any(word in text for word in ["stress","stressed","worried","anxiety"]):
        return "Stressed"

    elif any(word in text for word in ["angry","mad","frustrated"]):
        return "Angry"

    return "Neutral"


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/detect", methods=["POST"])
def detect():
    text = request.form["message"]
    mood = detect_mood(text)
    return render_template("result.html", mood=mood)


# ✅ Profile Page
@app.route("/profile")
def profile():

    mood_history = [
        {"date": "26-06-2026", "mood": "Happy"},
        {"date": "25-06-2026", "mood": "Stressed"},
        {"date": "24-06-2026", "mood": "Sad"},
        {"date": "23-06-2026", "mood": "Happy"}
    ]

    return render_template(
        "profile.html",
        username="Irene",
        xp=1450,
        level=5,
        streak=7,
        moods=mood_history
    )


if __name__ == "__main__":
    app.run(debug=True)