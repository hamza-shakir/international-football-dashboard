import pandas as pd

# processing results and penalty shootouts data
def results_data(results_df, shootouts_df):

    '''
    Let us add a new column in the shootouts dataframe which will come in handy post-merging. 
    This column will tell us if the match was extended for a penalty shootout or not.
    '''
    shootouts_df['shootout'] = True

    '''
    The 'first_shooter' column contains a lot of incomplete and inconsistent data,
    hence we wshall drop it to avoid confusion later on in our analysis.
    '''
    shootouts_df = shootouts_df.drop(columns = ['first_shooter'])

    '''
    Now let us merge both the dataframes to combine shooutout results. 
    This way we do not have to hop between two dataframes again and again as all data is in one dataframe.
    '''
    rs = pd.merge(results_df, shootouts_df, how = 'outer', on = ['date', 'home_team', 'away_team'])

    '''
    Our data looks good but now it looks like we have some null values that need to be addressed.
    On top of that we also seem to have a row with a lot of incomplete data. 
    It would be best for us to drop the that row (last row) in the dataframe as it seems 
    to be an outlier and won't have any impact on our analysis.
    '''
    rs.dropna(subset=['tournament'], inplace=True)

 
    # Let us rename the columns for consistency
    rs.rename(columns = {'date':'Date',
                        'home_team':'Home Team',
                        'away_team':'Away Team',
                        'home_score':'Home Score',
                        'away_score':'Away Score',
                        'tournament':'Tournament',
                        'city':'City',
                        'country':'Country',
                        'neutral':'Neutral Venue',
                        'winner':'Winning Team',
                        'shootout':'Shootout'
                        }, inplace = True)
    

    # changing date format from 'object' to 'datetime'
    rs['Date'] = pd.to_datetime(rs['Date'])

    # adding a new column 'year' by splitting the 'date' column
    rs['Year'] = pd.DatetimeIndex(rs['Date']).year


    # We shall now creating a column that displays the outcome of the match such as who won, lost or drew the game

    # winning team
    rs.loc[rs['Home Score'] > rs['Away Score'], 'Winning Team'] = rs['Home Team']
    rs.loc[rs['Home Score'] < rs['Away Score'], 'Winning Team'] = rs['Away Team']

    # losing team
    rs.loc[rs['Home Team']== rs['Winning Team'], 'Losing Team'] = rs['Away Team']
    rs.loc[rs['Away Team'] == rs['Winning Team'], 'Losing Team'] = rs['Home Team']


    # Replacing NULL values wherever necessary
    # rs['Winning Team'].fillna('Draw', inplace = True)
    # rs['Shootout'].fillna(False, inplace = True)
    # rs['Losing Team'].fillna('Draw', inplace = True)
    rs['Winning Team'] = rs['Winning Team'].fillna('Draw')
    rs['Shootout'] = rs['Shootout'].fillna(False)
    rs['Losing Team'] = rs['Losing Team'].fillna('Draw')


    '''
    Correcting error(s) in the outcome of a game that was missing in the extracted data. 
    Even though the game between Morocco and Guinea ended in a draw it resulted in Morocco 
    winning AFCON that year since the format back then did not feature knockout games hence 
    Morocco won the tournament as a result of finishing top of the group. The draw against Guinea 
    gave them that crucial point which meant they were AFCON champions.
    '''
    rs.loc[rs.Date == '1976-03-14', 'Winning Team'] = 'Morocco'
    rs.loc[rs.Date == '1976-03-14', 'Losing Team'] = 'Guinea'

    # Let us reposition the 'Year' and 'Shootout' columns for better visual understanding
    year = rs.pop('Year')
    rs.insert(0, 'Year', year)
    shootout = rs.pop('Shootout')
    rs.insert(6, 'Shootout', shootout)

    # Assigning unique IDs for each match
    rs['Match ID'] = rs.index
    match_id = rs.pop('Match ID')
    rs.insert(2, 'Match ID', match_id)

    return rs


# processing goalscorers' data
def goalscorers_data(goalscorers_df, rs):

    # renaming columns to maintain consistency
    goalscorers_df.rename(columns = {'date':'Date',
                        'home_team':'Home Team',
                        'away_team':'Away Team',
                        'team':'Scorer Team',
                        'scorer':'Scorer',
                        'minute':'Minute',
                        'own_goal':'Own Goal',
                        'penalty':'Penalty'
                        }, inplace = True)
    
    # changing date format from 'object' to 'datetime'
    goalscorers_df['Date'] = pd.to_datetime(goalscorers_df['Date'])

    # adding a new column 'year' by splitting the 'date' column
    goalscorers_df['Year'] = pd.DatetimeIndex(goalscorers_df['Date']).year

    # Let us reposition the 'Year' column for better visual understanding
    year = goalscorers_df.pop('Year')
    goalscorers_df.insert(0, 'Year', year)

    # merging goalscorers' data and results data
    gs = pd.merge(goalscorers_df, rs, how = 'outer', on = ['Year', 'Date', 'Home Team', 'Away Team'])

    # dropping columns that are irrelevant to this dataframe
    # gs = gs.drop(columns = ['Shootout'])

    return gs