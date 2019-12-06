
small = 147981
large = 691423

running = 0

def fits(i):
    i = str(i)
    match = False
    ascending = True
    for j in range(len(i)):
        try:
            if i[j] == i[j+1]:
                match = True
        except:
            continue
        try:
            if i[j] > i[j+1]:
                ascending = False
        except:
            continue
    return match and ascending
    


for i in range (small, large + 1):
    if fits(i):
        running += 1

print(running)