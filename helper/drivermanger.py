from appium import webdriver
import threading
import json

class DriverManger:
    instance=None
    mutex=threading.Lock()
    @staticmethod
    def getDriver():
        if(DriverManger.instance==None):
            DriverManger.mutex.acquire()
            if(DriverManger.instance==None):
                with open('config/driver.json', 'r') as f:
                    data = json.load(f)
                    DriverManger.instance = webdriver.Remote("http://localhost:4723/wd/hub", data['realOpts'])
            DriverManger.mutex.release()
        return DriverManger.instance
    
    @staticmethod
    def quit():
        if(DriverManger.instance != None):
            DriverManger.instance.quit()
            DriverManger.instance = None