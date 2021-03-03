#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import numpy and pandas (for the data load)
import numpy as np
import pandas as pd


# In[2]:


#Question for Somanchi:
# I am looking to plot out the number of people in the Phillipines that are very concerned about the spread of COVID
#in their community over the past year.


#So far I have masked around Philipines and very concerend and am now looking to plot this over the past year



# In[3]:



premise_data = pd.read_csv('covid-19_2020-12-31_survey_covid-19_impact_4850691271294976_4850691271294976_all-2.csv')


# In[ ]:


premise_data.head()


# In[ ]:


premise_data['how_satisfied_were_you_with_the_level_of_care_you_received'].value_counts()


# In[ ]:


premise_data.columns


# In[ ]:


premise_data['batch_date'] = pd.to_datetime(premise_data['batch_date'])
premise_data.dtypes


# In[ ]:


premise_data['batch_date'].min()
premise_data['batch_date'].max()


# In[ ]:


premise_data.set_index('batch_date', inplace=True)
premise_data.head()


# In[ ]:


countries = premise_data['L0_name'].value_counts()
print(countries)


# In[ ]:


premise_data['how_concerned_are_you_about_the_spread_of_covid_19_in_your_community'].value_counts()


# In[ ]:


mask_phil = (premise_data['L0_name'] == 'Philippines')
premise_data[mask_phil]

premise_data[mask_phil]['how_concerned_are_you_about_the_spread_of_covid_19_in_your_community'].value_counts()


# In[ ]:


scale_mapper = {'Very concerned':5, 'Concerned':4, 'Neither concerned nor unconcerned':3,'Unconcerned':2,'Very unconcerned':1}


# In[ ]:


# Map feature values to scale
premise_data['how_concerned_are_you_about_the_spread_of_covid_19_in_your_community'] = premise_data['how_concerned_are_you_about_the_spread_of_covid_19_in_your_community'].replace(scale_mapper)


# In[ ]:


premise_data.loc['Apr 2020']['how_concerned_are_you_about_the_spread_of_covid_19_in_your_community'].sum()
premise_data.loc['May 2020']['how_concerned_are_you_about_the_spread_of_covid_19_in_your_community'].sum()
premise_data.loc['June 2020']['how_concerned_are_you_about_the_spread_of_covid_19_in_your_community'].sum()
premise_data.loc['July 2020']['how_concerned_are_you_about_the_spread_of_covid_19_in_your_community'].sum()
premise_data.loc['Aug 2020']['how_concerned_are_you_about_the_spread_of_covid_19_in_your_community'].sum()
premise_data.loc['Sep 2020']['how_concerned_are_you_about_the_spread_of_covid_19_in_your_community'].sum()
premise_data.loc['Oct 2020']['how_concerned_are_you_about_the_spread_of_covid_19_in_your_community'].sum()
premise_data.loc['Nov 2020']['how_concerned_are_you_about_the_spread_of_covid_19_in_your_community'].sum()
premise_data.loc['Dec 2020']['how_concerned_are_you_about_the_spread_of_covid_19_in_your_community'].sum()
premise_data.loc['Jan 2021']['how_concerned_are_you_about_the_spread_of_covid_19_in_your_community'].sum()


# In[ ]:


concerned=premise_data[['how_concerned_are_you_about_the_spread_of_covid_19_in_your_community']]
concerned.head()


# In[ ]:


import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

plt.style.use('seaborn')


# In[ ]:


premise_data.resample('M').sum().head() #giving you the end of every month and the sum


# In[ ]:


concern_by_month= premise_data.groupby(['batch_date'])
concern_by_month.head()


# In[ ]:


by_month= concern_by_month[['how_concerned_are_you_about_the_spread_of_covid_19_in_your_community']].sum()
by_month.head()


# In[ ]:



figure, axes = plt.subplots()

by_month.loc['April 2020':'May 2020'].plot(ax = axes)
axes.legend()



# In[ ]:


group_by_month= premise_data.groupby(['how_concerned_are_you_about_the_spread_of_covid_19_in_your_community', 'batch_date'])


# In[ ]:


phil_data_mask = (premise_data['L0_name']=='Philippines') &  (premise_data['how_concerned_are_you_about_the_spread_of_covid_19_in_your_community']==5)
premise_data[phil_data_mask]


# In[ ]:


premise_data['batch_date'].min()
#premise_data['batch_date'].max()


# In[ ]:


phil_data_mask.loc['Apr 7th 2020':'May 7th 2020']


# In[ ]:


import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

plt.style.use('seaborn')


# In[ ]:


#basically I want to plot the sum for each month over the course of the year and then produce insights after that. 


# In[ ]:


premise_data.columns


# In[ ]:


#Recoding Factors Below 


# In[4]:


recode_cols = [col for col in premise_data.columns if 'concerned' in col]
print(recode_cols)


# In[5]:


premise_data['how_concerned_are_you_that_you_personally_will_contract_covid_19'].value_counts()


# In[6]:


premise_data['how_concerned_are_you_that_your_economic_situation_will_be_negatively_impacted_in_the_next_30_days_as_a_result_of_a_change_in_economic_activity'].value_counts()


# In[7]:


premise_data['has_your_income_been_at_all_affected_by_the_covid_19_pandemic'].value_counts()


# In[8]:


scale_mapper = {'Very unconcerned':1, 'Unconcerned':2, 'Neither concerned nor unconcerned':3, 'Concerned':4, 'Very concerned':5}
for col in recode_cols:
    premise_data[col]=premise_data[col].replace(scale_mapper)


# In[9]:


premise_data['how_concerned_are_you_that_you_personally_will_contract_covid_19'].value_counts()


# In[11]:


scale_mapper2 = {'Yes, I have been laid off or have otherwise lost my job':1, 'Yes, I have seen a reduction in my paycheck/hours/sales':2, 'No, not at all':3}
premise_data['has_your_income_been_at_all_affected_by_the_covid_19_pandemic']=premise_data['has_your_income_been_at_all_affected_by_the_covid_19_pandemic'].replace(scale_mapper2)


# In[12]:


premise_data['has_your_income_been_at_all_affected_by_the_covid_19_pandemic'].value_counts()


# In[ ]:





# In[ ]:




