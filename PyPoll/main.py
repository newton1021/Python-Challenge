# elections results

#import modules
import os
import csv

# create a dictionary to store the votes by candidates
votes = dict()
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
		
		#Parse out the row date (ID,county, candidate)
        # only need the candidate name
		#voterID = row[0]
		#county = row[1]
		candidate = row[2]
		total_votes += 1
		
        # of the candidate has been added to the dictionary
        # increase the value by one
        # else add it to the dictionary with a value of 1
		if candidate in votes:
			votes[candidate] += 1
		else:
			votes[candidate] = 1
		
mostVotes = 0
winner = ""

#Print results to the teminal
print('Election Results')
print(f'Total Votes {total_votes:,}')
for candidate in votes:
	num_votes = votes[candidate]
	if num_votes > mostVotes:
		mostVotes = num_votes
		winner = candidate
	
	print(f'{candidate:12} had {num_votes:10,} votes or {(num_votes/total_votes * 100):4.1f}%' )

print(f'The winner was {winner} with {mostVotes:,} votes')


# output the result to an md file

result_path = os.path.join( "analysis", "election_results.md")

with open(result_path, 'w') as result_file:
	result_file.write('##Election Results\n\n')
	result_file.write('___\n\n')
	result_file.write(f'Total Votes {total_votes:,}\n\n')
	
	result_file.write(f'|Candidate | % Votes  |Votes|\n')
	result_file.write(f'|----- | -----: |-----:|\n')
	
	for candidate in votes:
		num_votes = votes[candidate]
		result_file.write(f'|{candidate:12} | {(num_votes/total_votes * 100):4.1f}% | {num_votes:10,}|\n' )
		
	result_file.write(f'\nThe winner was {winner} with {mostVotes:,} votes')
	
