import allure
from TESTAPI.util.read_yaml import ReadConfig
import pytest


@allure.feature("接口自动化测试类")
class TestCaseRun:

    @allure.story("保单服务页接口")
    @pytest.mark.parametrize("data", ReadConfig("./case/Policy_services_case.yaml").read_config())
    def test01(self, my_fixture_three, data):
        data = my_fixture_three.read_case_data(data)
        assert data is True


if __name__ == '__main__':
    pytest.main(["-vs", "test_tpt_run.py"])

