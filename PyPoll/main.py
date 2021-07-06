import os

import csv

csvpath = os.path.join('Resources', 'election_data.csv')


with open(csvpath) as csvfile:

  
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    total_votes = 0
    
    for row in csvreader:
        total_votes = total_votes + 1

print(f'            Election Results')
print(f'-----------------------------------------')
print(f'Total Number of Votes Cast: {total_votes}')
print(f'------------------------------------------')
print(f'Khan:')
print(f'Correy:')
print(f'Li:')
print(f"O'Tooley:")
print(f'-----------------------------------------')
print(f'Winner:')
print(f'-----------------------------------------')
