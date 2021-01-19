from datetime import datetime
from random import randint

from TESTAPI.requests_api.requests_method import RunMethod
from TESTAPI.util.read_yaml import ReadConfig
from TESTAPI.util.logfun import LogGer
from TESTAPI.util.rely_dependent import RelyDependent
from TESTAPI.util.assert_case import AssertCase


class CaseSmokey:
    def __init__(self, case_file):
        """
        初始化方法
        """
        self.req = RunMethod()
        self.log = LogGer("./log/{0}.log".format(datetime.now().strftime('%Y-%m-%d')))
        self.AssertCase = AssertCase
        self.case_file = case_file

    def read_case_smokey(self, index):

        data = ReadConfig(self.case_file).read_config()
        # print(data, type(data))
        casename = data[index]["casename"]
        environment = data[index]["environment"]
        url = data[index]["url"]
        headers = data[index]["headers"]
        request_body = data[index]["request_body"]
        method = data[index]["method"]
        expect = data[index]["expect"]
        rely = data[index]["rely"]["yes_rely"]
        is_rely = data[index]["is_rely"]["isrely"]
        environment_data = ReadConfig("../config/environment1.yaml").read_config()
        if environment == "sit":
            url = url.replace("${url}", environment_data[environment])
        elif environment == "uat":
            url = url.replace("${url}", environment_data[environment])
        elif environment == "生产":
            url = url.replace("${url}", environment_data[environment])
        if is_rely is not None:
            requests_data = ReadConfig("../config/relydata.yaml").read_config()
            for i in requests_data:
                request_body[i] = requests_data.get(i)
            if headers is not None:
                res = self.req.run_main(url, method, data=request_body, header=headers)
                self.AssertCase().message_assert_case(expect, res.json())
            else:
                res = self.req.run_main(url, method, data=request_body)
                self.AssertCase().message_assert_case(expect, res.json())
            msg_data = f"请求开始：请求接口名称 {casename}\n{res.request}\n{res.headers}\n请求url {url}\n请求入参{request_body}\n响应code{res}\n响应结果{res.text}"
            self.log.log_fun(msg_data)
            if rely is not None:
                RelyDependent(res=res.json(), parameter=rely).rely_dependent()
        else:
            if headers is not None:
                res = self.req.run_main(url, method, data=request_body, header=headers)
                self.AssertCase().message_assert_case(expect, res.json())
            else:
                res = self.req.run_main(url, method, data=request_body)
                self.AssertCase().message_assert_case(expect, res.json())
            msg_data = f"请求开始：请求接口名称 {casename}\n{res.request}\n{res.headers}\n请求url {url}\n请求入参{request_body}\n响应code{res}\n响应结果{res.text}"
            self.log.log_fun(msg_data)
            if rely is not None:
                RelyDependent(res=res.json(), parameter=rely).rely_dependent()


