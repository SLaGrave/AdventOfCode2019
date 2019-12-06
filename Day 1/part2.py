import math

def fuelCalc(mass):
    fuel = math.floor(mass/3) - 2
    fuel = max(0, fuel)
    return fuel

masses = list()

with open('input1.txt') as infile:
    for line in infile:
        masses.append(int(line))
    
bigtotalfuel = 0
    
for mass in masses:
    fuel = 1
    totalFuel = 0
    while(fuel > 0):
        fuel = fuelCalc(mass)
        totalFuel += fuel
        mass = fuel
    bigtotalfuel += totalFuel

print(bigtotalfuel)