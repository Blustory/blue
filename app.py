from flask import Flask, redirect, render_template, url_for

app = Flask(__name__, template_folder="templates")


@app.route("/")
def home():
    name = "Blustory"
    height = 185
    skills = [
        "basketball",
        "coding",
        "reading",
        "minecraft",
        "gaming",
        "football",
        "swimming",
        "tennis",
        "volleyball",
    ]
    return render_template("index.html", name=name, height=height, skills=skills)


@app.route("/another")
def another():
    r_text = "This is another page"
    return render_template("another.html", r_text=r_text)


@app.route("/something")
def something():
    return redirect(url_for("home"))


@app.template_filter("mixup")
def mixup(s):
    return s[::-1]


@app.template_filter("add_67")
def add_67(s):
    return 67


if __name__ == "__main__":
    app.run(port=2323, debug=True, host="0.0.0.0")
