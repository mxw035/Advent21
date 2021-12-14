directions = []

direction = open("directions.txt")

for x in direction:
    directions.append(x)

aim = 0
horizontal = 0
depth = 0

i = 0
while i < len(directions):
    if "forward" in directions[i]:
        line = directions[i].rsplit(" ")
        horizontal = horizontal + int(line[1])
        depth = depth + (int(line[1]) * aim )
    elif "up" in directions[i]:
        line = directions[i].rsplit(" ")
        aim = aim - int(line[1])
    elif "down" in directions[i]:
        line = directions[i].rsplit(" ")
        aim = aim + int(line[1])
    i = i + 1

answer = horizontal * depth
print("Answer", answer)
