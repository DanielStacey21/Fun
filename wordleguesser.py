from tkinter import N
import pandas as pd
from random import randint
 
df = pd.read_csv(r"C:\Users\dstacey\Desktop\fiveletterwords.csv", sep = '\t', names = ['Word'])

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
    return lis

def greenapply(i, x, y):
    if x[y] == i:
        return x
    else:
        return
 
def green(df, i, y):
    df['Word'] = df['Word'].apply(lambda x: (greenapply(i, x, y)))
    df = df.dropna()
    return df
 
def yellowapply(i, x, y):
    if x[y] == i:
        return
    for w in x:
        if w == i:
            return x
    return
   
def yellow(df, i, y):
    df['Word'] = df['Word'].apply(lambda x: (yellowapply(i, x, y)))
    df = df.dropna()
    return df
 
def grayapply(i, x):
    for w in x:
        if w == i:
            return
    return x
   
def gray(df, i):
    df['Word'] = df['Word'].apply(lambda x: (grayapply(i, x)))
    df = df.dropna()
    return df

practice = input("practice mode? y for yes, n for no\n")

wordpick = pickrandom(df)

while practice == "y":
    for i in range(5):
        guess1 = input("Guess " + str(i+1) + ": ")
        guesscheck = check(wordpick, guess1)
        print(guesscheck)
        cont = True
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
            print(guess1)
            print(guesscheck)

    print("Word was " + wordpick)
    practice = "n"

cont = True
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
