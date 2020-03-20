#Brian Parish
#Python Homework
#pyPoll

import csv
import operator

#Create dictionary of candidates with vote tally
votes = {"Khan": 0,
         "Correy": 0,
         "Li": 0,
         "O'Tooley": 0}

with open('Resources/election_data.csv') as input_csv:
    polling_data = csv.reader(input_csv, delimiter=",")
    next(polling_data)
    for vote in polling_data:
        votes[vote[2]] += 1

#Find the winner of the election
Winner = max(votes.items(), key=operator.itemgetter(1))[0]
#total number of votes
count = sum(votes.values())

#Prepare output formatting
output_text =   "\nELECTION RESULTS" + \
                "\n------------------------------" + \
                "\nTotal Votes: " + str(count)
for candidate in votes:
    output_text += "\n" + candidate + ": " + str('{:,.3f}'.format(votes[candidate]/count * 100)) + "% (" + str(votes[candidate]) + ")"

output_text +=  "\n------------------------------" + \
                "\nThe winner is: " + Winner +  \
                "\n------------------------------"

#Write results to console
print(output_text)

#Write results to file
with open("Election results.txt", "w+") as output_file:
    output_file.write(output_text)
    output_file.close()
