import pandas as pd
import xlsxwriter

df = pd.read_csv('data.csv')


new_df = df[["Shelf No.","Long","Width","High"]]
vol_df = df[["Shelf No.","Long","Width","High","Available Qty."]]

vol_df["Volume"] = vol_df["Long"] * vol_df["Width"] * vol_df["High"] * vol_df["Available Qty."] /1000000
#vol_df["Volume"] = vol_df.iloc[:,1:5].multiply(axis=1)

#print(vol_df.head)

#print(new_df.columns)
#print(len(new_df))

overhang = []
for index, row in new_df.iterrows():
    if row["Long"] > 120 or row["Width"] > 120 or row["High"] > 120 :
        overhang.append(row["Shelf No."])

overvol = []
for index, row in vol_df.iterrows():
    if row["Volume"] > 1.918 :
        overvol.append(row["Shelf No."])


percentage = (len(overhang) / len(new_df)) * 100
print(f"Overhang : {percentage}% at {len(overhang)} pallets out of {len(new_df)}")
percentage_v = (len(overvol) / len(vol_df)) * 100
print(f"Overvol : {percentage_v}% at {len(overvol)} pallets out of {len(vol_df)}")


