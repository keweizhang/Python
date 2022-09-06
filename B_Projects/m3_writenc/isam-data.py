from netCDF4 import Dataset
import numpy as np
import sys

ifile  = sys.argv[1]
ofile  = sys.argv[2]

idata  = Dataset(ifile, mode='r')
odata  = Dataset(ofile, mode='a')

reg    = ['HZ','NJ','HF','SH','JS','AH','ZJ','OTH']
sec    = ['TRA']
pmcom  = ['AECI','AECJ','APOCI','APOCJ','APNCOMI','APNCOMJ','ASO4I','ASO4J','ANO3I','ANO3J','ANH4I','ANH4J']
ibo    = ['ICON','BCON','OTHR']

for i in sec:
    for j in reg:
        odata.variables['PMIJ_'+i+'_'+j][:,:,:,:] = 0.0

for i in sec:
    for j in reg:
        for k in pmcom:
             name = k+'_'+i+'_'+j
             print(name)
             odata.variables['PMIJ_'+i+'_'+j][:,:,:,:] = odata.variables['PMIJ_'+i+'_'+j][:,:,:,:] + idata.variables[name][:,:,:,:]

for i in ibo:
    odata.variables['PMIJ_'+i][:,:,:,:] = 0.0

for i in ibo:
    for k in pmcom:
         name = k+'_'+i
         print(name)
         odata.variables['PMIJ_'+i][:,:,:,:] = odata.variables['PMIJ_'+i][:,:,:,:] + idata.variables[name][:,:,:,:]

odata.close()
idata.close()
