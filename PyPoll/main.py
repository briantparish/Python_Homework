import csv
import operator

#Create dictionary of candidates with vote tally
votes = {"Khan": 0,
         "Correy": 0,
         "Li": 0,
         "O'Tooley": 0}
count = 0

with open('Resources/election_data.csv', encoding='utf8') as input_csv:
    polling_data = csv.reader(input_csv, delimiter=",")
    next(polling_data)
    for vote in polling_data:
        count += 1
        if(vote[2] == "Khan"):
            votes['Khan'] += 1
        elif(vote[2] == "Correy"):
            votes['Correy'] += 1
        elif(vote[2] == "Li"):
            votes['Li'] += 1
        elif(vote[2] == "O'Tooley"):
           votes["O'Tooley"] += 1

#Find the winner of the election
Winner = max(votes.items(), key=operator.itemgetter(1))[0]

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
