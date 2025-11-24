# src/main.py
from flask import Flask, request, jsonify

app = Flask(__name__)

def calculate(op, num1, num2):
    if op == "add":
        return num1 + num2
    elif op == "subtract":
        return num1 - num2
    elif op == "multiply":
        return num1 * num2
    elif op == "divide":
        if num2 == 0:
            return None
        return num1 / num2
    else:
        return None

@app.route("/calculate", methods=["GET"])
def calculate_route():
    op = request.args.get("op")
    try:
        num1 = float(request.args.get("num1"))
        num2 = float(request.args.get("num2"))
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid numbers"}), 400

    result = calculate(op, num1, num2)
    if result is None:
        return jsonify({"error": "Invalid operation or division by zero"}), 400
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
