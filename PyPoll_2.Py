# Import the csv and os modules
import os
import csv

# Open Election Results csv and assign variable for it
file_to_load = 'Resources/election_results.csv' 

#Open and Read election results
election_data = open(file_to_load, 'r')

# Open the election results and read the file
with open(file_to_load) as election_data:
    print(election_data)
#Close the file
election_data.close

# Create an analysis txt file csv and assign variable for it
file_to_save = 'Analysis/election_analysis.txt' 

#Open and Write election results
with open(file_to_save, 'w') as txt_file:
    #Write three counties to the file
    txt_file.write("Counties in the election\n________________\n\nArapahoe\nDenver\nJefferson")






 



# Data that needs to be gotten
# Total number of votes cast
# List of candidates who received votes
# Total number of votes
# Percentage of votes per candidate
# Total number of votes per candidate
# Winner of the election based on popular vote