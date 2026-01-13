from flask import Flask, jsonify
app = Flask(__name__)
@app.route("/orders")
def orders():
    return jsonify({"service": "Order"})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)