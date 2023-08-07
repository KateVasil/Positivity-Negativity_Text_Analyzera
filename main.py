import streamlit as st
import plotly.express as px
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import glob

analyzer = SentimentIntensityAnalyzer()

filepaths = glob.glob("diary/*.txt")
mood_scores = []

# Extract positivity and negativity data
for filepath in filepaths:
    file = open(filepath, "r")
    mood = file.read()
    score = analyzer.polarity_scores(mood)
    mood_scores.append(score.copy())
negativity =[dict['neg'] for dict in mood_scores]
positivity =[dict['pos'] for dict in mood_scores]

# Extract dates from filenames
dates = [filepath.strip("diary\\" + ".txt") for filepath in filepaths]

# Create page and display plots
st.title("Diary Tone")
st.subheader("Positivity")

figure = px.line(x=dates, y=positivity, labels={"x": "Dates", "y": "Positivity"})
st.plotly_chart(figure)

st.subheader("Negativity")

figure = px.line(x=dates, y=negativity, labels={"x": "Dates", "y": "Negativity"})
st.plotly_chart(figure)








