import HTMLTestRunnerCN
import unittest

# 继承unittest.TestCase
class MyTest(unittest.TestCase):
    def tearDown(self):
        print('执行用例之后')

    def setUp(self):
        print('执行用例之前')

    def test_run0(self):
        self.assertIs(1,1)

    def test_run2(self):
        self.assertIs(1,1)

    def test_run3(self):
        self.assertIs(1,1)

    def test_run1(self):
        self.assertIs(1,1)

    def test_run(self):
        test_suite = unittest.TestSuite()
        for i in range(4):
            test_name = 'test_run' + str(i)
            test_suite.addTest (MyTest(test_name))

        with open('Report.html', mode='wb') as fp:
            runner = HTMLTestRunnerCN.HTMLTestReportCN(stream=fp, title=u'api测试报告', description='测试情况')
            runner.run(test_suite)

if __name__ == "__main__":
    MyTest.test_run()