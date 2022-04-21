from cmath import sqrt
from tkinter import N
from idna import check_initial_combiner
import pandas as pd
from random import randint
import time
import openpyxl
import gc
import wordlepredict as wp


wb = openpyxl.load_workbook(r"C:\Users\dstacey\Desktop\fiveletterwords.xlsx")
sheet1 = wb['Sheet1']
max_row_for_B = max((b.row for b in sheet1['B'] if b.value is not None))+1
t = max_row_for_B
check_time = 0


def pickrandom(df):
    rand = randint(1,5757)
    return df['Word'][rand]

def check(wordch, wordg):
    p = 0
    h = 0
    lis = []
    while p != 5:
        i = 0
        while h != 5:
            if wordg[p] == wordch[p]:
                lis.append("g")
                break
            elif wordg[p] == wordch[h]:
                # print("win")
                lis.append("y")
                break
            elif wordg[p] != wordch[h]:
                i = i + 1   
            h = h + 1
            if i == 5:
                lis.append("r")
        h = 0
        p = p + 1
    del wordch, wordg, p, h, i
    return lis

def greenapply(i, x, y):
    if x[y] == i:
        del y, i
        return x
    else:
        del x, i, y
        return
 
def green(df, i, y):
    df['Word'] = df['Word'].apply(lambda x: (greenapply(i, x, y)))
    df = df.dropna()
    return df
 
def yellowapply(i, x, y):
    if x[y] == i:
        del x, y, i
        return
    for w in x:
        if w == i:
            del w, y, i
            return x
    del x, y, i, w
    return
   
def yellow(df, i, y):
    df['Word'] = df['Word'].apply(lambda x: (yellowapply(i, x, y)))
    df = df.dropna()
    del i, y
    return df
 
def grayapply(i, x):
    for w in x:
        if w == i:
            del x, w, i
            return
    del w, i
    return x
   
def gray(df, i):
    df['Word'] = df['Word'].apply(lambda x: (grayapply(i, x)))
    df = df.dropna()
    return df

def predictapply(chword, listy):
    
    dfman = pd.read_csv(r"C:\Users\dstacey\Desktop\fiveletterwords.csv", sep = '\t', names = ['Word'])
    start_time_check = time.time()
    listx = check(chword, listy)
    end_time_check = time.time() - start_time_check
    global check_time
    check_time = check_time + end_time_check
    x = 0
    for w in listx:
        start_time_green = time.time()
        letter = listy[x]
        place = x
        if w == "g":
            dfman = green(dfman, letter, place)
        end_time_green = time.time() - start_time_green
        start_time_yellow = time.time()
        if w == "y":
            dfman = yellow(dfman, letter, place)
        end_time_yellow = time.time() - start_time_yellow
        start_time_red = time.time()
        if w == "r":
            dfman = gray(dfman, letter)
        end_time_red = time.time() - start_time_red
        x = x + 1
        
        global green_time, yellow_time, red_time
        green_time = green_time + end_time_green
        yellow_time = yellow_time + end_time_yellow
        red_time = red_time + end_time_red

    end_time_check = 0
    start_time_check = 0
    lem = len(dfman)
    del dfman, listx, w, start_time_check, end_time_check, end_time_yellow, end_time_green, end_time_red, listy
    gc.collect()
    return lem


def predictx(x):
    print(x)
    global t, check_time, green_time, yellow_time, red_time
    check_time = 0
    green_time = 0
    yellow_time = 0
    red_time = 0
    start_time = time.time()
    print(t)
    mycell= sheet1.cell(row=t, column=2)  
    dforg = pd.read_csv(r"C:\Users\dstacey\Desktop\fiveletterwords.csv", sep = '\t', names = ['Word'])
    dforg['len'] = dforg['Word'].apply(lambda y: (predictapply(x, y)))
    ave = dforg['len'].mean()
    print(x)
    print(ave)
    mycell.value = ave
    t = t + 1
    wb.save(r"C:\Users\dstacey\Desktop\fiveletterwords.xlsx")
    print("--- %s seconds green ---" % (green_time))
    print("--- %s seconds yellow ---" % (yellow_time))
    print("--- %s seconds red ---" % (red_time))
    print("--- %s seconds check ---" % (check_time))
    print("--- %s seconds  overall---" % (time.time() - start_time))
    del x, ave, green_time, yellow_time, red_time, start_time, dforg
    gc.collect()


def predict():
    df = pd.read_csv(r"C:\Users\dstacey\Desktop\fiveletterwords.csv", sep = '\t', names = ['Word'])
    
    for x in df['Word'][t:]:
        predictx(x)
    

cont = True
df = pd.read_csv(r"C:\Users\dstacey\Desktop\fiveletterwords.csv", sep = '\t', names = ['Word'])
while cont == True:
    it = input("input - g for green, r for red, y for yellow\n")
    if it == 'g':
        place = int(input("place"))
        letter = input("letter")
        df = green(df, letter, place)
        print(df)
    if it == 'y':
        place = int(input("place"))
        letter = input("letter")
        df = yellow(df, letter, place)
        print(df)
    if it == 'r':
        letter = input("letter")
        df = gray(df, letter)
        print(df)
    if it == 'n':
        cont = False
    if it == 'test':
        wp.main(df)


