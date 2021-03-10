#!/usr/bin/env python
# coding: utf-8

# In[35]:


import numpy as np 
import pandas as pd 
from datetime import datetime, date, time
from datetime import timedelta
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use("fivethirtyeight")
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px

# set float display default
pd.set_option('display.float_format', lambda x: '%.2f' % x)

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)


# In[36]:


df = pd.read_csv("covid_with_factors.csv")


# In[37]:


df.head()


# In[38]:


column_values = df.apply(lambda x: len(x.unique()))
column_values[column_values >10]


# In[45]:


mult_responses = column_values[column_values >10].loc["what_kind_of_locations_or_facilities_are_offering_testing_in_your_city":"which_media_outlets_do_you_think_only_report_on_the_potential_disadvantages_of_a_covid_19_vaccine"]
print(mult_responses)


# In[44]:


df['what_kind_of_locations_or_facilities_are_offering_testing_in_your_city'].value_counts().sort_values(ascending=False)


# In[ ]:


get_ipython().run_line_magic('pinfo', 'what_kind_of_locations_or_facilities_are_offering_testing_in_your_city')
My primary care physicians office
Drive-up testing facility
Local health department
Urgent care clinic
Pharmacy
Emergency room
Hospital
Other


# In[27]:


df['locations_offering_testing_in_your_city_My_primary_care_physicians_office'] = df["what_kind_of_locations_or_facilities_are_offering_testing_in_your_city"].str.contains("My primary care physician", regex=False, na=False).astype(int)
#this is changing the name of the column in the data frame from what kind of locations to my primary care physicians office 


# In[29]:


df['locations_offering_testing_in_your_city_Drive_up_testing_facility'] = df["what_kind_of_locations_or_facilities_are_offering_testing_in_your_city"].str.contains("Drive-up testing facility", regex=False, na=False).astype(int)
df['locations_offering_testing_in_your_city_Local_health_department'] = df["what_kind_of_locations_or_facilities_are_offering_testing_in_your_city"].str.contains("Local health department", regex=False, na=False).astype(int)
df['locations_offering_testing_in_your_city_Urgent_care_clinic'] = df["what_kind_of_locations_or_facilities_are_offering_testing_in_your_city"].str.contains("Urgent care clinic", regex=False, na=False).astype(int)
df['locations_offering_testing_in_your_city_Pharmacy'] = df["what_kind_of_locations_or_facilities_are_offering_testing_in_your_city"].str.contains("Pharmacy", regex=False, na=False).astype(int)
df['locations_offering_testing_in_your_city_Emergency_room'] = df["what_kind_of_locations_or_facilities_are_offering_testing_in_your_city"].str.contains("Emergency room", regex=False, na=False).astype(int)
df['locations_offering_testing_in_your_city_Hospital'] = df["what_kind_of_locations_or_facilities_are_offering_testing_in_your_city"].str.contains("Hospital", regex=False, na=False).astype(int)
df['locations_offering_testing_in_your_city_Other'] = df["what_kind_of_locations_or_facilities_are_offering_testing_in_your_city"].str.contains("Other", regex=False, na=False).astype(int)


# In[30]:


check_cols = [col for col in df.columns if 'offering_testing_in_your_city' in col]
print(check_cols)


# In[31]:


df[check_cols][~df["what_kind_of_locations_or_facilities_are_offering_testing_in_your_city"].isnull()]


# In[46]:


df['which_of_the_following_activities_will_you_feel_comfortable_with_now_or_immediately_after_non_essential_businesses_re_open'].value_counts().sort_values(ascending=False)


# In[ ]:


'which_of_the_following_activities_will_you_feel_comfortable_with_now_or_immediately_after_non_essential_businesses_re_open

did not exist    
Visiting a friend’s home for a small social gathering (fewer than 10 people)
Shopping at non-essential stores
None of the above 
Shopping at non-essential stores^Visiting a friend’s home for a small social gathering (fewer than 10 people) 


# In[47]:


df['activities_will_you_feel_comfortable_with_now_or_immediately_after_non_essential_businesses_re_open_did_not_exist']=df['which_of_the_following_activities_will_you_feel_comfortable_with_now_or_immediately_after_non_essential_businesses_re_open'].str.contains('did not exist', regex=False, na=False).astype(int)


# In[48]:


df['activities_will_you_feel_comfortable_with_now_or_immediately_after_non_essential_businesses_re_open_Visiting_a_friends_home_fewer_than_10']=df['which_of_the_following_activities_will_you_feel_comfortable_with_now_or_immediately_after_non_essential_businesses_re_open'].str.contains('Visiting a friend’s home for a small social gathering (fewer than 10 people)', regex=False, na=False).astype(int)


# In[49]:


df['activities_will_you_feel_comfortable_with_now_or_immediately_after_non_essential_businesses_re_open_Shopping_at_non-essential_stores']=df['which_of_the_following_activities_will_you_feel_comfortable_with_now_or_immediately_after_non_essential_businesses_re_open'].str.contains('Shopping at non-essential stores', regex=False, na=False).astype(int)


# In[50]:


df['activities_will_you_feel_comfortable_with_now_or_immediately_after_non_essential_businesses_re_open_None_of_the_above']=df['which_of_the_following_activities_will_you_feel_comfortable_with_now_or_immediately_after_non_essential_businesses_re_open'].str.contains('None of the above', regex=False, na=False).astype(int)


# In[ ]:


#####next one 


# In[51]:


check_cols = [col for col in df.columns if 'now_or_immediately_after_non_essential_businesses_re_open' in col]
print(check_cols)


# In[52]:


df[check_cols][~df['which_of_the_following_activities_will_you_feel_comfortable_with_now_or_immediately_after_non_essential_businesses_re_open'].isnull()]


# In[ ]:




