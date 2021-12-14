directions = []
horizontal = 0
depth = 0

direction = open("directions.txt")

for x in direction:
    directions.append(x)

i=0
while i < len(directions):

    if "forward" in directions[i]:
        line = directions[i].rsplit(" ")
        horizontal = horizontal + int(line[1])
    elif "backward" in directions[i]:
        line = directions[i].rsplit(" ")
        horizontal = horizontal - int(line[1])
    elif "up" in directions[i]:
        line = directions[i].rsplit(" ")
        depth = depth - int(line[1])
    elif "down" in directions[i]:
        line = directions[i].rsplit(" ")
        depth = depth + int(line[1])

    i = i + 1

answer = depth * horizontal
print("Answer", answer)

