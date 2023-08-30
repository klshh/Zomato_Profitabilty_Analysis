import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("D:\\Projects\\Zomato Profitability Analysis\\Data Science Zomato\\datasets\\zomato.csv")
df = df.rename(columns = {'Country Code':'Country'})
dic_country = {1:'India',14:'Australia',30:'Brazil',37:'Canada',94:'Indonesia',148: 'New Zealand',162:'Phillipines',166: 'Qatar',184:'Singapore',189: 'South Africa',191:'Sri Lanka',208:'Turkey',214:'UAE',215:'United Kingdom',216:'United States'}
df = df.replace({'Country':dic_country})
df1 = df.groupby(['Country'],as_index=False).mean()[['Country','Average Cost for two']]
print("Avg Average cost for two in Rupees")
print(df1)

conv = {'India':0.012,'Australia':0.67,'Brazil':0.19,'Canada':0.75,'Indonesia':0.000065,'New Zealand':0.61,'Phillipines':0.017,'Qatar':0.27,'Singapore':0.73,'South Africa':0.058,'Sri Lanka':0.0027,'Turkey':0.054,'UAE':0.27,'United Kingdom':1.18,'United States':1}
df1['Average Cost for two'] = df1['Country'].map(conv).mul(df1['Average Cost for two'])

ax = sns.barplot(x = 'Country',y = 'Average Cost for two',data = df1)
ax.bar_label(ax.containers[0])
plt.xlabel("Countries")
plt.ylabel("Avg Average cost for two($)")
plt.title("Countries vs Avg Average cost for two($)")
plt.show()