#coding: utf-8

import selenium,os,sys
import time
from config import *
from selenium.common.exceptions import NoSuchElementException
from chat_friend import AloneChat
sys.path.append(os.getcwd())

class ChatGroup(AloneChat):
    def __init__(self,driver,user,passwd,url,friend,groupname):
        super(ChatGroup,self).__init__(driver,user,passwd,url,friend)
        self.groupname = groupname

    def publicgroup(self):
        funname = sys._getframe().f_code.co_name
        try:
            time.sleep(1)
            self.driver.find_element_by_xpath("//div[@class='fr']/i").click()
            self.driver.find_element_by_xpath("//i[@class='anticon anticon-usergroup-add']").click()
            groupnm = self.driver.find_element_by_xpath("//input[@id='name']")
            groupnm.send_keys(self.groupname)
            desc = self.driver.find_element_by_xpath("//textarea[@class='ant-input']")
            desc.send_keys(self.groupname)
            time.sleep(1)
            self.driver.find_element_by_xpath("//button[@class='ant-btn fr ant-btn-primary']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//button[@type='submit']").click()
            time.sleep(3)
            self.driver.find_element_by_xpath("//li[@class='ant-menu-item']/span").click()
            time.sleep(1)
            group = self.driver.find_element_by_xpath("//div[@class='nav-text']/div").text
            if str(group) == self.groupname:
                print "great public group successed,no verify"
                return True
            else:
                print "greage public group failed"
                return False
        except NoSuchElementException, error:
            print u"%s Failed" % funname, error
            self.screenshot("%s.png" % funname)
            return False

    def invitemember(self,member):
        funname = sys._getframe().f_code.co_name
        try:
            time.sleep(1)
            self.driver.find_element_by_xpath("//li[@class='ant-menu-item']/span").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//ul[@class='ant-menu ant-menu-inline ant-menu-light ant-menu-root']/li").click()
            self.driver.find_element_by_xpath("//div[@class='fr']/span/i").click()
            self.driver.find_element_by_xpath("//span[@class='fr']/i").click()
            self.driver.find_element_by_xpath("//li[@class='ant-dropdown-menu-item']/span").click()
            self.driver.find_element_by_xpath("//div[@class='ant-col-20']/input").send_keys(member)
            time.sleep(2)
            self.driver.find_element_by_xpath("//button[@class='ant-btn fr ant-btn-primary']").click()
            print "invit group member success"
            return True
        except NoSuchElementException, error:
            print u"%s Failed" % funname, error
            self.screenshot("%s.png" % funname)
            return False

    def verifyjoin(self):
        #this function return two value
        funname = sys._getframe().f_code.co_name
        try:
            time.sleep(1)
            self.driver.find_element_by_xpath("//li[@class='ant-menu-item']/span").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//ul[@class='ant-menu ant-menu-inline ant-menu-light ant-menu-root']/li").click()
            groupnum = self.driver.find_element_by_xpath("//div[@class='x-list-item x-chat-header']/div").text
            if groupnum:
                print "invited join group success,group num is: ", str(groupnum)
                return True,str(groupnum)
            else:
                print "invited join group failed ! "
                return False,None
        except NoSuchElementException, error:
            print u"%s Failed" % funname, error
            self.screenshot("%s.png" % funname)
            return False,None

    def applyjoin(self,groupnum):
        funname = sys._getframe().f_code.co_name
        try:
            self.driver.find_element_by_xpath("//div[@class='fr']/i").click()
            self.driver.find_element_by_xpath(
                "//ul[@class='ant-dropdown-menu ant-dropdown-menu-vertical x-header-ops__dropmenu ant-dropdown-menu-light ant-dropdown-menu-root']/li[2]/span/i").click()
            self.driver.find_element_by_xpath("//div[@class='ant-col-18']/input").send_keys(groupnum)
            self.driver.find_element_by_xpath("//div[@class='ant-col-6']/button").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//div[@class='x-dialog']/div[3]/button").click()
            self.driver.find_element_by_xpath("//div[@class='ant-modal-content']/button").click()
            value,gn = self.verifyjoin()
            if gn == groupnum:
                print "apply join group success"
                return True
            else:
                print "apply join group failed"
                return False
        except NoSuchElementException, error:
            print u"%s Failed" % funname, error
            self.screenshot("%s.png" % funname)
            return False