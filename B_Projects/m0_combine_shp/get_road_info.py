#coding=utf-8

import folium

from jsonpath import jsonpath
from folium import plugins
import json
import pandas as pd
import os
import numpy as np
import geopandas
from shapely import geometry
from matplotlib import pyplot as plt

path = r"D:\萧山json"
path2 = r"D:\萧山json\road_lines"
path3 = r"D:\萧山json\all_road_lines"

file = r"new.json"
file2 = r"road_location2.xlsx"

##1. 获取萧山道路信息
with open (os.path.join(path,file),'r') as file:
    json_data = json.loads(file.readline())

##尝试去掉市心南路的那一行，但未成功，不去掉也不影响
# lines_to_write = [line for line in json_data if not line.startswith("市心南路")]
# with open(os.path.join(path,file), "w") as f:
#     f.write(''.join(lines_to_write))


location = jsonpath(json_data,"$..path")
road_num = jsonpath(json_data,"$..code")

##2. 把每一行的经度、纬度互换位置,并把每个坐标点元素转为tuple格式
for j in range(len(location)):
    m = location[j]
    for i in range(len(m)):
        n = m[i]
        n.reverse()
        n = tuple(n)
        m[i]=n

##3. 把road_number转为list格式
for x in range(len(road_num)):
    k = road_num[x]
    k=k.split()
    road_num[x]=k

# # #获取道路信息导出为df
# df = pd.DataFrame(json_data)
# outfile = r"road_location3.xlsx"
# df.to_excel(os.path.join(path,outfile))


##把每个路段生成shp文件

lines_all = geopandas.GeoSeries(geometry.LineString(location[0]), crs='EPSG:4326', index=road_num[0])
for y in range(1,len(location)):
    line_points = location[y]
    id = str(road_num[y])
    if len(line_points) <= 1:
        print('road %s is empty'%(id))
    else:
        line_s1 = geopandas.GeoSeries(geometry.LineString(location[y]), crs='EPSG:4326', index=road_num[y])
        outfile = id+".shp"
        if line_s1.empty:
            print('road %s is empty'%(id))
        else:
            ##分别导出所有线段
            # line_s1.to_file(os.path.join(path2,outfile), driver='ESRI Shapefile', encoding='utf-8')
            ##合并所有线段
            lines_all = lines_all.union(line_s1)

lines_all.to_file(os.path.join(path3,"all_road_lines.shp"), driver='ESRI Shapefile', encoding='utf-8')


