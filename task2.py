""" 
COMP20008 Semester 2
Assignment 1 Task 2
"""
import pandas as pd

MINUTE = 60
HOUR = 24
DAY = 7
MONTH = 30
ERROR = -1

# converts the 'when' value into minutes
def convert_to_minutes(time_val, time_unit):

    # need to account for plural/singular, e.g. hour and hours
    if "minute" in time_unit:
        num_minutes = time_val
    elif "hour" in time_unit:
        num_minutes = time_val * MINUTE
    elif "day" in time_unit:
        num_minutes = time_val * HOUR * MINUTE
    elif "week" in time_unit:
        num_minutes = time_val * DAY * HOUR * MINUTE
    elif "month" in time_unit:
        num_minutes = time_val * MONTH * HOUR * MINUTE
    else:
        # should not reach here, simply a flag check
        num_minutes = ERROR
        print("error: this should not have happened")

    return num_minutes

def convert_view(view_unit, view_val):

    if view_unit == 'K':
        num_views = float(view_val[0:-1]) * 1000
    elif view_unit == 'M':
        num_views = float(view_val[0:-1]) * 1000 * 1000
    else:
        # should not reach here, simply a flag check
        num_views = ERROR

    return int(num_views)


# Task 2 - Data Cleaning (2 marks)
def task2(dataset_filename, output_filename):
    # Implement Task 2 here

    data_df = pd.read_csv(dataset_filename)
    
    for row in range(len(data_df)):
        # Clean up the 'views' column
        views_lst = data_df["views"][row].split()
        view_val = views_lst[0]
        view_unit = views_lst[0][-1]
        num_views = convert_view(view_unit, view_val)
        data_df["views"][row] = int(num_views)

        # Clean up the 'when' column
        when_lst = data_df["when"][row].split()
        time_val = int(when_lst[0])
        time_unit = when_lst[1]
        num_minutes = convert_to_minutes(time_val, time_unit)
        data_df["when"][row] = num_minutes
        
    # Write the cleaned df to a new csv file
    data_df.to_csv(output_filename, index=False)

    return


