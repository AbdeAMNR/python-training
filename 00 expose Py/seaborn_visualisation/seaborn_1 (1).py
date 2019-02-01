# In[14]:


import seaborn as sns

# from IPython.display import display


# In[15]:


get_ipython().magic('matplotlib inline')

# In[16]:


tips = sns.load_dataset('tips')
# iris = sns.load_dataset('iris')


# In[77]:


tips.head(8)

# In[18]:


sns.distplot(tips["total_bill"], kde=False)
# diagramme en baton


# In[19]:


sns.kdeplot(tips["total_bill"])
# courbe


# In[79]:


sns.jointplot(x="total_bill", y="tip", data=tips, kind="hex")
# kind="kde"
# kind="hex"
# kind="reg"
# graphique pour 2 variables


# In[21]:


sns.pairplot(tips, hue="sex", x_vars="size", y_vars=["tip", "total_bill"], kind="reg")
# grille de graphique


# In[22]:


sns.countplot(x="sex", data=tips)
# compte le nombre de variable
