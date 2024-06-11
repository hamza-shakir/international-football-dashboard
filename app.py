import streamlit as st
import pandas as pd
import datetime

from modules.data_processing import results_data, goalscorers_data
from modules.visualizations import trophy_count_hbarchart, goals_count_line_plot, tour_stats

#setting page configurations
st.set_page_config(page_title = "International Football Dashboard",
                   page_icon = ":soccer:",
                   initial_sidebar_state = "auto",
                   layout = "wide",
                   menu_items = {'About': "View the source code for this dashboard by clicking on the below github repo link: https://github.com/hamza-shakir/international-football-dashboard"})

# creating a large heading
st.title(":rainbow[International Football Dashboard] 🌍⚽📊")

# explaining a jist of this page in the sidebar
with st.sidebar:

    st.write("# :red[About]")
    st.markdown("""Following up on the [*Visualising Data in Football project*](https://github.com/hamza-shakir/visualizing-data-in-football), 
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
                * [*Jupyter notebook*](https://github.com/hamza-shakir/visualizing-data-in-football) where I carried out all the cleaning and analysis.
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
tournaments = ["FIFA World Cup", "Copa América", "AFC Asian Cup", "African Cup of Nations", "UEFA Euro"]
selected_tournament = row1[0].selectbox("Choose Tournament", 
                                        options = tournaments,
                                        placeholder = "Choose Tournament",
                                        help = "Select a tournament to view its stats",
                                        index = 0) 

# slider with a range of years to view data from
start_year, end_year = row1[1].select_slider("Select Year",
                                             options = range(1916, datetime.date.today().year + 1),
                                             value = (1916, datetime.date.today().year),
                                             help = "Select range of years between which you would like to view the stats")

#---------------------------------------------------------------------------------------------------------------------------------------

# creating tabs to view different charts and stats
tab1, tab2, tab3 = st.tabs(["Tournament Stats", "Goals Stats", "Penalty Stats"])


# Tournament Stats
with tab1:
    # Tournament champions section
    # st.subheader("Tale of Champions")
    st.markdown("<h2 style='text-align: center;'>Tale of Champions</h2>", unsafe_allow_html=True)

    # Trophies won as hosts toggle
    toggle = st.toggle('Trophies won as hosts',
                       value=True,
                       help="View how many teams have made the most out of their home advantage")
    

    # splitting the 2 charts into columns
    col1_1, col1_2 = st.columns([3,2])

    # Display trophies chart based on toggle state
    if toggle:
        fig_trophies, fig_pie_chart = trophy_count_hbarchart(selected_tournament, rs, start_year, end_year, toggle)
        with col1_1.container():
            st.plotly_chart(fig_trophies, use_container_width=True)

        with col1_2.container():
            st.plotly_chart(fig_pie_chart, use_container_width=True)
    else:
        with col1_1.container():
            st.plotly_chart(trophy_count_hbarchart(selected_tournament, rs, start_year, end_year, toggle), use_container_width=True)


    # visual divider between sections
    st.divider() #-----------------------------------------------------------------------------------------------------------------------------


    # Latest tournament results section
    # st.subheader("Latest Tournament Stats")
    st.markdown("<h2 style='text-align: center;'>Latest Tournament Stats</h2>", unsafe_allow_html=True)

    # Displaying the score from the latest finals
    col2_1, col2_2, col2_3 = st.columns(3, gap='medium')


    # Define the CSS style to hide the delta arrow in st.metric
    hide_arrow_style = """
    <style>
    [data-testid="stMetricDelta"] svg {
    display: none;
    }
    </style>
    """

    # Inject the CSS style
    st.markdown(hide_arrow_style, unsafe_allow_html=True)


    with col2_1.container(border=True):
        st.metric(label=":orange[Defending Champion]", 
                  value=tour_stats(selected_tournament, rs, start_year, end_year, "Champion"), 
                  delta=tour_stats(selected_tournament, rs, start_year, end_year, "tour_year"),
                  delta_color="off")
    
    with col2_2.container(border=True):
        st.metric(label="Final Score",
                  value=tour_stats(selected_tournament, rs, start_year, end_year, "Final Score"),
                  delta=tour_stats(selected_tournament, rs, start_year, end_year, "pens"))
    
    with col2_3.container(border=True):
        st.metric(label=":blue[Runner-up]",
                  value=tour_stats(selected_tournament, rs, start_year, end_year, "Runner-up"),
                  delta=tour_stats(selected_tournament, rs, start_year, end_year, "tour_year"),
                  delta_color="off")
    

    # visual divider between sections
    st.divider() #-----------------------------------------------------------------------------------------------------------------------------


    # Team Appearances section
    # st.subheader("Team Appearances")
    st.markdown("<h2 style='text-align: center;'>Team Appearances</h2>", unsafe_allow_html=True)

    # Displaying appearance stats
    col3_1, col3_2 = st.columns(2, gap='medium')

    with col3_1.container():
        st.subheader("Most Appearances in " + selected_tournament + " Finals")
        st.dataframe(tour_stats(selected_tournament, rs, start_year, end_year, "Final Appearances"),
                     use_container_width=True,
                     hide_index=True)

    with col3_2.container():
        st.subheader("Most Appearances in " + selected_tournament)
        st.dataframe(tour_stats(selected_tournament, rs, start_year, end_year, "Tournament Appearances"),
                     use_container_width=True,
                     hide_index=True)





# Goal Stats
with tab2:
    # Goal Trends section
    # st.subheader("Goal Trends")
    st.markdown("<h3 style='text-align: center;'>Goal Trends</h3>", unsafe_allow_html=True)

    # Goals count line plot
    st.plotly_chart(goals_count_line_plot(selected_tournament, rs, start_year, end_year), use_container_width=True)
    

    # visual divider between sections
    st.divider() #-----------------------------------------------------------------------------------------------------------------------------


    # Team Goal Stats section
    # st.subheader("Team Goal Stats")
    st.markdown("<h3 style='text-align: center;'>Team Goal Stats</h3>", unsafe_allow_html=True)

    col1_1, col1_2 = st.columns(2, gap='medium')

    with col1_1.container():
        # Teams who have scored the most goals of all time (table)
        st.dataframe(use_container_width=True,
                     hide_index=True)

    # with col1_2.container():
    #     # 
    #     st.dataframe(use_container_width=True,
    #                  hide_index=True)


    # # visual divider between sections
    # st.divider() #-----------------------------------------------------------------------------------------------------------------------------


    # # Player Goal Stats section
    # # st.subheader("Player Goal Stats")
    # st.markdown("<h3 style='text-align: center;'>Player Goal Stats</h3>", unsafe_allow_html=True)

    # col2_1, col2_2 = st.columns(2, gap='medium')


# Penalty Stats
# with tab3:
    

