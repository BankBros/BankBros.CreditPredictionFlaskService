# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 18:51:07 2019

@author: UE
"""
import pickle
from flask import Flask, request, render_template

app = Flask(__name__)
myModel = pickle.load(open('myModel.pkl','rb'))

@app.route('/')
def index():
    return render_template('input.html') 

@app.route('/result', methods=['GET', 'POST'])
def creditPrediction():
    if request.method == 'POST':
        creditAmount = request.form['creditAmount']
        personAge = request.form['age']
        personHome = request.form['home']
        personCreditCount = request.form['creditCount']
        personPhone = request.form['phone']
        
        predict = myModel.predict([[float(creditAmount),
                                    float(personAge),
                                    float(personHome),
                                    float(personCreditCount),
                                    float(personPhone),]])
        creditResult = predict[0]
        if(creditResult>=1):
            creditState = "Kredi verilebilir."
        else:
            creditState = "Kredi verilemez."
        
        return render_template("result.html",creditState = creditState)
    else:
        return render_template('input.html')

if __name__ == '__main__':
    try:
        app.run(debug=False, port=8080)
        print("Sunucu aktif!")
    except:
        print("Sunucu hatası!")