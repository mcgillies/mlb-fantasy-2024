import pandas as pd

def combine_metrics_stats(stats, metrics, save=True):
    """Combined the metrics from the previous year with the fantasy points - to predict fantasy points from previous 
    years metrics. 

    Args:
        stats (df): base stats for batters
        metrics (df): metrics for batter
        save (bool, optional): whether to save file. Defaults to True.

    Returns:
        _type_: dataframe 
    """

    metrics = metrics.rename(columns = {'last_name, first_name':'Name'})
    metrics = metrics.drop(columns = ['player_id'])
    metrics['year'] = metrics['year'] + 1
    metrics = metrics[metrics['year'] < 2024]
    stats = stats[stats['year'] > 2015]
    fpts = stats[['Name','Fpoints_G', 'year', 'age']]
    both = fpts.merge(metrics, on = ['Name', 'year'])

    if save:
        both.to_csv("data/batter_combined.csv")

    return both


def pitch_combine_metrics_stats(stats, metrics, save = True):
    """Combine pitcher fantasy points and metrics from the previous season. 

    Args:
        stats (df): pitcher base stats
        metrics (df): pitcher metrics
        save (bool, optional): whether to save the resulting df. Defaults to True.

    Returns:
        _type_: dataframe containing pitcher metrics and fantasy points
    """
    metrics = metrics.rename(columns = {'last_name, first_name':'Name'})
    metrics = metrics.drop(columns = ['player_id'])
    metrics['year'] = metrics['year'] + 1
    metrics = metrics[metrics['year'] < 2024]
    stats = stats[stats['year'] > 2015]
    fpts = stats[['Name','Fpoints_IP', 'year', 'age']]
    both = fpts.merge(metrics, on = ['Name', 'year'])
    if save:
        both.to_csv("data/pitcher_combined.csv")
    return both

