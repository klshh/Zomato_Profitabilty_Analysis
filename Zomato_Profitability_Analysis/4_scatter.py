import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("D:\\Projects\\Zomato Profitability Analysis\\Data Science Zomato\\datasets\\zomato.csv")
dfcc = df[df["Country Code"] == 1]

plt.scatter(dfcc["Average Cost for two"],dfcc["Aggregate rating"], c ="blue",edgecolor ="green")
plt.xticks([0,1000,2000,3000,4000,5000,6000,7000,8000])
plt.ylabel("Aggregate rating")
plt.xlabel("Average Cost for two")
plt.title("Average Cost for Two vs Aggregate rating")
plt.show()
