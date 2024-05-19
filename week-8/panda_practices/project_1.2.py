import pandas as pd

data = pd.read_csv("programming language trend over time.csv")


print(data[0:8])
df = data.iloc[0:4]
print(data[0:1])
