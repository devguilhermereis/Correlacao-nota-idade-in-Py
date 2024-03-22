#!/usr/bin/env python
# coding: utf-8

# In[61]:


#Pacotes necessários
from scipy import *
from statistics import mean, median
import pandas as pd
import numpy as np


# In[42]:


#Média e medianas - Notas e idades

lista_notas = [8,7,7,7,7,8,5,2,4,4,10,10,10,10,4,6,7,7,7,8]
lista_idades = [10,11,12,9,10,11,10,10,10,10,11,11,10,9,10,10,11,11,10,10]


# In[43]:


lista_notas


# In[44]:


lista_idades


# In[45]:


#Calculando a média e a mediana para notas

print('A média das notas é:', mean(lista_notas))
print('A mediana das notas é:', median(lista_notas))

#Calculando a média e a mediana das idades

print('A média das idades é:', mean(lista_idades))
print('A mediana das idades é:', median(lista_idades))


# In[46]:


dict = {'notas': lista_notas, 'idades': lista_idades}


# In[47]:


df = pd.DataFrame(dict)


# In[48]:


df


# In[49]:


#50% notas inferiores
mean(df.notas.sort_values(ascending=True)[0:10])


# In[50]:


#50% notas superiores
mean(df.notas.sort_values(ascending=True)[10:20])


# In[51]:


#50% idades inferiores
mean(df.idades.sort_values(ascending=True)[0:10])


# In[52]:


#50% idades inferiores
mean(df.idades.sort_values(ascending=True)[10:20])


# In[53]:


#média das notas para 50% menores idades
df_ordenado_idades = df.sort_values(by=['idades'])
df_recorte_menores_idades = df_ordenado_idades[0:10]
mean(df_recorte_menores_idades.notas)


# In[54]:


#média das notas para 50% maiores idades
df_ordenado_idades = df.sort_values(by=['idades'])
df_recorte_maiores_idades = df_ordenado_idades[10:20]
mean(df_recorte_maiores_idades.notas)


# In[58]:


#Coef notas
cv_notas = np.std(lista_notas) / mean(lista_notas)
cv_notas*100


# In[59]:


#Coef idades
cv_idades = np.std(lista_idades) / mean(lista_idades)
cv_idades*100


# In[62]:


from scipy import stats


# In[63]:


stats.pearsonr(df.notas, df.idades)

