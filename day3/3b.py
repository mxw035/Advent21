#alist = open("test.txt")
alist = open("real.txt")
alist2 = []
blist2 = []
co2list = []
oxygen = []

for x in alist:
    blist = x
    clist = str(blist)
    dlist = clist.strip()
    elist = dlist.split(",")
    #print("elist", elist)
    #print("len elist", len(elist))
    alist2.append(elist)
    blist2.append(elist)
    co2list.append(elist)
    oxygen.append(elist)
print("org alist2", alist2)
print("len alist2", len(alist2))

def oxyco2(alist2, blist2, co2list, oxygen, count):
    #print("alist", alist2)
    group = []
    for y in alist2:
        group.append(y[0][count])
    a = group.count("0")
    b = group.count("1")
    print("a", a)
    print("b", b)
    if a > b:
        print("zero")
        # when zero wins for oxygen pop 1 keep 0
        j = 0
        while j < b:
            k = group.index("1")
            group.pop(k)
            oxygen.pop(k)
            alist2.pop(k)
            j = j + 1
    elif b > a:
        print("one") # keep 1
        j = 0
        while j < a and j >= 0:
            #print("group", group)
            #print("alist", alist2)
            k = group.index("0")
            group.pop(k)
            oxygen.pop(k)
            alist2.pop(k)
            j = j + 1
    else:
        print("same")
        # if same for oxygen keep 1
        j = 0
        while j < a and j >= 0:
            #print("group", group)
            #print("alist", alist2)
            k = group.index("0")
            group.pop(k)
            oxygen.pop(k)
            alist2.pop(k)
            j = j + 1


def co2(blist2, co2list, count):
    group = []
    for y in blist2:
        group.append(y[0][count])
    a = group.count("0")
    b = group.count("1")
    print("a", a)
    print("b", b)
    if a > b:
        print("zero")
        # when zero wins for carbon keep 1
        j = 0
        while j < a:
            k = group.index("0")
            group.pop(k)
            co2list.pop(k)
            blist2.pop(k)
            j = j + 1
    elif b > a:
        print("one") # keep 0
        j = 0
        while j < b and j >= 0:
            #print("group", group)
            #print("alist", alist2)
            k = group.index("1")
            group.pop(k)
            co2list.pop(k)
            blist2.pop(k)
            j = j + 1
    else:
        print("same")
        # if same for carbon keep 0
        j = 0
        while j < b and j >= 0:
            #print("group", group)
            #print("alist", alist2)
            k = group.index("1")
            group.pop(k)
            co2list.pop(k)
            blist2.pop(k)
            j = j + 1


i = 0
while i < 12:
    print("i", i)
    oxyco2(alist2, blist2, co2list, oxygen, i)
    if (len(co2list) > 1):
        co2(blist2, co2list, i)
    i = i + 1
print("oxygen", oxygen)
print("co2", co2list)
