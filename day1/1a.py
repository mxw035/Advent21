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
        print(c)
        print(measure[c])
        print(p)
        print(measure[p])
        if measure[c] > measure[p]:
            print("Increased")
            inc = inc + 1
        elif measure[c] < measure[p]:
            print("Decreased")
            dec = dec + 1
        else:
            print("Same Error")
            er = er + 1
    else:
        print("No previous depth")

    i = i + 1
print(len(measure))
print(inc)
print(dec)
print(er)




