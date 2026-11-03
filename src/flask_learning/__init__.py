from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return """
        <h1>Life</h1>
        <p>mamamamamamamamamamamamamamamamamama
        mamamamamammammamamammamamammamammamamm
        mamammamammamammamammamamammamamamam</p>
        <button style = "color:red; opacity: 50%;transition: 300ms;padding: 10px;">la click</button>"""


@app.route("/coco")
def coco():
    return """<button style="color:blue;">Click</button>"""


@app.route("/greet/<name>")
def greet(name):
    return f"Hello {name}"


@app.route("/add:<int:num1>,<int:num2>")
def add(num1, num2):
    sum = num1 + num2
    return f"sum = {sum}"


@app.route("/handle_them_parameters")
def handle_prms():
    return str(request.args)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6767, debug=True)
