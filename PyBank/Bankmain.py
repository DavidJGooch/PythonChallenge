import os
import csv

#Set path for csv file
csvpath = os.path.join("PyBank", "Resources", "budget_data.csv")

#Variables
monthtotal = 0
nettotal = 0 
grtincrease = 0
grtdecrease = 0 
grtmonthinc = ""
grtmonthdec = ""
prevmonth = 0
change = 0

with open(csvpath) as csvfile:
    csvread = csv.reader(csvfile, delimiter=",")
    csvhead = next(csvread)
    for row in csvread:
        if prevmonth != 0:
            netchange = (prevmonth - int(row[1])) * -1
            change += netchange
            if netchange > grtincrease:
                grtincrease = netchange
                grtmonthinc = row[0]
            if netchange < grtdecrease:
                grtdecrease = netchange
                grtmonthdec = row[0]
        prevmonth = int(row[1])
        monthtotal +=1
        nettotal += int(row[1])

analysis = os.path.join("PyBank","BankAnalysis","BankResults.txt")

with open(analysis, 'w') as textfile:
    textfile.write("Financial Analysis")
    textfile.write('\n')
    textfile.write("-----------------------------------")
    textfile.write('\n')
    textfile.write(f'Total Months: {monthtotal}')
    textfile.write('\n')
    textfile.write(f'Total: ${nettotal}')
    textfile.write('\n')
    textfile.write(f'Average Change: ${round(change/(monthtotal - 1),2)}')
    textfile.write('\n')
    textfile.write(f'Greatest Increase in Profits: {grtmonthinc} (${grtincrease})')
    textfile.write('\n')
    textfile.write(f'Greatest Decrease in Profits: {grtmonthdec} (${grtdecrease})')
