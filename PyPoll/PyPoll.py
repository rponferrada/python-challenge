import os
import csv

csvpath = "./Resources/election_data.csv"
with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    
    total_votes = 0
    Khan_votes = 0
    Correy_votes = 0
    Li_votes = 0
    OTooley_votes = 0
    for row in csvreader:
        total_votes = total_votes + 1
        if (row[2] == 'Khan'):
            Khan_votes = Khan_votes + 1
        if (row[2] == 'Correy'):
            Correy_votes = Correy_votes + 1
        if (row[2] == 'Li'):
            Li_votes = Li_votes + 1
        if (row[2] == "O'Tooley"):
            OTooley_votes = OTooley_votes + 1

Khan_percent = Khan_votes / total_votes * 100
Khan_percent = "{:.3f}".format(Khan_percent)
Correy_percent = Correy_votes / total_votes * 100
Correy_percent = "{:.3f}".format(Correy_percent)
Li_percent = Li_votes / total_votes * 100
Li_percent = "{:.3f}".format(Li_percent)
OTooley_percent = OTooley_votes / total_votes * 100
OTooley_percent = "{:.3f}".format(OTooley_percent)

winner = "Khan"
if (Correy_votes > Khan_votes):
    winner = "Correy"
if (Li_votes > Correy_votes):
    winner = "Li"
if (OTooley_votes > Li_votes):
    winner = "O'Tooley"

output = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
    f"Khan: {Khan_percent}% ({Khan_votes})\n"
    f"Correy: {Correy_percent}% ({Correy_votes})\n"
    f"Li: {Li_percent}% ({Li_votes})\n"
    f"OTooley: {OTooley_percent}% ({OTooley_votes})\n"
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n"
)

with open ('./analysis/analysis.txt','w')as f:
    f.write(output)    
print(output)
