
import pickle
import streamlit as st
import pandas as pd

#loading the trained model
pickle_in=open('regression_gold.pkl', 'rb')
regression=pickle.load(pickle_in)

st.title('Prediction of Gold Price')
st.write('Prediction can be done upto 30 days')

slider_val=st.sidebar.slider('Slide for number of days of forecasting', min_value=0, max_value=30)
st.write(f'You selected {slider_val}')

if st.button ('Prediction'):
    st.write(f'Prediction for {slider_val} days')
    forecast_model=regression.forecast(slider_val)
    
    forecast_df = pd.DataFrame(forecast_model**2)
    forecast_df.columns =['Gold_Price']
    forecast_df['Date']=pd.date_range(start='12/22/2021', periods=slider_val)
    second_column = forecast_df.pop('Date')
    forecast_df.insert(0, 'Date', second_column)
    st.write(forecast_df)
    
