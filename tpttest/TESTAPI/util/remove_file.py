import os


class RemoveFile:
    def __init__(self, filepath):
        """
        初始化方法
        :param filepath: 传需要删除文件的文件夹路径
        """
        self.filepath = filepath

    def remove_file(self):
        """
        删除文件夹所有的文件
        :return:
        """
        if os.path.exists(self.filepath):
            f_list = os.listdir(self.filepath)
            for i in f_list:
                os.remove(self.filepath+"/"+i)
