
# coding: utf-8

# In[1]:

import numpy as np
import matplotlib.pyplot as plt
import os
from datetime import datetime
import pandas as pd
from collections import OrderedDict
from scipy.optimize import curve_fit
from datetime import date
from itertools import cycle
from sklearn.metrics import r2_score, mean_squared_error
import scipy
from scipy import stats
import statsmodels.api as sm
import calendar
from matplotlib.ticker import MaxNLocator
from mpl_toolkits.axes_grid.inset_locator import (inset_axes, InsetPosition,
                                                  mark_inset)
import os, sys


# In[2]:

fp= r"/all_mounts/masp26/SMOS_artic/BennetProjects/Paper3/_data/CDOM/v20191016/readme/stationlist_metadata.csv"
deli=","
Header= np.genfromtxt(fp, delimiter= deli , dtype="str" )[0]
Data_row= np.genfromtxt(fp, delimiter= deli ,skip_header=1 )
Data_col= zip(*np.genfromtxt(fp, delimiter= deli ,skip_header=1 ))
Data_str_row = np.genfromtxt(fp, delimiter= deli ,skip_header=1, dtype="str" )
Data_str_col = zip(*np.genfromtxt(fp, delimiter= deli ,skip_header=1, dtype="str" )) 
Datetimes=[]
Datetimes_withoutTime=[]
for e in Data_str_col[14]:
    Datetimes.append(datetime.strptime(e, '%Y-%m-%d'))
    
Station_litsMeta=  pd.DataFrame(
    {'Date': Datetimes,
     'Station': Data_str_col[3],
     'Lat': Data_str_col[17],
     'Lon': Data_str_col[18],
     'Depth': Data_str_col[4],
     'Pathlen': Data_str_col[5]
    })

Station_litsMeta['Station'] = 'stn' + Station_litsMeta['Station'].astype(str)


# In[3]:

path_CDOM_files = "/all_mounts/masp26/SMOS_artic/BennetProjects/Paper3/_data/CDOM/v20191016/data/"


wvl_CDOM_atsushi = []
CDOM_atsushi = []
dates=[]
stations=[]
for i, e in enumerate(os.listdir(path_CDOM_files)[0:]):
    if e.endswith(".dat"):
        deli=" "
        Header= np.genfromtxt(path_CDOM_files +"//" + e, delimiter= deli , dtype="str" )[0]
        Data_row= np.genfromtxt(path_CDOM_files +"//" + e, delimiter= deli ,skip_header=1 )
        Data_col= zip(*np.genfromtxt(path_CDOM_files +"//" + e, delimiter= deli ,skip_header=1, dtype=float ))
        wvl=Data_col[0]
        wvl_CDOM_atsushi.append(wvl)
        cdom=Data_col[1]
        CDOM_atsushi.append(cdom)

        #print e[16:22]
        dates.append(datetime.strptime(e[7:15], '%Y%m%d'))
        #print e[22]
        if e[22]=="_":
            stations.append(e[16:22])
        else:
            stations.append(e[16:23])


# In[4]:

#dat1.join(dat2)

for i, e in enumerate(os.listdir(path_CDOM_files)[0:1]):
    if e.endswith(".dat"):
        
        if e[22]=="_":
            stations.append(e[16:22])
            station=e[16:22]
        else:
            stations.append(e[16:23])
            station=e[16:23]
        date=datetime.strptime(e[7:15], '%Y%m%d')
        cdom_panda=pd.read_csv(path_CDOM_files +"//" + e, delimiter=deli) 
        ren = cdom_panda.rename(columns={'acdom_measured+fitted[m^-1]': station, 'Wavelength[nm]': "Station"})  # old method  
        ren.set_index('Station', inplace=True)
        del ren['QF']#cdom_panda.rename({'acdom_measured+fitted[m^-1]':"ss"},inplace=True)  # new method
        result = ren.transpose() 
        result.insert(0, "Date", date, True) 
        result.insert(0, "Station", station, True) 
        #print station
        
for i, e in enumerate(os.listdir(path_CDOM_files)[1:]):
    if e.endswith(".dat"):
        
        if e[22]=="_":
            stations.append(e[16:22])
            station=e[16:22]
        else:
            stations.append(e[16:23])
            station=e[16:23]
        #print station
        date=datetime.strptime(e[7:15], '%Y%m%d')
        cdom_panda=pd.read_csv(path_CDOM_files +"//" + e, delimiter=deli) 
        ren = cdom_panda.rename(columns={'acdom_measured+fitted[m^-1]': station, 'Wavelength[nm]': "StationID"})  # old method  
        ren.set_index('StationID', inplace=True)
        del ren['QF']#cdom_panda.rename({'acdom_measured+fitted[m^-1]':"ss"},inplace=True)  # new method
        result1 = ren.transpose() 
        result1.insert(0, "Date", date, True) 
        result1.insert(0, "Station", station, True) 
        
        result=pd.concat([result, result1], ignore_index=False)
    #result.append(result1, ignore_index = True)
    


# In[5]:

result_join= pd.merge(Station_litsMeta, result, how="outer")


# In[6]:

result_join.drop_duplicates(subset =200, keep = "first", inplace = True) 


# In[7]:

result_join.to_csv("/all_mounts/masp26/SMOS_artic/BennetProjects/Paper3/_data/CDOM/MetaDataCDOMJoin.csv", sep='\t', encoding='utf-8')


# In[41]:

for index, row in Station_litsMeta.iterrows():
    print(row['Station'], row['Lat'], row['Date'])


# In[ ]:



