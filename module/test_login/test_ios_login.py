import unittest
# from loginSelector import Login_Selector
from helper.drivermanger import DriverManger

class Appium_test(unittest.TestCase):
    # @classmethod
    # def setUpClass(self):
    #     self.loginSelectors = Login_Selector(DriverManger.getDriver())

    def test_iOS(self):
        self.assertEqual('iOS', 'iOS')

    def test_errorpassword(self):
        self.assertEqual('密码错误', '密码错误')

    def test_nouser(self):
        self.assertEqual('账号不存在', '账号不存在')

    # def test_tableview(self):
    #     testCases = ["aaa","bbb","ccc","ddd"]
    #     cellList = self.loginSelectors.TableCells()
    #     for i in range(len(cellList)):
    #         cellList[i].click()