# analysis of Profit lost 
# Geoffrey Flynn 
# 04-05-2021


import os
import csv
from datetime import datetime, date, time

# initialize values
firstdate = datetime.strptime("1-1-9900", "%m-%d-%Y") #date of the first entry
endDate = datetime.strptime("1-1-1900", "%m-%d-%Y") # date of the last transaction
total = 0.0	# Running total
max_profit = 0 # value of the max Profit
max_loss = 0	# value of the max loss
profit_date = datetime.strptime("1-1-9900", "%m-%d-%Y")
loss_date = datetime.strptime("1-1-9900", "%m-%d-%Y")

# path to file to analyse
bank_file = os.path.join( "Resources", "budget_data.csv")

# open the file as a csv file
with open(bank_file,'r') as data_file:
	csv_reader = csv.reader(data_file)
	# read in the header line (no data)
	header = next(csv_reader)
	
	#read the rest of the file and analyse the data
	for row in csv_reader:
		
		#conver the datastring to a datetime object the format is Jan-2021
		aDate = datetime.strptime(row[0], "%b-%Y")
		amount = int(row[1]) # conver the amount from a string to an integer
		total += amount # add the value to the running total
		
		# looking for the earliest date and the latest date
		if aDate < firstdate:
			firstdate = aDate
		elif aDate > endDate:
			endDate = aDate
		
		# finding the max profit and storing it and its date for later
		if amount > max_profit:
			max_profit = amount
			profit_date = aDate
		# finding the max profit and storing it and its date for later
		elif amount < max_loss:
			max_loss = amount
			loss_date = aDate
			
			
# Print the results to the terminal
print(f"{firstdate.strftime('%b-%Y')} to {endDate.strftime('%b-%Y')}")

# calc the differenc in months using the years and months
diff_months = (endDate.year - firstdate.year) * 12 + (endDate.month - firstdate.month)
print(f"Months => {diff_months}")
print(f'The total profit/loss is ${total:,.2f}')
print(f"Average = $ {total / diff_months:,.2f}")

print(f"Max Profit = $ {max_profit:,.2f} on {profit_date.strftime('%b-%Y')}")
print(f"Max Loss = $ {max_loss:,.2f} on {loss_date.strftime('%b-%Y')}")


# Create the output file as a markdown file.

result_path = os.path.join( "analysis", "budget_summary.md")

with open(result_path, 'w') as result_file:
	result_file.write('##Financial Analysis\n')
	result_file.write(f"**{firstdate.strftime('%b-%Y')} to {endDate.strftime('%b-%Y')}** \n\n")
	result_file.write('---\n')
	
	result_file.write(f'The total profit/loss is **${total:,.0f}** over {diff_months} months\n\n')
	result_file.write(f"- Average was $ {total / diff_months:,.2f}\n")
	
	result_file.write(f"- Max Profit was $ {max_profit:,.2f} on {profit_date.strftime('%b-%Y')}\n")
	result_file.write(f"- Max Loss was $ {max_loss:,.2f} on {loss_date.strftime('%b-%Y')}\n")
	