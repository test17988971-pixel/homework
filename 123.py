import pandas as pd
data=pd.read_csv('123.csv')

mask=(data.country=='US') & (data.price>100)
print(data[mask])