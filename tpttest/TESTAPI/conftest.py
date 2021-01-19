import pytest
from TESTAPI.util.read_yaml import ReadConfig
from TESTAPI.util.clear_logfile import ClearLogfile
from TESTAPI.util.remove_file import RemoveFile


@pytest.fixture(scope="session")
def my_fixture_log():
    print("-----------------测试用例之前删除历史依赖数据和7天前的日志文件以及json报告----------------------")
    ReadConfig("./config/relydata.yaml").clear_relydata()
    ClearLogfile("./log/").clear_logfile()
    # RemoveFile("./temp").remove_file()
    yield
    print("-----------------测试用例执行结束----------------------")
