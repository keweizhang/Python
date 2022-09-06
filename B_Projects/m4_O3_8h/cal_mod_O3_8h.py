import pandas as pd
import numpy as np
import os,sys
import os,sys,glob



path = r"D:\hz_4n_36_1km_case\four-city-mod\evalutaion\d02-base-v3.0"

file = r"d02-base-v3.0_plot_obs_mod_O3.xlsx"

outpath = r"D:\hz_4n_36_1km_case\hangzhou_4N_obs\yrd-6city-obs"


df=pd.read_excel(os.path.join(path,file))

print(df.head())

city_list =  ["hangzhou","hefei","nanjing","shanghai","shaoxing","jiaxing"]
df_all=pd.DataFrame()
for city in city_list:
    temp_df = df[df.site==str(city)]
    for i in range(7,len(temp_df)):
        temp_df.loc[i,"O3_8h"]=temp_df.loc[(i-7):i,"base"].mean()
    df_all=pd.concat([df,df_all],axis=0)

df_all.to_excel(os.path.join(outpath,"test-O3_8h.xlsx"))



