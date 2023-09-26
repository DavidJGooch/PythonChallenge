import os
import csv

#Set path for csv file
csvpath = os.path.join("PyBank", "Resources", "budget_data.csv")
 
#initialize variables
monthcount = 0
total_profit = 0
profit_loss = []
#Open and read csv file
with open(csvpath) as csv_file:
    Bankcsv = csv.reader(csv_file, delimiter=",")
    #Skip header row
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")
   #Count row number 
    for row in Bankcsv:
        monthcount += 1
#print total months
print("Total Months:", monthcount)

#Total Profit/Loss:
with open(csvpath) as csv_file:
    Bankcsv = csv.reader(csv_file, delimiter=",")
    #Skip header row
    csv_header = next(csv_file)
    total = sum(int(r[1]) for r in csv.reader(csv_file))
print("Total:", total)
