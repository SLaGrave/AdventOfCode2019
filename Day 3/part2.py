
wire1 = list()
wire2 = list()

with open('input1.txt') as infile:
    once = True
    for line in infile:
        if once:
            once = False
            position = (0, 0, 0)
            a = line.split(',')
            for direction in a:
                length = int(direction[1:])
                if direction[0] == 'R':
                    for x in range(length):
                        point = (position[0] + 1, position[1], position[2] + 1)
                        position = point
                        wire1.append(point)
                elif direction[0] == 'L':
                    for x in range(length):
                        point = (position[0] - 1, position[1], position[2] + 1)
                        position = point
                        wire1.append(point)
                elif direction[0] =='U':
                    for x in range(length):
                        point = (position[0], position[1]+1, position[2] + 1)
                        position = point
                        wire1.append(point)
                else:
                    for x in range(length):
                        point = (position[0], position[1] - 1, position[2] + 1)
                        position = point
                        wire1.append(point)
            
        else:
            once = False
            position = (0, 0, 0)
            a = line.split(',')
            for direction in a:
                length = int(direction[1:])
                if direction[0] == 'R':
                    for x in range(length):
                        point = (position[0] + 1, position[1], position[2] + 1)
                        position = point
                        wire2.append(point)
                elif direction[0] == 'L':
                    for x in range(length):
                        point = (position[0] - 1, position[1], position[2] + 1)
                        position = point
                        wire2.append(point)
                elif direction[0] =='U':
                    for x in range(length):
                        point = (position[0], position[1]+1, position[2] + 1)
                        position = point
                        wire2.append(point)
                else:
                    for x in range(length):
                        point = (position[0], position[1] - 1, position[2] + 1)
                        position = point
                        wire2.append(point)


intersections = [(970, 1159), (970, 1387), (1381, 1428), (1381, 1565), (1403, 1850), (1906, 1428), (2072, 1383), (2326, 1383), (2487, 1383), (2511, 1383), (2546, 1383), (3385, 1259), (3791, 1598), (3791, 1974), (4052, 1974), (4303, 1752), (4503, 1752)]
x1 = list()
x2 = list()
for x in wire1:
    if (x[0], x[1]) in intersections:
        x1.append(x)
for x in wire2:
    if (x[0], x[1]) in intersections:
        x2.append(x)
x1 = sorted(x1)
x2 = sorted(x2)

low = 999999999999999999999999999
for i in range (len(x2)):
    q = x1[i][2] + x2[i][2]
    if q < low:
        low = q

print (low)