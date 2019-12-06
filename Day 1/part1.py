import math

masses = list()

with open('input1.txt') as infile:
    for line in infile:
        masses.append(int(line))

runningTotal = 0

for mass in masses:
    fuel = math.floor(mass/3) - 2
    runningTotal += fuel

print(runningTotal)