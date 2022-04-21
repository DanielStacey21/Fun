from cmath import sqrt
from tkinter import N
from idna import check_initial_combiner
import pandas as pd
from random import randint
import time
import openpyxl
import gc
from pathlib import Path


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
    
    dfman = pd.read_csv(r"C:\\folder\subfolder\out.csv", sep = '\t', names = ['Word'])
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
    del dfman, listx, w, listy
    gc.collect()
    return lem


def predictx(x):
    print(x)
    
    dforg = pd.read_csv(r"C:\\folder\subfolder\out.csv", sep = '\t', names = ['Word'])
    dforg['len'] = dforg['Word'].apply(lambda y: (predictapply(x, y)))
    ave = dforg['len'].mean()
    # total = 0
    # top = 0
    # for i in df['Word']:
    #     lem = predictapply(x, i)
    #     total = total + lem
    # ave = total/len(df)
    print(x)
    print(ave)
    mycell.value = ave
    t = t + 1
    # wb.save(r"C:\Users\dstacey\Desktop\fiveletterwords.xlsx")
    print("--- %s seconds green ---" % (green_time))
    print("--- %s seconds yellow ---" % (yellow_time))
    print("--- %s seconds red ---" % (red_time))
    print("--- %s seconds check ---" % (check_time))
    print("--- %s seconds  overall---" % (time.time() - start_time))
    del x, ave, green_time, yellow_time, red_time, start_time, dforg
    gc.collect()
    # return ave
    # for i in df['Word']:
    #     lem = predictapply(x, i)
    #     top = top + ((lem - ave) * (lem - ave))
    # var = top/N
    # stdev = sqrt(var)
    # print("Word: "+ x +"\naverage: "+ ave+ "\nstandard deviation: "+ stdev)



def predict(df):
    # df = pd.read_csv(r"C:\Users\dstacey\Desktop\fiveletterwords.csv", sep = '\t', names = ['Word'])
    
    filepath = Path('folder/subfolder/out.csv')  
    filepath.parent.mkdir(parents=True, exist_ok=True)  
    df.to_csv(filepath)  

    for x in df['Word'][t:]:
        predictx(x)
    
    # df['Ave'] = df['Word'].apply(lambda x: (predictx(x)))

    # lem = 0
    # minval = 100000
    # mini = "none"
    # for i in df['Word']:
    #     lem = predictx(i)
    #     if lem < minval:
    #         minval = lem
    #         mini = i
    # print("MIN VALUE ____________________________")
    # print(mini)
    # print(minval)

    





# practice = input("practice mode? y for yes, n for no\n")

# wordpick = pickrandom(df)

# while practice == "y":
#     for i in range(5):
#         guess1 = input("Guess " + str(i+1) + ": ")
#         guesscheck = check(wordpick, guess1)
#         print(guesscheck)
#         cont = True
#         while cont == True:
#             it = input("input - g for green, r for red, y for yellow\n")
#             if it == 'g':
#                 place = int(input("place"))
#                 letter = input("letter")
#                 df = green(df, letter, place)
#                 print(df)
#             if it == 'y':
#                 place = int(input("place"))
#                 letter = input("letter")
#                 df = yellow(df, letter, place)
#                 print(df)
#             if it == 'r':
#                 letter = input("letter")
#                 df = gray(df, letter)
#                 print(df)
#             if it == 'n':
#                 cont = False
#             print(guess1)
#             print(guesscheck)

#     print("Word was " + wordpick)
#     practice = "n"

# cont = True
# df = pd.read_csv(r"C:\Users\dstacey\Desktop\fiveletterwords.csv", sep = '\t', names = ['Word'])
# while cont == True:
#     it = input("input - g for green, r for red, y for yellow\n")
#     if it == 'g':
#         place = int(input("place"))
#         letter = input("letter")
#         df = green(df, letter, place)
#         print(df)
#     if it == 'y':
#         place = int(input("place"))
#         letter = input("letter")
#         df = yellow(df, letter, place)
#         print(df)
#     if it == 'r':
#         letter = input("letter")
#         df = gray(df, letter)
#         print(df)
#     if it == 'n':
#         cont = False


