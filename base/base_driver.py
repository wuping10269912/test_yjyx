import time
from appium import webdriver
import yaml
from log.logging_test import loging
import  logging
def init_driver():
    # desires_caps = {}
    # desires_caps['platformName'] = 'Android'
    # desires_caps['platformVersion'] = '5.1.1'
    # desires_caps['deviceName'] = '127.0.0.1:62001'
    # desires_caps['appPackage'] = 'edu.yjyx.student'
    # #desires_caps['appPackage'] = 'com.songqin.sqcs'
    # #desires_caps['appActivity'] = '.MainActivity'
    # desires_caps['appActivity'] = '.module.main.ui.AccessActivity'
    # desires_caps['unicodeKeyboard'] = True
    # desires_caps['resetKeyboard'] = True
    # # 驱动
    # time.sleep(3)
    # driver = webdriver.Remote('http://localhost:4723/wd/hub', desires_caps)
    # print(driver.current_activity)
    file=open("E:\python\oa\data\desired_caps.yaml",'r')
    data=yaml.load(file)
    loging()
    desired_caps={}
    desired_caps['platformName']=data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['app'] = data['app']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['automationName'] = data['automationName']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']
    driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)
    return driver

if __name__== "__main__":
    init_driver()

