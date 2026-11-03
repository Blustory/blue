from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """<h1 style = "color:red;">Welcome home</h1>"""


@app.route("/contact:<name>")
def contact(name):
    return f"Hello {name} contact us at <i>Blustory.g@gmail.com</i>"


@app.route("/about")
def about():
    return """<b style = "color:red;">We Sell drugs</b>"""


@app.route("/products")
def products():
    return """<ul>
    <li>Lean</li>
    <li>Cocaine</li>
    <li>Juana</li>
    <li>Weed</li>
    </ul"""


if __name__ == "__main__":
    app.run(port=2323, debug=False, host="0.0.0.0")
