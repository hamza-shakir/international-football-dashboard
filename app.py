import streamlit as st
import pandas as pd
import datetime

from data_processing import results_data, goalscorers_data
from visualizations import trophy_count_hbarchart, goals_count_line_plot

#setting page configurations
st.set_page_config(page_title = "International Football Dashboard",
                   page_icon = ":soccer:",
                   initial_sidebar_state = "auto",
                   layout = "wide",
                   menu_items = {'About': "View the source code for this dashboard by clicking on the below github repo link: https://github.com/Hamza-149/international-football-dashboard"})

# creating a large heading
st.title(":rainbow[International Football Dashboard] 🌍⚽📊")

# explaining a jist of this page in the sidebar
with st.sidebar:

    st.write("# :red[About]")
    st.markdown("""Following up on the [*Visualising Data in Football project*](https://github.com/Hamza-149/visualizing-data-in-football), 
                I built an interactive user-friendly dashboard which will allow users to freely interact and explore visualizations 
                and stats of international football tournaments over the years.""")
    
    st.write("# :red[Tournaments Analyzed]")
    st.markdown("""
                * FIFA World Cup
                * UEFA Euro
                * Copa América
                * African Cup of Nations
                * AFC Asian cup
                """)

    st.write("# :red[References]")
    st.markdown("""
                * The [*dataset*](https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017) 
                I used for the analysis was obtained from [*Kaggle*](https://www.kaggle.com/).
                * To clean some of the data that I extracted from kaggle, I cross-referenced it with the data available on Wikipedia.
                * [*Jupyter notebook*](https://github.com/Hamza-149/visualizing-data-in-football) where I carried out all the cleaning and analysis.
                """)


#-----------------------------------data processing--------------------------------------------------------------
    

# reading the CSV files
results_df = pd.read_csv('datasets/results.csv')
shootouts_df = pd.read_csv('datasets/shootouts.csv')
goalscorers_df = pd.read_csv('datasets/goalscorers.csv')

# cleaning and preparing our results data
rs = results_data(results_df, shootouts_df)

# cleaning and preparing our goalscorers data
gs = goalscorers_data(goalscorers_df, rs)


#---------------------------------------dispalying content---------------------------------------------------------


# creating 2 columns for a tournament dropdown list and a slider with a range of years
fixed_header = st.container()
row1 = fixed_header.columns([1, 3], gap='medium')

# creating sticky header for the dropdown list and a slider
fixed_header.write("""<div class='fixed-header'/>""", unsafe_allow_html=True)

# Custom CSS for the sticky header
st.markdown(
    """
<style>
    div[data-testid="stVerticalBlock"] div:has(div.fixed-header) {
        position: sticky;
        top: 2.875rem;
        background-color: #0E1117;
        z-index: 999;
    }
</style>
    """,
    unsafe_allow_html=True
)

# dropdown list for selecting tournament of choice
tournaments = ["All", "FIFA World Cup", "Copa América", "AFC Asian Cup", "African Cup of Nations", "UEFA Euro"]
selected_tournament = row1[0].selectbox("Choose Tournament", 
                                        options = tournaments,
                                        placeholder = "Choose Tournament",
                                        help = "Select a tournament to view its stats",
                                        index = 1) 

# slider with a range of years to view data from
start_year, end_year = row1[1].select_slider("Select Year",
                                             options = range(1916, datetime.date.today().year + 1),
                                             value = (1916, datetime.date.today().year),
                                             help = "Select range of years between which you would like to view the stats")

#---------------------------------------------------------------------------------------------------------------------------------------

# creating tabs to view different charts and stats
tab1, tab2, tab3, tab4 = st.tabs(["Trophies won", "Goals scored", "Team Stats", "Team Comparison"])


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


#
tab3.write("## ⚙ *:orange[Under development]* ⚙")


#
tab4.write("## ⚙ *:orange[Under development]* ⚙")