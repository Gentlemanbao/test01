from TESTAPI.util.read_yaml import ReadConfig


class RelyDependent:
    def __init__(self, res, parameter=None):
        """
        初始化init方法
        :param res: 响应结果
        :param parameter:  需要提取的请求参数
        """
        self.readconfig = ReadConfig("./config/relydata.yaml")
        self.res = res
        self.parameter = parameter

    def rely_dependent(self):
        """
        提取响应内容，并且存储到文件中
        :return:
        """
        if "," in self.parameter:
            parameters = self.parameter.split(sep=",")
            for item in parameters:
                pra = item.split(sep=".")  # 再次分割
                parameter_data = {pra[2]: self.res[pra[0]][pra[1]][pra[2]]}
                self.readconfig.write_config(parameter_data)
        else:
            if "0" in self.parameter:
                pra = self.parameter.split(sep=".")
                print(pra, type(pra))
                parameter_data = {pra[3]: self.res[pra[0]][pra[1]][int(pra[2])][pra[3]]}
            else:
                pra = self.parameter.split(sep=".")
                parameter_data = {pra[2]: self.res[pra[0]][pra[1]][pra[2]]}
            self.readconfig.write_config(parameter_data)
