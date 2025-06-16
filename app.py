import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
fandango = pd.read_csv('fandango_scrape.csv')
sites = pd.read_csv('all_sites_scores.csv')

# Merge datasets
merged = pd.merge(fandango, sites, on='FILM')

# UI Starts
st.title("🎬 Movie Rating Bias Explorer")

# Movie Selection
movie = st.selectbox("🎞️ Choose a Movie:", merged['FILM'].unique())

# Get data for selected movie
data = merged[merged['FILM'] == movie].iloc[0]

# Show ratings in columns
st.markdown("### ⭐ Ratings Summary")
col1, col2 = st.columns(2)
with col1:
    st.metric("Fandango", data['STARS'])
    st.metric("Rotten Tomatoes", data['RottenTomatoes'] / 20)
with col2:
    st.metric("IMDB", data['IMDB'])
    st.metric("Metacritic", data['Metacritic'] / 20)

# Barplot
st.markdown("### 📊 Rating Comparison")
fig, ax = plt.subplots()
ratings = {
    "Fandango": data['STARS'],
    "IMDB": data['IMDB'],
    "RT": data['RottenTomatoes'] / 20,
    "Metacritic": data['Metacritic'] / 20
}
sns.barplot(x=list(ratings.keys()), y=list(ratings.values()), palette='viridis',hue=list(ratings.keys()), ax=ax)
ax.set_ylabel("Normalized Rating")
st.pyplot(fig)
