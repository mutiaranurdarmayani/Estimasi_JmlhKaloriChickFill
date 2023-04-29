import pickle
import streamlit as sm

model = pickle.load(open('Estimasi_Jumlah Kalori Menu Chick-fil-A.sav', 'rb'))

sm.title('Estimasi Jumlah Kalori Menu Chick-fil-A')
sm.write('---')

Protein = sm.number_input('Input Protein(G)')
Fat = sm.number_input('Input Lemak(G)')
Cholesterol = sm.number_input('Input Cholesterol (MG)')
Carbohydrates = sm.number_input('Input Karbohidrat(G)')
Sugar = sm.number_input('Input Gula(G)')
Sodium = sm.number_input('Input Sodium(MG)')

predict = ''

if sm.button('Estimasi Kalori'):
    predict = model.predict(
        [[Protein,Fat,Cholesterol,Carbohydrates,Sugar,Sodium]]
    )
    sm.write ('Estimasi Jumlah Kalori Menu Chick-fil-A (kCal) :', predict)