from appium import webdriver

class Login_Selector:
    def __init__(self,driver):
        self.driver = driver
    @property
    def loginBtn(self):
        return self.driver.find_element_by_accessibility_id("loginbtn")
    def UNTextField(self):
        return self.driver.find_element_by_accessibility_id("UNTextField")
    def tableviewBtn(self):
        return self.driver.find_elements_by_ios_predicate("lable == 'tableview'") 
    def TableCells(self):
        return self.driver.find_elements_by_ios_predicate("type == 'XCUIElementTypeCell'")