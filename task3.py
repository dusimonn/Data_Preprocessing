""" 
COMP20008 Semester 2
Assignment 1 Task 3
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 3 - Preliminary Visualisation (1 mark)
def task3(dataset_filename, output_filename):
    # Implement Task 3 here

    data_df = pd.read_csv(dataset_filename)
    
    # Only include articles within 144000 minutes
    criteria = data_df["when"] <= 14400
    data_df = data_df[criteria]
    
    # Plotting the scatterplot
    plt.rcParams["figure.figsize"] = (14, 8)
    plt.rc('font', size=16)
    plt.scatter(x=data_df["when"], y=data_df["views"], s=100, alpha=0.4, c='blue')

    # Add in useful visualisation properties
    plt.grid()
    plt.xlabel("Minutes Since Publication")
    plt.ylabel("Number of Views")
    plt.title("Published Time vs Number of Views")

    # Save as png file
    plt.savefig(output_filename)

    return
