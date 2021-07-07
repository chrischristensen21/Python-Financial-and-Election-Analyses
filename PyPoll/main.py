import os

import csv

csvpath = os.path.join('Resources', 'election_data.csv')


with open(csvpath) as csvfile:

  
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    candidates = {}
    total_votes = 0
    winner_count = 0
    winner_name = ""
    
    for row in csvreader:
        total_votes = total_votes + 1
        candidate_name = row[2]
        if candidate_name in candidates:
            candidates[candidate_name] = candidates[candidate_name] + 1
        else:
            candidates[candidate_name] = 1

print(f'            Election Results')
print(f'-----------------------------------------')
print(f'Total Number of Votes Cast: {total_votes}')
for key, value in candidates.items():
  if value > winner_count:
    winner_name = key
    winner_count = value
  percent_vote = (value / total_votes) * 100
  percent_vote_rounded = round(percent_vote,4)
  print(f'{key} {percent_vote_rounded} % ({value})')
print(f'-----------------------------------------')  
print(f'Winner: {winner_name} {winner_count}')
print(f'-----------------------------------------')

file_name = "pypoll.txt"
with open(file_name, "w") as txt_file:

  txt_file.write(f'            Election Results\n')
  txt_file.write(f'-----------------------------------------\n')
  txt_file.write(f'Total Number of Votes Cast: {total_votes}\n') 
  txt_file.write(f'{key} {percent_vote_rounded} % ({value})\n')
  txt_file.write(f'-----------------------------------------\n')  
  txt_file.write(f'Winner: {winner_name} {winner_count}\n')
  txt_file.write(f'-----------------------------------------\n')