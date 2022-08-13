import pandas as pd
import numpy as np
import os

class FSSC_data():
    '''
    1. 读取原始csv数据为alldata
    2. 选取Flag为1，也就是有效数据，为rawdata
    3. 去掉离群值，得到得到标定结果数据calidata
    '''

    def __init__(self):
        self.alldata = 0
        self.rawdata = 0
        self.calidata = 0
        #pd.DataFrame()

    def load_data(self):
        '''读取原始保存的csv数据'''
        
        # 识别以'FNC'开头的csv数据文件，自动获取数据文件名
        filelist = [files for files in os.listdir() if files[0:3] == 'FNC']
        # 导入，对于属于同一组实验的几个数据文件也进行合并
        alldata = pd.DataFrame()
        for filename in filelist:
            tempdata = pd.read_csv(filename)
            alldata = alldata.append(tempdata)

        self.alldata = alldata
        self.rawdata = alldata.loc[alldata['Flag'] == 1]

    def clean_data(self):
        '''将有效数据进行清晰，并计算均值和标准偏差，保存标定结果'''

        # 获取标定的粒径
        Dd_list = self.rawdata.loc[:,'Dd']
        Dd_list = np.array(Dd_list.drop_duplicates())
        # 初始化结果
        N = np.size(Dd_list)
        caliresult = np.zeros((N,4))
        # 计算每个粒径对应数据的均值和标准偏差
        for i in range(N):
            # 提取一个粒径对应的数据
            Dd = Dd_list[i]
            tempdata = self.rawdata.loc[self.rawdata['Dd'] == Dd]
            # 剔除异常值（将与均值相差超过三倍标准差的元素定义为离群值）
            Fact = np.mean(tempdata['Fact'])
            Sigma = np.std(tempdata['Fact'])
            # 注意：切片判断时不能用and，需要用位运算符 &
            single_Dd_data = tempdata.loc[
                (tempdata['Fact'] > Fact-3*Sigma) & (tempdata['Fact'] < Fact+3*Sigma)]
            # 计算清洗后数据的统计结果
            Fact = np.mean(single_Dd_data['Fact'])
            Sigma = np.std(single_Dd_data['Fact'])
            Flow = np.mean(single_Dd_data['CapillaryFlow'])

            caliresult[i,:] = [Dd, Fact, Sigma, Flow]

        # 转化为df数据并保存csv文件    
        self.calidata = pd.DataFrame(caliresult, columns=['Dd','Fact','std','Flow'])
        self.calidata.to_csv('calidata.csv',index=False)    # index控制不写入行号



