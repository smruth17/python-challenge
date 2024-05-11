# Modules
import csv

# Set path for file
csvpath = "PyBank/resources/budget_data.csv"

# variables
month_count = 0
total_profit = 0

# For changes in Profit/Losses
last_month_profit = 0
changes = []
month_changes = []

# Open the CSV with UTF-8 e
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # After header
    for row in csvreader:

        # count months
        month_count = month_count + 1

        # add profit
        total_profit = total_profit + int(row[1])


        # If first row, there is no change
        if (month_count ==1):
            
            last_month_profit = int(row[1])
        else:
            change = int(row[1]) - last_month_profit
            changes.append(change)
            month_changes.append(row[0])
        
            # reset the last month profit 
            last_month_profit = int(row[1])


    ave_change = sum(changes) / len(changes)
   
    max_change = max(changes)
    max_month_indx= changes.index(max_change)
    max_month = month_changes[max_month_indx]

    min_change = min(changes)
    min_month_indx= changes.index(min_change)
    min_month = month_changes[min_month_indx]


    output = f"""Financial Analysis
    ----------------------------
    Total Months: {month_count}
    Total: ${total_profit}
    Average Change: ${round(ave_change,2)}
    Greatest Increase in Profits: {max_month} (${max_change})
    Greatest Decrease in Profits: {min_month} (${min_change})"""

    print(output)

    with(open("output_pybank.txt", 'w') as f):
        f.write(output)
