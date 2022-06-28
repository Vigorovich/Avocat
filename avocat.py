#!/usr/bin/env python
# coding: utf-8

# # Analyse de données sur un dataset choisi sur kaggle (data set sur les avocats)

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot
import pylab


# In[3]:


avocado = pd.read_csv("data2.csv", sep=";")


# In[4]:


#Lecture du data set
avocado.head(10)


# In[5]:


#Suppression de la première colonne
avocado= avocado.drop(columns={"Unnamed: 0"})


# In[6]:


#Informations sur le nombre de colonnes et de lignes

avocado.shape


# In[7]:


#Information sur le type des variables
avocado.info()


# In[8]:


#Vérification de doublons
avocado.duplicated().sum()


# In[9]:


#Vérification de données manquantes
avocado.isna().sum()


# In[10]:


round(avocado.describe())


# In[11]:


plt.bar(avocado["type"],avocado["AveragePrice"])
plt.title("Prix moyen par type d'avocat")
plt.show()


# In[52]:


plt.bar(avocado["region"],avocado["AveragePrice"])
plt.rcParams["figure.figsize"]=[20,20]
plt.xticks(rotation=90)
plt.title("Prix moyen des avocats en fonction des régions")
plt.show()


# In[19]:


data=avocado["year"].value_counts()


# In[25]:


plt.rcParams["figure.figsize"]=[9,9]
plt.pie(data.values, labels=data.index, autopct='%1.1f%%', startangle=90)
plt.title("Pourcentage d'avocat produit par année")
plt.draw()


# In[54]:


#Evolution du prix des avocats dans une ville précise
#Les lignes conçernant la ville de Seatle sont entre 2238 et 2288
first_year_seatle = avocado[2238:2288]

x= first_year_seatle["Date"]
y= first_year_seatle["AveragePrice"]

plt.figure(figsize=(10,10))
plt.plot(x,y)
plt.title("Evolution du prix en 2015 à Seatle")
plt.xlabel("Par semaine décroissante")#Parce que je n'ai toujours pas réussi à inverser l'ordre 
plt.ylabel("Prix moyen")
plt.xticks(rotation=45)

plt.show()


# # Corrélation 

# In[9]:


data = avocado.drop(["Unnamed: 0","Date","type","year","region"],axis=1)
data.corr(method="spearman").style.format("{:.2}").background_gradient(cmap=pyplot.get_cmap('coolwarm'))


# # Régression linéaire

# In[42]:


X= avocado.iloc[0:52,2]
Y= avocado.iloc[0:52,7]


# In[43]:


axes =plt.axes()
axes.grid()
plt.scatter(X,Y)
plt.title("Corrélation linéaire entre le prix moyen et le total de sac(en 2015,en Albany)")
plt.show()


# In[44]:


from scipy import stats
slope, intercept, r_value, p_value, std_err = stats.linregress(X, Y)


# In[45]:


def predict(X):
   return slope * X + intercept


# In[46]:


fitLine = predict(X)
plt.plot(X, fitLine, c='r')


# In[ ]:




