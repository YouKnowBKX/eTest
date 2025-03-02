# fixture固件
import pytest

from commons.yaml_util import Yamlutil


# from commons.yaml_util import clear_yaml

#
# @pytest.fixture(scope="module",autouse=True)
# def sql():
#     print("打开数据库")
#     yield
#     print("关闭数据库")


#每次请求之前清空yaml文件
@pytest.fixture(scope="session",autouse=True)
def clears():
    Yamlutil("../extract.yaml").clear_yaml()