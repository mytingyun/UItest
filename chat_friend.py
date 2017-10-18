#coding: utf-8

import selenium,os,sys
import time
from config import *
from selenium.common.exceptions import NoSuchElementException

#options = webdriver.ChromeOptions()
#options.add_argument('disable-infobars')
#browser = webdriver.Chrome(chrome_options=options)
sys.path.append(os.getcwd())
class AloneChat:
    def __init__(self,driver,user,passwd,url,friend):
        self.driver = driver
        self.user = user
        self.passwd = passwd
        self.url = url
        self.friend = friend
    def sign_in(self):
        try:
            self.driver.get(self.url)
            self.driver.find_element_by_xpath("//div[@class='extra']/p/span").click()
            self.driver.find_element_by_xpath("//div[@class='ant-form-item-control ']/input").send_keys(self.user)
            self.driver.find_element_by_xpath("//div[@class='ant-form-item-control ']/input").send_keys(self.passwd)
            self.driver.find_element_by_xpath("//div[@class='ant-form-item-control ']/input").send_keys(self.user)
            self.driver.find_element_by_xpath("//div[@class='ant-row']/button").click()
            time.sleep(1)
            return True
        except NoSuchElementException,error:
            print "Sign in Failed",error
            self.screenshot("sing_in.png")
            return False
    def login(self):
        try:
            self.driver.get(self.url)
            self.driver.find_element_by_id("username").send_keys(self.user)
            self.driver.find_element_by_id("password").send_keys(self.passwd)
            self.driver.find_element_by_xpath("//div[@class='ant-row']/button").click()
            time.sleep(2)
            return True
        except NoSuchElementException,error:
            print "login Failed",error
            self.screenshot("login.png")
            return False
    def logout(self):
        try:
            self.driver.find_element_by_xpath("//i[@class='anticon anticon-setting ant-dropdown-trigger']").click()
            self.driver.find_element_by_xpath("//i[@class='anticon anticon-logout']").click()
            return True
        except NoSuchElementException, error:
            print "logout Failed", error
            self.screenshot("logout.png")
            return False
    def addfirend(self):
        funname = sys._getframe().f_code.co_name
        try:
            time.sleep(2)
            self.driver.find_element_by_xpath("//div[@class='fr']/i").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//i[@class='anticon anticon-user-add']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//div[@class='ant-col-20']/input").send_keys(self.friend)
            self.driver.find_element_by_xpath("//div[@class='ant-col-4']/button").click()
            return True
        except NoSuchElementException, error:
            print "%s Failed" %funname, error
            self.screenshot("%s.png" %funname)
            return False
    def refusefriend(self):
        funname = sys._getframe().f_code.co_name
        try:
            time.sleep(2)
            self.driver.find_element_by_xpath("//div[@class='ant-col-10']/button[2]").click()
            return True
        except NoSuchElementException, error:
            print "%s Failed" % funname, error
            self.screenshot("%s.png" % funname)
            return False
    def agreefriend(self):
        funname = sys._getframe().f_code.co_name
        try:
            time.sleep(2)
            self.driver.find_element_by_xpath("//div[@class='ant-col-10']/button").click()
            return True
        except NoSuchElementException, error:
            print "%s Failed" % funname, error
            self.screenshot("%s.png" % funname)
            return False
    def sendMSfirend(self):
        funname = sys._getframe().f_code.co_name
        try:
            time.sleep(2)
            self.driver.find_element_by_xpath("//div[@class='nav-text']/div").click()
            time.sleep(1)
            self.driver.find_element_by_class_name("ant-input").send_keys(message)
            self.driver.find_element_by_xpath("//span[@class='ant-input-group-addon']/i").click()
            return True
        except NoSuchElementException, error:
            print "%s Failed" % funname, error
            self.screenshot("%s.png" % funname)
            return False
    def refresh(self):
        try:
            self.driver.refresh()
        except Exception as e:
            print ("Exception found", format(e))
    def receiveMess(self):
        try:
            if self.driver.find_element_by_xpath("//p[@class='current']"):
                data = self.driver.find_element_by_xpath("//p[@class='current']").text
                if int(data) < receive_message_num:
                    print "Failed, Receive message is not complete, expect num is: %s ,now num is: %s" % (receive_message_num,str(data))
                    self.screenshot("receive.png")
                    return False
                else:
                    print "Pass, New message is exist，num is: %s" % str(data)
                    return True
        except NoSuchElementException,e:
            print "No message received，verify failed",e
            return False

    def addtoblack(self):
        funname = sys._getframe().f_code.co_name
        try:
            self.driver.find_element_by_xpath("//div[@class='nav-text']/div").click()
            self.driver.find_element_by_xpath("//div[@class='fr']/span/i").click()
            self.driver.find_element_by_xpath("//li[@class='ant-dropdown-menu-item']/i").click()
            return True
        except NoSuchElementException, error:
            print "%s Failed" % funname, error
            self.screenshot("%s.png" % funname)
            return False
    def removeblack(self):
        funname = sys._getframe().f_code.co_name
        try:
            self.driver.find_element_by_xpath("//div[@class='fl']/i").click()
            self.driver.find_element_by_xpath("//li[@class='ant-dropdown-menu-item']/span/i").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//i[@class='fr iconfont icon-circle-minus']").click()
            self.driver.find_element_by_xpath("//span[@class='ant-modal-close-x']").click()
            return True
        except NoSuchElementException, error:
            print "%s Failed" % funname, error
            self.screenshot("%s.png" % funname)
            return False
    def delfriend(self):
        funname = sys._getframe().f_code.co_name
        try:
            self.driver.find_element_by_xpath("//div[@class='nav-text']/div").click()
            self.driver.find_element_by_xpath("//div[@class='fr']/span/i").click()
            self.driver.find_element_by_xpath("//i[@class='iconfont icon-trash']").click()
            return True
        except NoSuchElementException, error:
            print "%s Failed" % funname, error
            self.screenshot("%s.png" % funname)
            return False
    def cleanchat(self):
        funname = sys._getframe().f_code.co_name
        try:
            self.driver.find_element_by_xpath("//div[@class='nav-text']/div").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//i[@class='icon iconfont icon-trash']").click()
            return True
        except NoSuchElementException, error:
            print "%s Failed, clean button is not found" % funname, error
            self.screenshot("%s.png" % funname)
            return False
    def sendimage(self):
        funname = sys._getframe().f_code.co_name
        try:
            self.driver.find_element_by_xpath("//div[@class='nav-text']/div").click()
            time.sleep(1)
            upimage = self.driver.find_element_by_id("uploadImage")
            upimage.send_keys("%s/123.png" %os.getcwd())
            return True
        except NoSuchElementException, error:
            print "%s Failed, clean button is not found" % funname, error
            self.screenshot("%s.png" % funname)
            return False
    def sendfile(self):
        funname = sys._getframe().f_code.co_name
        try:
            self.driver.find_element_by_xpath("//div[@class='nav-text']/div").click()
            time.sleep(1)
            upfile = self.driver.find_element_by_id("uploadFile")
            upfile.send_keys("%s/123.png" % os.getcwd())
            return True
        except NoSuchElementException, error:
            print "%s Failed, clean button is not found" % funname, error
            self.screenshot("%s.png" % funname)
            return False
    def screenshot(self,file):
        self.driver.get_screenshot_as_file("%s/errorpng/%s" %(os.getcwd(),file))
    def quitBrowser(self):
        self.driver.quit()






