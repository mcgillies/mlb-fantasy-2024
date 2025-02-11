import seaborn as sns
from pandas.plotting import scatter_matrix
import numpy as np
def plot_top_x_corr(data, num, type, col):

    numeric_data = data.select_dtypes(include=[np.number])
    correlations = numeric_data.corr()[col].abs().sort_values(ascending=False)
    top_cols = correlations.iloc[1:num].index  
    if type == "scatter":
        scatter_matrix(data[top_cols], figsize=(12, 12), diagonal='kde', alpha=0.5)
    elif type == "correlation":
        sns.heatmap(data[top_cols].corr(), annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
    else: 
        raise Exception("This is not a valid type")
        Exception("This is not a valid type")