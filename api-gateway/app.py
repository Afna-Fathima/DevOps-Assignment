from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "API Gateway running", "endpoints": ["/users", "/products", "/orders"]}

@app.route("/users")
def users():
    return requests.get("http://localhost:5001/users").text

@app.route("/products")
def products():
    return requests.get("http://localhost:5002/products").text

@app.route("/orders")
def orders():
    return requests.get("http://localhost:5003/orders").text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)