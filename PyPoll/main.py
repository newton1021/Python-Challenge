# elections results


import os
import csv

candidates = dict()
total_votes = 0
# path to file to analyse
source_file = os.path.join( "Resources", "election_data.csv")

# open the file as a csv file
with open(source_file,'r') as data_file:
	csv_reader = csv.reader(data_file)
	# read in the header line (no data)
	header = next(csv_reader)
	
	#read the rest of the file and analyse the data
	for row in csv_reader:
		
		#conver the datastring to a datetime object the format is Jan-2021
		voterID = row[0]
		county = row[1]
		candidate = row[2]
		total_votes += 1
		
		if candidate in candidates:
			candidates[candidate] += 1
		else:
			candidates[candidate] = 1
		
mostVotes = 0
winner = ""

#Print results to the teminal
print('Election Results')
print(f'Total Votes {total_votes:,}')
for candidate in candidates:
	votes = candidates[candidate]
	if votes > mostVotes:
		mostVotes = votes
		winner = candidate
	
	print(f'{candidate:12} had {votes:10,} votes or {(votes/total_votes * 100):4.1f}%' )

print(f'The winner was {winner} with {mostVotes:,} votes')


# output the result to an md file

result_path = os.path.join( "analysis", "election_results.md")

with open(result_path, 'w') as result_file:
	result_file.write('##Election Results\n\n')
	result_file.write('___\n\n')
	result_file.write(f'Total Votes {total_votes:,}\n\n')
	
	result_file.write(f'|Candidate | % Votes  |Votes|\n')
	result_file.write(f'|----- | -----: |-----:|\n')
	
	for candidate in candidates:
		votes = candidates[candidate]
		if votes > mostVotes:
			mostVotes = votes
			winner = candidate
			
		result_file.write(f'|{candidate:12} | {(votes/total_votes * 100):4.1f}% | {votes:10,}|\n' )
		
	result_file.write(f'\nThe winner was {winner} with {mostVotes:,} votes')
	