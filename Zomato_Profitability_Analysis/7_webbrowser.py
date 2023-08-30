import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df1 = pd.read_csv("D:\\Projects\\Zomato Profitability Analysis\\Data Science Zomato\\datasets\\India_Latest.csv")
df = pd.read_csv("D:\\Projects\\Zomato Profitability Analysis\\Data Science Zomato\\datasets\\onlinedeliverydata1.csv")

total = len(df["Medium (P1)"])
ax = sns.countplot(x=df["Medium (P1)"])
for p in ax.patches:
    percentage = "{:.1f}%".format(100 * p.get_height()/total)
    x = p.get_x() + p.get_width()/2
    y = p.get_height()
    ax.annotate(percentage, (x, y), ha = "center")
plt.show()

