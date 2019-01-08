import unittest
from appium import webdriver
import time
import json
from loginSelector import Login_Selector
from drivermanger import DriverManger
# 利用unittest并生成测试
# 报告
class Appium_test(unittest.TestCase):
    def initDriver(self):
        with open('config/driver.json', 'r') as f:
            data = json.load(f)
        data['realOpts']
        # desired_caps = {
        #     "platformName": "iOS",
        #     "platformVersion": "9.4",
        #     "automationName": "xcuitest",
        #     "deviceName": "GXXmobile",
        #     "xcodeOrgId": "W7Q3L59QS3",
        #     "xcodeSigningId": "iPhone Developer",
        #     "udid": "dbaf9b9f351f0928cca949d3dea06b514e07b97d",
        #     "bundleId": "com.gosuncn.appiumdemo.AppiumDemo",
        #     "autoAcceptAlerts": True,
        #     "showIOSLog": True,
        #     "app": "/Users/yingjielee/Desktop/gitworkspace/webdriverioclient/AppiumDemo.ipa",
        # }
        print ("data['realOpts']: ", data['realOpts'])
        self.driver = webdriver.Remote(
            "http://192.168.36.42:4723/wd/hub", data['realOpts'])
        self.loginSelectors = Login_Selector(DriverManger.getDriver())
        
    @classmethod
    def setUpClass(self):
        self.initDriver(self)
        
    def setUp(self):
        print("start test")
    
    def tearDown(self):
        time.sleep(1)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
    
    def test_showsetting(self):
        self.assertEqual('正确跳转到主页', '正确跳转到主页')

    def test_login(self):
        #第一个测试用例
        #查找用户名输入框
        usernameTextField = self.loginSelectors.UNTextField()
        #输入用户名
        self.driver.set_value(usernameTextField, 'admin')
        #获取用户名文本框的值
        text = usernameTextField.get_attribute('value')
        #断言-判断用户文本框的值是否符合预期
        self.assertEqual('admin', text)
        #按下登录按钮
        self.loginSelectors.loginBtn().click()
        #查找登录提示框
        loginhub = self.driver.find_element_by_accessibility_id("loginhub")
        #断言-判断登录提示框的内容是否成功
        self.assertEqual('登录成功', loginhub.get_attribute('value'))