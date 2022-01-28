import os
import csv

#CSV File Path

csvpath = os.path.join('budget_data.csv')

#Variables
total_months = 0
total_revenue =0
changes =[]
date_count = []
greatest_inc = 0
greatest_inc_month = 0
greatest_dec = 0
greatest_dec_month = 0

# Open CSV
with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)
    row = next(csvreader)
# Total months and total revenue
    previous_profit = int(row[1])
    total_months = total_months + 1
    total_revenue = total_revenue + int(row[1])
    greatest_inc = int(row[1])
    greatest_inc_month = row[0]

    for row in csvreader:
 
        total_months = total_months + 1
        total_revenue = total_revenue + int(row[1])
        
        #Greatest increase
        if int(row[1]) > greatest_inc:
            greatest_inc = int(row[1])
            greatest_inc_month = row[0]
            
        #Greatest decrease
        if int(row[1]) < greatest_dec:
            greatest_dec = int(row[1])
            greatest_dec_month = row[0]  

        # Month to month changes
        change = int(row[1]) - previous_profit
        changes.append(change)
        previous_profit = int(row[1])
        date_count.append(row[0])
      
    # Average and date
    average_change = sum(changes)/len(changes)

    high = max(changes)
    low = min(changes)

    #Printing
    print("Financial Analysis")
    print("Total Months:" + str(total_months))
    print("Total Amount:" + str(total_revenue))
    print(average_change)
    print(greatest_inc_month, max(changes))
    print(greatest_dec_month, min(changes))