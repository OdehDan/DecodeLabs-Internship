# Pipeline Fault Detection System

A machine learning web app that predicts whether a pipeline segment is faulty or operating normally using real-time SCADA sensor data.

## Problem
Pipeline failures can cause explosions, environmental damage, and costly downtime. Early fault detection is critical.

## Solution
Trained a Random Forest classifier on SCADA pipeline sensor data to detect faults in real time with 97% accuracy and 95% recall.

## Features Used
- Pressure, Flow Rate, Temperature
- Valve Status, Pump State, Pump Speed
- Compressor State, Energy Consumption
- Engineered features: Pressure Flow Ratio, High Energy Low Flow flag

## Model Performance
| Metric | Score |
|--------|-------|
| Accuracy | 97% |
| Precision | 95% |
| Recall | 95% |
| ROC-AUC | 98% |

## Tech Stack
Python, Scikit-learn, Streamlit, Pandas, NumPy

## Live Demo
[Click here to try the app](paste_your_streamlit_url_here)
