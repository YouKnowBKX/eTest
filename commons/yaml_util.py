# import os
#
# import yaml
#
# #写入
# def write_yaml(data):
#     with open(os.getcwd()+"/extract.yaml","a",encoding="utf-8") as f:
#         yaml.dump(data,stream=f,allow_unicode=True)
#
# #读取
# def read_yaml(key):
#     with open(os.getcwd()+"/extract.yaml","r",encoding="utf-8") as f:
#         value = yaml.load(f,yaml.FullLoader)
#         return value[key]
#


import yaml

class Yamlutil:
    def __init__(self,yaml_file):
        self.file = yaml_file

    #读取
    def read_yaml(self):
        with open(self.file,"r",encoding="utf-8") as f:
            value = yaml.load(f,yaml.FullLoader)
            return value
    #写入
    def write_yaml(self,data):
        with open(self.file,"w",encoding="utf-8") as f:
            yaml.dump(data, stream=f, allow_unicode=True)
    #清空
    def clear_yaml(self):
        with open(self.file, "w", encoding="utf-8") as f:
            f.truncate()


if __name__ == '__main__':
    Yamlutil("../testcases/test_api.yaml").read_yaml()


