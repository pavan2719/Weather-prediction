# Interactive Weather Dashboard

import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression
import plotly.graph_objects as go

st.title("🌦️ Weather Prediction Dashboard")

# User input
temps = st.text_input("Enter past temperatures (comma-separated):", "30,32,31,29,33")

# Convert input
temps = list(map(float, temps.split(",")))
days = np.arange(1, len(temps)+1).reshape(-1, 1)

# Train model
model = LinearRegression()
model.fit(days, temps)

# Prediction
next_day = np.array([[len(temps)+1]])
prediction = model.predict(next_day)[0]

st.write("### Predicted Temperature:", round(prediction, 2))

# Graph
fig = go.Figure()

fig.add_trace(go.Scatter(x=days.flatten(), y=temps, mode='lines+markers', name='Past'))

fig.add_trace(go.Scatter(x=[len(temps)+1], y=[prediction], mode='markers', name='Prediction'))

st.plotly_chart(fig)