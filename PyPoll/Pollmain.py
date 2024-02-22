import os
import csv

#Set path for csv file
csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")
 
votecount = 0
candidates = {}

with open(csvpath) as csvfile:
    csvread = csv.reader(csvfile, delimiter=",")
    csvhead = next(csvread)
    for row in csvread:
        candidate = str(row[2])
        if candidate not in candidates:
            candidates[candidate]=1
        else:
            candidates[candidate]+=1
        votecount+=1

analysis = os.path.join("PyPoll","PollAnalysis","PollResults.txt")
with open(analysis,'w') as textfile:
    textfile.write("Election Results")
    textfile.write("\n")
    textfile.write("------------------------------")
    textfile.write("\n")
    textfile.write(f"Total Votes: {votecount}")
    textfile.write("\n")
    textfile.write("------------------------------")
    textfile.write("\n")
    for name,value in candidates.items():
        textfile.write(f"{name}: {(value/votecount):.3%} ({value})")
        textfile.write("\n")
    textfile.write("------------------------------")
    textfile.write("\n")
    finaltally = 0
    finalwinner = ""
    for name,value in candidates.items():
        if value > finaltally:
            finaltally = value
            del finalwinner
            finalwinner = name
    textfile.write(f"Winner: {finalwinner}")
    textfile.write("\n")
    textfile.write("------------------------------")