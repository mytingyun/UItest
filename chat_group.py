#coding: utf-8

import selenium,os,sys
import time
from config import *
from chat_friend import AloneChat
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
sys.path.append(os.getcwd())


class ChatGroup(AloneChat):
    def __init__(self,driver,user,passwd,url,friend,groupname):
        super(ChatGroup,self).__init__(driver,user,passwd,url,friend)
        self.groupname = groupname

    def publicgroup(self):
        funname = sys._getframe().f_code.co_name
        try:
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_xpath("//div[@class='fr']/i")).click()
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//i[@class='anticon anticon-usergroup-add']")).click()
            groupnm = self.driver.find_element_by_xpath("//input[@id='name']")
            groupnm.send_keys(self.groupname)
            desc = self.driver.find_element_by_xpath("//textarea[@class='ant-input']")
            desc.send_keys(self.groupname)
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//button[@class='ant-btn fr ant-btn-primary']")).click()
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_xpath("//button[@type='submit']")).click()
            time.sleep(0.5)
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_xpath(
                "//ul[@class='ant-menu ant-menu-horizontal x-header-tab__menu ant-menu-light ant-menu-root']/li[2]")).click()
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//div[@class='nav-text']/div"))
            group = self.driver.find_element_by_xpath("//div[@class='nav-text']/div").text
            if str(group) == self.groupname:
                print u"great public group successed,no verify"
                return True
            else:
                self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
                print u"greage public group failed"
                return False
        except Exception, error:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            print u"%s Failed" % funname, error
            return False

    def invitemember(self,member):
        funname = sys._getframe().f_code.co_name
        try:
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_xpath(
                "//ul[@class='ant-menu ant-menu-horizontal x-header-tab__menu ant-menu-light ant-menu-root']/li[2]")).click()
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//div[@class='nav-text']/div")).click()
            self.driver.find_element_by_xpath("//div[@class='fr']/span/i").click()
            self.driver.find_element_by_xpath("//span[@class='fr']/i").click()
            self.driver.find_element_by_xpath(
                "//ul[@class='ant-dropdown-menu ant-dropdown-menu-vertical ant-dropdown-menu-light ant-dropdown-menu-root']/li/span").click()
            self.driver.find_element_by_xpath("//div[@class='ant-col-20']/input").send_keys(member)
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//button[@class='ant-btn fr ant-btn-primary']")).click()
            time.sleep(0.5)
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//div[@class='ant-card-head']/div/i")).click()
            print u"invit group member success"
            return True
        except Exception, error:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            print u"%s Failed" % funname, error
            return False

    def verifyjoin(self):
        #this function return two value,
        funname = sys._getframe().f_code.co_name
        try:
            # precise catch chatfriend, chatgroup, chatroom list
            time.sleep(0.5)
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_xpath(
                "//ul[@class='ant-menu ant-menu-horizontal x-header-tab__menu ant-menu-light ant-menu-root']/li[2]")).click()
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//div[@class='nav-text']/div")).click()
            groupnum = self.driver.find_element_by_xpath("//div[@class='x-list-item x-chat-header']/div").text
            if groupnum:
                print u"invited join group success,group num is: ", str(groupnum)
                return True,str(groupnum)
            else:
                self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
                print u"invited join group failed ! "
                return False,None
        except Exception, error:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            print u"%s Failed" % funname, error
            return False,None

    def applyjoin(self,groupnum):
        funname = sys._getframe().f_code.co_name
        try:
            self.driver.find_element_by_xpath("//div[@class='fr']/i").click()
            self.driver.find_element_by_xpath(
                "//ul[@class='ant-dropdown-menu ant-dropdown-menu-vertical x-header-ops__dropmenu ant-dropdown-menu-light ant-dropdown-menu-root']/li[2]/span/i").click()
            self.driver.find_element_by_xpath("//div[@class='ant-col-18']/input").send_keys(groupnum)
            self.driver.find_element_by_xpath("//div[@class='ant-col-6']/button").click()
            time.sleep(0.3)
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//div[@class='x-dialog']/div[3]/button")).click()
            self.driver.find_element_by_xpath("//div[@class='ant-modal-content']/button").click()
            value,gn = self.verifyjoin()
            if gn == groupnum:
                print u"apply join group success"
                return True
            else:
                self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
                print u"apply join group failed"
                return False
        except NoSuchElementException, error:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            print u"%s Failed" % funname, error
            return False
    def sendgroupMess(self,groupmess_num):
        funname = sys._getframe().f_code.co_name
        try:
            self.driver.find_element_by_xpath(
                "//ul[@class='ant-menu ant-menu-horizontal x-header-tab__menu ant-menu-light ant-menu-root']/li[2]").click()
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//div[@class='nav-text']/div")).click()
            self.sendimage()
            self.sendfile()
            for num in range(groupmess_num-2):
                self.sendMSfirend()
            return True
        except Exception, error:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            print u"%s Failed" % funname, error
            return False
    def groupMessNum(self,groupmess_num):
        funname = sys._getframe().f_code.co_name
        try:
            time.sleep(1)
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_xpath(
                "//ul[@class='ant-menu ant-menu-horizontal x-header-tab__menu ant-menu-light ant-menu-root']/li[2]")).click()
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//div[@class='nav-text']/div")).click()
            try:
                WebDriverWait(self.driver, sleeptime).until(
                    lambda x: x.find_element_by_xpath("//div[@class='x-chat-content']/div[%d]" % groupmess_num))
                if self.driver.find_element_by_xpath("//div[@class='x-chat-content']/div[%d]" %groupmess_num):
                    print u"Verify chatgroup message OK, number is: ", groupmess_num
                    return True
            except Exception, error:
                self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
                print u"Verify chatgroup message failed, number is not %d" %groupmess_num, error
                return False
        except NoSuchElementException, error:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            print u"%s Failed" % funname, error
            return False

    def groupRcvImage(self):
        funname = sys._getframe().f_code.co_name
        try:
            time.sleep(1)
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_xpath(
                "//ul[@class='ant-menu ant-menu-horizontal x-header-tab__menu ant-menu-light ant-menu-root']/li[2]")).click()
            result = self.receiveimage()
            return result
        except NoSuchElementException,err:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            print "Group receive images message failed",err
            return False
    def groupRcvFile(self):
        funname = sys._getframe().f_code.co_name
        try:
            time.sleep(1)
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_xpath(
                "//ul[@class='ant-menu ant-menu-horizontal x-header-tab__menu ant-menu-light ant-menu-root']/li[2]")).click()
            result = self.receivefile()
            return result
        except NoSuchElementException,err:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            print "Group receive file message failed",err
            return False

    def operateMember(self,num):
        #num is: 1,to admin; 2, mute; 3,add to black list; 4,del member
        funname = sys._getframe().f_code.co_name
        try:
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_xpath(
                "//ul[@class='ant-menu ant-menu-horizontal x-header-tab__menu ant-menu-light ant-menu-root']/li[2]")).click()
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//div[@class='nav-text']/div")).click()
            self.driver.find_element_by_xpath("//ul[@class='ant-menu ant-menu-inline ant-menu-light ant-menu-root']/li").click()
            self.driver.find_element_by_xpath("//div[@class='fr']/span/i").click()
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//tr[@class='ant-table-row  ant-table-row-level-0']/td"))
            if self.driver.find_element_by_xpath("//tr[@class='ant-table-row  ant-table-row-level-0']/td"):
                nowuser = self.driver.find_element_by_xpath("//tr[@class='ant-table-row  ant-table-row-level-0']/td").text
                self.driver.find_element_by_xpath("//tr[@class='ant-table-row  ant-table-row-level-0']/td[2]/span/i[%d]" % num).click()
                WebDriverWait(self.driver, sleeptime).until(
                    lambda x: x.find_element_by_xpath("//div[@class='ant-popover-message-title']"))
                comments = self.driver.find_element_by_xpath("//div[@class='ant-popover-message-title']").text
                self.driver.find_element_by_xpath("//div[@class='ant-popover-buttons']/button[2]").click()
                self.driver.find_element_by_xpath("//div[@class='ant-card-extra']/i").click()
                print u"user %s is operate %s success" % (nowuser,comments)
            return True,str(nowuser)
        except NoSuchElementException, error:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            print u"%s Failed " % (funname), error
            return False,None
    def verifyDelete(self,nowuser):
        funname = sys._getframe().f_code.co_name
        try:
            self.driver.find_element_by_xpath("//li[@class='ant-menu-item']/span").click()
            try:
                WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_xpath("//div[@class='nav-text']/div"))
                print u"user %s deleted failed" % nowuser
                self.screenshot("%s.png" % funname)
                return False
            except Exception:
                print u"user %s deleted success" % nowuser
                return True
        except Exception, error:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            print u"%s Failed" % funname, error
            return False
    def verifyBlkList(self,nowuser):
        funname = sys._getframe().f_code.co_name
        try:
            self.driver.find_element_by_xpath("//div[@class='fr']/span/i").click()
            self.driver.find_element_by_xpath("//span[@class='fr']/i").click()
            self.driver.find_element_by_xpath("//i[@class='anticon anticon-frown']").click()
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//div[@class='ant-table-content']/div/table/tbody/tr/td"))
            blackuser = self.driver.find_element_by_xpath("//div[@class='ant-table-content']/div/table/tbody/tr/td").text
            if str(blackuser) == nowuser:
                print u"add %s to black list success" % nowuser
                return True
            else:
                self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
                print u"add %s to black list failed" % nowuser
                return False
        except Exception, error:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            print u"%s Failed" % funname, error
            return False

    def groupRemoveblack(self):
        funname = sys._getframe().f_code.co_name
        try:
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_xpath(
                "//ul[@class='ant-menu ant-menu-horizontal x-header-tab__menu ant-menu-light ant-menu-root']/li[2]")).click()
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//div[@class='nav-text']/div")).click()
            self.driver.find_element_by_xpath(
                "//ul[@class='ant-menu ant-menu-inline ant-menu-light ant-menu-root']/li").click()
            self.driver.find_element_by_xpath("//div[@class='fr']/span/i").click()
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_xpath("//span[@class='fr']/i")).click()

            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//i[@class='anticon anticon-frown']")).click()
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_xpath(
                "//div[@class='ant-table-content']/div/table/tbody/tr/td[2]/a")).click()
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//div[@class='ant-popover-inner-content']/div[2]/button[2]")).click()
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//div[@class='ant-modal-content']/button")).click()
            time.sleep(1)
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_xpath("//span[@class='fr']/i")).click()
            self.driver.find_element_by_xpath("//ul[@class='ant-dropdown-menu ant-dropdown-menu-vertical ant-dropdown-menu-light ant-dropdown-menu-root']/li[3]/span").click()
            WebDriverWait(self.driver, sleeptime).until_not(
                lambda x: x.find_element_by_xpath("//div[@class='ant-table-content']/div/table/tbody/tr/td"))
            try:
                if self.driver.find_element_by_xpath("//div[@class='ant-table-content']/div/table/tbody/tr/td").text:
                    print u"remove black list failed"
                    self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
                    return False
            except Exception:
                print u"remove black list success"
                return True
        except NoSuchElementException, error:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            print u"%s Failed" % funname, error
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
            # click chatgroup
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_xpath(
                "//ul[@class='ant-menu ant-menu-horizontal x-header-tab__menu ant-menu-light ant-menu-root']/li[2]")).click()
            # click group name
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//div[@class='nav-text']/div")).click()
            # click group infomation
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_xpath("//div[@class='fr']/span/i")).click()
            # click group setup
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//div[@class='ant-card-body']/h3/span/i")).click()
            # click modify group infomation
            self.driver.find_element_by_xpath(
                "//ul[@class='ant-dropdown-menu ant-dropdown-menu-vertical ant-dropdown-menu-light ant-dropdown-menu-root']/li[2]/span").click()
            # input new group infomation
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//div[@class='ant-form-item-control-wrapper']/div/input")).send_keys(
                "%snew" % groupname)
            # click modify button
            self.driver.find_element_by_xpath("//div[@class='ant-modal-footer']/button[2]").click()
            self.driver.refresh()
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_xpath(
                "//ul[@class='ant-menu ant-menu-inline ant-menu-light ant-menu-root']/li/div/div"))
            newgroup = self.driver.find_element_by_xpath(
                "//ul[@class='ant-menu ant-menu-inline ant-menu-light ant-menu-root']/li/div/div").text
            if str(newgroup) == "%snew" % groupname:
                print u"group name modify success, new group name is: %s" % newgroup
                return True
            else:
                self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
                print u"group name modify failed"
                return False
        except Exception, error:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            print u"%s Failed" % funname, error
            return False
    def cleangrpMessage(self,groupmess_num):
        funname = sys._getframe().f_code.co_name
        try:
            self.sendgroupMess(groupmess_num)
            self.groupMessNum(groupmess_num)
            self.driver.find_element_by_xpath("//i[@class='icon iconfont icon-trash']").click()
            try:
                if self.driver.find_element_by_xpath("//div[@class='x-chat-content']/div"):
                    self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
                    print "clean group message failed"
                    return False
            except Exception,error:
                print "clean group message success"
                return True
        except Exception, error:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            print u"%s Failed" % funname, error
            return False
    def dissolveGroup(self,groupnum):
        funname = sys._getframe().f_code.co_name
        try:
            # click chatgroup
            time.sleep(0.5)
            self.driver.find_element_by_xpath(
                "//ul[@class='ant-menu ant-menu-horizontal x-header-tab__menu ant-menu-light ant-menu-root']/li[2]").click()
            # click group name
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//div[@class='nav-text']/div")).click()
            # click group infomation
            self.driver.find_element_by_xpath("//div[@class='fr']/span/i").click()
            # click group setup
            self.driver.find_element_by_xpath("//div[@class='ant-card-body']/h3/span/i").click()
            # click dissolve group
            time.sleep(0.5)
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_xpath(
                "//ul[@class='ant-dropdown-menu ant-dropdown-menu-vertical ant-dropdown-menu-light ant-dropdown-menu-root']/li[4]/span/i")).click()
            time.sleep(0.5)
            admin = getGroupAdmin(groupnum)
            if "error" in admin:
                print "dissolve group %s success, %s" %(groupnum, admin["error_description"])
                return True
            else:
                print "dissolve group %s failed" % groupnum
                return False
        except Exception, error:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            print u"%s Failed" % funname, error
            return False
    def publicgroupYES(self):
        funname = sys._getframe().f_code.co_name
        try:
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_xpath("//div[@class='fr']/i")).click()
            time.sleep(0.5)
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//i[@class='anticon anticon-usergroup-add']")).click()
            groupnm = self.driver.find_element_by_xpath("//input[@id='name']")
            groupnm.send_keys(self.groupname)
            desc = self.driver.find_element_by_xpath("//textarea[@class='ant-input']")
            desc.send_keys(self.groupname)
            self.driver.find_element_by_xpath("//form[@class='ant-form ant-form-horizontal x-add-group']/div/div[4]/div/div/div/label/span").click()
            self.driver.find_element_by_xpath("//button[@class='ant-btn fr ant-btn-primary']").click()
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_xpath("//button[@type='submit']")).click()
            time.sleep(0.5)
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_xpath(
                "//ul[@class='ant-menu ant-menu-horizontal x-header-tab__menu ant-menu-light ant-menu-root']/li[2]")).click()
            # click group name
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//div[@class='nav-text']/div")).click()
            group = self.driver.find_element_by_xpath("//div[@class='nav-text']/div").text
            groupnum = self.driver.find_element_by_xpath("//div[@class='x-list-item x-chat-header']/div").text
            if str(group) == self.groupname:
                print u"great public group need agree successed,no verify,group id is: %s" % groupnum
                return True,groupnum
            else:
                self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
                print u"greage public group need agree failed"
                return False,None
        except Exception, error:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            print u"%s Failed" % funname, error
            return False,None
    def applyPubGrp(self,groupnum):
        funname = sys._getframe().f_code.co_name
        try:
            self.driver.find_element_by_xpath("//div[@class='fr']/i").click()
            self.driver.find_element_by_xpath(
                "//ul[@class='ant-dropdown-menu ant-dropdown-menu-vertical x-header-ops__dropmenu ant-dropdown-menu-light ant-dropdown-menu-root']/li[2]/span/i").click()
            self.driver.find_element_by_xpath("//div[@class='ant-col-18']/input").send_keys(groupnum)
            self.driver.find_element_by_xpath("//div[@class='ant-col-6']/button").click()
            time.sleep(0.5)
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//div[@class='x-dialog']/div[3]/button")).click()
            self.driver.find_element_by_xpath("//div[@class='ant-modal-content']/button").click()
        except Exception, error:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            print u"%s Failed" % funname, error
            return False

    def refusejoinGrp(self):
        funname = sys._getframe().f_code.co_name
        try:
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//div[@class='ant-col-10']/button[2]")).click()
            print "refuse join group success"
            return True
        except Exception, error:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            print u"%s Failed" % funname, error
            return False
    def agreejoinGrp(self):
        funname = sys._getframe().f_code.co_name
        try:
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//div[@class='ant-row']/div[2]/button")).click()
            print "agree join group success"
            return True
        except Exception, error:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            print u"%s Failed" % funname, error
            return False

    def privaGrpAllow(self):
        funname = sys._getframe().f_code.co_name
        try:
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_xpath("//div[@class='fr']/i")).click()
            #self.driver.find_element_by_xpath("//i[@class='anticon anticon-usergroup-add']").click()
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//i[@class='anticon anticon-usergroup-add']")).click()
            groupnm = self.driver.find_element_by_xpath("//input[@id='name']")
            groupnm.send_keys(self.groupname)
            desc = self.driver.find_element_by_xpath("//textarea[@class='ant-input']")
            desc.send_keys(self.groupname)
            self.driver.find_element_by_xpath(
                "//form[@class='ant-form ant-form-horizontal x-add-group']/div/div[3]/div/div/div/label/span").click()
            self.driver.find_element_by_xpath("//button[@class='ant-btn fr ant-btn-primary']").click()
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_xpath("//button[@type='submit']")).click()
            time.sleep(0.5)
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_xpath(
                "//ul[@class='ant-menu ant-menu-horizontal x-header-tab__menu ant-menu-light ant-menu-root']/li[2]")).click()
            # click group name
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//div[@class='nav-text']/div")).click()
            group = self.driver.find_element_by_xpath("//div[@class='nav-text']/div").text
            groupnum = self.driver.find_element_by_xpath("//div[@class='x-list-item x-chat-header']/div").text
            if str(group) == self.groupname:
                print u"great private group allow invite successed"
                return True, groupnum
            else:
                self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
                print u"greage private group allow invite failed"
                return False, None
        except Exception, error:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            print u"%s Failed" % funname, error
            return False, None

    def privaGrpNoAllow(self):
        funname = sys._getframe().f_code.co_name
        try:
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_xpath("//div[@class='fr']/i")).click()
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_xpath("//i[@class='anticon anticon-usergroup-add']")).click()
            groupnm = self.driver.find_element_by_xpath("//input[@id='name']")
            groupnm.send_keys(self.groupname)
            desc = self.driver.find_element_by_xpath("//textarea[@class='ant-input']")
            desc.send_keys(self.groupname)
            self.driver.find_element_by_xpath(
                "//form[@class='ant-form ant-form-horizontal x-add-group']/div/div[3]/div/div/div/label/span").click()
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_xpath("//input[@type='checkbox']")).click()
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//button[@class='ant-btn fr ant-btn-primary']")).click()
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_xpath("//button[@type='submit']")).click()
            time.sleep(0.5)
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_xpath(
                "//ul[@class='ant-menu ant-menu-horizontal x-header-tab__menu ant-menu-light ant-menu-root']/li[2]")).click()
            # click group name
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//div[@class='nav-text']/div")).click()
            group = self.driver.find_element_by_xpath("//div[@class='nav-text']/div").text
            groupnum = self.driver.find_element_by_xpath("//div[@class='x-list-item x-chat-header']/div").text
            if str(group) == self.groupname:
                print u"great private group not allow invite successed"
                return True, groupnum
            else:
                self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
                print u"greage private group not allow invite failed"
                return False, None
        except Exception, error:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            print u"%s Failed" % funname, error
            return False, None