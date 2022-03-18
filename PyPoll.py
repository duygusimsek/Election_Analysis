# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize total vote counter
total_votes= 0
#declare an array for candidate options 
candidate_options =[]
#declare an empty dictionary
candidate_votes={}

#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    # To do: read and analyze the data here
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    #to read and print the header row
    headers=next(file_reader)

    #print each row in the CSV file
    for row in file_reader:
        total_votes += 1
        #print the candidate name from each row
        candidate_name = row[2]

        #doesn't match any existing candidate
        if candidate_name not in candidate_options:
            #add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            #tracking each candidates' vote count
            candidate_votes[candidate_name]= 0
        candidate_votes[candidate_name] += 1


#iterate through the candidate list
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage= float(votes/total_votes) * 100
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

   #Determine winning vote count and candidate

    if (votes > winning_count) and (vote_percentage > winning_percentage):
     winning_count = votes
     winning_percentage = vote_percentage
     winning_candidate = candidate_name
     winning_candidate_summary=(
        f"-------------------------\n"
        f"Winner:{winning_candidate}\n"
        f"Winning Vote Count:{winning_count:,}\n"
        f"Winning Percentage:{winning_percentage:.1f}%\n"
        f"-------------------------\n")
print(winning_candidate_summary)
candidate_votes[candidate_name] += 1
