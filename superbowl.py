# generate random integer values
from random import seed
from random import randint
import random
import numpy as np

# prob = [[190, 90, 70, 290, 250, 120, 220, 330, 100, 90],
#  [60, 90, 60, 110, 200, 40, 70, 120, 110, 40],
#  [70, 50, 10, 40, 50, 40, 50, 80, 60, 40],
#  [270, 140, 40, 110, 120, 70, 170, 240, 80, 90],
#  [220, 190, 50, 90, 70, 40, 120, 300, 100, 60],
#  [100, 40, 20, 50, 30, 10, 70, 50, 50, 20],
#  [200, 70, 50, 1.7, 1.3, 70, 100, 110, 60, 70],
#  [340, 140, 90, 240, 300, 50, 90, 170, 100, 100],
#  [70,110, 50, 70,80, 40, 50, 70, 40, 30],
#  [90, 40, 60, 70, 60, 20, 60, 100, 30, 40]]

prob = [190, 90, 70, 290, 250, 120, 220, 330, 100, 90,
 60, 90, 60, 110, 200, 40, 70, 120, 110, 40,
 70, 50, 10, 40, 50, 40, 50, 80, 60, 40,
 270, 140, 40, 110, 120, 70, 170, 240, 80, 90,
 220, 190, 50, 90, 70, 40, 120, 300, 100, 60,
 100, 40, 20, 50, 30, 10, 70, 50, 50, 20,
 200, 70, 50, 170, 130, 70, 100, 110, 60, 70,
 340, 140, 90, 240, 300, 50, 90, 170, 100, 100,
 70,110, 50, 70,80, 40, 50, 70, 40, 30,
 90, 40, 60, 70, 60, 20, 60, 100, 30, 40]

prob1 = [740, 100, 40, 420, 390, 50, 200, 610, 50, 80,
100, 60, 20, 90, 120, 20, 50, 130, 60, 20,
40, 20, 10, 20, 20, 10, 20, 50, 10, 10,
420, 90, 20, 170, 220, 20, 70, 330, 50, 50,
390, 120, 20, 220, 230, 50, 70, 240, 70, 60,
50, 20, 10, 20, 50, 10, 10, 50, 20, 10,
200, 50, 20, 70, 70, 10, 30, 120, 30, 20,
610, 130, 50, 330, 240, 50, 120, 400, 50, 50,
50, 60, 10, 50, 70, 20, 30, 50, 20, 10, 
80, 20, 10, 50, 60, 10, 20, 50, 10, 0]

def wincounter(list, winlist, l):
    p = 0
    h = 0
    wins = 0
    winlength = 4
    while p != l:
        while h != 4:
            if list[p] == winlist[h]:
                 # print("win") 
                wins = wins + 1
            h = h + 1
        h = 0
        p = p + 1
    return wins

def samerow(l):
    list1 = []
    list2 = []
    i = 0
    rand = randint(0,9)
    while i != l:
        list1.append(rand)
        i = i + 1
    list2 = random.sample(range(10), l)
    list1  = [i * 10 for i in list1]
    sumlist = np.add(list1, list2)
    return sumlist

def samecol(l):
    list1 = []
    list2 = []
    i = 0
    rand = randint(0,9)
    while i != l:
        list1.append(rand)
        i = i + 1
    list2 = random.sample(range(10), l)
    list2  = [i * 10 for i in list2]
    sumlist = np.add(list1, list2)
    return sumlist

def rand(l):
    list1 = []
    list2 = []
    list1 = random.sample(range(10), l)
    list2 = random.sample(range(10), l)
    list1  = [i * 10 for i in list1]
    sumlist = np.add(list1, list2)
    return sumlist




bestgainavg = -100
bestwinavg = -100
winlist = []
length1 = 11
for i in range(length1):

    totalwins = 0
    totalgain = 0
    
    winlength = 4
    t = 0
    contin = 1000000
    while t != contin: 
        
        winlength = 4
        # x = random.sample(range(100), 1)
        # u = 0
        # while u != length:
        #     x = x + (u*10) + u
        #     list1.append(x)
        # list1 = random.sample(range(10), length)
        
        w = 0
        # while w != winlength:
        #     rand = randint(0,99)
        #     win.append(rand)
        #     w = w + 1
        win1 = random.choices(range(100), weights=prob1, k=winlength)
        col = samecol(i)
        # row = samerow(i)
        # diffrowcol = rand(i)
        sumlist = [19, 13, 15, 18]
        blsumlist = [59, 92, 89, 8, 61, 65]
        dwsumlist = [24, 88, 49, 64]
        rexsumlist = [50,71,93,36]

        wins = 0
        wins = wincounter(col, win1, i)
        t = t + 1
        totalwins = totalwins + wins
        cost = -i * 5
        gain = (wins * 125) + cost
        totalgain = totalgain + gain
    if i == 0:
        avgwin = (totalwins/contin)
    else:
        avgwin = (totalwins/contin)/i
    avgwin_str = str(avgwin)
    avgwin = float(avgwin)
    avggain = totalgain/contin
    avggain = float(avggain)
    avggain_str = str(avggain)
    bestgainavg_str = str(bestgainavg)
    bestgainavg = float(bestgainavg)
    bestwinavg_str = str(bestwinavg)
    length_str = str(i)
    bestwinavg = float(bestwinavg)
    
    winlist.append(avggain)
    print(length_str + " average profit: " + avggain_str)
    print(length_str + " average wins: " + avgwin_str)
    
    if avggain > bestgainavg:
        print(length_str + " best gain avg: " + avggain_str)
        bestgainavg = avggain_str
        bestgainavglen = length_str
    if avgwin > bestwinavg:
        print(length_str + " best win avg: " + avgwin_str)
        bestwinavg = avgwin_str
        bestwinavglen = length_str
    print("____________________________")
print(bestgainavglen + " best overall gain avg: " + bestgainavg_str)
print(bestwinavglen + " best overall win avg: " + bestwinavg_str)
print(winlist)