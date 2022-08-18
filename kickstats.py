import pandas as pd

df = pd.read_csv(r"F:\BS-15\kick.csv")

def score(A, B, C, D, E, attempt, made):
    points = ((A + B + C)*3) + (D*4) + (E*5) + ((attempt-made)*-1)
    return points

df = df.fillna(0)

print(df)

df['points'] = df.apply(lambda x: score( x['0-19FGM'], x['20-29FGM'], x['30-39FGM'], x['40-49FGM'], x['50FGM'], x['allFGA'], x['allFGM']), axis = 1)



print(df)