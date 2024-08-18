import pickle
from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app=application

##Import logistic and standard scaler pickle
logistic_model=pickle.load(open('models/logistic.pkl','rb'))
standard_model=pickle.load(open('models/scaler.pkl','rb'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/data_analysis')
def data_analysis():
    return render_template('data_analysis.html')

@app.route('/predict',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='POST':
        ISI=float(request.form.get('ISI'))
        FFMC=float(request.form.get('FFMC'))
        
        new_scale_data=standard_model.transform([[ISI,FFMC]])
        result=logistic_model.predict(new_scale_data)

        return render_template('home.html',results=result[0])

    else:
        return render_template('home.html')
    
if __name__=="__main__":
    app.run(host="0.0.0.0")
