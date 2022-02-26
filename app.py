import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
flask_app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))
modelparent = pickle.load(open("modelparent.pkl", "rb"))
modelteacher = pickle.load(open("modelteacher.pkl", "rb"))

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/teacher")
def Home01():
    return render_template("teacher.html")

@flask_app.route("/parent")
def Home02():
    return render_template("parent.html")   

@flask_app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    return render_template("prediction.html",data = prediction)

@flask_app.route("/predictparent", methods = ["POST"])
def predictparent():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = modelparent.predict(features)
    return render_template("prediction.html",data = prediction)

@flask_app.route("/predictteacher", methods = ["POST"])
def predictteacher():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = modelteacher.predict(features)
    return render_template("prediction.html",data = prediction)

if __name__ == "__main__":
    flask_app.run(debug=True)