import csv
import matplotlib.pyploy as plt
games = []
record = []
wins = 0

f = open('cardinals34.csv')
for row in csv.reader(f):
    if not row[0].isdigit():
        continue
    if row[6].startswith('W') and row[13] == "Dean":
        wins += 1
        games.append(int(row[0]))
        record.append(wins)
plt.title('Dean Brothers progress toward 49 wins')
plt.xlabel('Game number')
plt.ylabel('Win count')
plt.plot(games,record,'r+')
plt.savefig(games.pdf)
