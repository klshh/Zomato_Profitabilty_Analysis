import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("D:\\Projects\\Zomato Profitability Analysis\\Data Science Zomato\\datasets\\Segmentation of Restaurants.csv")

ax = sns.countplot(data = df, x = "TIER")
ax.bar_label(ax.containers[0])
plt.title("Segmentation of Restaurants")
plt.show()
