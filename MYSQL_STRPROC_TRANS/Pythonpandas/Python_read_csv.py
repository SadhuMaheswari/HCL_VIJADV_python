import pandas as pd
data=pd.read_csv("..//data/tips.csv")
#print(data.isna().any())
#print(data.isna().sum())
#tips_male_fm=data.filter(['tip','sex'])
#print(tips_male_fm.groupby('sex').sum())
#print(tips_male_fm.sex.value_counts(normalize=True))
#print(pd.crosstab(index=data['sex'],column=data['smoker']))
#day_wise=data.filter(['tip','day'])
#print(day_wise.groupby('day').sum())
#df2=pd.DataFrame
'''
d1={'Name':['pankaj','Meghna','Lisa'],'Country':['India','India','USA'],
    'Role':['CEO','CTO','CTO']}
df1=pd.DataFrame(d1)
print(df1)
df2=pd.DataFrame({'ID':[1,2,3,],'Name':['pankaj','Anupam','Amit']})
print(df2)
df_merged = df1.merge(df2,how='right',on=df2['ID'])
print(df_merged)
'''

print(data.head(2))