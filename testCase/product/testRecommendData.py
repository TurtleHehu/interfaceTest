import unittest
import paramunittest
from common import common
from common.Log import MyLog
import readConfig as readConfig
from common import configHttp as configHttp

recommendData_xls = common.get_xls("recommendData.xlsx", "getRecommendData")
localReadConfig = readConfig.ReadConfig()
localConfigHttp = configHttp.ConfigHttp()


@paramunittest.parametrized(*recommendData_xls)
class RecommendData(unittest.TestCase):
    def setParameters(self, case_name, method, token, mddId, type, result, errcode, msg, result_id):
        """
        set params
        :param case_name:
        :param method:
        :param token:
        :param mddId:
        :param type:
        :param result:
        :param errcode:
        :param msg:
        :param result_id:
        :return:
        """
        self.case_name = str(case_name)
        self.method = str(method)
        self.token = str(token)
        self.mddId = str(mddId)
        self.type =  str(type)
        self.result = str(result)
        self.errcode = int(errcode)
        self.msg = str(msg)
        self.result_id = int(result_id)
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

    def testGetRecommendData(self):
        """
        test body
        :return:
        """
        self.logger.info("test start")
        # set uel
        self.url = common.get_url_from_xml('recommendData')
        localConfigHttp.set_url(self.url)
        # set params
        if self.mddId == '' or self.mddId is None:
            params = None
        elif self.mddId == 'null' or self.type == 'null':
            params = {"mddId": "","type": ""}
        else:
            params = {"mddId": self.mddId, "type": self.type}

        localConfigHttp.set_params(params)
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
        self.log.build_case_line(self.case_name, str(self.info['errcode']), self.info['msg'])

    def checkResult(self):
        self.info = self.response.json()
        common.show_return_msg(self.response)

        if self.result == '0':
            self.assertEqual(self.info['errcode'], self.errcode)
            mddId = common.get_value_from_return_json(self.info, "gonglveList", "id")
            self.assertEqual(mddId, self.result_id)
        if self.result == '1':
            self.assertEqual(self.info['errcode'], self.info['errcode'])
            self.assertEqual(self.info['msg'], self.msg)