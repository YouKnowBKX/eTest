import pytest

from commons.request_util import RequestUtil
from commons.yaml_util import Yamlutil


class TestApi:

    @pytest.mark.parametrize("args",Yamlutil("./testcases/test_api.yaml").read_yaml())
    def test_get_access_token(self,args):
        url = args["request"]["url"]
        params = args["request"]["params"]
        headers = args["request"]["headers"]
        response = RequestUtil().all_send_request(method="get",url=url,params=params,headers=headers)
        print(response.text)
        json_data = response.json()
    #     #断言验证
    #     # assert response.status_code == 200, f"HTTP状态码应为200，实际为{response.status_code}"
    #     # # json_data = response.json()
    #     # # assert "access_token" in json_data, "响应中缺少access_token字段"
    #     # # assert "expires_in" in json_data, "响应中缺少expires_in字段"
    #     # # expires_in = json_data.get("expires_in")
    #     # # assert expires_in == 7200, f"expires_in应为7200，实际为{expires_in}"
    #     #
        result = {"access_token":json_data.get("access_token")}
        print(result,type(result))
        Yamlutil("./extract.yaml").write_yaml(result)

    #跳过
    # @pytest.mark.skip(reason="yaml文件中第二天用例获取不到access_token")
    def test_creat_tag(self):

        url = "https://api.weixin.qq.com/cgi-bin/tags/create"
        params = {"access_token": Yamlutil("./extract.yaml").read_yaml()["access_token"]}
        json = {"tag":{"name": "重庆"}}
        headers = {
            "Content-Type": "application/json",
            "charset": "utf-8"
        }
        response = RequestUtil().all_send_request(method = "post",url=url,json=json,params=params,headers=headers)
        print(response.json())


    def test_get_tag(self):
        url = "https://api.weixin.qq.com/cgi-bin/tags/get"
        params = {"access_token":Yamlutil("./extract.yaml").read_yaml()["access_token"]}
        access_token = Yamlutil("./extract.yaml").read_yaml()["access_token"]
        print(f"Access token from file: {access_token}")  # 打印读取的值
        response = RequestUtil().all_send_request(method="get",url=url,params=params)
        print(response.text)
