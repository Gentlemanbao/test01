import os
from datetime import datetime


class ClearLogfile:
    def __init__(self, logfile):
        """
        初始化方法
        :param logfile: 传需要删除的文件的目录路径
        """
        self.logfile = logfile

    def clear_logfile(self):
        """
        删除文件夹下生成日期超过7天的log文件
        :return:
        """
        f_list = os.listdir(self.logfile)
        for filename in f_list:
            if os.path.splitext(filename)[1] == ".log":
                file_crate_time = filename.split(sep=".")[0]
                now_time = datetime.now().strftime('%Y-%m-%d')
                d1 = file_crate_time.split(sep="-")
                d2 = now_time.split(sep="-")
                d1_time = datetime(int(d1[0]), int(d1[1]), int(d1[2]))
                d2_time = datetime(int(d2[0]), int(d2[1]), int(d2[2]))
                count_time = (d2_time - d1_time).days
                if count_time >= 7:
                    os.remove(self.logfile+"/"+filename)







