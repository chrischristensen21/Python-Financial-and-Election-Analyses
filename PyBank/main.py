# Your task is to create a Python script that analyzes the records to calculate each of the following:
    #The total number of months included in the dataset
    #The net total amount of "Profit/Losses" over the entire period
    #The average of the changes in "Profit/Losses" over the entire period
    #The greatest increase in profits (date and amount) over the entire period
    #The greatest decrease in losses (date and amount) over the entire period

import os

import csv

csvpath = os.path.join('Resources', 'budget_data.csv')


with open(csvpath) as csvfile:

  
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    total= 0
    current_month= 0
    previous_month = 0

    total_change = 0
    months = 0
    max_change = 0
    min_change = 999999999999999999
    
    for row in csvreader:

        total= total + int(row[1])

        months = months + 1

        current_month = int(row[1])

        if months > 1:
            change = current_month - previous_month

            total_change = total_change + change

            if change > max_change:
                max_change = change
                max_date = str(row[0])

            if change < min_change:
                min_change = change
                min_date = str(row[0])

        previous_month = int(row[1])

            
    
    average_change = total_change / (months - 1) 

print(f'                          Financial Analysis')
print(f'-----------------------------------------------------------------------')
print(f'Total Months in Period: {months}')
print(f'Sum Total of all Profits and Losses Over Period: ${total}')
print(f'Average Change of Profits and Losses Over Period: ${average_change}')
print(f'Greatest Increase in Profits: {max_date} ${max_change}')
print(f'Greatest Decrease in Profits: {min_date} ${min_change}')
print(f'-----------------------------------------------------------------------')

file_name = "pybank.txt"
with open(file_name, "w") as txt_file:


    txt_file.write(f'                          Financial Analysis\n')
    txt_file.write(f'-----------------------------------------------------------------------\n')
    txt_file.write(f'Total Months in Period: {months}\n')
    txt_file.write(f'Sum Total of all Profits and Losses Over Period: ${total}\n')
    txt_file.write(f'Average Change of Profits and Losses Over Period: ${average_change}\n')
    txt_file.write(f'Greatest Increase in Profits: {max_date} ${max_change}\n')
    txt_file.write(f'Greatest Decrease in Profits: {min_date} ${min_change}\n')
    txt_file.write(f'-----------------------------------------------------------------------\n')
    

