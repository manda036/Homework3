import os
import csv
Voter_ID = []
Candidate = []
election = os.path.join("election_data.csv")
with open (election, newline="") as pypoll:
    electiondata = csv.reader(pypoll, delimiter=",")
    next(electiondata, None)
    total_votes = len(list(electiondata))

with open (election, newline="") as pypoll:
    electiondata = csv.reader(pypoll, delimiter=",")
    for row in electiondata:
        Voter_ID.append(row[0])
        Candidate.append(row[2])
#for name in 
Candidate_1 = [name for name in Candidate if name == candidate_list[0]]
Candidate_2 = [name for name in Candidate if name == candidate_list[1]]
Candidate_3 = [name for name in Candidate if name == candidate_list[2]]
Candidate_4 = [name for name in Candidate if name == candidate_list[3]]
Candidate_1_total = len(Candidate_1)
Candidate_1_percentage = (Candidate_1_total/total_votes)*100
Candidate_2_total = len(Candidate_2)
Candidate_2_percentage = (Candidate_2_total/total_votes)*100
Candidate_3_total = len(Candidate_3)
Candidate_3_percentage = (Candidate_3_total/total_votes)*100
Candidate_4_total = len(Candidate_4)
Candidate_4_percentage = (Candidate_4_total/total_votes)*100

#Figure out how to calculate Winner

print("Election Results")
print("-----------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------")
print(f"{candidate_list[0]}: {Candidate_1_percentage}% ({Candidate_1_total})")
print(f"{candidate_list[1]}: {Candidate_2_percentage}% ({Candidate_2_total})")
print(f"{candidate_list[2]}: {Candidate_3_percentage}% ({Candidate_3_total})")
print(f"{candidate_list[3]}: {Candidate_4_percentage}% ({Candidate_4_total})")
print("-----------------------------")
#print(f"Winner: )