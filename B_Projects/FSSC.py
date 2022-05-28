class FSSC_data():
    '''读取原始数据'''
    def __init__(self, rawdata):
        self.rawdata = pd.DataFrame()

    def load_data():
        # 用'FNC'开头识别数据文件，自动获取数据文件名
        pass
        # filelist = [files for files in os.listdir() if files[0:3] == 'FNC']
        # # 导入，对于属于同一组实验的几个数据文件也进行合并
        # rawdata = pd.DataFrame()
        # for filename in filelist:
        #     tempdata = pd.read_csv(filename)
        #     rawdata = rawdata.append(tempdata)
class FSSC():
    '''
    用于处理快速扫描过饱和度计数器的数据
    '''

    def __init__(self):
        self.data = FSSC_data()