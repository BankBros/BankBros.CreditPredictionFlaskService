# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 18:51:07 2019

@author: UE
"""
import pickle
from flask import Flask, request, jsonify, render_template

class predictionDefault:
    def __init__(self,result):
        self.result = result;
    
    def serialie(self):
        return {'Değerlendirme Sonucu': self.result}

app = Flask(__name__)
myModel = pickle.load(open('myModel.pkl','rb'))
@app.route('/')
def index():
    #return '<h1>BankBros Krediler Anasayfası</h1>'
    return render_template('input.html') 

@app.route('/result', methods=['GET', 'POST'])
def creditPrediction():
    if(request.data != None):
        data = request.get_json()
        creditAmount = data['Amount']
        personAge = data['Age']
        personHome = data['HasHome']
        personCreditCount = data['UsedCredits']
        personPhone = data['HasPhone']
        
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
        
        return jsonify({"error":None, "data":{"Kredi başvuru sonucu:":creditState}})
    else:
        return jsonify({"error":"Bir hata meydana geldi.", "data":None})

if __name__ == '__main__':
    try:
        app.run(debug=False)
        print("Sunucu aktif!")
    except:
        print("Sunucu hatası!")