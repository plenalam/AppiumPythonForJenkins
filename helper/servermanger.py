import subprocess
import os
import signal
import time


class AppiumServer:
    def __init__(self):
        self.name = ''
        self.port = ''
        self.pid = ''
        self.device = ''


class AppiumServerManger:
    def __init__(self):
        self.appiumServerList = {}

    def startServer(self, name, port):
        cmd = "appium -p" + port
        print("command:"+cmd)
        appium_server = AppiumServerManger()
        appium_server.name = name
        appium_server.port = port

        output = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        appium_server.pid = output.pid
        print("pid:"+appium_server.pid)

        self.appiumServerList[name] = appium_server

    def closeServer(self, name):
        appium_server = self.appiumServerList[name]
        if not appium_server:
            return
        try:
            os.kill(appium_server.pid, signal.SIGTERM)
        except OSError as e:
            pass
        finally:
            del self.appiumServerList[name]


if __name__ == '__main__':
    appiumservermanger = AppiumServerManger()
    appiumservermanger.startServer(name="test",port=4333)
    time.sleep(15)
    appiumservermanger.closeServer(name="test")