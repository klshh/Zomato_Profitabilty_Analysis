import pandas as pd

df1 = pd.read_csv("D:\\Projects\\Zomato Profitability Analysis\\Data Science Zomato\\datasets\\weightage.csv")
df = pd.read_csv("D:\\Projects\\Zomato Profitability Analysis\\Data Science Zomato\\datasets\\onlinedeliverydata1.csv")

count = 0
for x in df["Influence of rating"]:
    if x == "Yes":
        count += 1
per = (count/len(df["Influence of rating"]))*100
print("{:.1f}%".format(per))
count = 0
for x in df["Medium (P1)"]:
    if x == "Food delivery apps":
        count += 1
per1 = (count/len(df["Medium (P1)"]))*100
print("{:.1f}%".format(per1))
count= 0
for x in df["Medium (P1)"]:
    if x == "Walk-in":
        count += 1
per2 = (count/len(df["Medium (P1)"]))*100
print("{:.1f}%".format(per2))

weight_aov = 50
min = min(per1, per2, per)
rate = per/min
foodapp = per1/min
walk = per2/min

sum = rate+foodapp+walk
res = weight_aov/sum

weight_rate = rate*res
weight_foodapp = foodapp*res
weight_walk = walk*res
e = []
f = []
g = []
h = []
final = []
for x in df1["cost points"]:
    e.append(x*weight_aov)
for x in df1["rating points"]:
    f.append(x*weight_rate)
for x in df1["DeliveryPoints"]:
    g.append(x*weight_foodapp)
for x in df1["BookingPoints"]:
    h.append(x*weight_walk)

for i in range(len(e)):
    final.append(round((e[i]+f[i]+g[i]+h[i])/100))

df1["tier rating"] = final

tier = []
for x in df1["tier rating"]:
    if x == 1:
        tier.append(4)
    if x == 2:
        tier.append(3)
    if x == 3:
        tier.append(2)
    if x == 4:
        tier.append(1)

df1["TIER"] = tier

p = df1.to_csv("Segmentation of Restaurants.csv")
print(p)





