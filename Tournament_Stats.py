import streamlit as st
import pandas as pd
import datetime

from data_processing import processing_data
from visualizations import trophy_count_hbarchart, goals_count_line_plot

#setting page configurations
st.set_page_config(page_title = "International Football Dashboard",
                   page_icon = ":soccer:",
                   initial_sidebar_state = "auto",
                   layout = "wide",
                   menu_items = {'About': "View the source code for this dashboard by clicking on the below github repo link: https://github.com/Hamza-149/international-football-dashboard"})

# creating a large heading
st.title("International Football Dashboard 🌍⚽📊")


# reading the CSV files
results_df = pd.read_csv('datasets/results.csv')
shootouts_df = pd.read_csv('datasets/shootouts.csv')
goalscorers_df = pd.read_csv('datasets/goalscorers.csv')

# cleaning and preparing our data
rs = processing_data(results_df, shootouts_df)


#------------------------------------------------------------------------------------------------

# creating 2 columns for a dropdown list and a slider
row1 = st.columns([1, 3], gap='medium')

# Tournament options and default selection
tournaments = ["All", "FIFA World Cup", "Copa América", "AFC Asian Cup", "African Cup of Nations", "UEFA Euro"]
selected_tournament = row1[0].selectbox("Choose Tournament", 
                                        options = tournaments,
                                        placeholder = "Choose Tournament",
                                        help = "Select a tournament to view its stats",
                                        index = 1) 

# Range of years to view data from
start_year, end_year = row1[1].select_slider("Select Year",
                                             options = range(1916, datetime.date.today().year + 1),
                                             value = (1916, datetime.date.today().year),
                                             help = "Select range of years between which you would like to view the stats")

# creating tabs to view different charts
tab1, tab2 = st.tabs(["Trophies won", "Goals scored"])

# displaying trophy count chart
toggle = tab1.toggle('Trophies won as hosts')

if toggle:
    fig_trophies, fig_pie_chart = trophy_count_hbarchart(selected_tournament, rs, start_year, end_year, toggle)
    tab1.plotly_chart(fig_trophies, use_container_width=True)
    tab1.plotly_chart(fig_pie_chart, use_container_width=True)

else:
    tab1.plotly_chart(trophy_count_hbarchart(selected_tournament, rs, start_year, end_year, toggle), use_container_width=True)


# displaying goal count chart
tab2.plotly_chart(goals_count_line_plot(selected_tournament, rs, start_year, end_year), use_container_width=True)