import pandas as pd
#1
d=pd.read_csv('file:///C:/Users/vsivkov/Desktop/lab1/brooklyn_sales_map.csv',sep=',')
print(d['building_class_category'].unique())

#2
d['building_class_category'] = d['building_class_category'].fillna('NAN').replace(regex = ' +', value = ' ').replace(regex = '/', value = ' ').str.upper()
nabor = d['building_class_category'].unique()
for i in nabor:
    res = d.loc[d['building_class_category'] == i]
    res.to_csv((str(i)).replace("/"," ")+'.csv') 

#3
columnsNameNumb = d.select_dtypes(include='number').columns
columnsNameStr = d.select_dtypes(exclude='number').columns
for colum in columnsNameNumb:
    column = d[colum]
    print('NaN = ' + str(column.isnull().sum()))
    print('Median = ' + str(column.median()))
    print('Max = ' + str(column.max()))
    print('Min = ' + str(column.min()))
    print('Mean = ' + str(column.mean()))
    
for colum in columnsNameStr:
    column = d[colum]
    print(column)
    print('Nan = ' + str(column.isnull().sum()))
    print('StrUni = ' + str(column.nunique()))

#4
Category = d['building_class_category'].count()
for i in nabor:
    Count = (d.loc[d['building_class_category'] == i])['building_class_category'].count()
    print(str(i) + ' = ' + str(Count/Category))

#5
columnsNameNumb = d.select_dtypes(include='number').columns
for colum in columnsNameNumb:
    column = d[colum]
    column = (column - column.min() / column.max() - column.min())
print(column)