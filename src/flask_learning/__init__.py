from flask import Flask, request, make_response, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return """
        <h1>Life</h1>
        <p>mamamamamamamamamamamamamamamamamama
        mamamamamammammamamammamamammamammamamm
        mamammamammamammamammamamammamamamam</p>
        <button style = "color:red; opacity: 50%;transition: 300ms;padding: 10px;">la click</button>"""


@app.route("/coco", methods=["GET", "POST", "PUT", "DELETE"])
def coco():
    return """<button style="color:blue;">Click</button>"""


@app.route("/greet/<name>")
def greet(name):
    response = make_response(f"Hello, {name}!")
    response.status_code = 237
    response.headers["My-Header"] = "Hello, World!"
    return response


@app.route("/add/<int:num1>/<int:num2>")
def add(num1, num2):
    sum = num1 + num2
    return f"sum = {sum}"


@app.route("/handle_them_parameters")
def handle_prms():
    if "name" in request.args.keys() and "age" in request.args.keys():
        name = request.args.get("name")
        age = request.args.get("age")
        return f"Hello {name}, you are {age} years old"
    else:
        return "Please provide name and age in the query parameters"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6767, debug=True)
