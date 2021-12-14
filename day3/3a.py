alist = open("real.txt")
groupa = [] #1
groupb = [] #2
groupc = [] #3
groupd = [] #4
groupe = [] #5
groupf = [] #6
groupg = [] #7
grouph = [] #8
groupi = [] #9
groupj = [] #10
groupk = [] #11
groupl = [] #12
gamma = []
epsilon = []
for x in alist:
    blist = x
    clist = blist.strip()
    dlist = clist.split(" ")
    #print(dlist[0][0])
    #print("len", len(dlist[0]))
    #print("len", len(dlist[0][0]))

    #print(dlist)
    #print(dlist[0][0])
    groupa.append(dlist[0][0])
    groupb.append(dlist[0][1])
    groupc.append(dlist[0][2])
    groupd.append(dlist[0][3])
    groupe.append(dlist[0][4])
    groupf.append(dlist[0][5])
    groupg.append(dlist[0][6])
    grouph.append(dlist[0][7])
    groupi.append(dlist[0][8])
    groupj.append(dlist[0][9])
    groupk.append(dlist[0][10])
    groupl.append(dlist[0][11])
#fxn a
def groupACount(groupa):
    a = groupa.count("0")
    b = groupa.count("1")
    #print("aa", a)
    #print("ba", b)

    if a > b:
        gamma.append(0)
        epsilon.append(1)
    else:
        gamma.append(1)
        epsilon.append(0)
#fxn b
def groupBCount(groupb):
    a = groupb.count("0")
    b = groupb.count("1")
    #print("ab", a)
    #print("bb", b)
    if a > b:
        gamma.append(0)
        epsilon.append(1)
    else:
        gamma.append(1)
        epsilon.append(0)
#fxnc
def groupCCount(groupc):
    a = groupc.count("0")
    b = groupc.count("1")
    #print("ac", a)
    #print("bc", b)
    if a > b:
        gamma.append(0)
        epsilon.append(1)
    else:
        gamma.append(1)
        epsilon.append(0)
# fxn d
def groupDCount(groupd):
    a = groupd.count("0")
    b = groupd.count("1")
    #print("ad", a)
    #print("bd", b)
    if a > b:
        gamma.append(0)
        epsilon.append(1)
    else:
        gamma.append(1)
        epsilon.append(0)
#fxn e
def groupECount(groupe):
    a = groupe.count("0")
    b = groupe.count("1")
    #print("ae", a)
    #print("be", b)

    if a > b:
        gamma.append(0)
        epsilon.append(1)
    else:
        gamma.append(1)
        epsilon.append(0)
#fxn f
def groupFCount(groupf):
    a = groupf.count("0")
    b = groupf.count("1")
    #print("ae", a)
    #print("be", b)

    if a > b:
        gamma.append(0)
        epsilon.append(1)
    else:
        gamma.append(1)
        epsilon.append(0)
#fxn g
def groupGCount(groupg):
    a = groupg.count("0")
    b = groupg.count("1")
    #print("ae", a)
    #print("be", b)

    if a > b:
        gamma.append(0)
        epsilon.append(1)
    else:
        gamma.append(1)
        epsilon.append(0)
#fxn h
def groupHCount(grouph):
    a = grouph.count("0")
    b = grouph.count("1")
    #print("ae", a)
    #print("be", b)

    if a > b:
        gamma.append(0)
        epsilon.append(1)
    else:
        gamma.append(1)
        epsilon.append(0)
#fxn i
def groupICount(groupi):
    a = groupi.count("0")
    b = groupi.count("1")
    #print("ae", a)
    #print("be", b)

    if a > b:
        gamma.append(0)
        epsilon.append(1)
    else:
        gamma.append(1)
        epsilon.append(0)
#fxn j
def groupJCount(groupj):
    a = groupj.count("0")
    b = groupj.count("1")
    #print("ae", a)
    #print("be", b)

    if a > b:
        gamma.append(0)
        epsilon.append(1)
    else:
        gamma.append(1)
        epsilon.append(0)
#fxn k
def groupKCount(groupk):
    a = groupk.count("0")
    b = groupk.count("1")
    #print("ae", a)
    #print("be", b)

    if a > b:
        gamma.append(0)
        epsilon.append(1)
    else:
        gamma.append(1)
        epsilon.append(0)
#fxn l
def groupLCount(groupl):
    a = groupl.count("0")
    b = groupl.count("1")
    #print("ae", a)
    #print("be", b)

    if a > b:
        gamma.append(0)
        epsilon.append(1)
    else:
        gamma.append(1)
        epsilon.append(0)

groupACount(groupa)
groupBCount(groupb)
groupCCount(groupc)
groupDCount(groupd)
groupECount(groupe)
groupFCount(groupf)
groupGCount(groupg)
groupHCount(grouph)
groupICount(groupi)
groupJCount(groupj)
groupKCount(groupk)
groupLCount(groupl)

print("gamma", gamma)
print("epsilon", epsilon)
