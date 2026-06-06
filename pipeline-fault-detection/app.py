import joblib
import streamlit as st
import pandas as pd
import os

base_path = os.path.dirname(__file__)
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
st.title("Pipeline Fault Prediction")

segment_id = st.number_input("Segment ID", value=50.00)
pressure = st.number_input("Pressure", value=116.00)
flow_rate = st.number_input("flow_rate", value=8.00)
temperature = st.number_input("Temperature", value=39.00)
valve_status = st.number_input("Valve Status", value=2.00)
pump_state = st.number_input("Pump State", value=1.00)
pump_speed = st.number_input("Pump Speed", value=1680.00)
compressor_state = st.number_input("Compressor State", value=1.00)
energy_consumption = st.number_input("Energy Consumption", value=59.00)
pressure_flow_rate = st.number_input("Pressure Flow Rate", value=96.00)
high_energy_low_flow = st.number_input("High Energy Low Flow", value=1.00)

if st.button("Predict"):
  input_data = pd.DataFrame([[segment_id, pressure, flow_rate, temperature, valve_status, pump_state, pump_speed, compressor_state, energy_consumption, pressure_flow_rate, high_energy_low_flow]])
  input_scaled = scaler.transform(input_data)
  prediction = model.predict(input_scaled)

  if prediction[0] == 0:
    st.success("Normal - This pipeline segment is operating normally.")
  else:
    st.error("Fault Detected - This pipeline segment is faulty.")
    st.error("Fault Detected - This pipeline segment is faulty.")
    
