import os
import csv

# Path to the CSV file
bank_csv = os.path.join("Resources", "budget_data.csv")

# Set Variable and lists
total_months = 0
total_pl = 0
previous_pl= 0
changes_list = []
months = []
total_change = 0




# Open the CSV file
with open(bank_csv, newline='') as csvfile:
    # Create a CSV reader object
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row
    header = next(csvreader)
    

    for row in csvreader:
    
        # finds total number of months
        total_months += 1

        # total amount of profit/losses over the period 
        pl = int(row[1])
        total_pl += pl

        # Average profit/loss
        if previous_pl != 0:
            changes_pl = pl - previous_pl
            changes_list.append(changes_pl)
            months.append(row[0])
            total_change += changes_pl

        previous_pl = pl

    average = total_change / (total_months - 1)

    # Greatest Increase
    great_inc = max(changes_list)
    great_inc_month = months[changes_list.index(great_inc)]

    # Greates Decrease
    great_dec = min(changes_list)
    great_dec_month = months[changes_list.index(great_dec)]

            

    print("Financial Analysis")

    print("----------------------------")

    print(f"Total Months: {total_months}")
    print(f"Total is ${total_pl}")
    print(f'Average Change: ${average:.2f}')
    print(f'Greatest Increase in Profits: {great_inc_month} (${great_inc})')   
    print(f'Greatest Decrease in Profits: {great_dec_month} (${great_dec})')

# Outputs the results in a .txt file in the analysis folder

output_file = os.path.join('analysis', 'pyBank_output.txt')

with open(output_file, "w") as f:
    print("Financial Analysis", file=f)

    print("----------------------------", file=f)

    print(f"Total Months: {total_months}", file=f)
    print(f"Total is ${total_pl}")
    print(f'Average Change: ${average:.2f}', file=f)
    print(f'Greatest Increase in Profits: {great_inc_month} (${great_inc})', file=f)   
    print(f'Greatest Decrease in Profits: {great_dec_month} (${great_dec})', file=f)








