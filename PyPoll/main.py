import os
import csv

poll_csv = os.path.join("Resources","election_data.csv")

total_votes = 0
canditates_name = []
votes = []
percentage_votes = []
                        
# Open the CSV file
with open(poll_csv, newline='') as csvfile:
    # Create a CSV reader object
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row
    header = next(csvreader)

    for row in csvreader:
    
        # finds total number of votes
        total_votes += 1

        #Complete list of candidate who received votes 
        if row[2] not in canditates_name:
            canditates_name.append(row[2])
            name = canditates_name.index(row[2])
            votes.append(1)
        
        else: 
            name = canditates_name.index(row[2])
            votes[name] += 1

    # Percentage of votes each candidate won
    for voteCount in votes:
        percentage = (voteCount / total_votes) 
        percentage_votes.append(percentage)

    # Winner of the election 
    election_winner = max(votes)
    name = votes.index(election_winner)
    winner = canditates_name[name]





    print(f"Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for x in range(len(canditates_name)):
        print(f"{canditates_name[x]}: {percentage_votes[x]:.3%} ({votes[x]})")
    print("-------------------------")
    print(f"Winner: {winner} ")
    print("-------------------------")


# Outputs resluts to a .txt file in the analysis folder 
    output_file = os.path.join('analysis', 'pyPoll_output.txt')

with open(output_file, "w") as f:
    print(f"Election Results", file=f)
    print("-------------------------", file=f)
    print(f"Total Votes: {total_votes}", file=f)
    print("-------------------------",file=f)
    for x in range(len(canditates_name)):
        print(f"{canditates_name[x]}: {percentage_votes[x]:.3%} ({votes[x]})", file=f)
    print("-------------------------", file=f)
    print(f"Winner: {winner} ", file=f)
    print("-------------------------", file=f)