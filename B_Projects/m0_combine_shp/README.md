# 将json中的数据存为shp文件

> 原本的需求是将多个shp文件合并
> 但是考虑到这些数据本身就在一起，思路是将其存在一个shp文件中

## 文件列表

|文件夹|内容|来源|
|---|---|---|
|after_combine|先前的合并文件（无法正常画出图像）|解压自`合并后shp.zip`|
|test_combine|包括所有单一的shp文件|解压自`test_combine.zip`|
|all|处理后的shp文件||

|文件|内容|来源|
|---|---|---|
|`合并后shp.zip`||Ⓜ️|
|`test_combine.zip`||Ⓜ️|
|`new.json`|原始数据|Ⓜ️|
|`json_to_shp.py`|读取json数据，并存为可以被ArcGIS处理的单个shp文件||
|`combine_shp.ipynb`|处理过程的notebook||



