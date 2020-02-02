# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources" , "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize variables
total_votes = 0
candidate_options = []
candidate_votes = {}
name_exists = False
# Initialize variables for the winning candidate and Winning count tracker
winning_candidate =""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row to skip it
    headers = next(file_reader)
    
    # Loop through the rows in the file
    for row in file_reader:
        total_votes += 1

        candidate_name = row[2]

        # Looking for the unique candidate names
        if candidate_name not in candidate_options:
            # Adding a unique candidate name to the list of candidate names
            candidate_options.append(candidate_name)
            # Begin tracking new candidate's vote count
            candidate_votes[candidate_name] = 0

        # Every row is a +1 vote towards the current candidate
        candidate_votes[candidate_name] += 1

# Loop through {candidate name: votes} dictionary
for candidate in candidate_votes:

    # Retrieve vote count (value) for each candidate (key)
    votes = candidate_votes[candidate]
    # Calculate the percentage of votes.
    vote_percentage = int(votes) / int(total_votes) * 100

    # Print out each candidate's name, vote count and percentage of votes to the terminal.
    print(f"{candidate}: received {votes: ,} votes, which is {vote_percentage: .1f}% of the total vote.\n")

    # Determine winning number of votes and candidate name
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate

# Print out the winning candidate, vote count and percentage to the terminal.
winning_candidate_summary = (
    f"--------------------------------------\n"
    f"Winning candidate: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count: ,}\n"
    f"Winning Percentage: {winning_percentage: .1f}%\n"
    f"--------------------------------------\n")
print(winning_candidate_summary)

# Close the file
#election_data.close()