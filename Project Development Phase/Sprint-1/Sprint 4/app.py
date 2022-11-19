import flask
from flask import render_template, request
from flask_cors import CORS
import joblib
import pickle
app= flask.Flask(__name__,static_url_path='')
cors(app)

@app.route('/',methods=['GET'])
def sendHomePage():
  return render_template("index.html")

@app.route('/Predict',methods = ['POST'])
def PredictQuality():
  temperature=float(request.form['temperature'])
  do=float(request.form['do'])
  ph=float(request.form['ph'])
  conductivity=float(request.form['co'])
  bod=float(request.form['bod'])
  tc=float(request.form['tc'])
  ni=float(request.form['ni'])
  fec_col=float(request,form['fec'])
  tot_col=float(request.form['tot'])
  x=[[temperature,do,ph,conductivity,bod,ni,fec_col,tot_col]]
  print(x)