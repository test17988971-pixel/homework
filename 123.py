import pandas as pd
data=pd.read_csv('titanic.csv')
print(data.info())


import pandas as pd
data=pd.read_csv('titanic.csv')
print(data['Sex'].value_counts())


import pandas as pd
data=pd.read_csv('titanic.csv')
print(data['Survived'].value_counts())


import pandas as pd
data=pd.read_csv('titanic.csv')
print(data.groupby('Sex')['Survived'].value_counts())


import pandas as pd
data=pd.read_csv('titanic.csv')
print(data.groupby('Pclass')['Survived'].value_counts())


import pandas as pd
data=pd.read_csv('titanic.csv')
print(data['Age'].describe())


import pandas as pd
data=pd.read_csv('titanic.csv')
data['FamilySize']=data['Parch']+data['SibSp']+1
print(data['FamilySize'][15])


import pandas as pd
data=pd.read_csv('titanic.csv')
print(data.groupby('Survived')['Age'].mean())


import pandas as pd
data=pd.read_csv('titanic.csv')
print(data[(data['Sex'] == 'female') & (data['Pclass'] == 1) & (data['Survived'] == 1)].count())


import pandas as pd
data=pd.read_csv('titanic.csv')
print(data[(data['Age'] < 18) & (data['Parch'] == 0)].count())