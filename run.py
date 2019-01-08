import unittest
import os
import threading

class RunTest:
    def __init__(self):
        self.moduleOrderList = ["test_login","test_home","test_setting"]
    #检查并发现全部测试用例
    def ALLTestSuite(self):
        case_path = os.path.join(os.getcwd(),"module")
        discover = unittest.defaultTestLoader.discover(case_path)
        return discover
    #按规定顺序执行,只执行iOS用例
    def iOSOrderTestSuite(self):
        testSuite = unittest.TestSuite()
        for moduleName in self.moduleOrderList:
            #按顺序到模块目录检索
            case_path = os.path.join(os.getcwd(),"module/"+moduleName)
            print(case_path)
            #加入Common的测试用例
            # discover = unittest.defaultTestLoader.discover(case_path,pattern="test_common*.py", top_level_dir=None)
            # testSuite.addTests(discover)
            #加入iOS独有的测试用例
            discover = unittest.defaultTestLoader.discover("module/"+moduleName,pattern="test_ios_*.py",top_level_dir=os.path.join(os.getcwd()))
            testSuite.addTests(discover)
        return testSuite
    def run(self,testType):
        #根据启动标识启动测试用例
        if testType == "iOS":
            unittest.TextTestRunner().run(self.iOSOrderTestSuite())
        else:
            unittest.TextTestRunner().run(self.ALLTestSuite())

if __name__ == '__main__':
    threadTest = RunTest()
    threadTest.run("iOS")
    