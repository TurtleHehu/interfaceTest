# -*- encoding:utf-8-*-

import configparser
from datetime import datetime
import os

# 获取当前路径、配置文件全路径
proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.ini")


class ConfigOperation():
    cf = configparser.ConfigParser()
    cf.read(configPath)

    # 定义获取config下的value
    def getConfigValue(self, name):
        value = self.cf.get("config", name)
        return value

    # 定义获取cmd下name的value
    def getCmdValue(self, name):
        value = self.cf.get("cmd", name)
        return value

    # 定义方法，修改config分组下面name的值value
    def setConfigValue(self, name, value):
        self.cf.set("config", name, value)
        fp = open(r'config.ini', 'w')
        self.cf.write(fp)

    # 定义方法，修改cmd分组下name的值value
    def setCmdValue(self, name, value):
        self.cf.set("cmd", name, value)
        fp = open(r'configPath', 'w')
        self.cf.write(fp)


if __name__ == '__main__':
    cf = ConfigOperation()
    print(cf.getConfigValue("appPackage"))
    cf.setConfigValue("appPackage", "asdasd")
    print(cf.getConfigValue("appPackage"))
    cf.setConfigValue("appPackage2", "asdasd")
    print(cf.getConfigValue("appPackage2"))
    print (str(datetime.now().strftime("%Y%m%d%H%M%S")))
