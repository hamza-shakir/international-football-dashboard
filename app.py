import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import datetime

from data_processing import processing_data
from visualizations import trophy_count_hbarchart


# setting the page title
st.set_page_config(page_title="International Football Dashboard")
# creating a large heading
st.title("International Football Dashboard")

# adding a selectbox to the sidebar
selected_tab = st.sidebar.radio(
    'Choose tab:',
    ('Tournaments Stats', 'Compare Teams')
)

# reading the CSV files
results_df = pd.read_csv('datasets/results.csv')
shootouts_df = pd.read_csv('datasets/shootouts.csv')
goalscorers_df = pd.read_csv('datasets/goalscorers.csv')

# cleaning and preparing our data
rs = processing_data(results_df, shootouts_df)


#------------------------------------------------------------------------------------------------


selected_range = st.slider("Select Year", 1916, datetime.date.today().year, datetime.date.today().year)


# Tournament options and default selection
tournaments = ["All", "FIFA World Cup", "Copa América", "AFC Asian Cup", "African Cup of Nations", "UEFA Euro"]
selected_tournament = st.selectbox("Choose Tournament", tournaments, index=0)  # Default: World Cup

# displaying trophy count chart
trophy_count_hbarchart(selected_tournament, rs)


