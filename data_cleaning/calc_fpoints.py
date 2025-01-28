import pandas as pd

def calc_fpoints_batter(data, output=True, path="data/batter_fpoints.csv"):
    """Takes a data frame with base MLB stats and calculates
    fantasy points as a column

    Args:
        data (pd.DataFrame): base MLB stats
        output (bool): whether to export data
        path (string): path to export data to

    Returns:
        pandas data frame w/ fantasy points column
    """
    data = data.rename(columns={"last_name, first_name":"Name", "player_age":"age", "b_rbi":'RBI', 'b_total_bases':'TB', 
                    'r_total_stolen_base':'SB', 'b_game':'G', 'r_run':'R', 'strikeout':'K', 'walk':'BB'})
    data = data.drop(columns = ['player_id'])
    data.head()
    data['Fpoints'] = data['BB'] + data['RBI'] + data['TB'] + data['SB'] + data['R'] - data['K']
    data['Fpoints_G'] = data['Fpoints']/data['G']

    if output:
        data.to_csv(path)

    return data


def calc_fpoints_pitcher(data, output=True, path = "data/pitcher_fpoints.csv"):
    """Takes base pitcher stats and calculates fantasy points 

    Args:
        data (pd.DataFrame): base stats df
        output (bool, optional): whether to export dataframe. Defaults to True.
        path (str, optional): path to export file. Defaults to "data/pitcher_fpoints.csv".

    Returns:
        pd.dataframe: df containing fantasy points
    """
    data = data.rename(columns={"last_name, first_name":"Name", "player_age":"age", "p_earned_run":'ER', 'hit':'H', 
                    'p_save':'S', 'p_win':'W', 'p_loss':'L', 'strikeout':'K', 'walk':'BB', 'p_formatted_ip':'IP', 
                           'p_hold':'Hold'})
    data = data.drop(columns = ['player_id'])

    data['Fpoints'] = 3*data['IP'] + data['K'] - 2*data['ER']  - data['H'] - data['BB']
    data['Fpoints_IP'] = data['Fpoints']/data['IP'] 

    if output:
        data.to_csv(path)

    return data    


