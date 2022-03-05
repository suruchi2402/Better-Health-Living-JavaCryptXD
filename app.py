import numpy as np
import pymongo
import pickle
from flask import Flask,render_template,request, send_file

flask_app = Flask(__name__)
if __name__ == "__main__":
    print("welcome to pymongo !!")
client = pymongo.MongoClient("mongodb://localhost:27017/")
print(client)
db = client["login"]
collection = db["authentication"]

@flask_app.route("/signup" , methods=["POST"])
def register():
    user = request.form.get("Username")
    passwd = request.form.get("password")
    output=collection.find_one({"name": user})
    if output is None:
        collection.insert_one({"name": user, "password": passwd})
        print("Suruchi")
        return render_template("redirect.html") 
    else:
        print(output)
        return render_template("err.html")
        
                  


@flask_app.route("/login", methods=["POST"])
def addDB():
    user = request.form.get("Username")
    passwd = request.form.get("password")
    output=collection.find_one({"name": user})
    # print(output)
    if output['password']==passwd:
        return render_template("xyz.html")
    else:
        return render_template("err.html")




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

@flask_app.route("/home")
def Home03():
    return render_template("home.html")

@flask_app.route("/birth")
def Home04():
    return render_template("birth.html")


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

@flask_app.route('/download')
def download_file():
    p = "Book6.xlsm"
    return send_file(p, as_attachment=True)

if __name__ == "__main__":
    flask_app.run(debug=True)
# app.run(port=80,debug=True)