# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 18:05:45 2019

@author: UE
"""
import warnings
warnings.filterwarnings('ignore')

#Verisetinin alınması
import pandas as pd
df = pd.read_csv('krediVeriseti.csv', sep = ";")

#Veriseti üzerinde düzenlemeler
df.evDurumu[df.evDurumu == 'evsahibi'] = 1
df.evDurumu[df.evDurumu == 'kiraci'] = 0

df.telefonDurumu[df.telefonDurumu == 'var'] = 1
df.telefonDurumu[df.telefonDurumu == 'yok'] = 0

df.KrediDurumu[df.KrediDurumu == 'krediver'] = 1
df.KrediDurumu[df.KrediDurumu == 'verme'] = 0

df = df.astype(float)
df.head()
#Train-Test verilerinin seçilmesi
from sklearn.model_selection import train_test_split
X=df.drop('KrediDurumu',axis=1)
Y=df['KrediDurumu']
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.3,random_state=1)

#Eğitim gerçekleştirilmesi ve başarım
from sklearn.linear_model import LogisticRegression
log=LogisticRegression()
log.fit(x_train,y_train)

#Modelin uygulanması
test = log.predict([[45676,27,1,1,0]])
if(round(test[0])>=1):
    print("Kredi verilebilir")
else:
    print("Kredi verilemez")  

#Modelin kaydedilmesi
import pickle
pickle.dump(log, open('myModel.pkl','wb'))

