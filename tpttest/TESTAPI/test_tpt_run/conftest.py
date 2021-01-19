import pytest
from TESTAPI.case_base.case_base import CaseBase


@pytest.fixture(scope="class")
def my_fixture_three(my_fixture_log):
    print("-----------------测试用例开始执行----------------------")
    case = CaseBase()
    yield case
    print("-----------------测试用例执行结束----------------------")
