import requests as requests


class Client:
    def __init__(self, url):
        self.url = url

    @staticmethod
    def post_unauthorized(url, uri, json):
        url = url + uri
        response = requests.post(url, json=json, verify=False)
        return response

    @staticmethod
    def put_unauthorized(url, uri, data):
        url = url + uri
        response = requests.put(url, data=data, verify=False)
        return response

    @staticmethod
    def delete_unauthorized(url, uri):
        url = url + uri
        response = requests.delete(url, verify=False)
        return response

    @staticmethod
    def get_unauthorized(url, uri, params=None):
        url = url + uri
        response = requests.get(url, params, verify=False)
        return response


class FunctionClient:
    def __init__(self, url, status_code):
        self.url = url
        self.status_code = status_code

    @staticmethod
    def get_unauthorized(url, uri, params=None):
        url = url + uri
        response = requests.get(url, params, verify=False)
        return response
