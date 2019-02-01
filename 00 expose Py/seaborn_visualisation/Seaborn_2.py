# coding: utf-8

# ###### import seaborn as sns
# %matplotlib inline
# tips = sns.load_dataset("tips")
# tips.head()

# In[24]:


import seaborn as sns

# In[25]:


get_ipython().magic('matplotlib inline')

# In[26]:


tips = sns.load_dataset('tips')

# In[27]:


sns.lmplot(x="total_bill", y="tip", data=tips, hue="sex", markers=['o', 'v'])
# markers=['o','v']
# scatter_kws={'s':120}


# In[28]:


sns.lmplot(x="total_bill", y="tip", data=tips, col="sex")
# row="time"
# dessiner une grille en spécifiant le critère ligne | colonne


# In[29]:


sns.lmplot(x="total_bill", y="tip", data=tips, col="day", hue="sex")
# aspect=0.5,size=8
