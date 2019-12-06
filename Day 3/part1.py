
wire1 = list()
wire2 = list()

with open('input1.txt') as infile:
    once = True
    for line in infile:
        if once:
            once = False
            position = (0, 0)
            a = line.split(',')
            for direction in a:
                length = int(direction[1:])
                if direction[0] == 'R':
                    for x in range(length):
                        point = (position[0] + 1, position[1])
                        position = point
                        wire1.append(point)
                elif direction[0] == 'L':
                    for x in range(length):
                        point = (position[0] - 1, position[1])
                        position = point
                        wire1.append(point)
                elif direction[0] =='U':
                    for x in range(length):
                        point = (position[0], position[1]+1)
                        position = point
                        wire1.append(point)
                else:
                    for x in range(length):
                        point = (position[0], position[1] - 1)
                        position = point
                        wire1.append(point)
            
        else:
            once = False
            position = (0, 0)
            a = line.split(',')
            for direction in a:
                length = int(direction[1:])
                if direction[0] == 'R':
                    for x in range(length):
                        point = (position[0] + 1, position[1])
                        position = point
                        wire2.append(point)
                elif direction[0] == 'L':
                    for x in range(length):
                        point = (position[0] - 1, position[1])
                        position = point
                        wire2.append(point)
                elif direction[0] =='U':
                    for x in range(length):
                        point = (position[0], position[1]+1)
                        position = point
                        wire2.append(point)
                else:
                    for x in range(length):
                        point = (position[0], position[1] - 1)
                        position = point
                        wire2.append(point)


intersections = set(wire1) & set(wire2)
intersections = sorted(list(intersections))

intersections = list(intersections)

print(intersections)

low = 10000000000000000000000

for v in intersections:
    x = v[0] + v[1]
    if x < low:
        low = x

print(low)