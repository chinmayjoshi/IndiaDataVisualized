import pandas as pd 

def column_operation_year(dataframe):

	yearList = dataframe.Year.tolist()

	for i,e in enumerate(yearList):

		yearList[i] = yearList[i][:4]

	dataframe['Year'] = pd.Series(yearList).values

	return dataframe





df = pd.read_excel("../csvFiles/revenueData.XLS")
df = column_operation_year(df)



df = df.filter(['Year','Direct tax','Indirect tax','Tax revenue'],axis=1)

#print df.head()

directList = df['Direct tax'].tolist()
indirectList = df['Indirect tax'].tolist()
taxRevenue = df['Tax revenue'].tolist()



for i, (e1,e2,e3) in enumerate(zip(directList,indirectList,taxRevenue)) :

	directList[i] = directList[i]/taxRevenue[i]
	indirectList[i] = indirectList[i]/taxRevenue[i]

df = df.drop(columns = ['Tax revenue','Indirect tax', 'Direct tax'])

df['Indirect tax']  = pd.Series(indirectList).values
df['Direct tax'] = pd.Series(directList).values


df.to_csv("../csvFiles/directIndirectLines.csv", index = False)







