
# coding: utf-8

# In[14]:

name = "something"
name = "Su Ji"


# In[15]:


age = 30


# In[16]:


print(name)


# In[17]:


print(age)


# In[18]:


print("my name is")


# In[19]:


print("my name is", name)


# In[20]:


print("my age is", age)


# In[21]:


print("my name is", name, "and my age is", age)


# In[24]:


newage = age - 10


# In[25]:


print(newage)


# In[26]:


multipliedage = age * 2


# In[27]:


print("your age is actually", newage)


# In[28]:


print("your age is actually", multipliedage)


# In[29]:


NewAge = 100


# In[30]:


newage = 50


# In[31]:


sequence = "CTAGCTAG"


# In[32]:


print(sequence)


# In[33]:


print(sequence[0])


# In[34]:


print(sequence[3])


# In[35]:


print("my forth letter is", sequence[3])


# In[36]:


print("my fourth letter is", sequence[3])


# In[37]:


len(sequence)


# In[38]:


print("the length of the sequence", len(sequence))


# In[39]:


cox1 = "CTAG"


# In[40]:


print(sequence[0,3])


# In[41]:


print(sequence[0;3])


# In[42]:


sequence[0:2]


# In[43]:


sequence[0:3]


# In[44]:


type(sequence)


# In[45]:


type(age)


# In[46]:


cox2 = "TACG"


# In[47]:


cox1 = "CTAG"


# In[48]:


cox1 - cox2


# In[49]:


cox1 + cox2


# In[50]:


firstname = "suji"


# In[51]:


lastname = "park"


# In[52]:


firstname + lastname


# In[53]:


firstname + " " + lastname


# In[54]:


age


# In[55]:


len(age)


# In[56]:


name


# In[57]:


age


# In[58]:


name + age


# In[59]:


5**2


# In[60]:


print(5**2)


# In[61]:


print("5 square is", 5**2)


# In[62]:


5%2


# In[63]:


# this is a comment


# In[64]:


# adding two sequences because they turned out to be the same genes


# In[65]:


cox1 + cox2


# In[66]:


max(22,2,5)


# In[67]:


max(23,2,5)


# In[68]:


max(3,"suji")


# In[69]:


round(3.1415)


# In[70]:


round(3.1415,2)


# In[71]:


min(23,2,5)


# In[72]:


help(min)


# In[73]:


help(round)


# In[74]:


help(round


# In[75]:


name = "suji


# In[76]:


print("age is", aged)


# In[77]:


max(21,32,45)


# In[78]:


max(21,32,45) + min(21,32,45)


# In[79]:


hundred_C = "c" * 100


# In[80]:


print(hundred_C)


# In[81]:


hundred_C + cox1


# In[82]:


cox1 + hundred_C


# In[83]:


len(hundred_C+cox1)


# In[84]:


import math


# In[85]:


math.cos(180)


# In[86]:


math.sin(180)


# In[87]:


math.cos(180*pi/180)


# In[88]:


print("the sine of 180 is", math.sin(180))


# In[89]:


math.pi


# In[90]:


math.sin(math.pi)


# In[91]:


math.sin(180*math.pi/180)


# In[92]:


math.cos(math.pi)


# In[93]:


math.cos(90*math.pi/180)


# In[94]:


help(math)


# In[95]:


math.sqrt(4)


# In[96]:


import math as m


# In[97]:


m.sqrt(4)


# In[98]:


from math import cos


# In[99]:


cos(m.pi)


# In[100]:


from math import cos, pi


# In[101]:


cos(pi)


# In[102]:


from math import degrees, pi


# In[103]:


angle = degrees(pi/2)


# In[104]:


angle


# In[105]:


from math import *


# In[106]:


import pandas


# In[107]:


pandas.read_csv("data/gapminder_gdp_oceania.csv")


# In[108]:


pandas.read_csv("data/gapminder_gdp_asia")


# In[109]:


pandas.read_csv("data/gapminder_gdp_asia.cs")


# In[110]:


pandas.read_csv("data/gapminder_gdp_asia.csv")


# In[111]:


pandas.read_csv("data/gapminder_gdp_europe.csv")


# In[112]:


pandas.read_csv("data/gapminder_gdp_americas.csv")


# In[113]:


pandas.read_csv("data/gapminder_gdp_oceania.csv")


# In[114]:


data = pandas.read_csv("data/gapminder_gdp_oceania.csv")


# In[115]:


print(data)


# In[116]:


data = pandas.read_csv("data/gapminder_gdp_oceania.csv", index_col="country")


# In[117]:


print(data)


# In[118]:


data.info()


# In[119]:


data


# In[120]:


data.T


# In[121]:


data.describe()


# In[122]:


data.T.describe()


# In[123]:


data_america = pandas.read_csv("data/gapminder_gdp_americas.csv")


# In[124]:


data_america.describe()


# In[125]:


data_america.T.describe()


# In[126]:


data_america = pandas.read_csv("data/gapminder_gdp_africa.csv", index_col="country")


# In[127]:


data_america.T.describe()


# In[128]:


data.columns


# In[129]:


data_america.columns


# In[130]:


data


# In[131]:


data(1,2)


# In[132]:


data.iloc[1.2]


# In[133]:


data.iloc[1,2]


# In[134]:


data.iloc[0,0]


# In[135]:


data.loc["Australia","gdpPercap_1952"]


# In[136]:


data


# In[137]:


data.loc["Australia",:]


# In[138]:


data.loc[:,"gdpPercap_1952"]


# In[139]:


data.loc[:,"gdpPercap_1952", "gdpPercap_1962"]


# In[140]:


data.loc[:,"gdpPercap_1952": "gdpPercap_1962"]


# In[141]:


data.loc["Australia","gdpPercap_1952": "gdpPercap_1962"]


# In[142]:


data.loc[:,"gdpPercap_1952": "gdpPercap_1962"].max()


# In[143]:


data.loc["Australia","gdpPercap_1952": "gdpPercap_1962"].max()


# In[144]:


data.loc[:,"gdpPercap_1952": "gdpPercap_1962"].min()


# In[145]:


data.loc["Australia","gdpPercap_1952": "gdpPercap_1962"].min()


# In[146]:


subset = data.loc[:,"gdpPercap_1952": "gdpPercap_1962"]


# In[147]:


print(subset)


# In[148]:


print(subset>11000)


# In[149]:


subset[subset>11000]


# In[150]:


subset[subset>11000].describe()


# In[151]:


data_eu = pandas.read_csv("data/gapminder_gdp_europe.csv", index_col="country")


# In[152]:


data_eu("Serbia", "gdpPercap_2007")


# In[153]:


data_eu.loc("Serbia","gdpPercap_2007")


# In[154]:


data_eu


# In[155]:


data_eu.loc["Servia","gdpPercap_2007"]


# In[156]:


data_eu.loc["Serbia","gdpPercap_2007"]


# In[157]:


data_eu.loc["Italy":"Norway", "gdpPercap_1962":"gdpPercap_1972"]

