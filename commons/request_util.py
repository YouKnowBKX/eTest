import requests


class RequestUtil:

    session = requests.session()

    # 统一发送请求
    def all_send_request(self,**kwargs):
        response = RequestUtil.session.request(**kwargs)
        # print(kwargs["method"])
        return response