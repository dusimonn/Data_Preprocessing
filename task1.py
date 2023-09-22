""" 
COMP20008 Semester 2
Assignment 1 Task 1
"""
import pandas as pd

# Task 1 - Summary Statistics (1 mark)
def task1(dataset_filename):
    # Implement Task 1 here

    data_df = pd.read_csv(dataset_filename)
    num_rows = len(data_df) # gives the number of rows
    num_cols = len(data_df.columns) # gives the number of columns

    str_x = "Number of rows: " + str(num_rows)
    str_y = "Number of columns: " + str(num_cols)

    print(str_x)
    print(str_y)

    return [str_x, str_y]
