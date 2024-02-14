import streamlit as st
import pandas as pd
import plotly.graph_objs as go



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
            fig_host_trophies.update_layout(barmode='overlay', yaxis_title='Number of Titles')

            return fig_host_trophies


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
            fig_host_trophies.update_layout(barmode='overlay', yaxis_title='Number of Titles')

            return fig_host_trophies


    # Update layout settings
    fig_trophies.update_layout(xaxis_title='No. of Trophies Won',
                               barmode='overlay',
                               )
        
    fig_trophies.update_layout(dragmode=False)
    # st.plotly_chart(fig_trophies)
    return fig_trophies



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
        fig_goals.add_trace(go.Scatter(x=tournament_goals.index, y=tournament_goals['Goals Scored'], mode='lines+markers', name=tournament_name))
 

    # Update layout settings
    fig_goals.update_layout(xaxis_title='Year', 
                      yaxis_title='Goals Scored',
                      margin={"r": 20, "t": 20, "b": 20}
                      )

    return fig_goals