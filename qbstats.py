import pandas as pd

df = pd.read_csv(r"F:\BS-15\QB.csv")

def score(yds, td, inter):
    points = (yds*.04) + (td*4) + (inter*-2)
    return points

print(df)

df['points'] = df.apply(lambda x: score( x['Yds'], x['TD'], x['Int']), axis = 1)

print(df)