import pandas as pd

data = pd.read_csv("Top-Apps-in-Google-Play.csv")


print(data[0:8])

df = data.iloc[0:4]

print(data[0:1])
