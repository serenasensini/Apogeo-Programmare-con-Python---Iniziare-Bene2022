#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Caso di studio: Titanic


# In[ ]:


# Import delle librerie
import pandas as pd


# In[ ]:


# Leggo dal CSV
data = pd.read_csv("titanic.csv")


# In[5]:


# Stampo i primi cinque record del dataset
data.head()


# In[18]:


# Stampo le informazioni su righe e colonne del dataset
data.shape


# In[7]:


# Stampo i nomi delle colonne
data.columns.values


# In[8]:


# Calcolo la media dell'età dei passeggeri
data['Age'].mean()


# In[40]:


# Visualizzo l'età dei passeggeri tramite un istogramma a barre
data.hist(column="Age")


# In[45]:


# Uso matplotlib per rappresentare l'eta dei passeggeri
import matplotlib.pyplot as plt

# Creazione dell'istogramma
plt.hist(data.Age, color = "skyblue")
# Definizione dei dati da rappresentare
plt.axvline(data.Age.mean(), color='k', linestyle='dashed', linewidth=1)
# Titolo del grafico
plt.title('Ages of Passengers on Titanic')
# Etichetta dell'asse y
plt.ylabel('Count')
# Etichetta dell'asse x
plt.xlabel('Age (in Years)')

plt.savefig("ages_passengers_titanic.png")


# In[10]:


# Calcolo della correlazione: misura di quanto due o più attributi di uno stesso gruppo abbiano la tendenza a variare insieme

# Correlazione tra i sopravvissuti e l'età
correlation = data['Survived'].corr(data['Age'])

'''
# 1 = esiste una correlazione, per cui se uno dei due attributi aumenta, anche l'altro aumenta proporzionalmente
# -1 = esiste una correlazione inversa, per cui se uno dei due attributi aumenta, l'altro diminuisce proporzionalmente
# 0 = non esiste correlazione tra i due attributi
'''
# Stampa correlazione
correlation


# In[ ]:


# Stampa delle righe dalla 1 alla 4 della colonna "Survived" e "Age"
data.loc[1:4, ["Survived", "Age"]]


# In[16]:


# Converte la colonna "Sex" in due colonne dove "female" e "male" sono associati a valori binari che il sistema può interpretare
data['Sex'].str.get_dummies()


# In[49]:


'''
str.get_dummies crea variabili fittizie (intere) che corrispondono ai valori della stringa e corrwith è un altro modo per calcolare la correlazione quando è necessario farlo tra una combinazione di righe e colonne (corr funziona solo con le colonne).
'''
data['Sex'].str.get_dummies().corrwith(data['Survived']/data['Survived'].max())


# In[50]:


data.corr()


# In[65]:


'''
Donne e bambini? Conosciamo tutti il vecchio detto che quando una nave sta affondando,  "donne e bambini prima di tutti" nelle scialuppe di salvataggio. Questo vecchio modo dire rispecchia la realtà dei sopravvissuti sul Titanic? Sono sopravvissute più donne e bambini degli uomini adulti? Il sesso, l'età o la classe delle persone contavano di più sul Titanic per la loro sopravvivenza? '''


# In[20]:


children = data[data['Age'] < 16]
children.shape


# In[21]:


children.head()


# In[53]:


children.hist()


# In[22]:


living_children = data[(data['Age'] < 16) & (data['Survived'] == 1)]
living_children.hist()
living_children.count()


# In[56]:


not_surviving_children = data[(data['Age'] < 16) & (data['Survived'] == 0)]
not_surviving_children
not_surviving_children.count()


# In[59]:


# Probabilità di sopravvivenza se donna o bambino

women_and_children = data[(data['Sex'] == "female") | (data['Age'] < 16)]
w_a_c_survival_rate = women_and_children['Survived'].value_counts(normalize=True) * 100
w_a_c_survival_rate


# In[26]:


data.shape


# In[27]:


data[data['Survived']==1].count()


# In[64]:


# Probabilità di sopravvivenza se uomo

adult_men = data[(data['Sex'].str.match('male')) & (data['Age'] > 16)]
a_m_survival_rate = adult_men['Survived'].value_counts(normalize=True) * 100
a_m_survival_rate


# In[ ]:


# Meno di 1 uomo su 5 sul Titanic è sopravvissuto.

# Quasi 4 donne su 5 sul Titanic sono sopravvissute.


# In[67]:


surviving_men = data[(data['Sex'] == "male") & (data['Age'] > 16) & (data['Survived'] == 1)]
surviving_men.describe()


# In[68]:


dead_men = data[(data['Sex'] == "male") & (data['Age'] > 16) & (data['Survived'] == 0)]
dead_men.describe()

