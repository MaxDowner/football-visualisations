import pandas as pd

import matplotlib.pyplot as plt
import numpy as np


# store the url of the webpage containing the desired table in a variable
# use the read_html function to read the table into a list
# store the 0th element of the output list into a dataframe
# print the data frame
# advanced_stats_url = "https://fbref.com/en/comps/Big5/2023-2024/keepersadv/players/2023-2024-Big-5-European-Leagues-Stats"
# advanced_stats_list = pd.read_html(advanced_stats_url)
# advanced_stats_df = advanced_stats_list[0]
# print(advanced_stats_df)
# print(type(advanced_stats_df))

# as above but for basic goalkeeping stats rather than advanced stats
# basic_stats_url = "https://fbref.com/en/comps/Big5/2023-2024/keepers/players/2023-2024-Big-5-European-Leagues-Stats"
# basic_stats_list = pd.read_html(basic_stats_url)
# basic_stats_df = basic_stats_list[0]
# print(basic_stats_df)

# repeated "Unnamed X_level_0", I think due to how the headers are structured

# got confused with read_html creating a list of dataframes rather than a dataframe
# print(type()) confirms we have a dataframe now

# next jobs are
#   access the PSxg-GA column (series?) in advanced_stats_df
#   access the shots faced column (series) in basic_stats_df
# series are nested ('Expected', 'PSxG+/-')

# print(advanced_stats_df.columns.values)


# plot PSxG-GA against shots faced using matplotlib.pyploy

# maybe hack around  for now, bypassing pandas and going from sheets > matplotlib

# Plotting

# Setting up the figure

# initialising fig and ax
fig, ax = plt.subplots()
# plot
# ax.scatter(x, y)

# https://matplotlib.org/stable/tutorials/lifecycle.html

