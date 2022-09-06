import pandas as pd
import geopandas
from shapely import geometry
import json

# 原本的需求是将多个shp文件合并
# 但是考虑到这些数据本身就在一起，思路是将其存在一个shp文件中

# 读取json文件，并将其转化为dataframe操作
filename = './new.json'
with open (filename) as file_obj:
    json_data = json.loads(file_obj.readline())
raw_data = pd.DataFrame(json_data)

# 清洗数据，去除道路编号不存在和数据点不够两对的数据
data = raw_data.loc[(raw_data.code.str.len() > 4) & (raw_data.path.str.len() > 1)]

# 原始数据的经度和纬度需要调换位置
locations = [[single_loc[::-1] for single_loc in loc] for loc in data.path]
# 提取道路编号信息
road_num = list(data.code)

# 将经纬度数据转化为可以识别的地理信息数据
# 注意LineString需要至少两对经纬度数据，需要提前清洗数据
# 多个线段的数据直接用list存在一起即可合并为一个数据
shp_data = geopandas.GeoSeries([geometry.LineString(location) for location in locations], crs='EPSG:4326', index = road_num)

# 将数据写入本地shp文件
outfile = './all/all.shp'
shp_data.to_file(outfile, driver='ESRI Shapefile', encoding='utf-8')

# 读取并绘图
# data = geopandas.read_file('./all/all.shp')
# data.plot(aspect = 1)