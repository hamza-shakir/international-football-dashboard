import streamlit as st
import pandas as pd
import plotly.graph_objs as go


# creates a bar chart to view the past champions of a given tournament
def trophy_count_hbarchart(tournament_name, rs, start_year, end_year, toggle):
    # determining the year range between which the user wants to view the data
    rs = rs[(rs['Year']>=start_year) & (rs['Year']<=end_year)]

    # Create a single plot with horizontal bar subplots
    fig_trophies = go.Figure()
    fig_host_trophies = go.Figure()

    if tournament_name == "All":
        #creating dataframes for major tournaments
        world_cup = rs.loc[rs['Tournament'] == 'FIFA World Cup']
        copa_america = rs.loc[rs['Tournament'] == 'Copa América']
        afcon = rs.loc[rs['Tournament'] == 'African Cup of Nations']
        euros = rs.loc[rs['Tournament'] == 'UEFA Euro']
        asian_cup = rs.loc[rs['Tournament'] == 'AFC Asian Cup']

        # creating dataframes for finals of the respective tournaments
        world_cup_groupby = world_cup.groupby('Year')
        world_cup_final = world_cup_groupby.last()

        copa_america_groupby = copa_america.groupby('Year')
        copa_america_final = copa_america_groupby.last()

        afcon_groupby = afcon.groupby('Year')
        afcon_final = afcon_groupby.last()

        euros_groupby = euros.groupby('Year')
        euros_final = euros_groupby.last()

        asian_cup_groupby = asian_cup.groupby('Year')
        asian_cup_final = asian_cup_groupby.last()

        # resolving certain faults in the Finals data
        indexNames = copa_america_final[copa_america_final['Winning Team'] == 'Draw'].index
        copa_america_final.drop(indexNames, inplace = True)

        # creating dataframes to identify the winners and how many times they have won the tournament
        world_cup_champions = pd.DataFrame(world_cup_final['Winning Team'].value_counts().sort_index())
        copa_america_champions = pd.DataFrame(copa_america_final['Winning Team'].value_counts().sort_index())
        afcon_champions = pd.DataFrame(afcon_final['Winning Team'].value_counts().sort_index())
        euros_champions = pd.DataFrame(euros_final['Winning Team'].value_counts().sort_index())
        asian_cup_champions = pd.DataFrame(asian_cup_final['Winning Team'].value_counts().sort_index())

        # Resetting index
        world_cup_champions.reset_index(drop=False, inplace=True)
        copa_america_champions.reset_index(drop=False, inplace=True)
        afcon_champions.reset_index(drop=False, inplace=True)
        euros_champions.reset_index(drop=False, inplace=True)
        asian_cup_champions.reset_index(drop=False, inplace=True)

        # Renaming columns
        world_cup_champions.rename(columns={'Winning Team': 'Winner', 'count': 'Trophies won overall'}, inplace=True)
        copa_america_champions.rename(columns={'Winning Team': 'Winner', 'count': 'Trophies won overall'}, inplace=True)
        afcon_champions.rename(columns={'Winning Team': 'Winner', 'count': 'Trophies won overall'}, inplace=True)
        euros_champions.rename(columns={'Winning Team': 'Winner', 'count': 'Trophies won overall'}, inplace=True)
        asian_cup_champions.rename(columns={'Winning Team': 'Winner', 'count': 'Trophies won overall'}, inplace=True)

        # Sort dataframes by trophies won in descending order
        world_cup_champions_sorted = world_cup_champions.sort_values(by='Trophies won overall', ascending=True)
        copa_america_champions_sorted = copa_america_champions.sort_values(by='Trophies won overall', ascending=True)
        afcon_champions_sorted = afcon_champions.sort_values(by='Trophies won overall', ascending=True)
        euros_champions_sorted = euros_champions.sort_values(by='Trophies won overall', ascending=True)
        asian_cup_champions_sorted = asian_cup_champions.sort_values(by='Trophies won overall', ascending=True)

        # checking if toggle for viewing 'trophies won as hosts' is off
        if toggle is False:
            # Add horizontal bar plots to the single plot
            fig_trophies.add_trace(go.Bar(y=world_cup_champions_sorted['Winner'], x=world_cup_champions_sorted['Trophies won overall'], orientation='h', name='FIFA World Cup'))
            fig_trophies.add_trace(go.Bar(y=copa_america_champions_sorted['Winner'], x=copa_america_champions_sorted['Trophies won overall'], orientation='h', name='Copa América'))
            fig_trophies.add_trace(go.Bar(y=afcon_champions_sorted['Winner'], x=afcon_champions_sorted['Trophies won overall'], orientation='h', name='African Cup of Nations'))
            fig_trophies.add_trace(go.Bar(y=euros_champions_sorted['Winner'], x=euros_champions_sorted['Trophies won overall'], orientation='h', name='UEFA Euro'))
            fig_trophies.add_trace(go.Bar(y=asian_cup_champions_sorted['Winner'], x=asian_cup_champions_sorted['Trophies won overall'], orientation='h', name='AFC Asian Cup'))
        
        # executes only when toggle for viewing 'trophies won as hosts' is on
        else:
            # creating dataframes to identify the winners who also happend to be hosts and how many times they have won the tournament
            world_cup_host_champions = world_cup_final[world_cup_final['Winning Team'] == world_cup_final['Country']]
            copa_america_host_champions = copa_america_final[copa_america_final['Winning Team'] == copa_america_final['Country']]
            afcon_host_champions = afcon_final[afcon_final['Winning Team'] == afcon_final['Country']]
            euros_host_champions = euros_final[euros_final['Winning Team'] == euros_final['Country']]
            asian_cup_host_champions = asian_cup_final[asian_cup_final['Winning Team'] == asian_cup_final['Country']]

            world_cup_host_champions = pd.DataFrame(world_cup_host_champions['Winning Team'].value_counts().sort_index())
            copa_america_host_champions = pd.DataFrame(copa_america_host_champions['Winning Team'].value_counts().sort_index())
            afcon_host_champions = pd.DataFrame(afcon_host_champions['Winning Team'].value_counts().sort_index())
            euros_host_champions = pd.DataFrame(euros_host_champions['Winning Team'].value_counts().sort_index())
            asian_cup_host_champions = pd.DataFrame(asian_cup_host_champions['Winning Team'].value_counts().sort_index())

            # Resetting index
            world_cup_host_champions.reset_index(drop=False, inplace=True)
            copa_america_host_champions.reset_index(drop=False, inplace=True)
            afcon_host_champions.reset_index(drop=False, inplace=True)
            euros_host_champions.reset_index(drop=False, inplace=True)
            asian_cup_host_champions.reset_index(drop=False, inplace=True)

            # Renaming columns
            world_cup_host_champions.rename(columns={'Winning Team': 'Winner', 'count': 'Trophies won as host'}, inplace=True)
            copa_america_host_champions.rename(columns={'Winning Team': 'Winner', 'count': 'Trophies won as host'}, inplace=True)
            afcon_host_champions.rename(columns={'Winning Team': 'Winner', 'count': 'Trophies won as host'}, inplace=True)
            euros_host_champions.rename(columns={'Winning Team': 'Winner', 'count': 'Trophies won as host'}, inplace=True)
            asian_cup_host_champions.rename(columns={'Winning Team': 'Winner', 'count': 'Trophies won as host'}, inplace=True)

            # merging the champions and the host_champions dataframes
            world_cup_champions_df = pd.merge(world_cup_champions, world_cup_host_champions, how = 'outer', on = ['Winner'])
            copa_america_champions_df = pd.merge(copa_america_champions, copa_america_host_champions, how = 'outer', on = ['Winner'])
            afcon_champions_df = pd.merge(afcon_champions, afcon_host_champions, how = 'outer', on = ['Winner'])
            euros_champions_df = pd.merge(euros_champions, euros_host_champions, how = 'outer', on = ['Winner'])
            asian_cup_champions_df = pd.merge(asian_cup_champions, asian_cup_host_champions, how='outer', on=['Winner'])

            # replacing null values with 0  for the teams that didn't win any tournaments as hosts
            world_cup_champions_df.fillna(0, inplace=True)
            copa_america_champions_df.fillna(0, inplace=True)
            afcon_champions_df.fillna(0, inplace=True)
            euros_champions_df.fillna(0, inplace=True)
            asian_cup_champions_df.fillna(0, inplace=True)

            # changing datatype of 'Trophies won as host' column from float to int
            world_cup_champions_df['Trophies won as host'] = world_cup_champions_df['Trophies won as host'].astype(int)
            copa_america_champions_df['Trophies won as host'] = copa_america_champions_df['Trophies won as host'].astype(int)
            afcon_champions_df['Trophies won as host'] = afcon_champions_df['Trophies won as host'].astype(int)
            euros_champions_df['Trophies won as host'] = euros_champions_df['Trophies won as host'].astype(int)
            asian_cup_champions_df['Trophies won as host'] = asian_cup_champions_df['Trophies won as host'].astype(int)

            # Sort dataframes by trophies won in descending order
            world_cup_champions_df_sorted = world_cup_champions_df.sort_values(by='Trophies won overall', ascending=True)
            copa_america_champions_df_sorted = copa_america_champions_df.sort_values(by='Trophies won overall', ascending=True)
            afcon_champions_df_sorted = afcon_champions_df.sort_values(by='Trophies won overall', ascending=True)
            euros_champions_df_sorted = euros_champions_df.sort_values(by='Trophies won overall', ascending=True)
            asian_cup_champions_df_sorted = asian_cup_champions_df.sort_values(by='Trophies won overall', ascending=True)

            # Add horizontal bar plots to the single plot
            fig_host_trophies.add_trace(go.Bar(y=world_cup_champions_df_sorted['Winner'], x=world_cup_champions_df_sorted['Trophies won overall'], orientation='h', name='Trophies won overall - World Cup'))
            fig_host_trophies.add_trace(go.Bar(y=world_cup_champions_df_sorted['Winner'], x=world_cup_champions_df_sorted['Trophies won as host'], orientation='h', name='Trophies won as host - World Cup'))
            fig_host_trophies.add_trace(go.Bar(y=copa_america_champions_df_sorted['Winner'], x=copa_america_champions_df_sorted['Trophies won overall'], orientation='h', name='Trophies won overall - Copa America'))
            fig_host_trophies.add_trace(go.Bar(y=copa_america_champions_df_sorted['Winner'], x=copa_america_champions_df_sorted['Trophies won as host'], orientation='h', name='Trophies won as host - Copa America'))
            fig_host_trophies.add_trace(go.Bar(y=afcon_champions_df_sorted['Winner'], x=afcon_champions_df_sorted['Trophies won overall'], orientation='h', name='Trophies won overall - AFCON'))
            fig_host_trophies.add_trace(go.Bar(y=afcon_champions_df_sorted['Winner'], x=afcon_champions_df_sorted['Trophies won as host'], orientation='h', name='Trophies won as host - AFCON'))
            fig_host_trophies.add_trace(go.Bar(y=euros_champions_df_sorted['Winner'], x=euros_champions_df_sorted['Trophies won overall'], orientation='h', name='Trophies won overall - UEFA Euro'))
            fig_host_trophies.add_trace(go.Bar(y=euros_champions_df_sorted['Winner'], x=euros_champions_df_sorted['Trophies won as host'], orientation='h', name='Trophies won as host - UEFA Euro'))
            fig_host_trophies.add_trace(go.Bar(y=asian_cup_champions_df_sorted['Winner'], x=asian_cup_champions_df_sorted['Trophies won overall'], orientation='h', name='Trophies won overall - AFC Asian Cup'))
            fig_host_trophies.add_trace(go.Bar(y=asian_cup_champions_df_sorted['Winner'], x=asian_cup_champions_df_sorted['Trophies won as host'], orientation='h', name='Trophies won as host - AFC Asian Cup'))

            # Update layout settings
            fig_host_trophies.update_layout(barmode='overlay', 
                                            xaxis_title='Number of Trophies Won',
                                            legend=dict(xanchor="right", yanchor="bottom", x=0.95, y=0.3),
                                            margin={"t":50, "b": 10},
                                            dragmode=False)

            # calling function to display (pie chart) comparison between trophies by hosts and neutrals
            all_tournaments_champions_df_sorted = pd.concat([world_cup_champions_df_sorted,
                                                             copa_america_champions_df_sorted,
                                                             afcon_champions_df_sorted,
                                                             euros_champions_df_sorted,
                                                             asian_cup_champions_df_sorted])
            
            fig_pie_chart = trophies_won_hosting_pie_chart(all_tournaments_champions_df_sorted)

            return fig_host_trophies, fig_pie_chart


    else:
        # creating dataframe for the tournament of choice
        tournament = rs.loc[rs['Tournament'] == tournament_name]

        # creating dataframes for finals of the respective tournaments
        tournament_groupby = tournament.groupby('Year')
        tournament_final = tournament_groupby.last()

        # resolving certain faults in the Finals data of the 'Copa América'
        if tournament_name == 'Copa América':
            # resolving certain faults in the Finals data
            indexNames = tournament_final[tournament_final['Winning Team'] == 'Draw'].index
            tournament_final.drop(indexNames, inplace = True)

        # creating dataframes to identify the winners and how many times they have won the tournament
        tournament_champions = pd.DataFrame(tournament_final['Winning Team'].value_counts().sort_index())

        # Resetting index
        tournament_champions.reset_index(drop=False, inplace=True)

        # Renaming columns
        tournament_champions.rename(columns={'Winning Team': 'Winner', 'count': 'Trophies won overall'}, inplace=True)

        # Sort dataframes by trophies won in descending order
        tournament_champions_sorted = tournament_champions.sort_values(by='Trophies won overall', ascending=True)


        # checking if toggle for viewing 'trophies won as hosts' is off
        if toggle is False:
            # Add horizontal bar plots to the single plot
            fig_trophies.add_trace(go.Bar(y=tournament_champions_sorted['Winner'], x=tournament_champions_sorted['Trophies won overall'], orientation='h', name=tournament_name))


        # executes only when toggle for viewing 'trophies won as hosts' is on
        else:
            # creating dataframe to identify the winners who also happend to be hosts and how many times they have won the tournament
            tournament_host_champions = tournament_final[tournament_final['Winning Team'] == tournament_final['Country']]

            tournament_host_champions = pd.DataFrame(tournament_host_champions['Winning Team'].value_counts().sort_index())

            # Resetting index
            tournament_host_champions.reset_index(drop=False, inplace=True)

            # Renaming columns
            tournament_host_champions.rename(columns={'Winning Team': 'Winner', 'count': 'Trophies won as host'}, inplace=True)

            # merging the champions and the host_champions dataframes
            tournament_champions_df = pd.merge(tournament_champions, tournament_host_champions, how = 'outer', on = ['Winner'])

            # replacing null values with 0  for the teams that didn't win any tournaments as hosts
            tournament_champions_df.fillna(0, inplace=True)

            # changing datatype of 'Trophies won as host' column from float to int
            tournament_champions_df['Trophies won as host'] = tournament_champions_df['Trophies won as host'].astype(int)

            # Sort dataframe by trophies won in descending order
            tournament_champions_df_sorted = tournament_champions_df.sort_values(by='Trophies won overall', ascending=True)

            fig_host_trophies.add_trace(go.Bar(y=tournament_champions_df_sorted['Winner'], x=tournament_champions_df_sorted['Trophies won overall'], orientation='h', name='Trophies won overall'))
            fig_host_trophies.add_trace(go.Bar(y=tournament_champions_df_sorted['Winner'], x=tournament_champions_df_sorted['Trophies won as host'], orientation='h', name='Trophies won as host'))

            # Update layout settings
            fig_host_trophies.update_layout(barmode='overlay', 
                                            xaxis_title='Number of Trophies Won',
                                            legend=dict(xanchor="right", yanchor="bottom", x=0.95, y=0.3),
                                            margin={"t":50, "b": 10},
                                            dragmode=False)

            # calling function to display (pie chart) comparison between trophies by hosts and neutrals
            fig_pie_chart = trophies_won_hosting_pie_chart(tournament_champions_df_sorted)

            return fig_host_trophies, fig_pie_chart


    # Update layout settings
    fig_trophies.update_layout(xaxis_title='Number of Trophies Won',
                               barmode='overlay',
                               legend=dict(xanchor="right", yanchor="top", x=0.95, y=0.65),
                               margin={"t":50, "b": 10},
                               dragmode=False)
        
    return fig_trophies


# creates pie chart which to view the comparison between teams that were champions while hosting vs those who weren't hosting
def trophies_won_hosting_pie_chart(rs):
    # calcualting the the sum values of the no. of times hosts and neutrals have won tournaments
    hosts_count = rs['Trophies won as host'].sum()
    neutral_count = rs['Trophies won overall'].sum() - rs['Trophies won as host'].sum()

    # creating values and labels arrays for pie chart
    values = [hosts_count, neutral_count]
    labels = ['Host Champions', 'Neutral Champions']

    # Specify the index of the slice you want to explode (0 for first, 1 for second)
    exploded_slice_index = 0

    fig_pie_chart = go.Figure(data=[go.Pie(labels=labels, 
                                           values=values,
                                           # Apply pull to the desired slice index
                                           pull=[0, 0.1] if exploded_slice_index == 0 else [0.1, 0])])

    return fig_pie_chart


# creates a line plot to view the goals scored in each tournament
def goals_count_line_plot(tournament_name, rs, start_year, end_year):
    # determining the year range between which the user wants to view the data
    rs = rs[(rs['Year']>=start_year) & (rs['Year']<=end_year)]

     # Create a single plot
    fig_goals = go.Figure()

    if tournament_name == "All":
        # creating dataframes for major tournaments
        world_cup = rs.loc[rs['Tournament'] == 'FIFA World Cup']
        copa_america = rs.loc[rs['Tournament'] == 'Copa América']
        afcon = rs.loc[rs['Tournament'] == 'African Cup of Nations']
        euros = rs.loc[rs['Tournament'] == 'UEFA Euro']
        asian_cup = rs.loc[rs['Tournament'] == 'AFC Asian Cup']

        # grouping dataframes with respect to the year and goals scored
        world_cup_goals = world_cup.groupby('Year')[['Home Score', 'Away Score']].sum()
        copa_america_goals = copa_america.groupby('Year')[['Home Score', 'Away Score']].sum()
        afcon_goals = afcon.groupby('Year')[['Home Score', 'Away Score']].sum()
        euros_goals = euros.groupby('Year')[['Home Score', 'Away Score']].sum()
        asian_cup_goals = asian_cup.groupby('Year')[['Home Score', 'Away Score']].sum()

        world_cup_goals['Goals Scored'] = world_cup_goals['Home Score'] + world_cup_goals['Away Score']
        copa_america_goals['Goals Scored'] = copa_america_goals['Home Score'] + copa_america_goals['Away Score']
        afcon_goals['Goals Scored'] = afcon_goals['Home Score'] + afcon_goals['Away Score']
        euros_goals['Goals Scored'] = euros_goals['Home Score'] + euros_goals['Away Score']
        asian_cup_goals['Goals Scored'] = asian_cup_goals['Home Score'] + asian_cup_goals['Away Score']

        # Add line plots to the single plot
        fig_goals.add_trace(go.Scatter(x=world_cup_goals.index, y=world_cup_goals['Goals Scored'], mode='lines+markers', name='FIFA World Cup'))
        fig_goals.add_trace(go.Scatter(x=copa_america_goals.index, y=copa_america_goals['Goals Scored'], mode='lines+markers', name='Copa América'))
        fig_goals.add_trace(go.Scatter(x=afcon_goals.index, y=afcon_goals['Goals Scored'], mode='lines+markers', name='African Cup of Nations'))
        fig_goals.add_trace(go.Scatter(x=euros_goals.index, y=euros_goals['Goals Scored'], mode='lines+markers', name='UEFA Euro'))
        fig_goals.add_trace(go.Scatter(x=asian_cup_goals.index, y=asian_cup_goals['Goals Scored'], mode='lines+markers', name='AFC Asian Cup'))

    else :
        # creating dataframe for the tournament of choice
        tournament = rs.loc[rs['Tournament'] == tournament_name]

        # grouping dataframes with respect to the year and goals scored
        tournament_goals = tournament.groupby('Year')[['Home Score', 'Away Score']].sum()

        tournament_goals['Goals Scored'] = tournament_goals['Home Score'] + tournament_goals['Away Score']

        # Add line plots to the single plot
        fig_goals.add_trace(go.Scatter(x=tournament_goals.index,
                                       y=tournament_goals['Goals Scored'],
                                       mode='lines+markers',
                                    #    marker_color='#FF4B4B',
                                       name=tournament_name))
 

    # Update layout settings
    fig_goals.update_layout(xaxis_title='Year', 
                      yaxis_title='Goals Scored',
                      margin={"t": 50, "b": 20},
                      xaxis_showgrid=True,
                      yaxis_showgrid=True,
                      dragmode=False,
                      legend=dict(xanchor="left", yanchor="top", x=0.03, y=0.95))

    return fig_goals


# creates a pie chart to show the difference in success rates of taking the first penalty vs the second penalty in a shootout
def pen_pie_chart(tournament_name, gs, start_year, end_year):
    # Create a single plot
    fig_pen_pie_chart = go.Figure()

    # determining the year range between which the user wants to view the data
    gs = gs[(gs['Year']>=start_year) & (gs['Year']<=end_year)]

    # creating dataframe for the tournament of choice
    tournament = gs.loc[gs['Tournament'] == tournament_name]

    # Filter the DataFrame to include only rows where 'Shootout' is True
    shootout_matches = tournament[tournament['Shootout'] == True]

    # Calcualting the number of win rate for taking the penalty first vs second
    first_shooter_wins = len(shootout_matches[shootout_matches['Winning Team'] == shootout_matches['first_shooter']])
    second_shooter_wins = len(shootout_matches[shootout_matches['Winning Team'] != shootout_matches['first_shooter']])

    # Creating values and labels arrays for pie chart
    values = [first_shooter_wins , second_shooter_wins ]
    labels = ['Takes 1st penalty', 'Takes second penalty']

    fig_pen_pie_chart = go.Figure(data=[go.Pie(labels=labels, values=values)])

    return fig_pen_pie_chart


# creates a scatter plot showing the minutes at which goals were scored
def goal_min_hist(tournament_name, gs, start_year, end_year):
    # determining the year range between which the user wants to view the data
    gs = gs[(gs['Year']>=start_year) & (gs['Year']<=end_year)]

    # creating dataframe for the tournament of choice
    tournament = gs.loc[gs['Tournament'] == tournament_name]
    tournament = tournament.dropna(subset=['Minute'])

    # Create a single plot
    fig_goal_min = go.Figure()

    # Create a DataFrame
    goal_data = pd.DataFrame({'Minute': tournament['Minute']})

    # Create a histogram
    fig_goal_min_hist = go.Figure(data=[go.Histogram(x=goal_data['Minute'],
                                                     nbinsx=30)])

    # Update layout
    fig_goal_min_hist.update_layout(
        xaxis_title='Minute',
        yaxis_title='Count of Goals',
        dragmode=False
    )
    
    return fig_goal_min_hist


# retrieving stats for the "Tournament Stats" tab
def tour_stats(tournament_name, rs, gs, start_year, end_year, stat):
    if gs is not None:
        # determining the year range between which the user wants to view the data
        gs = gs[(gs['Year']>=start_year) & (gs['Year']<=end_year)]

        # creating dataframe for the tournament of choice
        gs_tournament = gs.loc[gs['Tournament'] == tournament_name]

    if rs is not None:
        # determining the year range between which the user wants to view the data
        rs = rs[(rs['Year']>=start_year) & (rs['Year']<=end_year)]

        # creating dataframe for the tournament of choice
        rs_tournament = rs.loc[rs['Tournament'] == tournament_name]

        # creating dataframes for finals of the respective tournaments
        rs_tournament_groupby = rs_tournament.groupby('Year')
        rs_tournament_final = rs_tournament_groupby.last()

        # resolving certain faults in the Finals data of the 'Copa América'
        if tournament_name == 'Copa América':
            # resolving certain faults in the Finals data
            indexNames = rs_tournament_final[rs_tournament_final['Winning Team'] == 'Draw'].index
            rs_tournament_final.drop(indexNames, inplace = True)


    # Obtaining champion's name
    if stat == "Champion":
        return rs_tournament['Winning Team'].iloc[-1]


    # Obtaining runner-up name
    elif stat == "Runner-up":
        return rs_tournament['Losing Team'].iloc[-1]
    

    # Year in which the tournament was played in
    elif stat == "tour_year":
        return int(rs_tournament['Year'].iloc[-1])
    

    # Obtaining Finals scoreline
    elif stat == "Final Score":
        if rs_tournament['Winning Team'].iloc[-1] == rs_tournament['Home Team'].iloc[-1]:
            return str(int(rs_tournament['Home Score'].iloc[-1])) + " - " + str(int(rs_tournament['Away Score'].iloc[-1]))
        else:
            return str(int(rs_tournament['Away Score'].iloc[-1])) + " - " + str(int(rs_tournament['Home Score'].iloc[-1]))
    

    # Checking if Finals was decided on penalties
    elif stat == "pens":
        if rs_tournament['Shootout'].iloc[-1] == True:
            return "Won via Penalties"
        else:
            return None
        

    # Finals appearnace count
    elif stat == "Final Appearances":
        combined_teams = pd.concat([rs_tournament_final['Winning Team'], rs_tournament_final['Losing Team']], ignore_index=True)

        # creating dataframes to identify the winners and how many times they have won the tournament
        final_appearances = pd.DataFrame(combined_teams.value_counts())

        # Resetting index
        final_appearances.reset_index(drop=False, inplace=True)

        # Renaming columns
        final_appearances.rename(columns={'index': 'Country', 'count': 'Most Appearances in Finals'}, inplace=True)

        # Sort dataframes by trophies won in descending order
        final_appearances = final_appearances.sort_values(by='Most Appearances in Finals', ascending=False)

        return final_appearances
    

    # Tournament appearance count
    elif stat == "Tournament Appearances":
        # Create a list of all teams
        all_teams = pd.concat([rs_tournament['Home Team'], rs_tournament['Away Team']], ignore_index=True).unique()

        # Initialize the new dataframe
        team_years = {'Country': [], 'Number of Tournaments played in': []}

        # Calculate the number of unique years each team played
        for team in all_teams:
            years_played = rs_tournament[(rs_tournament['Home Team'] == team) | (rs_tournament['Away Team'] == team)]['Year'].nunique()
            team_years['Country'].append(team)
            team_years['Number of Tournaments played in'].append(years_played)

        # Create the final dataframe
        total_appearances = pd.DataFrame(team_years)

        # Sort dataframes by trophies won in descending order
        total_appearances = total_appearances.sort_values(by='Number of Tournaments played in', ascending=False).reset_index(drop=True)

        return total_appearances
    

    # Top goalscorers of all time
    elif stat == "Top Goalscorers All-time":
        # Group by scorer and team, count total goals
        total_goals = gs_tournament[gs_tournament['Own Goal'] == False].groupby(['Scorer', 'Scorer Team']).size().reset_index(name='Goals Scored')

        # Filter non-penalty goals and count them
        non_penalty_goals = gs_tournament[gs_tournament['Penalty'] == False].groupby(['Scorer', 'Scorer Team']).size().reset_index(name='Non-Penalty Goals')

        # Merge the two dataframes on 'Scorer' and 'Team'
        goalscorers_df = pd.merge(total_goals, non_penalty_goals, on=['Scorer', 'Scorer Team'], how='left')

        # Fill NaN values in 'Non-Penalty Goals' column with 0
        goalscorers_df ['Non-Penalty Goals'] = goalscorers_df ['Non-Penalty Goals'].fillna(0).astype(int)

        # Create column for number of penalty goals scored
        goalscorers_df ['Penalty Goals'] = abs(goalscorers_df ['Goals Scored'] - goalscorers_df ['Non-Penalty Goals'])

        # Sort dataframes by trophies won in descending order
        goalscorers_df = goalscorers_df.sort_values(by='Goals Scored', ascending=False).reset_index(drop=True)

        # Create a column to show the Ranking of the goalscorer
        goalscorers_df['Rank'] = goalscorers_df.index + 1

        # Reshuffling the column order
        scorer_rank = goalscorers_df.pop('Rank')
        goalscorers_df.insert(0, 'Rank', scorer_rank)

        # Renaming columns
        goalscorers_df.rename(columns={'Scorer Team': 'Country',
                                       'Scorer': 'Player'}, inplace=True)

        return goalscorers_df
    

    # Top goalscorers of latest tournament
    elif stat == "Top Goalscorers Latest Tournament":
        # Group by scorer and team, count total goals
        total_goals = gs_tournament[(gs_tournament['Own Goal'] == False) & (gs_tournament['Year'] == gs_tournament['Year'].iloc[-1])].groupby(['Scorer', 'Scorer Team']).size().reset_index(name='Goals Scored')

        # Filter non-penalty goals and count them
        non_penalty_goals = gs_tournament[(gs_tournament['Penalty'] == False) & (gs_tournament['Year'] == gs_tournament['Year'].iloc[-1])].groupby(['Scorer', 'Scorer Team']).size().reset_index(name='Non-Penalty Goals')

        # Merge the two dataframes on 'Scorer' and 'Team'
        goalscorers_df = pd.merge(total_goals, non_penalty_goals, on=['Scorer', 'Scorer Team'], how='left')

        # Fill NaN values in 'Non-Penalty Goals' column with 0
        goalscorers_df ['Non-Penalty Goals'] = goalscorers_df ['Non-Penalty Goals'].fillna(0).astype(int)

        # Create column for number of penalty goals scored
        goalscorers_df ['Penalty Goals'] = abs(goalscorers_df ['Goals Scored'] - goalscorers_df ['Non-Penalty Goals'])

        # Sort dataframes by trophies won in descending order
        goalscorers_df = goalscorers_df.sort_values(by='Goals Scored', ascending=False).reset_index(drop=True)

        # Create a column to show the Ranking of the goalscorer
        goalscorers_df['Rank'] = goalscorers_df.index + 1

        # Reshuffling the column order
        scorer_rank = goalscorers_df.pop('Rank')
        goalscorers_df.insert(0, 'Rank', scorer_rank)

        # Renaming columns
        goalscorers_df.rename(columns={'Scorer Team': 'Country',
                                       'Scorer': 'Player'}, inplace=True)

        return goalscorers_df
    

    # Teams with most goals scored
    elif stat == "Teams with Most Goals Scored":
    # Group by scorer and team, count total goals
        total_goals = gs_tournament[gs_tournament['Own Goal'] == False].groupby(['Scorer Team']).size().reset_index(name='Goals Scored')

        # Filter non-penalty goals and count them
        non_penalty_goals = gs_tournament[gs_tournament['Penalty'] == False].groupby(['Scorer Team']).size().reset_index(name='Non-Penalty Goals')

        # Merge the two dataframes on 'Scorer' and 'Team'
        teamgoals_df = pd.merge(total_goals, non_penalty_goals, on=['Scorer Team'], how='left')

        # Fill NaN values in 'Non-Penalty Goals' column with 0
        teamgoals_df ['Non-Penalty Goals'] = teamgoals_df ['Non-Penalty Goals'].fillna(0).astype(int)

        # Create column for number of penalty goals scored
        teamgoals_df ['Penalty Goals'] = abs(teamgoals_df ['Goals Scored'] - teamgoals_df ['Non-Penalty Goals'])

        # Calculating the number of matches played per team
        # Count home matches
        home_matches = rs_tournament['Home Team'].value_counts().reset_index()
        home_matches.columns = ['Scorer Team', 'Home Matches']

        # Count away matches
        away_matches = rs_tournament['Away Team'].value_counts().reset_index()
        away_matches.columns = ['Scorer Team', 'Away Matches']

        # Merge home and away matches
        matches_played_df = pd.merge(home_matches, away_matches, on='Scorer Team', how='outer').fillna(0)

        # Calculate total matches
        matches_played_df['Matches Played'] = matches_played_df['Home Matches'] + matches_played_df['Away Matches']

        teamgoals_df = pd.merge(teamgoals_df, matches_played_df[['Scorer Team', 'Matches Played']], on=['Scorer Team'], how='left')

        # Adding goal per 90 column
        teamgoals_df['Goals per 90'] = round(teamgoals_df['Goals Scored'] / teamgoals_df['Matches Played'], 2)

        # Sort dataframes by trophies won in descending order
        teamgoals_df = teamgoals_df.sort_values(by='Goals Scored', ascending=False).reset_index(drop=True)

        # Reordering the columns
        teamgoals_df = teamgoals_df[['Scorer Team',
                                     'Matches Played',
                                     'Goals Scored',
                                     'Non-Penalty Goals',
                                     'Penalty Goals',
                                     'Goals per 90']]
        
        # Renaming columns
        teamgoals_df.rename(columns={'Scorer Team': 'Country'}, inplace=True)

        # Display the result
        return teamgoals_df
    

    # Teams who have played in most penalty shootouts and their respective success rates
    elif stat == "Pen Shootout Stats":
        # Filter the DataFrame to include only rows where 'Shootout' is True
        shootout_matches = rs_tournament[rs_tournament['Shootout'] == True]

        # Calculate the number of wins and losses
        wins = shootout_matches['Winning Team'].value_counts().reset_index()
        wins.columns = ['Country', 'Wins']

        losses = shootout_matches['Losing Team'].value_counts().reset_index()
        losses.columns = ['Country', 'Losses']

        # Merge the two DataFrames on the 'Team' column
        shootout_appearances = pd.merge(wins, losses, on='Country', how='outer').fillna(0)

        # Calculating the total number of penalty shootouts partcipated in
        shootout_appearances['Penalty Shootouts'] = shootout_appearances['Wins'] + shootout_appearances['Losses']

        # Sort dataframes by trophies won in descending order
        shootout_appearances = shootout_appearances.sort_values(by='Penalty Shootouts', ascending=False)

        # Reshuffling the column order
        pen_shoutout_total = shootout_appearances.pop('Penalty Shootouts')
        shootout_appearances.insert(1, 'Penalty Shootouts', pen_shoutout_total)

        return shootout_appearances
        