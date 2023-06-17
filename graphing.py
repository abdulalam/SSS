import pandas as pd
from matplotlib import pyplot as plt
import datetime

df = pd.read_csv('data (2).csv', encoding= 'unicode_escape')
df = df[["Putaway Staff","Added time"]]
df['Added time']=pd.to_datetime(df['Added time'], infer_datetime_format=True)
df['freq'] = 1
df.sort_values(["Putaway Staff","Added time"], inplace=True)
df = df.reset_index()

""" print(df.head())
print(df.shape)
print(df.columns)
print(df.iloc[1])
print(df[["Added time","Putaway Staff"]]) """

last = 1
count = 0
for index, row in df.iterrows():
        if row['Putaway Staff'] == last:
            count += 1        
            df.at[index,'freq'] = count
            last = row['Putaway Staff']
            
        else:
              count = 1
              df.at[index,'freq'] = count
              last = row["Putaway Staff"]

df.to_csv('out.csv')

topPickers = df['Putaway Staff'].value_counts().index
print(df['Putaway Staff'].value_counts())
y = 0
for picker in topPickers:
    if y < 11:
        user = df[df['Putaway Staff'] == picker]
        plt.plot(user['Added time'], user['freq'],label = picker, marker ="o")
        y += 1

plt.legend()
plt.show() 

