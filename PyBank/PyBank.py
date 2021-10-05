import os
import csv

csvpath = "./Resources/budget_data.csv"
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    total_months = 0
    total = 0
    average = 0
    prev_value = 0
    curr_value = 0
    great_inc = 0
    great_dec = 0
    for row in csvreader:
        total_months = total_months + 1
        total = total + int(row[1])
        curr_value = int(row[1])
        if (prev_value != 0): 
            average = average + curr_value - prev_value
            if ((curr_value - prev_value) > great_inc):
                great_inc = curr_value - prev_value
                month_inc = row[0]
            if ((curr_value - prev_value) < great_dec):
                great_dec = curr_value - prev_value
                month_dec = row[0] 
        prev_value = int(row[1])
    average = average / (total_months - 1)

with open ('./analysis/analysis.txt','w')as f:
    f.write('Financial Analysis')
    f.write('\n')
    f.write('---------------------------')
    f.write('\n')
    f.write('Total Months: ')
    f.write(str(total_months))
    f.write('\n')
    f.write('Total: $')
    f.write(str(total))
    f.write('\n')
    f.write('Average Change: $')
    f.write("{:.2f}".format(average))
    f.write('\n')
    f.write('Greatest Increase in Profits: ')
    f.write(str(month_inc))
    f.write(' ($')
    f.write(str(great_inc))
    f.write(')')
    f.write('\n')
    f.write('Greatest Decrease in Profits: ')
    f.write(str(month_dec))
    f.write(' ($')
    f.write(str(great_dec))
    f.write(')')

print('Financial Analysis')
print('---------------------------')
print('Total Months: ', total_months)
print('Total: $', total)
print('Average Change: $', '{:.2f}'.format(average))
print('Greatest Increase in Profits: ', month_inc, ' ($', great_inc, ')')
print('Greatest Decrease in Profits: ', month_dec, ' ($', great_dec, ')')
