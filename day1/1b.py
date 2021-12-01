import csv
import sys

depth = open("index.txt")

measure = [] 
sumcheck = 0 
results = []
sums = []

for x in depth:
    measure.append(int(x))

length = len(measure)

i = 0

while i <= len(measure)-3:
    r = i + 3
    one = i
    two = i + 1
    three = i + 2
    groupsum = measure[one] + measure[two] + measure[three]
    sums.append(groupsum)
    total = 0
    for s in range(i, r):
        total = total + measure[s]
    sumcheck = total

    results.append(sumcheck)

    i = i + 1
inc = 0
dec = 0
er = 0

g = 0
while g < len(sums):
    if g == 0:
        print("No previous Depth")
    elif g > 0:
        if sums[g] > sums[g-1]:
            inc = inc + 1
        elif sums[g] < sums[g-1]:
            dec = dec + 1
        else:
            er = er + 1
    g = g + 1

print("Increased", inc)
