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
            time.sleep(4)
            self.driver.find_element_by_xpath("//li[@class='ant-menu-item']/span").click()
            time.sleep(1)
            group = self.driver.find_element_by_xpath("//div[@class='nav-text']/div").text
            if str(group) == self.groupname:
                print u"great public group successed,no verify"
                return True
            else:
                print u"greage public group failed"
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
            print u"invit group member success"
            return True
        except NoSuchElementException, error:
            print u"%s Failed" % funname, error
            self.screenshot("%s.png" % funname)
            return False

    def verifyjoin(self):
        #this function return two value,
        funname = sys._getframe().f_code.co_name
        try:
            time.sleep(2)
            #precise catch chatfriend, chatgroup, chatroom
            self.driver.find_element_by_xpath("//ul[@class='ant-menu ant-menu-horizontal x-header-tab__menu ant-menu-light ant-menu-root']/li[2]").click()
            time.sleep(3)
            self.driver.find_element_by_xpath("//div[@class='nav-text']/div").click()
            groupnum = self.driver.find_element_by_xpath("//div[@class='x-list-item x-chat-header']/div").text
            if groupnum:
                print u"invited join group success,group num is: ", str(groupnum)
                return True,str(groupnum)
            else:
                print u"invited join group failed ! "
                return False,None
        except Exception, error:
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
                print u"apply join group success"
                return True
            else:
                print u"apply join group failed"
                return False
        except NoSuchElementException, error:
            print u"%s Failed" % funname, error
            self.screenshot("%s.png" % funname)
            return False
    def sendgroupMess(self,groupmess_num):
        funname = sys._getframe().f_code.co_name
        try:
            self.driver.find_element_by_xpath("//li[@class='ant-menu-item']/span").click()
            time.sleep(1)
            self.sendimage()
            self.sendfile()
            for num in range(groupmess_num-2):
                self.sendMSfirend()
            return True
        except NoSuchElementException, error:
            print u"%s Failed" % funname, error
            self.screenshot("%s.png" % funname)
            return False
    def groupMessNum(self,groupmess_num):
        funname = sys._getframe().f_code.co_name
        try:
            time.sleep(2)
            self.driver.find_element_by_xpath(
                "//ul[@class='ant-menu ant-menu-horizontal x-header-tab__menu ant-menu-light ant-menu-root']/li[2]").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//div[@class='nav-text']/div").click()
            try:
                if self.driver.find_element_by_xpath("//div[@class='x-chat-content']/div[%d]" %groupmess_num):
                    print u"Verify chatgroup message OK, number is: ", groupmess_num
                    return True
            except NoSuchElementException, error:
                print u"Verify chatgroup message failed, number is not %d" %groupmess_num, error
                self.screenshot("%s.png" % funname)
                return False
        except NoSuchElementException, error:
            print u"%s Failed" % funname, error
            self.screenshot("%s.png" % funname)
            return False
    def operateMember(self,num):
        #num is: 1,to admin; 2, mute; 3,add to black list; 4,del member
        funname = sys._getframe().f_code.co_name
        try:
            self.driver.find_element_by_xpath("//li[@class='ant-menu-item']/span").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//div[@class='nav-text']/div").click()
            self.driver.find_element_by_xpath("//ul[@class='ant-menu ant-menu-inline ant-menu-light ant-menu-root']/li").click()
            self.driver.find_element_by_xpath("//div[@class='fr']/span/i").click()
            time.sleep(2)

            if self.driver.find_element_by_xpath("//tr[@class='ant-table-row  ant-table-row-level-0']/td"):
                global nowuser
                nowuser = self.driver.find_element_by_xpath("//tr[@class='ant-table-row  ant-table-row-level-0']/td").text
                self.driver.find_element_by_xpath("//tr[@class='ant-table-row  ant-table-row-level-0']/td[2]/span/i[%d]" % num).click()
                time.sleep(3)
                comments = self.driver.find_element_by_xpath("//div[@class='ant-popover-message-title']").text
                self.driver.find_element_by_xpath("//div[@class='ant-popover-buttons']/button[2]").click()
                self.driver.find_element_by_xpath("//div[@class='ant-card-extra']/i").click()
                print u"user %s is operate %s success" % (nowuser,comments)
            return True,str(nowuser)
        except NoSuchElementException, error:
            print u"%s Failed " % (funname), error
            self.screenshot("%s.png" % funname)
            return False,None
    def verifyDelete(self,nowuser):
        funname = sys._getframe().f_code.co_name
        try:
            self.driver.find_element_by_xpath("//li[@class='ant-menu-item']/span").click()
            time.sleep(2)
            try:
                self.driver.find_element_by_xpath("//div[@class='nav-text']/div")
                print u"user %s deleted failed" % nowuser
                self.screenshot("%s.png" % funname)
                return False
            except NoSuchElementException:
                print u"user %s deleted success" % nowuser
                return True
        except NoSuchElementException, error:
            print u"%s Failed" % funname, error
            self.screenshot("%s.png" % funname)
            return False
    def verifyBlkList(self,nowuser):
        funname = sys._getframe().f_code.co_name
        try:
            self.driver.find_element_by_xpath("//div[@class='fr']/span/i").click()
            self.driver.find_element_by_xpath("//span[@class='fr']/i").click()
            self.driver.find_element_by_xpath("//i[@class='anticon anticon-frown']").click()
            time.sleep(2)
            blackuser = self.driver.find_element_by_xpath("//div[@class='ant-table-content']/div/table/tbody/tr/td").text
            if str(blackuser) == nowuser:
                print u"add %s to black list success" % nowuser
                return True
            else:
                print u"add %s to black list failed" % nowuser
                return False
        except NoSuchElementException, error:
            print u"%s Failed" % funname, error
            self.screenshot("%s.png" % funname)
            return False

    def groupRemoveblack(self):
        funname = sys._getframe().f_code.co_name
        try:
            self.driver.find_element_by_xpath("//li[@class='ant-menu-item']/span").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//div[@class='nav-text']/div").click()
            self.driver.find_element_by_xpath(
                "//ul[@class='ant-menu ant-menu-inline ant-menu-light ant-menu-root']/li").click()
            self.driver.find_element_by_xpath("//div[@class='fr']/span/i").click()

            time.sleep(2)
            self.driver.find_element_by_xpath("//span[@class='fr']/i").click()
            self.driver.find_element_by_xpath("//i[@class='anticon anticon-frown']").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//div[@class='ant-table-content']/div/table/tbody/tr/td[2]/a").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//div[@class='ant-popover-inner-content']/div[2]/button[2]").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//div[@class='ant-modal-content']/button").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//span[@class='fr']/i").click()
            self.driver.find_element_by_xpath("//ul[@class='ant-dropdown-menu ant-dropdown-menu-vertical ant-dropdown-menu-light ant-dropdown-menu-root']/li[3]/span").click()
            time.sleep(2)
            try:
                if self.driver.find_element_by_xpath("//div[@class='ant-table-content']/div/table/tbody/tr/td").text:
                    print u"remove black list failed"
                    self.screenshot("%s.png" % funname)
                    return False
            except NoSuchElementException:
                print u"remove black list success"
                return True
        except NoSuchElementException, error:
            print u"%s Failed" % funname, error
            self.screenshot("%s.png" % funname)
            return False
    def groupadmin(self,groupnum,adminuser):
        admin = getGroupAdmin(groupnum)
        if admin["data"]:
            if admin["data"][0] == adminuser:
                print "add group admin %s sucess" % adminuser
                return True
            else:
                print "add group admin %s failed, now admin is: %s" %(adminuser, admin["data"][0])
                return False
        else:
            print "group admin is None"
            return False
    def modifyGrpName(self):
        funname = sys._getframe().f_code.co_name
        try:
            time.sleep(1)
            # click chatgroup
            self.driver.find_element_by_xpath(
                "//ul[@class='ant-menu ant-menu-horizontal x-header-tab__menu ant-menu-light ant-menu-root']/li[2]").click()
            time.sleep(3)
            # click group name
            self.driver.find_element_by_xpath("//div[@class='nav-text']/div").click()
            # click group infomation
            self.driver.find_element_by_xpath("//div[@class='fr']/span/i").click()
            # click group setup
            self.driver.find_element_by_xpath("//div[@class='ant-card-body']/h3/span/i").click()
            # click modify group infomation
            self.driver.find_element_by_xpath(
                "//ul[@class='ant-dropdown-menu ant-dropdown-menu-vertical ant-dropdown-menu-light ant-dropdown-menu-root']/li[2]/span").click()
            time.sleep(1)
            # input new group infomation
            self.driver.find_element_by_xpath("//div[@class='ant-form-item-control-wrapper']/div/input").send_keys(
                "%snew" % groupname)
            # click modify button
            self.driver.find_element_by_xpath("//div[@class='ant-modal-footer']/button[2]").click()
            self.driver.refresh()
            time.sleep(3)
            newgroup = self.driver.find_element_by_xpath(
                "//ul[@class='ant-menu ant-menu-inline ant-menu-light ant-menu-root']/li/div/div").text

            if str(newgroup) == "%snew" % groupname:
                print u"group name modify success"
                return True
            else:
                print u"group name modify failed"
                return False
        except NoSuchElementException, error:
            print u"%s Failed" % funname, error
            self.screenshot("%s.png" % funname)
            return False