import os

import requests
import readConfig as readConfig
from common.Log import MyLog as Log


localReadConfig = readConfig.ReadConfig()

class ConfigHttp:

    def __init__(self):
        global scheme, schemes, bbs_host, www_host, net_host, port, timeout
        scheme = localReadConfig.get_http("scheme")
        schemes = localReadConfig.get_http("schemes")
        bbs_host = localReadConfig.get_http("baseurl_bbs")
        www_host = localReadConfig.get_http("baseurl_www")
        net_host = localReadConfig.get_http ("baseurl_net")
        port = localReadConfig.get_http("port")
        timeout = localReadConfig.get_http("timeout")
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}
        self.state = 0

    def set_bbs_url(self, url):
        """
        set url
        :param: interface url
        :return:
        """
        self.url = schemes+'://'+bbs_host+url

    def set_bbs_www(self, url):
        """
        set url
        :param: interface url
        :return:
        """
        self.url = scheme+'://'+www_host+url

    def set_bbs_net(self, url):
        """
        set url
        :param: interface url
        :return:
        """
        self.url = scheme+'://'+net_host+url

    def set_headers(self, header):
        """
        set headers
        :param header:
        :return:
        """
        self.headers = header

    def set_params(self, param):
        """
        set params
        :param param:
        :return:
        """
        self.params = param

    def set_data(self, data):
        """
        set data
        :param data:
        :return:
        """
        self.data = data

    def set_files(self, filename):
        """
        set upload files
        :param filename:
        :return:
        """
        if filename != '':
            file_path = os.path.join(os.path.split(os.getcwd())[0], 'testfile', 'img' , filename)
            self.files = {'file': open(file_path, 'rb')}

        if filename == '' or filename is None:
            self.state = 1

    # defined http get method
    def get(self):
        """
        defined get method
        :return:
        """
        try:
            response = requests.get(self.url, headers=self.headers, params=self.params, timeout=float(timeout))
            # response.raise_for_status()
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None

    # defined http post method
    # include get params and post data
    # uninclude upload file
    def post(self):
        """
        defined post method
        :return:
        """
        try:
            response = requests.post(self.url, headers=self.headers, params=self.params, data=self.data, timeout=float(timeout))
            # response.raise_for_status()
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None

    # defined http post method
    # include upload file
    def postWithFile(self):
        """
        defined post method
        :return:
        """
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data, files=self.files, timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None

    # defined http post method
    # for json
    def postWithJson(self):
        """
        defined post method
        :return:
        """
        try:
            response = requests.post(self.url, headers=self.headers, json=self.data, timeout=float(timeout))
            return response
        except TimeoutError:
            self.logger.error("Time out!")
            return None

if __name__ == "__main__":
    print("ConfigHTTP")
