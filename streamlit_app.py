
import streamlit as st
import pandas as pd
import pickle

# Load team dictionary and model
team_dict = pickle.load(open("team_dict.pkl", "rb"))
model = pickle.load(open("model.pkl", "rb"))

st.title("⚽ Football Match Predictor")

teams = list(team_dict.keys())

home_team = st.selectbox("Select Home Team", teams)
away_team = st.selectbox("Select Away Team", teams)

if st.button("Predict"):
    if home_team == away_team:
        st.warning("Home and away teams must be different!")
    else:
        home_encoded = team_dict[home_team]
        away_encoded = team_dict[away_team]
        prediction = model.predict([[home_encoded, away_encoded]])[0]
        outcome = {0: "🏠 Home Win", 1: "🤝 Draw", 2: "🛫 Away Win"}
        st.success(f"Prediction: {outcome[prediction]}")
