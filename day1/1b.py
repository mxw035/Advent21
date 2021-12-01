import csv
import sys

#opens the index.txt which is the input depths
depth = open("index.txt")

#defines global var used for the problem
measure = [] # will be the array the entire 2000 depth points are stored
sumcheck = 0 # sets the sumcheck to 0 so that the sum of the groups of threes can be added
results = [] # where the total from sum check can be stored, aka all 666 sums
sums = []

#for loop that looks at each line in depth and adds them to the measure array
for x in depth:
    # x should be value 0 - 1999 adding all 2000 to the measure array
    measure.append(int(x))


# checks the length of the array which is 2000
length = len(measure)

#starts a while loop that will look at five groups only to test code and then will be changed to look through groupNum
i = 0
#while i <= 5:
# while less than or equal to 666 looks at all groups

while i <= len(measure)-3:
    # r is i + 3 so example is 0 + 3 r would be 3 when testing the greatest s value should be 8
    r = i + 3
    one = i
    two = i + 1
    three = i + 2
    #print("One", measure[i])
    #print("Two", measure[i+1])
    #print("Three", measure[i+2])
    groupsum = measure[one] + measure[two] + measure[three]
    sums.append(groupsum)
    # uses i and r to group numbers into groups of three
    # s is the things in the array from i to r
    # sets total to 0 so that the values can be added
    total = 0
    for s in range(i, r):
        # dosent do r just i to r-1
        #adds the group of three together assinging the sum to sumcheck
        total = total + measure[s]
    sumcheck = total

    # adds the sum check for each group of 3 to results
    results.append(sumcheck)

    i = i + 1

# declares the global counters
#increased counter
inc = 0
#decreased counter
dec = 0
#stays the same counter
er = 0

# while loop to compare groups
g = 0
print("Sums length", len(sums))
while g < len(sums):
    #g is the index 0 - 1997
    if g == 0:
        print("No comparison [0]")
    elif g > 0:
        #now comapre g and g-1
        if sums[g] > sums[g-1]:
            print("Increased")
            inc = inc + 1
        elif sums[g] < sums[g-1]:
            print("Decreased")
            dec = dec + 1
        else:
            print("Same Depth")
            er = er + 1
    else:
        print("Complete")
    g = g + 1

print(" ")
print("Complete")
print(" ")
print("Increased", inc)
print("Decreased", dec)
print("Stays Same", er)
print("Total Groups", inc + dec + er)
