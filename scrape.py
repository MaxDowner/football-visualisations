import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# store the url of the webpage containing the desired table in a variable
# use the read_html function to read the table into a list
# store the 0th element of the output list into a dataframe
# print the data frame

advanced_stats_url = "https://fbref.com/en/comps/Big5/2023-2024/keepersadv/players/2023-2024-Big-5-European-Leagues-Stats"
advanced_stats_list = pd.read_html(advanced_stats_url)
advanced_stats_df = advanced_stats_list[0]
# print(advanced_stats_df)
# print(type(advanced_stats_df))

# as above but for basic goalkeeping stats rather than advanced stats

basic_stats_url = "https://fbref.com/en/comps/Big5/2023-2024/keepers/players/2023-2024-Big-5-European-Leagues-Stats"
basic_stats_list = pd.read_html(basic_stats_url)
basic_stats_df = basic_stats_list[0]
# print(basic_stats_df)

# repeated "Unnamed X_level_0", due to how the headers are structured

advanced_stats_df.columns = ['_'.join(col) for col in advanced_stats_df.columns.values]
basic_stats_df.columns = ['_'.join(col) for col in basic_stats_df.columns.values]

advanced_stats_df.drop_duplicates(inplace=True)
basic_stats_df.drop_duplicates(inplace=True)
# print(advanced_stats_df.columns)
# print(basic_stats_df.columns)

# got confused with read_html creating a list of dataframes rather than a dataframe
# print(type()) confirms we have a dataframe now

# access the PSxg-GA column (series?) in advanced_stats_df and assign to a variable
# access the shots faced column (series) in basic_stats_df and assign to a variable
# print(advanced_stats_df.loc[:,"Expected_PSxG/SoT"]) confirmed the correct data

psxg = advanced_stats_df.loc[:,"Expected_PSxG"]
shots_faced = basic_stats_df.loc[:,"Performance_SoTA"]
# print(psxg.shape)
# print(shots_faced)

if psxg.shape == shots_faced.shape:
    print("good to go")

# Plotting

# Setting up the figure
# initialising fig and ax

fig, ax = plt.subplots()
ax.scatter(shots_faced, psxg)
plt.show()

# https://matplotlib.org/stable/tutorials/lifecycle.html

