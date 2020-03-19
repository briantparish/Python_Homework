import csv

months = 0
profit = 0
largest_profit = 0
largest_profit_month = ""
largest_loss = 0.
largest_loss_month = ""
average_profit = 0

with open('Resources/budget_data.csv', newline='') as input_csv:
    budget_data = csv.reader(input_csv, delimiter = ',')
    next(budget_data)
    for row in budget_data:
        months += 1
        profit = profit + int(row[1])
        if(int(row[1]) > largest_profit):
            largest_profit = int(row[1])
            largest_profit_month = row
        if(int(row[1]) < largest_loss):
            largest_loss = int(row[1])
            largest_loss_month = row
    average_profit = float(profit / months)

output_text =   "Financial Analysis" + \
                "\n----------------------------" + \
                "\nTotal Months: " + str(months) + \
                "\nTotal: $" + str(profit) + \
                "\nAverage Change: " + '${:,.2f}'.format(average_profit) + \
                "\nGreatest Increase in Profits: " + largest_profit_month[0] + ": ($" + str(largest_profit_month[1]) + ")" + \
                "\nGreatest Decrease in Profits: " + largest_loss_month[0] + ": ($" + str(largest_loss_month[1]) + ")"

print(output_text)

#Write to file
with open("Results.txt", "w+") as output_file:
    output_file.write(output_text)
    output_file.close()
