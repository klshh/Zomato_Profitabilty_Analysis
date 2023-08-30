import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("D:\\Projects\\Zomato Profitability Analysis\\Data Science Zomato\\datasets\\zomato.csv")
dic_country = {1:'India',14:'Australia',30:'Brazil',37:'Canada',94:'Indonesia',148: 'New Zealand',162:'Phillipines',166: 'Qatar',184:'Singapore',189: 'South Africa',191:'Sri Lanka',208:'Turkey',214:'UAE',215:'United Kingdom',216:'United States'}
df = df.replace({'Country Code':dic_country})

ax = sns.countplot(data=df, y='Country Code')
ax.bar_label(ax.containers[0])
plt.ylabel("Countries")
plt.xlabel("number of Restaurants")
plt.title("Number of restaurants")
plt.show()
