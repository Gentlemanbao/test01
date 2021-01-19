import json
import requests


class RunMethod:

    def post_main(self, url, data, header=None):
        if header is not None:
            res = requests.post(url=url, data=json.dumps(data), headers=header)
        else:
            res = requests.post(url=url, json=data)
        return res

    def get_main(self, url, data=None, header=None):
        if header is not None:
            res = requests.get(url=url, params=data, headers=header)
        else:
            res = requests.get(url=url, params=data)
        return res

    def delete_main(self, url, data=None, header=None):
        if header is not None:
            res = requests.delete(url=url, data=json.dumps(data), headers=header)
        else:
            res = requests.delete(url=url, data=json.dumps(data))
        return res

    def put_main(self, url, data=None, header=None):
        if header is not None:
            res = requests.put(url=url, data=json.dumps(data), headers=header)
        else:
            res = requests.put(url=url, data=json.dumps(data))
        return res

    def run_main(self, url, method, data=None, header=None):
        res = None
        if method == "post":
            res = self.post_main(url, data, header)
        elif method == "get":
            res = self.get_main(url, data, header)
        elif method == "delete":
            res = self.get_main(url, data, header)
        elif method == "put":
            res = self.get_main(url, data, header)
        return res

