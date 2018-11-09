import pandas as pd 
from tabulate import tabulate 

df = pd.read_excel("revenueData.XLS")

df = df.tail(7)

df = df.reset_index(drop=True)



yearList = df.Year.tolist();


for i, e in enumerate(yearList):
    
        yearList[i] = yearList[i][:4]

se = pd.Series(yearList)

TaxRevenue = df['Tax revenue']

df = df.drop(columns =['Year','Direct tax','Indirect tax'])

df['Year'] = se.values


gdp = [87363.29,92130.17,98013.7,105276.74,113861.45,121960.06,130108.43]

cuList = df['Customs duties'].tolist()
piList = df['Personal Income Tax'].tolist()
exList = df['Excise duties'].tolist()
corpList = df['Corporation tax'].tolist()
trList = df['Tax revenue'].tolist()



for i, (e1,e2,e3,e4) in enumerate(zip(cuList,piList,exList,corpList)):
    
        cuList[i] = cuList[i]/gdp[i] * 100
        piList[i] = piList[i]/gdp[i] * 100
        exList[i] = exList[i]/gdp[i] * 100
        corpList[i] = corpList[i]/gdp[i] * 100
        trList[i] = trList[i]/gdp[i] * 100

print df
print gdp
print cuList

df = df.drop(columns =['Customs duties','Personal Income Tax','Excise duties','Corporation tax'])

df['Customs duties'] = pd.Series(cuList).values
df['Personal Income Tax'] = pd.Series(piList).values
df['Excise duties'] = pd.Series(exList).values
df['Corporation tax'] = pd.Series(corpList).values
df['Tax revenue'] = pd.Series(trList).values

print df

#Customs duties ;; Personal Income Tax ;; Excise duties ;; Corporation tax


df.to_csv("taxLines.csv",index = False)
