import pandas as pd
d={'Team':["India","Austrlia","Pakistan","srilanka","England"],'Rank':[1,2,3,4,5],
   'Winper':['60%','55%','45%','35%','48%']}
df=pd.DataFrame(d)
df.rename(columns={'Rank':'Ranking'},inplace=True)
print(df.loc[:,['Team']])