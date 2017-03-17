# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv
player = [100000,1]
winner = 'Quakes'
with open('football.csv', 'r') as f:
    next(f)
    csv_f = csv.reader(f)
    for line in f:
        line = line.split(',')
        a = int(line[6])
        b = int(line[7])
        print(line)
        if abs(a - b) < abs(player[0] - player[1]):
            winner = line[0]
            player[0] = a
            player[1] = b      
        
print(winner) 
