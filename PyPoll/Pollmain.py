import os
import csv

#Set path for csv file
csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")
 
#Total Months:
#initialize month count
votecount = 0
#Open and read csv file
with open(csvpath) as csv_file:
    Pollcsv = csv.reader(csv_file, delimiter=",")
    #Skip header row
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")
   #Count row number 
    for row in Pollcsv:
        votecount += 1
#print total months
print("Total Votes:", votecount)


