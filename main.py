import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#-----------Understanding data-------------------
colors = pd.read_csv('colors.csv')
sets = pd.read_csv('sets.csv')

#--------------Reading data-------------
print(colors.head(10))
print(sets.head(10))

#-----------Exploring Colors-----------
n_color = colors['name'].nunique()
print('there are {} different colors in this dataset'.format(n_color))

colors['name'] = colors['name'].apply(lambda x : x.lower())
colors['name'] = [i.replace(' ','_') for i in colors['name']]

plt.figure(figsize=(25,10))
sns.countplot(colors['name'] , edgecolor = 'k' , palette='Set1')
plt.xticks(rotation = 90)
plt.show()

#-------------Transparent Colors in Lego Sets--------------
transparent = colors.groupby(colors['is_trans']).count()
print(transparent)

plt.figure(figsize=(10,10))
sns.countplot(x = 'is_trans' , data = colors)
plt.show()

#-----------Explore Lego Sets------------------
ave = sets[['year' , 'num_parts']].groupby('year' ,  as_index=False ).mean()
print(ave)
ave.plot(x = 'year', y = 'num_parts' , color = 'darkblue' )
plt.show()

#-------------Lego Themes Over Years--------------
themes = sets[['year' , 'theme_id']].groupby('year' , as_index=False).count()
print(themes)