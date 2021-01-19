import json

def binary_file(res):
    """
    请求内容二进制文件处理
    :param res: 响应二进制流
    :return:
    """
    with open("../config/policy.pdf", "wb") as f:
        f.write(res.content)


