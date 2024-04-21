from flask import Flask, request, render_template, jsonify

# Alternatively can use Django, FastAPI, or anything similar
from source_code.pipeline.prediction_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/predict", methods=["POST", "GET"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("form.html")
    else:
        data = CustomData(
            Airline=request.form.get("airline"),
            Flight=float(request.form.get("flight")),
            AirportFrom=request.form.get("airport_from"),
            AirportTo=request.form.get("airport_to"),
            DayOfWeek=float(request.form.get("day_of_week")),
            Time=float(request.form.get("time")),
            Length=float(request.form.get("length")),
        )
    new_data = data.get_data_as_dataframe()
    predict_pipeline = PredictPipeline()
    pred = predict_pipeline.predict(new_data)

    results = round(pred[0], 2)

    return render_template("results.html", final_result=results)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

# http://127.0.0.1:5000/ in browser
