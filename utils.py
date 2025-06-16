import pandas as pd
import matplotlib.pyplot as plt

# 🚀 1. Function to load and merge data
def load_and_merge():
    fandango = pd.read_csv('fandango_scrape.csv')        
    sites = pd.read_csv('all_sites_scores.csv')          
    df = pd.merge(fandango, sites, on='FILM')
    return df.dropna()

# 🎨 2. Function to create comparison bar chart
def make_comparison_chart(row):
    data = {
        'Fandango': row['STARS'],
        'IMDB': row['IMDB_Norm'],
        'RT': row['RT_Norm'],
        'Metacritic': row['Meta_Norm']
    }
    platforms = list(data.keys())
    scores = list(data.values())

    fig, ax = plt.subplots()
    bars = ax.bar(platforms, scores, color=['#6a5acd', '#20b2aa', '#3cb371', '#90ee90'])
    
    ax.set_ylabel("Normalized Rating")
    ax.set_ylim(0, 10)
    ax.set_title("Rating Comparison")
    return fig
