# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

import datetime

now = datetime.datetime.now()
print("The time right now is,", now)

import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources" , "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Using the with statement open the file as a text file
#with open(file_to_save, "w") as txt_file:
#    txt_file.write("Counties in the Election\n")
#    txt_file.write("------------------------\n")
#    txt_file.write("Arapahoe\nDenver\nJefferson")

# Open the election results and read the file
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row
    headers = next(file_reader)
    print(headers)

# Close the file
#election_data.close()