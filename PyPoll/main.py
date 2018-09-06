import os
import csv
Voter_ID = []
Candidate = []
candidate_list = []
total_votes = 0
candidate_votes = []    
Winner = ""        
election = os.path.join("election_data.csv")
with open (election, newline="") as pypoll:
    electiondata = csv.reader(pypoll, delimiter=",")
    next(electiondata)
    for row in electiondata:
        total_votes += 1
        Voter_ID.append(row[0])
        Candidate.append(row[2])
        if row[2] not in candidate_list:
            candidate_list.append(row[2])

Candidate_1 = [name for name in Candidate if name == candidate_list[0]]
Candidate_2 = [name for name in Candidate if name == candidate_list[1]]
Candidate_3 = [name for name in Candidate if name == candidate_list[2]]
Candidate_4 = [name for name in Candidate if name == candidate_list[3]]
Candidate_1_total = len(Candidate_1)
candidate_votes.append(Candidate_1_total)
Candidate_1_percentage = float((Candidate_1_total/total_votes)*100)
Candidate_2_total = len(Candidate_2)
candidate_votes.append(Candidate_2_total)
Candidate_2_percentage = float((Candidate_2_total/total_votes)*100)
Candidate_3_total = len(Candidate_3)
candidate_votes.append(Candidate_3_total)
Candidate_3_percentage = float((Candidate_3_total/total_votes)*100)
Candidate_4_total = len(Candidate_4)
candidate_votes.append(Candidate_4_total)
Candidate_4_percentage = float((Candidate_4_total/total_votes)*100)


if max(candidate_votes) == Candidate_1_total:
    Winner = candidate_list[0]
elif max(candidate_votes) == Candidate_2_total:
    Winner = candidate_list[1]
elif max(candidate_votes) == Candidate_3_total:
    Winner = candidate_list[2]
else:
    Winner = candidate_list[3]
    
print("Election Results")
print("-----------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------")
print(f"{candidate_list[0]}: {Candidate_1_percentage}% ({Candidate_1_total})")
print(f"{candidate_list[1]}: {Candidate_2_percentage}% ({Candidate_2_total})")
print(f"{candidate_list[2]}: {Candidate_3_percentage}% ({Candidate_3_total})")
print(f"{candidate_list[3]}: {Candidate_4_percentage}% ({Candidate_4_total})")
print("-----------------------------")
print(f"Winner: {Winner}")
print("-----------------------------")