""" 
COMP20008 Semester 2
Assignment 1 Task 5
"""

import pandas as pd
import json
import matplotlib.pyplot as plt

NUM_ARTICLE_TITLES = 5

# Reads the df and adds new vocab to dict with associated freq and view_count
def create_vocab_list(my_dict, data_df):

    for i in range(len(data_df)):
        word_list = eval(data_df["words"][i])
        # Only worry about unique words, remove duplicates
        word_list = list(set(word_list)) 
        for word in word_list:
            freq_view = [1, 0]
            # The word is new so add into dict
            if word not in my_dict:
                my_dict[word] = freq_view
                my_dict[word][1] += data_df["views"][i]
            # The world is not new so increase count
            else:
                # Only increase word_freq if it is word first appearance in article
                my_dict[word][0] += 1 
                my_dict[word][1] += data_df["views"][i]
        
    return my_dict

# Remove any words that do not appear more than 5
def remove_rare_vocab(my_dict):

    remove_words = []
    for key, val in my_dict.items():
        if val[0] < NUM_ARTICLE_TITLES:
            remove_words.append(key)

    for word in remove_words:
        del my_dict[word]

    return my_dict

# Finds the associated average view count for each word
def insert_ave_view(my_dict):

    for key, val in my_dict.items():
        ave_view = float(val[1]) / float(val[0])
        my_dict[key] = ave_view

    return my_dict

# Task 5 - Preliminary Analysis (1 mark)
def task5(dataset_filename, json_output_filename, plot_output_filename):
    # Implement Task 5 here

    data_df = pd.read_csv(dataset_filename)
    my_dict = {}

    # Add all the words across articles
    my_dict = create_vocab_list(my_dict, data_df)

    # Extract the strong words
    my_dict = remove_rare_vocab(my_dict)
    
    # Calculate average view per strong word
    my_dict = insert_ave_view(my_dict)

    # Export my_dict to an JSON file
    json.dump(my_dict, open(json_output_filename, "w"))

    sorted_items = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
    top_5 = dict(reversed(sorted_items[0:5]))    

    # Create and save bar chart
    my_df = pd.DataFrame({'word': top_5.keys(), 'average view count': top_5.values()})
    plt.rcParams["figure.figsize"] = (18, 14)
    plt.rc('font', size=16)
    plt.bar(my_df['word'], my_df['average view count'])

    # Add in useful visualisation properties
    plt.xlabel("Highest Average View Words")
    plt.ylabel("Average View Count")
    plt.title("Average Views of Top 5 Words Common Words")
    
    # Save it to output file
    plt.savefig(plot_output_filename)    

    return
