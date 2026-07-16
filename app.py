from flask import Flask, render_template, request
from utils.predictor import predict_house_price

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict")
def predict():
    return render_template("predict.html")


@app.route("/result", methods=["POST"])
def result():

    predicted_price = predict_house_price(request.form)

    return render_template(
        "result.html",
        predicted_price=predicted_price
    )


if __name__ == "__main__":
    app.run(debug=True)