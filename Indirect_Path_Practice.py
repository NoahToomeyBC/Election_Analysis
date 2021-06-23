import os
import csv
os.path.join("Resources", "election_results.csv")
# Assign a vartiable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
#Open and read election results file
with open(file_to_load) as election_data:
    #print the data
    print(election_data)