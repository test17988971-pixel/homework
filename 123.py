import pandas as pd
data=pd.read_csv('titanic.csv')
print(data[(data['Age'] < 18) & (data['Parch'] == 0)].count())