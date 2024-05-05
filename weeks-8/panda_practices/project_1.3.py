import pandas as pd

data = pd.read_csv("BTC_DATA_V3.0.csv")


print(data[0:8])
df = data.iloc[0:4]
print(data[0:1])