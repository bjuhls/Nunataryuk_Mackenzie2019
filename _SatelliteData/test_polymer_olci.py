
# coding: utf-8

# In[ ]:

#!/usr/bin/env python

from polymer.level1_olci import Level1_OLCI
from polymer.main import run_atm_corr, Level1, Level2
from polymer.level2_hdf import Level2_HDF
from polymer.level1_ascii import Level1_ASCII
from polymer.level1_nasa import Level1_NASA
from pylab import plot


PathIn="/home/bjuhls/WindowsShare/_FU/_progs/Polymer/testdata/S3A_OL_1_EFR____20190621T185813_20190621T190113_20190623T013227_0179_046_113_1800_MAR_O_NT_002.SEN3"

run_atm_corr(Level1_OLCI(PathIn), Level2(filename='/home/bjuhls/WindowsShare/_FU/_progs/Polymer/testdata/output_polymer.hdf'), multiprocessing=-1)   # activate multiprocessing)

