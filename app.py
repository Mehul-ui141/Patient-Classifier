from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    features = np.array([[
        data["temp"],
        data["oxygen"],
        data["bp"],
        data["comfort"]
    ]])

    result = model.predict(features)[0]

    return jsonify({"prediction": int(result)})

if __name__ == "__main__":
    app.run(debug=True)