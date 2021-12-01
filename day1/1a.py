import csv
import sys

measure = []
inc = 0
dec = 0
er = 0
depth = open("index.txt", "r")

for x in depth:
    measure.append(int(x))
i = 0
while i < len(measure):
    c = int(i)
    p = int(i - 1)
    if p >= 0:
        if measure[c] > measure[p]:
            inc = inc + 1
        elif measure[c] < measure[p]:
            dec = dec + 1
        else:
            er = er + 1
    else:
        print("No previous depth")
    i = i + 1
print(inc)




