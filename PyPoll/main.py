import csv

csvpath = "PyPoll/resources/election_data.csv"

vote_count = 0
candidate_dict = {}


# Open the CSV with UTF-8
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read header row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:

        # count votes 
        vote_count += 1

        # add to dictionary
        candidate = row[2]
        if candidate in candidate_dict.keys():
            candidate_dict[candidate] += 1
        else:
            candidate_dict[candidate] = 1

# create output - used Xpert and Prof
output = f"""Election Results
-------------------------
Total Votes: {vote_count}
-------------------------\n"""

max_candidate = ""
max_votes = 0
for candidate in candidate_dict.keys():
    votes = candidate_dict[candidate]
    percent_votes = (votes / vote_count) * 100

    line = f"{candidate}: {round(percent_votes, 3)}% ({votes})\n"
    output += line

    if votes > max_votes:
        max_candidate = candidate
        max_votes = votes

last_line = f"""-------------------------
Winner: {max_candidate}
-------------------------"""
output += last_line

print(output)

# Generate txt file - assistance from Prof
with(open("output_pypoll.txt", 'w') as f):
    f.write(output)








 



        
        





