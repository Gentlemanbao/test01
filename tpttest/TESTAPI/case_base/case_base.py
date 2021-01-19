from datetime import datetime
from TESTAPI.requests_api.requests_method import RunMethod
from TESTAPI.util.read_yaml import ReadConfig
from TESTAPI.util.logfun import LogGer
from TESTAPI.util.rely_dependent import RelyDependent
from TESTAPI.util.assert_case import AssertCase
from random import randint


class CaseBase:
    def __init__(self):
        """
        初始化方法
        """
        self.req = RunMethod()
        self.log = LogGer("./log/{0}.log".format(datetime.now().strftime('%Y-%m-%d')))
        self.AssertCase = AssertCase

    def read_case_data(self, data):
        """
        读取用例并且请求接口
        :param data: 传入读取的测试用例参数
        :return:
        """
        casename = data["casename"]
        environment = data["environment"]
        url = data["url"]
        headers = data["headers"]
        request_body = data["request_body"]
        method = data["method"]
        expect = data["expect"]
        rely = data["rely"]["yes_rely"]
        is_rely = data["is_rely"]["isrely"]
        environment_data = ReadConfig("./config/tpt_environment.yaml").read_config()
        if environment == "sit":
            url = url.replace("${url}", environment_data[environment])
        elif environment == "uat":
            url = url.replace("${url}", environment_data[environment])
        elif environment == "生产":
            url = url.replace("${url}", environment_data[environment])
        else:
            url = url
        if is_rely is not None:
            requests_data = ReadConfig("./config/relydata.yaml").read_config()
            for i in requests_data:
                request_body[i] = requests_data.get(i)
            if headers is not None:
                res = self.req.run_main(url, method, data=request_body, header=headers)
                assert_data = self.AssertCase().message_assert_case(expect, res.json())
            else:
                res = self.req.run_main(url, method, data=request_body)
                assert_data = self.AssertCase().message_assert_case(expect, res.json())
            msg_data = f"请求开始：请求接口名称 {casename}\n{res.request}\n{res.headers}\n请求url {url}\n请求入参{request_body}\n响应code{res}\n响应结果{res.text}"
            self.log.log_fun(msg_data)
            if rely is not None:
                RelyDependent(res=res.json(), parameter=rely).rely_dependent()
        else:
            if headers is not None:
                res = self.req.run_main(url, method, data=request_body, header=headers)
                assert_data = self.AssertCase().message_assert_case(expect, res.json())
            else:
                res = self.req.run_main(url, method, data=request_body)
                assert_data = self.AssertCase().message_assert_case(expect, res.json())
            msg_data = f"请求开始：请求接口名称 {casename}\n{res.request}\n{res.headers}\n请求url {url}\n请求入参{request_body}\n响应code{res}\n响应结果{res.text}"
            self.log.log_fun(msg_data)
            if rely is not None:
                RelyDependent(res=res.json(), parameter=rely).rely_dependent()
        return assert_data


