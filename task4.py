""" 
COMP20008 Semester 2
Assignment 1 Task 4
"""

import re
import pandas as pd

# Processes the old title and returns a list of tokens
def process_title(data_title):
    target = r"[^A-Za-z\s]"
    replace = r""

    # Remove all non-alpha character except \s
    new_title = re.sub(target, replace, data_title)

    # Convert to lowercase
    new_title = new_title.lower()

    # Tokenize the title
    token_list = new_title.split()

    return token_list

# Task 4 - Text Preprocessing (1 mark)
def task4(dataset_filename, output_filename):
    # Implement Task 4 here

    data_df = pd.read_csv(dataset_filename)

    # Create the new "words" column
    data_df["words"] = data_df["title"].apply(process_title)
    
    # Save to output file
    data_df.to_csv(output_filename, index=False)
    
    return
