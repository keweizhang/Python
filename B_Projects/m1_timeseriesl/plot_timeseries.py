from fnmatch import translate
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import ceil
import os

def kw_plot(plotdata, site, pollutant):
    '''
    将处理后的数据进行绘图
    '''

    x_time = plotdata.time.reset_index(drop=True)
    y_model = plotdata.model.reset_index(drop=True)
    y_obs = plotdata.obs.reset_index(drop=True)

    plt.figure(figsize=(8,6), dpi=300)
    plt.plot(x_time, y_obs, color = 'k', marker = 'o', markersize = 2, linewidth = 1)
    plt.plot(x_time, y_model, color = 'r', marker = 'o', markersize = 2, linewidth = 1)

    x_tick = ['2021-09-17', '2021-09-23', '2021-09-29', '2021-10-05']
    # 根绝物种不同，分别设置y刻度
    unit = ' ($\mu g/m{^3}$)'
    if pollutant == 'CO':
        y_step = 0.5
        unit = ' ($mg/m{^3}$)'
    elif (pollutant == 'SO2') or (pollutant == 'NO2'):
        y_step = 20
    elif (pollutant == 'PM2.5') or (pollutant == 'PM10'):
        y_step = 50
    else:
        y_step = 100
    
    y_max = (ceil(max(y_model.append(y_obs)/y_step))+2)*y_step
    y_tick = np.arange(y_step, y_max, y_step)
    
    ax = plt.gca()
    # 设置坐标轴线宽
    ax.spines[:].set_linewidth(2)
    # 设置横纵坐标刻度位置，刻度标签大小
    ax.xaxis.set_ticks(x_tick)
    ax.set_xticklabels(x_tick, size = 14)
    ax.yaxis.set_ticks(y_tick)
    ax.set_yticklabels(y_tick, size = 14)
    
    # 需要指定一个有中文字体显示的字体，否则中文显示乱码
    font_lable = {'family': 'MicroSoft Yahei','weight': 'bold','size': 14}
    plt.ylabel(pollutant+unit, fontdict = font_lable)
    # 按照相对位置指定添加的文本坐标
    plt.text(0.45, 0.935, site, 
            fontdict = font_lable, 
            transform = ax.transAxes,
            horizontalalignment = 'center', 
            verticalalignment = 'center')
    # 添加图例，默认在右上角
    plt.legend(['观测值', '模拟值'], ncol = 2, prop = {'family': 'MicroSoft Yahei', 'size':12})
    
    # 保存图片
    savefolder = './case1/'     # 此处指定了文件夹
    save_name = 'case1-'+pollutant+'-'+site+'.png'
    plt.savefig(savefolder+save_name, dpi = 300, bbox_inches='tight')

# 读取待处理数据的文件列表
filefolder = './case1_plot_obs_mod/'
filenames = os.listdir(filefolder)

# 为了方便数据处理，读取的时候更变了表头
name = ['time', 'site', 'obs', 'model']

for filename in filenames:
    data = pd.read_excel(filefolder+filename, names = name)
    # 从文件名中提取污染物信息
    p_start = filename.find('_', -11)+1
    p_end = filename.find('.xlsx')
    pollutant = filename[p_start:p_end]

    # 提取站点信息, 剔除重复行
    sites = list(data.site.drop_duplicates())

    plotdata = {}
    for site in sites:
        # 分割不同站点数据并存为字典
        plotdata[site] = data.loc[data.site == site]
        # 对每个站点数据进行绘图
        kw_plot(plotdata[site], site, pollutant)

