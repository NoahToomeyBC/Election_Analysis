# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize total vote counter
total_votes = 0 
#initialize candidate options list
candidate_options = []
#initialize candidate votes dictionary
candidate_votes = {}
# initialize empty winning candidate
winning_candidate = ""
#initialize winning count, set to 0
winning_count = 0
#initialize winning percentage, set to 0
winning_percentage = 0

# Open the election results and read the file. 
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    #read the header row
    headers = next(file_reader)

    # print each row in the csv file.
    for row in file_reader:

        #Add to the total vote count
        total_votes += 1
        # Print candidate name
        candidate_name = row[2]
        
        if candidate_name not in candidate_options:
            #add candidate name to candidate list
            candidate_options.append(candidate_name)

            #begin tracking the candidate's vote count
            candidate_votes[candidate_name] = 0
        #add a vote to the candidates count
        candidate_votes[candidate_name] +=1


    for candidate_name in candidate_votes:

        votes = candidate_votes[candidate_name]   
        vote_percentage = float(votes) / float(total_votes) * 100
        #determine winning vote count and candidate
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #If true then set winning_count = votes and winning percent = vote percentage
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

#print out total votes candidate name and amount of votes
print(f"Total Votes: {total_votes}")

