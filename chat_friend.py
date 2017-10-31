#coding: utf-8

import selenium,os,sys
import time
from config import *
from selenium.common.exceptions import NoSuchElementException

#options = webdriver.ChromeOptions()
#options.add_argument('disable-infobars')
#browser = webdriver.Chrome(chrome_options=options)
sys.path.append(os.getcwd())
class AloneChat(object):
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
            print u"此次注册的用户名是：%s, 密码是：%s, 昵称是：%s" %(self.user,self.passwd,self.user)
            time.sleep(1)
            return True
        except NoSuchElementException,error:
            print u"Sign in Failed",error
            self.screenshot("sing_in.png")
            return False
    def login(self):
        funname = sys._getframe().f_code.co_name
        try:
            self.driver.get(self.url)
            self.driver.find_element_by_id("username").send_keys(self.user)
            self.driver.find_element_by_id("password").send_keys(self.passwd)
            self.driver.find_element_by_xpath("//div[@class='ant-row']/button").click()
            #time.sleep(3)
            while True:
                try:
                    if self.driver.find_element_by_xpath("//div[@id='x-header-ops']/div[2]"):
                        break
                except NoSuchElementException:
                    print "waiting the network...."
                    time.sleep(0.5)
                    continue
            username = self.driver.find_element_by_xpath("//div[@id='x-header-ops']/div[2]").text
            if str(username) == self.user:
                print u"此次登陆的用户名为：", self.user
                return True
            else:
                print u"用户%s登陆失败" % self.user
                self.screenshot("%s.png" % funname)
                return False

        except NoSuchElementException,error:
            print u"%s Failed" % funname, error
            self.screenshot("%s.png" % funname)
            return False
    def logout(self):
        try:
            self.driver.find_element_by_xpath("//i[@class='anticon anticon-setting ant-dropdown-trigger']").click()
            self.driver.find_element_by_xpath("//i[@class='anticon anticon-logout']").click()
            return True
        except NoSuchElementException, error:
            print u"logout Failed", error
            self.screenshot("logout.png")
            return False
    def addfirend(self):
        funname = sys._getframe().f_code.co_name  #get self functioin name
        try:
            time.sleep(2)
            self.driver.find_element_by_xpath("//div[@class='fr']/i").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//i[@class='anticon anticon-user-add']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//div[@class='ant-col-20']/input").send_keys(self.friend)
            self.driver.find_element_by_xpath("//div[@class='ant-col-4']/button").click()
            print u"添加的好友是：", self.friend
            return True
        except NoSuchElementException, error:
            print u"%s Failed" %funname, error
            self.screenshot("%s.png" %funname)
            return False
    def refusefriend(self):
        funname = sys._getframe().f_code.co_name
        try:
            time.sleep(2)
            self.driver.find_element_by_xpath("//div[@class='ant-col-10']/button[2]").click()
            print u"拒绝来自%s的添加好友申请" % self.friend
            return True
        except NoSuchElementException, error:
            print u"%s Failed" % funname, error
            self.screenshot("%s.png" % funname)
            return False
    def agreefriend(self):
        funname = sys._getframe().f_code.co_name
        try:
            time.sleep(2)
            self.driver.find_element_by_xpath("//div[@class='ant-col-10']/button").click()
            print u"同意来自%s的添加好友申请" % self.friend
            return True
        except NoSuchElementException, error:
            print u"%s Failed" % funname, error
            self.screenshot("%s.png" % funname)
            return False
    def sendMSfirend(self):
        funname = sys._getframe().f_code.co_name
        message = randoms()
        try:
            time.sleep(1)
            self.driver.find_element_by_xpath("//div[@class='nav-text']/div").click()
            time.sleep(1)
            self.driver.find_element_by_class_name("ant-input").send_keys(message)
            self.driver.find_element_by_xpath("//span[@class='ant-input-group-addon']/i").click()
            print u"用户%s发送文本消息，内容为%s" %(self.user,message)
            return True
        except NoSuchElementException, error:
            print u"%s Failed" % funname, error
            self.screenshot("%s.png" % funname)
            return False
    def refresh(self):
        try:
            self.driver.refresh()
        except Exception as e:
            print (u"Exception found", format(e))
    def receiveMess(self,message_num):
        time.sleep(2)
        try:
            if self.driver.find_element_by_xpath("//p[@class='current']"):
                data = self.driver.find_element_by_xpath("//p[@class='current']").text
                if int(data) != message_num:
                    print u"Failed, Receive message is not complete, expect num is: %s ,now num is: %s" % (str(message_num),str(data))
                    self.screenshot("receive.png")
                    return False
                else:
                    print u"Pass, New message is exist，num is: %s" % str(data)
                    return True
        except NoSuchElementException,e:
            print u"No message received，verify failed",e
            return False

    def addtoblack(self):
        funname = sys._getframe().f_code.co_name
        try:
            self.driver.find_element_by_xpath("//div[@class='nav-text']/div").click()
            self.driver.find_element_by_xpath("//div[@class='fr']/span/i").click()
            self.driver.find_element_by_xpath("//li[@class='ant-dropdown-menu-item']/i").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//div[@class='fl']/i").click()
            self.driver.find_element_by_xpath("//li[@class='ant-dropdown-menu-item']/span/i").click()
            time.sleep(2)
            blackuser = self.driver.find_element_by_xpath("//div[@class='force-overflow']/p").text
            if str(blackuser) == self.friend:
                print u"将好友%s成功加入到黑名单" % self.friend
                return True
            else:
                print u"好友%s加入到黑名单失败" % self.friend
                return False
        except NoSuchElementException, error:
            print u"%s Failed" % funname, error
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
            print u"将好友%s从黑名单中移除" % self.friend
            return True
        except NoSuchElementException, error:
            print u"%s Failed" % funname, error
            self.screenshot("%s.png" % funname)
            return False
    def delfriend(self):
        funname = sys._getframe().f_code.co_name
        try:
            self.driver.find_element_by_xpath("//div[@class='nav-text']/div").click()
            self.driver.find_element_by_xpath("//div[@class='fr']/span/i").click()
            self.driver.find_element_by_xpath("//i[@class='iconfont icon-trash']").click()
            print u"将好友%s删除" % self.friend
            return True
        except NoSuchElementException, error:
            print u"%s Failed" % funname, error
            self.screenshot("%s.png" % funname)
            return False
    def cleanchat(self):
        funname = sys._getframe().f_code.co_name
        try:
            self.driver.find_element_by_xpath("//div[@class='nav-text']/div").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//i[@class='icon iconfont icon-trash']").click()
            print u"清空聊天历史记录"
            return True
        except NoSuchElementException, error:
            print u"%s Failed, clean button is not found" % funname, error
            self.screenshot("%s.png" % funname)
            return False
    def sendimage(self):
        funname = sys._getframe().f_code.co_name
        try:
            self.driver.find_element_by_xpath("//div[@class='nav-text']/div").click()
            time.sleep(1)
            upimage = self.driver.find_element_by_id("uploadImage")
            upimage.send_keys("%s/123.png" %os.getcwd())
            print u"用户%s发送图片消息成功" % self.user
            return True
        except NoSuchElementException, error:
            print u"%s Failed, clean button is not found" % funname, error
            self.screenshot("%s.png" % funname)
            return False
    def sendfile(self):
        funname = sys._getframe().f_code.co_name
        try:
            self.driver.find_element_by_xpath("//div[@class='nav-text']/div").click()
            time.sleep(1)
            upfile = self.driver.find_element_by_id("uploadFile")
            upfile.send_keys("%s/123.png" % os.getcwd())
            print u"用户%s发送文件消息成功" % self.user
            return True
        except NoSuchElementException, error:
            print u"%s Failed, clean button is not found" % funname, error
            self.screenshot("%s.png" % funname)
            return False
    def screenshot(self,file):
        self.driver.get_screenshot_as_file("%s/errorpng/%s" %(os.getcwd(),file))
    def closewindow(self):
        try:
            if self.driver.find_element_by_xpath("//div[@class='ant-modal-content']"):
                self.driver.find_element_by_xpath("//div[@class='ant-modal-content']/button/span").click()
            else:
                pass
        except:
            pass
    def quitBrowser(self):
        self.driver.quit()






