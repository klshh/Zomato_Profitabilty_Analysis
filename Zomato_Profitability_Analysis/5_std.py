import pandas as pd

df = pd.read_csv("D:\\Projects\\Zomato Profitability Analysis\\Data Science Zomato\\datasets\\India_Latest.csv")

std1 = df["Average Cost for two"].std()
m = df["Average Cost for two"].mean()
min = df["Average Cost for two"].min()
max = df["Average Cost for two"].max()

l = []
for x in df["Average Cost for two"]:
    if x >= min and x <= m-std1:
        l.append(1)
    if x > m-std1 and x <= m:
        l.append(2)
    if x > m and x <=m+std1:
        l.append(3)
    if x > m+std1 and x <= max:
        l.append(4)

df["cost points"] = l

std = df['Aggregate rating'].std()
mean = df['Aggregate rating'].mean()
min = df['Aggregate rating'].min()
max = df['Aggregate rating'].max()
y = []
for x in df['Aggregate rating']:
    if x >= min and x <= mean-std:
        y.append(1)
    if x > mean-std and x <= mean:
        y.append(2)
    if x > mean and x <=mean+std:
        y.append(3)
    if x > mean+std and x <= max:
        y.append(4)

df["rating points"] = y

z = df.to_csv("weightage.csv")
print(z)

