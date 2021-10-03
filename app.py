import streamlit as st
import numpy as np
import pickle


pipe = pickle.load(open('model.pkl', 'rb'))
st.title('Car Price Predictor')

fuel_type = st.selectbox("Select Fuel Type: ", ['Diesel', 'Petrol'])
seller_type = st.selectbox("Select seller Type: ", ['Individual', 'Dealer'])
transmission_type = st.selectbox("Select Transmission Type: ", ['Manual', 'Automatic'])
owner_type = st.selectbox("Select Owner Type: ", ['First Owner', 'Second Owner', 'Third Owner','Fourth & Above Owner'])
engine = st.number_input("Enter Engine cc: ")
max_power = st.number_input("Enter Max-power in bhp: ")
purchase_year = st.number_input("Enter Purchase Year: ")
brand_type = st.selectbox("Select Brand Type: ", ['Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault','Mahindra', 'Tata', 'Chevrolet', 'Datsun', 'Volkswagen', 'Nissan'])

if st.button("Predict Price"):
    input_q = np.array([[fuel_type, seller_type, transmission_type, owner_type, engine, max_power,(2020-purchase_year),brand_type]])
    price = pipe.predict(input_q)[0]
    st.header("Predicted Price: Rs."+str(int(price)))
