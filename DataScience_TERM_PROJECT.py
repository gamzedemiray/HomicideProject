import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import re as re
import requests
from IPython.display import display

homicide = pd.read_csv("/Users/gamzedemiray/database.csv" ,dtype={'Perpetrator Age':str})
homicide.columns[16]
homicide['Perpetrator Age'].value_counts()
pd.set_option('display.max_columns', None)
homicide[homicide['Perpetrator Age']==0]
homicide['Perpetrator Age'].dtype
homicide['Perpetrator Age'].describe
homicide[homicide['Perpetrator Age'].isnull()]
homicide[homicide['Perpetrator Age']==' ']
# after running the above without the dtype specifier there was an error.
# The problem is that record with 'Record ID' = 634667 has a single blank space for "Perpetrator Age" and that one entry
# messes up the read_csv algorithm which tries to guess the type of data in each column.  It assumes everything is integer
# but then doesn't need to know what to do with the " " entry.  This is an unfortunate limitation!  Is there a way around it?
# What I've done is forced the column to be interpreted as a string, then convert it to a int below, after substituting the
# space with an empty string
homicide['Perpetrator Age'] = pd.to_numeric(homicide['Perpetrator Age'].str.replace(' ','0'))
homicide['Perpetrator Age'].mean()
homicide.isnull().values.any()


# Github test   , dummy line