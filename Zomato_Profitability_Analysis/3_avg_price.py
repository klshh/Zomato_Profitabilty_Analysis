import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("D:\\Projects\\Zomato Profitability Analysis\\Data Science Zomato\\datasets\\zomato.csv")

dic_country = {1:'India',14:'Australia',30:'Brazil',37:'Canada',94:'Indonesia',148: 'New Zealand',162:'Phillipines',166: 'Qatar',184:'Singapore',189: 'South Africa',191:'Sri Lanka',208:'Turkey',214:'UAE',215:'United Kingdom',216:'United States'}
conv = {'India':0.012,'Australia':0.67,'Brazil':0.19,'Canada':0.75,'Indonesia':0.000065,'New Zealand':0.61,'Phillipines':0.017,'Qatar':0.27,'Singapore':0.73,'South Africa':0.058,'Sri Lanka':0.0027,'Turkey':0.054,'UAE':0.27,'United Kingdom':1.18,'United States':1}

dfcc = df.replace({'Country Code':dic_country})
dfcc['Average Cost for two'] = dfcc['Country Code'].map(conv).mul(dfcc['Average Cost for two'])

p1 = dfcc[dfcc["Price range"] == 1].groupby("Country Code").mean().reset_index()
p2 = dfcc[dfcc["Price range"] == 2].groupby("Country Code").mean().reset_index()
p3 = dfcc[dfcc["Price range"] == 3].groupby("Country Code").mean().reset_index()
p4 = dfcc[dfcc["Price range"] == 4].groupby("Country Code").mean().reset_index()

fig, axes = plt.subplots(1, 4) 

sns.barplot( data = p1, x="Average Cost for two", y="Country Code", ax=axes[0]).set(title = "Price Range 1")
axes[0].set_xticks([0, 100, 200])
sns.barplot(data = p2, x="Average Cost for two", y="Country Code", ax=axes[1]).set(title = "Price Range 2")
axes[1].set_xticks([0, 100, 200])
axes[1].set(ylabel=None)
sns.barplot( data = p3, x="Average Cost for two", y="Country Code", ax=axes[2]).set(title = "Price Range 3")
axes[2].set_xticks([0, 100, 200])
axes[2].set(ylabel=None)
sns.barplot( data = p4, x="Average Cost for two", y="Country Code", ax=axes[3]).set(title = "Price Range 4")
axes[3].set_xticks([0, 100, 200])
axes[3].set(ylabel=None)

axes[0].bar_label(axes[0].containers[0])
axes[1].bar_label(axes[1].containers[0])
axes[2].bar_label(axes[2].containers[0])
axes[3].bar_label(axes[3].containers[0])
plt.show()

