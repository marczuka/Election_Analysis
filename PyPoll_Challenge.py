# The data we need to retrieve:
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
# 6. A complete list of counties contributed to the election.
# 7. The total number of votes cast for each county.
# 8. The percentage of votes cast for each county from the total vote count.
# 9. The county that had the largest voter turnout.

import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources" , "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize variables for the candidates and the votes they received
total_votes = 0
candidate_options = []
candidate_votes = {}
# Initialize variables for the winning candidate and Winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Initialize variables to store counties and the votes cast for each county
county_list = []
county_votes = {}
# Initialize variables for the county with the largest turnout and votes tracker
largest_county_turnout = ""
largest_county_count = 0
largest_county_percentage = 0

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
        county_name = row[1]

        # Looking for the unique candidate names
        if candidate_name not in candidate_options:
            # Adding a unique candidate name to the list of candidate names
            candidate_options.append(candidate_name)
            # Begin tracking new candidate's vote count
            candidate_votes[candidate_name] = 0
        
        # Looking for the unique county names
        if county_name not in county_list:
            # Adding unique county name to the county list
            county_list.append(county_name)
            # Begin tracking votes for that county
            county_votes[county_name] = 0

        # Every row is a +1 vote towards the current candidate
        candidate_votes[candidate_name] += 1
        # Every row in a source file is also a +1 vote for the current county
        county_votes[county_name] += 1

with open(file_to_save, "w") as txt_file:

    # Print final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes: ,}\n"
        f"-------------------------\n"
        f"\nCounty Votes:\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Loop through {county name: votes} dictionary
    for county in county_votes:

        # Retrieve vote count (value) for each county (key)
        votes_cnt = county_votes[county]
        # Calculate the percentage of votes for each county
        vote_percentage_cnt = int(votes_cnt) / int(total_votes) * 100

        # Print out each county name, vote count and percentage of votes for the county to the terminal.
        county_results = (f"{county}: {vote_percentage_cnt: .1f}% ({votes_cnt: ,})\n")
        print(county_results)
        # Save the county results to the text file.
        txt_file.write(county_results)

        # Determine winning number of votes and the largest county turnout
        if (votes_cnt > largest_county_count) and (vote_percentage_cnt > largest_county_percentage):
            # Assign new largest values to the county votes and percentage
            largest_county_count = votes_cnt
            largest_county_percentage = vote_percentage_cnt
            largest_county_turnout = county

    # Print out the county name with the largest voter turnout
    largest_county_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {largest_county_turnout}\n"
        f"-------------------------\n")
    print(largest_county_summary)
    # Save the county name with the largest voter turnout to the text file
    txt_file.write(largest_county_summary)

    # Loop through {candidate name: votes} dictionary
    for candidate in candidate_votes:

        # Retrieve vote count (value) for each candidate (key)
        votes = candidate_votes[candidate]
        # Calculate the percentage of votes.
        vote_percentage = int(votes) / int(total_votes) * 100

        # Print out each candidate's name, vote count and percentage of votes to the terminal.
        candidate_results = (f"{candidate}: {vote_percentage: .1f}% ({votes: ,})\n")
        print(candidate_results)
        # Save the candidate results to the text file.
        txt_file.write(candidate_results)

        # Determine winning number of votes and candidate name
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate

    # Print out the winning candidate, vote count and percentage to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count: ,}\n"
        f"Winning Percentage: {winning_percentage: .1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary, end = "")
    # Save the winning candidate, vote count and percentage to the text file.
    txt_file.write(winning_candidate_summary)
    