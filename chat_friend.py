#coding: utf-8

import selenium,os,sys
import time
from config import *

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
        self.driver.get(self.url)
        self.driver.find_element_by_xpath("//div[@class='extra']/p/span").click()
        self.driver.find_element_by_xpath("//div[@class='ant-form-item-control ']/input").send_keys(self.user)
        self.driver.find_element_by_xpath("//div[@class='ant-form-item-control ']/input").send_keys(self.passwd)
        self.driver.find_element_by_xpath("//div[@class='ant-form-item-control ']/input").send_keys(self.user)
        self.driver.find_element_by_xpath("//div[@class='ant-row']/button").click()
        time.sleep(3)

    def login(self):
        self.driver.get(self.url)
        self.driver.find_element_by_id("username").send_keys(self.user)
        self.driver.find_element_by_id("password").send_keys(self.passwd)
        self.driver.find_element_by_xpath("//div[@class='ant-row']/button").click()
        time.sleep(3)

    def logout(self):
        self.driver.find_element_by_xpath("//i[@class='anticon anticon-setting ant-dropdown-trigger']").click()
        self.driver.find_element_by_xpath("//i[@class='anticon anticon-logout']").click()


    def addfirend(self):
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@class='fr']/i").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//i[@class='anticon anticon-user-add']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@class='ant-col-20']/input").send_keys(self.friend)
        self.driver.find_element_by_xpath("//div[@class='ant-col-4']/button").click()

    def refusefriend(self):
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@class='ant-col-10']/button[2]").click()

    def agreefriend(self):
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@class='ant-col-10']/button").click()

    def sendMSfirend(self):
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@class='nav-text']/div").click()
        time.sleep(1)
        self.driver.find_element_by_class_name("ant-input").send_keys(message)
        self.driver.find_element_by_xpath("//span[@class='ant-input-group-addon']/i").click()

    def refresh(self):
        try:
            self.driver.refresh()
        except Exception as e:
            print ("Exception found", format(e))

    def receiveMess(self):
        try:
            if self.driver.find_element_by_xpath("//p[@class='current']"):
                print "OK,New message is exist"
                return True
        except selenium.common.exceptions.NoSuchElementException,e:
            print "No message received，verify failed",e
            return False

    def addtoblack(self):
        self.driver.find_element_by_xpath("//div[@class='nav-text']/div").click()
        self.driver.find_element_by_xpath("//div[@class='fr']/span/i").click()
        self.driver.find_element_by_xpath("//li[@class='ant-dropdown-menu-item']/i").click()
        return True

    def removeblack(self):
        self.driver.find_element_by_xpath("//div[@class='fl']/i").click()
        self.driver.find_element_by_xpath("//li[@class='ant-dropdown-menu-item']/span/i").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//i[@class='fr iconfont icon-circle-minus']").click()
        self.driver.find_element_by_xpath("//span[@class='ant-modal-close-x']").click()
        return True

    def delfriend(self):
        self.driver.find_element_by_xpath("//div[@class='nav-text']/div").click()
        self.driver.find_element_by_xpath("//div[@class='fr']/span/i").click()
        self.driver.find_element_by_xpath("//i[@class='iconfont icon-trash']").click()
        return True

    def cleanchat(self):
        self.driver.find_element_by_xpath("//i[@class='icon iconfont icon-trash']").click()
        return True

    def sendimage(self):
        upimage = self.driver.find_element_by_id("uploadImage")
        upimage.send_keys("%s/123.png" %os.getcwd())
        return True

    def sendfile(self):
        upfile = self.driver.find_element_by_id("uploadFile")
        upfile.send_keys("%s/123.png" % os.getcwd())
        return True

    def quitBrowser(self):
        self.driver.quit()






