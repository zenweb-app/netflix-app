# -*- coding: utf-8 -*-
"""Streamlit Netflix Dashboard.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fNA5h9eETbDRImS25gDu8Q2XtBB-Fu7J
"""

from google.colab import files
import pandas as pd

# Upload the file
uploaded = files.upload()

# Read the CSV file
file_name = "netflix_titles.csv"
df = pd.read_csv(file_name)

# Display the first few rows
df.head()

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py

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
# Updated to use the correct column names
fig1 = px.bar(df['release_year'].value_counts().sort_index().reset_index(),
              x="release_year",  # Use 'release_year' for the x-axis
              y="count",  # Use 'count' for the y-axis (automatically generated by value_counts)
              labels={"release_year": "Release Year", "count": "Number of Titles"},
              color="count", color_continuous_scale="viridis")
st.plotly_chart(fig1)

# Pie Chart: Movies vs TV Shows
st.subheader("Movies vs TV Shows")
fig2 = px.pie(df, names='type', title='Content Type Distribution')
st.plotly_chart(fig2)

# Data Table
st.subheader("Data Preview")
st.dataframe(df)

