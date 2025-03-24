#!/usr/bin/env python
# coding: utf-8

# ## Practice Exercise 0

# Below is a dataset and my recommendation for visualizations to create.
# 
# Visualizations covered:
# - horizontal bar plot
# - vertical bar plot
# - box plot
# - histogram

# ### Import Modules

# In[ ]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('', 'matplotlib inline')


# ### Titanic Dataset

# The Titanic is a well-known ship that sunk on its maiden voyage in 1912 after collision with an iceberg. Many were killed in the incident. You may recognize this name from the movie with Leonardo DiCaprio. 
# 
# Please read up on the data dictionary here: https://www.kaggle.com/c/titanic/data
# 
# We'll do exploratory analysis to learn about the people on the ship.

# #### Question 1: A l'aide de pandas importez et lisez le dataset
# 

# In[27]:


path=""
df = pd.read_csv(path+'41_Titanic2.csv')
df


# #### Question 2: Quel est le type de la variable df?
# 
# You can use the built-in type function to check: https://docs.python.org/3/library/functions.html#type
# 

# In[28]:


df.dtypes


# Pandas dataframe

# #### Question 3:Affichez les 5 premières lignes et les 5 dernières lignes du dataset
# 

# In[5]:


# les 5 premières lignes du dataset
df.head()


# In[6]:


# les 5 dernières lignes du dataset
df.tail()


# #### Question 4: De combien de ligne ,colonne est constitué le dataset?
# 

# In[10]:


df.shape
#(nombre de lignes, nombre de colonnes)


# #### Question 5: Dessinez le plot de l'age
# 
# I'd recommend reading up on the math behind box plots and other examples: 
# - https://help.plot.ly/what-is-a-box-plot/
# - https://dfrieds.com/data-visualizations/when-use-box-plots
# 
# - X-axis should be age. 
# - Include a relevant title
# - Make the plot's figure slightly bigger than the default styles
# - Make the font size of the title, x-ticks and x-label to be slightly larger than the default so it's easier to read.
# 
# You may need to filter the dataframe by a specific column. If you don't know how, you can see an example here: https://chrisalbon.com/python/data_wrangling/filter_dataframes/
# 
# I'd recommend using Seaborn's box plot functionality. However, make sure to filter out null age values! https://seaborn.pydata.org/generated/seaborn.boxplot.html
# 
# I provide code in the first box that should apply styles to all plots created in this Notebook. You can learn more here: https://seaborn.pydata.org/tutorial/aesthetics.html

# In[11]:


df_filtered = df[df['age'].notnull()]
sns.set(style="darkgrid", font_scale=1.2)
plt.figure(figsize=(8, 3))  
sns.boxplot(x='age', data=df_filtered)
plt.title('Plot des ages',fontsize=20)
plt.xlabel('Age', fontsize=13)
plt.ylabel('Fréquence', fontsize=13)
plt.show()


# #### Question 6: Y'a t'il des valeurs extremes?

# #Oui, on remarque qu'il y'a des valeurs extremes que l'ont peu voir situées en dehors des limites de la boite à moustaches

# #### Question 7: Ecrivez un code pour afficher les quantiles?
# 
# Hint: you can use Pandas `quantile()` method to find the 25th and 75th percentile: https://pandas.pydata.org/pandas-docs/version/0.23.1/generated/pandas.Series.quantile.html. 
# 
# Alternatively, you can see the output with Pandas `describe()` method: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.describe.html

# In[13]:


quantiles = df['age'].describe()
quantiles


# Premier quantile : 21.125
# Deuxième quantile (médiane) : 28
# Troisième quantile : 38

# #### Question 8: Quelle l'age du passager le plus vieux du titanic?
# 
# Hint: you can use the `max()` method found here: https://pandas.pydata.org/pandas-docs/version/0.21/generated/pandas.Series.max.html
# 
# Please answer this question programmatically.

# In[26]:


df['age'].max()
print("L'age du passager le plus vieux du titanic est de", df['age'].max(), "ans" )


# #### Question 9: Quel est l'age du plus jeune?
# 
# 

# In[15]:


df['age'].min()
print("L'age du passager le plus jeune du titanic est de", df['age'].min(), "ans" )


# #### Question 10: Dessiner l'histogramme de l'age des personnes du titanic?
# 
# You can learn more about histograms here: 
# 
# - https://www.mathsisfun.com/data/histograms.html
# - https://dfrieds.com/data-visualizations/when-use-histogram
# - https://help.plot.ly/histogram/
# 
# A histogram is another type of visualization used to visualize the distribution of a continous variable - in our case, age of people on the Titanic.
# 
# I'd recommend using Seaborn's `distplot()` method. I prefer this Seaborn method over Pandas Plot because Seaborn's method automatically calculates an optimal bin size. Learn more here: https://seaborn.pydata.org/generated/seaborn.distplot.html
# 
# With your plot, include:
# - title
# - x-label
# - y-label
# 
# 

# In[22]:


sns.set(style="darkgrid", font_scale=1)
plt.figure(figsize=(7, 6))
sns.histplot(data=df, x='age', kde=False)
plt.title("Histogramme des ages des personnes du Titanic",fontsize=17)
plt.xlabel('Ages',fontsize=13)
plt.ylabel('Fréquences',fontsize=13)
plt.show()


# This histogram reveals similar information to the box plot above. I'm curious to learn more about the age differences of different genders of the Titanic.

# #### Question 11: Draw two box plots on the same axes/plot to compare the ages of males versus females
# 
# Please read the documentation on this Seaborn page about how to easily build side-to-side box plots: https://seaborn.pydata.org/generated/seaborn.boxplot.html
# 
# You only need one line of code to generate this visualization and one additional line to set a title.
# 
# Criteria for visualization:
# - Orientation of both box plots should be vertical
# - Make sure the x-axis and y-axis have proper labels
# - Include a detailed title
# - Make sure the figure size is slightly larger than default
# - Make sure the labels, ticks and title are larger font size than the default

# In[25]:


sns.set(style="darkgrid", font_scale=1)
plt.figure(figsize=(7, 7)) 
sns.boxplot(x='sex', y='age', data=df)
plt.title('Plots des âges entre les hommes et les femmes sur le Titanic', fontsize=17)
plt.xlabel('Genre', fontsize=10)
plt.ylabel('Age', fontsize=10)
plt.show()


# #### Question 13: Y'a t'il des valeurs extremes pour les hommes et les femmes

# En observant les deux boites à moustache, on remarque qu'il n'y a pas de valeurs en dehors des limites du graphique chez les femmes alors qu'il y en a chez les hommes donc on peut een déduire qu'il n'y a pas de valeurs extremes chez les femmes tandis qu'il y'a des valeurs extremes chez les hommes.

# #### Question 14: faire un boxplot de la distribution des montants.
# 
# A box plot is ideal here because we can easily see outliers of people that paid a very large amount of money for their ticket.
# 
# - X-axis should be fare amount (U.S. dollars). 
# - Include a relevant title.
# - Make the plot's figure slightly bigger than the default styles.
# - Make the font size of the title, x-ticks and x-label to be slightly larger than the default so it's easier to read.

# In[33]:


sns.set(style="darkgrid", font_scale=1)
plt.figure(figsize=(10, 8)) 
sns.boxplot(x='fare', data=df)
plt.title('Distribution des montants', fontsize=18)
plt.xlabel('Fare Amount in USD', fontsize=14)
plt.xticks(fontsize=13)  
plt.ylabel('Fréquences', fontsize=15)
plt.show()


# #### Question 15: Créer un boxplot groupeé par class

# Criteria for visualization:
# - Orientation of both box plots should be horizontal
# - Make sure the x-axis and y-axis have proper labels
# - Include a detailed title
# - Make sure the figure size is slightly larger than default
# - Make sure the labels, ticks and title are larger font size than the default

# In[36]:


sns.set(style="darkgrid", font_scale=1)
plt.figure(figsize=(8, 7))  
sns.boxplot(x='fare', y='class', data=df, orient='h')
plt.title('Boxplot par Class', fontsize=17)
plt.xlabel('Fare in USD', fontsize=13)
plt.ylabel('Class', fontsize=13)
plt.xticks(fontsize=13)  
plt.yticks(fontsize=13)  
plt.show()


# #### Question 16: Quel classe de ticket à la plus grande medianne?

# In[37]:


mediane = df.groupby('class')['fare'].median
mediane ('class')


# La classe de ticket à la plus grande médianne est la première.

# #### Question 17: quel classe de ticket a le plus grand range?
# 
# Documentation on what is the definition of range: https://www.mathsisfun.com/definitions/range-statistics-.html

# In[42]:


range = df.groupby('class')['fare'].apply(lambda x: x.max() - x.min())
classe_max_range = range.idxmax()
classe_max_range


# La classe avec le plus grand range est la première.

# #### Question 18:Creer un boxplot grouper en foncton des variables: `class` and `survived`.
# 
# Criteria for visualization:
# - Orientation of box plots should be horizontal
# - Make sure the x-axis and y-axis have proper labels
# - Include a detailed title
# - Make sure the figure size is slightly larger than default
# - Make sure the labels, ticks and title are larger font size than the default
# - The legend should show the survival categories

# In[47]:


sns.set(style="darkgrid", font_scale=1)
plt.figure(figsize=(12, 10))  
sns.boxplot(x='fare', y='class', hue='survived', data=df, orient='h')
plt.title('Boxplot par Class et Survival', fontsize=17)
plt.xlabel('Fare', fontsize=13)
plt.ylabel('Class',fontsize=13)
plt.xticks(fontsize=13)  
plt.yticks(fontsize=13) 
plt.legend(title='Survived', loc='best', fontsize=16)
plt.show()


# #### Question 19: Pour quel classe de ticket le plus grand montant de ticket à été payé

# En observant le graphique, le plus grand montant de ticket a été payé par la première classe. 

# #### Question 20: Creer un bar plot du nombre en de personne embarqués en fonction de la ville
# 
# Our DataFrame provides a row for each unique person. We want to show the count of people from each town using bars.
# 
# You can read more about vertical bar charts here: https://dfrieds.com/data-visualizations/when-use-vertical-bar-chart
# 
# We can use Seaborn's `countplot()` method to create the bar plot and help us calculate the count of people in each town. Read more here: https://seaborn.pydata.org/generated/seaborn.countplot.html. You'll have to use the `x`, `data`, and `orient` arguments to create the desired visualization.
# 
# Criteria for visualization:
# - Vertical bar plot
# - Make sure the x-axis and y-axis have proper labels
# - Include a detailed title
# - Make sure the figure size is slightly larger than default
# - Make sure the labels, ticks and title are larger font size than the default

# In[49]:


sns.set(style="darkgrid")
plt.figure(figsize=(7, 7)) 
sns.countplot(x='embarked', data=df)
plt.title('Nombre de personnes embarquées en fonction de la ville', fontsize=18)
plt.xlabel('Ville', fontsize=13)
plt.ylabel('Nombre de peersonnes embarquées', fontsize=13)
plt.xticks(fontsize=13)  
plt.yticks(fontsize=13)  
plt.show()

