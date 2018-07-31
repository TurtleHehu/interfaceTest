import unittest
import paramunittest
from common import common
from common.Log import MyLog
import readConfig as readConfig
from common import configHttp as configHttp

productInfo_xls = common.get_xls("channelCn.xlsx", "getChannelCn")
localReadConfig = readConfig.ReadConfig()
localConfigHttp = configHttp.ConfigHttp()


@paramunittest.parametrized(*productInfo_xls)
class ProductInfo(unittest.TestCase):
    def setParameters(self, case_name, method, token, result, status, msg):
        """
        set params
        :param case_name:
        :param method:
        :param token:
        :param result:
        :param status:
        :param msg:
        :return:
        """
        self.case_name = str(case_name)
        self.method = str(method)
        self.token = str(token)
        self.result = str(result)
        self.status = int(status)
        self.msg = str(msg)
        self.response = None
        self.info = None

    def description(self):
        """

        :return:
        """
        self.case_name

    def setUp(self):
        """

        :return:
        """
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()

    def testGetChannelCn(self):
        """
        test body
        :return:
        """
        # set uel国内频道
        self.url = common.get_url_from_xml('channelCn')
        localConfigHttp.set_mini_url(self.url)
        # set params
        # if self.goodsId == '' or self.goodsId is None:
        #     params = None
        # elif self.goodsId == 'null':
        #     params = {"goods_id": ""}
        # else:
        #     params = {"goods_id": self.goodsId}
        # localConfigHttp.set_params(params)
        # set headers
        if self.token == '0':
            token = localReadConfig.get_headers("token_v")
        else:
            token = self.token
        headers = {"token": str(token)}
        localConfigHttp.set_headers(headers)
        # get http
        self.response = localConfigHttp.get()
        # check result
        self.checkResult()

    def tearDown(self):
        """

        :return:
        """
        self.log.build_case_line(self.case_name, str(self.info['status']), self.info['msg'])

    def checkResult(self):
        self.info = self.response.json()
        common.show_return_msg(self.response)

        if self.result == '0':
            self.assertEqual(self.info['status'], self.status)
            self.assertEqual(self.info['msg'], self.msg)
        if self.result == '1':
            self.assertEqual(self.info['status'], self.status)
            self.assertEqual(self.info['msg'], self.msg)

