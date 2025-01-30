%%writefile app.py
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv("netflix_titles.csv")

df = load_data()

# Title
st.title("Netflix Titles Dashboard")

# Overview Metrics
st.write(f"Total Titles: {df.shape[0]}")
st.write(f"Movies: {df[df['type'] == 'Movie'].shape[0]}")
st.write(f"TV Shows: {df[df['type'] == 'TV Show'].shape[0]}")

# Filters
content_type = st.selectbox("Filter by Type:", ["All", "Movie", "TV Show"])
if content_type != "All":
    df = df[df["type"] == content_type]

# Bar Chart: Titles Per Year
st.subheader("Titles Released Per Year")
fig1 = px.bar(df['release_year'].value_counts().sort_index().reset_index(), x="index", y="release_year",
              labels={"index": "Release Year", "release_year": "Number of Titles"},
              color="release_year", color_continuous_scale="viridis")
st.plotly_chart(fig1)

# Pie Chart: Movies vs TV Shows
st.subheader("Movies vs TV Shows")
fig2 = px.pie(df, names='type', title='Content Type Distribution')
st.plotly_chart(fig2)

# Data Table
st.subheader("Data Preview")
st.dataframe(df)
