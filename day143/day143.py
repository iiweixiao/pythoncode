import pandas as pd

df = pd.read_excel('test.xlsx', index_col=0)
df1 = df.head()
print(df1)

df2 = pd.read_excel('test.xlsx', header=0)
df2.head()
print(df2)

df3 = pd.read_excel('test.xlsx', sheet_name='Sheet1')
df3.head()
print(df3.head())

df4 = pd.read_excel('test.xlsx', header=None)
df4.head()
print(df4.head())

df5 = pd.read_excel('test.xlsx', usecols=[0])
df5.head()
print(df5.head())

df6 = pd.read_excel('test.xlsx', usecols=[0, 2, 3])
df6.head()
print(df6.head())

df7 = pd.read_excel('test.xlsx', usecols=['姓名', '课程'])
df7.head()
print(df7.head())
