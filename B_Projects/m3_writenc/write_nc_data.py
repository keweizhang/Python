import netCDF4 as nc
from netCDF4 import Dataset
import os
import pandas as pd
import xarray as xr

##Xue Chen 2022.08
##根据萧山本地的排放，修改MECI排放文件中指定网格的数值

path = r"D:\hz_4n_36_1km_case\MEIC_emis\meic_local\d04_raw"
path2 = r"D:\萧山json\萧山核心区属性表"

path3 = r"D:\hz_4n_36_1km_case\MEIC_emis\meic_local\test3"

file1 = r"tra_9"
file2 = r"tra_10"

file3 = r"all_gird_emis_Sep.xlsx"
file4 = r"all_gird_emis_Oct.xlsx"

factor_sep = 0.0458
factor_oct = 0.0311

emis_nc = xr.open_dataset(os.path.join(path,file2))
emis_grid = pd.read_excel(os.path.join(path2,file3),sheet_name="nc_data")

##不同物种的修改方式
##1. 萧山有的物种，在指定网格赋值修改
list1 = ["VOC","CO","NOx","SO2","PM2_5","PMcoarse"]

##2. CB05物种 萧山没有，根据VOC排放量和MEIC总量的比例，在指定网格乘以修正系数  sep 0.0458; oct 0.0311
list2 = ["CB05_ALD2","CB05_ALDX","CB05_ETHA","CB05_ETH","CB05_ETOH","CB05_FORM","CB05_IOLE","CB05_ISOP",
         "CB05_MEOH","CB05_NVOL","CB05_OLE","CB05_PAR",	"CB05_TERP","CB05_TOL",	"CB05_UNR",	"CB05_XYL"]

##3. 萧山没有的物种不做修改
# list3 = ["CO2","NH3","BC","OC"]

row_list = emis_grid["ROW"].to_list()
col_list = emis_grid["COL"].to_list()

for poll in list1:
    poll_nc = emis_nc[poll]
    for i in range(len(emis_grid)):
        row = row_list[i]
        col = col_list[i]
        a = emis_grid[(emis_grid.ROW==row) &(emis_grid.COL==col)][poll]
        a = float(a)
        poll_nc[0,0,row,col]=a*0.000001

for var in list2:
    var_nc = emis_nc[var]
    for i in range(len(emis_grid)):
        row = row_list[i]
        col = col_list[i]
        var_nc[0,0,row,col]=var_nc[0,0,row,col]*factor_sep
        var_nc[0, 0, row, col]=var_nc[0,0,row,col]*factor_oct

emis_nc.to_netcdf(os.path.join(path3,"tra_9"))

# emis_nc.to_netcdf(os.path.join(path3,"tra_10"))





