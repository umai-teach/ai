# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YT6syUxmpky0x2bbhfgYhhP1mGQnvMrM
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 

sns.set_style('white') 
# %matplotlib inline 

column_names = ['user_id', 'item_id', 'rating', 'timestamp']

path = 'C:/Users/Khan/Downloads/file.tsv'

df = pd.read_csv(path, sep='\t', names=column_names)

df.head()

movie_titles = pd.read_csv('C:/Users/Khan/Downloads/Movie_Id_Titles.csv')
movie_titles.head()
data = pd.merge(df, movie_titles, on='item_id')
data.head()

data.groupby('title')['rating'].mean().sort_values(ascending=False).head()
data.groupby('title')['rating'].count().sort_values(ascending=False).head()

ratings = pd.DataFrame(data.groupby('title')['rating'].mean())

ratings['num of ratings'] = pd.DataFrame(data.groupby('title')['rating'].count())

ratings.head()

 
plt.figure(figsize =(10, 4)) 

ratings['num of ratings'].hist(bins = 70) 

 
plt.figure(figsize =(10, 4)) 

ratings['rating'].hist(bins = 70) 

moviemat = data.pivot_table(index ='user_id', 
			columns ='title', values ='rating') 

moviemat.head() 

ratings.sort_values('num of ratings', ascending = False).head(10) 
 
starwars_user_ratings = moviemat['Star Wars (1977)'] 
liarliar_user_ratings = moviemat['Liar Liar (1997)'] 

starwars_user_ratings.head() 

similar_to_starwars = moviemat.corrwith(starwars_user_ratings) 
similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings) 

corr_starwars = pd.DataFrame(similar_to_starwars, columns =['Correlation']) 
corr_starwars.dropna(inplace = True) 

corr_starwars.head() 
 
corr_starwars.sort_values('Correlation', ascending = False).head(10) 
corr_starwars = corr_starwars.join(ratings['num of ratings']) 

corr_starwars.head() 

corr_starwars[corr_starwars['num of ratings']>100].sort_values('Correlation', ascending = False).head()  
corr_liarliar = pd.DataFrame(similar_to_liarliar, columns =['Correlation']) 
corr_liarliar.dropna(inplace = True) 

corr_liarliar = corr_liarliar.join(ratings['num of ratings']) 
corr_liarliar[corr_liarliar['num of ratings']>100].sort_values('Correlation', ascending = False).head()

