#coding: utf-8

import selenium,os,sys
import time
from config import *
from selenium.webdriver.support.ui import WebDriverWait
from pymouse import PyMouse
from selenium.common.exceptions import NoSuchElementException
mouse = PyMouse()
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
            self.driver.set_page_load_timeout(30)
            self.driver.get(self.url)
            self.driver.find_element_by_xpath("//div[@class='extra']/p/span").click()
            self.driver.find_element_by_xpath("//div[@class='ant-form-item-control ']/input").send_keys(self.user)
            self.driver.find_element_by_xpath("//div[@class='ant-form-item-control ']/input").send_keys(self.passwd)
            self.driver.find_element_by_xpath("//div[@class='ant-form-item-control ']/input").send_keys(self.user)
            self.driver.find_element_by_xpath("//div[@class='ant-row']/button").click()
            print u"此次注册的用户名是：%s, 密码是：%s, 昵称是：%s" %(self.user,self.passwd,self.user)
            time.sleep(1)
            return True
        except Exception,error:
            self.screenshot("sing_in_%s.png" % time.strftime('%H_%M_%S'))
            print u"Sign in Failed",error
            return False
    def login(self):
        funname = sys._getframe().f_code.co_name
        try:
            self.driver.set_page_load_timeout(60)

            self.driver.get(self.url)
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_id("username")).send_keys(self.user)
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_id("password")).send_keys(self.passwd)
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//div[@class='ant-row']/button")).click()
            #while True:
            #    try:
            #        if self.driver.find_element_by_xpath("//div[@id='x-header-ops']/div[2]"):
             #           break
            #    except Exception:
            #        print "waiting the login...."
            #        time.sleep(0.5)
             #       continue
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_xpath("//div[@id='x-header-ops']/div[2]"))
            username = self.driver.find_element_by_xpath("//div[@id='x-header-ops']/div[2]").text
            if str(username) == self.user:
                print u"用户名%s登陆成功" % self.user
                return True
            else:
                self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
                print u"用户%s登陆失败" % self.user
                return False

        except Exception,error:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            print u"%s Failed" % funname, error
            return False
    def logout(self):
        try:
            self.driver.find_element_by_xpath("//i[@class='anticon anticon-setting ant-dropdown-trigger']").click()
            self.driver.find_element_by_xpath("//i[@class='anticon anticon-logout']").click()
            return True
        except Exception, error:
            self.screenshot("logout_%s.png" % time.strftime('%H_%M_%S'))
            print u"logout Failed", error
            return False
    def addfirend(self):
        funname = sys._getframe().f_code.co_name  #get self functioin name
        try:
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_xpath(
                "//div[@class='fr']/i")).click()
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//i[@class='anticon anticon-user-add']")).click()
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//div[@class='ant-col-20']/input")).send_keys(self.friend)
            self.driver.find_element_by_xpath("//div[@class='ant-col-4']/button").click()
            print u"添加的好友是：", self.friend
            return True
        except Exception, error:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            print u"%s Failed" %funname, error
            return False
    def refusefriend(self):
        funname = sys._getframe().f_code.co_name
        try:
            time.sleep(0.5)
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//div[@class='ant-col-10']/button[2]")).click()
            print u"拒绝来自%s的添加好友申请" % self.friend
            return True
        except Exception, error:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            print u"%s Failed" % funname, error
            return False
    def agreefriend(self):
        funname = sys._getframe().f_code.co_name
        try:
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//div[@class='ant-col-10']/button")).click()
            print u"同意来自%s的添加好友申请" % self.friend
            return True
        except Exception, error:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            print u"%s Failed" % funname, error
            return False
    def sendMSfirend(self):
        funname = sys._getframe().f_code.co_name
        message = randoms()
        self.driver.maximize_window()
        try:
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//div[@class='nav-text']/div")).click()
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_class_name("ant-input")).send_keys(message)
            self.driver.find_element_by_xpath("//span[@class='ant-input-group-addon']/i").click()
            print u"用户%s发送文本消息，内容为%s" %(self.user,message)
            return True
        except Exception, error:
            print u"%s Failed" % funname, error
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
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
                    self.screenshot("receive_%s.png" % time.strftime('%H_%M_%S'))
                    print u"Failed, Receive message is not complete, expect num is: %s ,now num is: %s" % (str(message_num),str(data))
                    return False
                else:
                    print u"Pass, New message is exist，num is: %s" % str(data)
                    return True
        except Exception,e:
            self.screenshot("receive_%s.png" % time.strftime('%H_%M_%S'))
            print u"No message received，verify failed",e
            return False

    def addtoblack(self):
        funname = sys._getframe().f_code.co_name
        try:
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//div[@class='nav-text']/div")).click()
            self.driver.find_element_by_xpath("//div[@class='fr']/span/i").click()
            self.driver.find_element_by_xpath("//li[@class='ant-dropdown-menu-item']/i").click()
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_xpath("//div[@class='fl']/i")).click()
            self.driver.find_element_by_xpath("//li[@class='ant-dropdown-menu-item']/span/i").click()
            time.sleep(0.5)
            blackuser = self.driver.find_element_by_xpath("//div[@class='force-overflow']/p").text
            if str(blackuser) == self.friend:
                print u"将好友%s成功加入到黑名单" % self.friend
                return True
            else:
                self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
                print u"好友%s加入到黑名单失败" % self.friend
                return False
        except Exception, error:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            print u"%s Failed" % funname, error
            return False
    def removeblack(self):
        funname = sys._getframe().f_code.co_name
        try:
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_xpath("//div[@class='fl']/i")).click()
            self.driver.find_element_by_xpath("//li[@class='ant-dropdown-menu-item']/span/i").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//i[@class='fr iconfont icon-circle-minus']").click()
            self.driver.find_element_by_xpath("//span[@class='ant-modal-close-x']").click()
            print u"将好友%s从黑名单中移除" % self.friend
            return True
        except Exception, error:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            print u"%s Failed" % funname, error
            return False
    def delfriend(self):
        funname = sys._getframe().f_code.co_name
        try:
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//div[@class='nav-text']/div")).click()
            self.driver.find_element_by_xpath("//div[@class='fr']/span/i").click()
            self.driver.find_element_by_xpath("//i[@class='iconfont icon-trash']").click()
            print u"将好友%s删除" % self.friend
            return True
        except Exception, error:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            print u"%s Failed" % funname, error
            return False
    def cleanchat(self):
        funname = sys._getframe().f_code.co_name
        try:
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//div[@class='nav-text']/div")).click()
            time.sleep(2)
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//i[@class='icon iconfont icon-trash']")).click()
            print u"清空聊天历史记录"
            return True
        except Exception, error:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            print u"%s Failed, clean button is not found" % funname, error
            return False
    def sendimage(self):
        funname = sys._getframe().f_code.co_name
        try:
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//div[@class='nav-text']/div")).click()
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_id("uploadImage"))
            upimage = self.driver.find_element_by_id("uploadImage")
            upimage.send_keys("%s/123.png" %os.getcwd())
            print u"用户%s发送图片消息成功" % self.user
            return True
        except Exception, error:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            print u"%s Failed," % funname, error
            return False
    def receiveimage(self):
        funname = sys._getframe().f_code.co_name
        try:
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//div[@class='nav-text']/div")).click()
            #time.sleep(1)
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_xpath("//div[@class='x-message-img']/img"))
            if self.driver.find_element_by_xpath("//div[@class='x-message-img']/img"):
                imageurl = self.driver.find_element_by_xpath("//div[@class='x-message-img']/img").get_attribute("src")
                print "image url: ", imageurl
                code = requests.get(imageurl)
                if code.status_code == 200:
                    print "image messages receive success"
                    return True
                else:
                    self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
                    print "image messages receive failed"
                    return False
        except Exception, error:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            print "not receive image messsage", error
            return False

    def sendfile(self):
        funname = sys._getframe().f_code.co_name
        try:
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//div[@class='nav-text']/div")).click()
            WebDriverWait(self.driver, sleeptime).until(lambda x: x.find_element_by_id("uploadFile"))
            upfile = self.driver.find_element_by_id("uploadFile")
            upfile.send_keys("%s/config.py" % os.getcwd())
            print u"用户%s发送文件消息成功" % self.user
            return True
        except Exception, error:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            print u"%s Failed, " % funname, error
            return False
    def receivefile(self):
        funname = sys._getframe().f_code.co_name
        try:
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//div[@class='nav-text']/div")).click()
            WebDriverWait(self.driver, sleeptime).until(
                lambda x: x.find_element_by_xpath("//div[@class='x-message-file']/div/div[2]/a"))
            if self.driver.find_element_by_xpath("//div[@class='x-message-file']/div/div[2]/a"):
                fileurl = self.driver.find_element_by_xpath("//div[@class='x-message-file']/div/div[2]/a").get_attribute("href")
                print "file url: ", fileurl
                code = requests.get(fileurl)
                if code.status_code == 200:
                    print "File messages receive success"
                    return True
                else:
                    self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
                    print "File messages receive failed"
                    return False
        except NoSuchElementException, error:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            print "not receive file messsage", error
            return False

    def clickVideoAllow(self):
        time.sleep(2)
        #use mouse.position() location
        mouse.click(385, 201)

    def clickAudioAllow(self):
        time.sleep(2)
        # use mouse.position() location
        mouse.click(379, 183)

    def openDevTool(self):
        mouse.click(385, 301, 2)
        time.sleep(1)
        mouse.click(428, 488)

    def inviteAuVid(self,num):
        # num is videois 3, Audio 4
        funname = sys._getframe().f_code.co_name
        try:
            time.sleep(1)
            self.driver.find_element_by_xpath("//div[@class='x-list-item x-chat-ops']/label[%d]/i" %num).click()
            print "%s invite %s audio or Video chat" %(self.user,self.friend)
        except Exception, error:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            print "invite friend %s Video failed" % self.friend, error
    def defineWindows(self):
        oldtab = self.driver.current_window_handle
        return oldtab
    def goBack(self,oldtab):
        self.driver.switch_to_window(oldtab)
        time.sleep(2)

    def agreeVideo(self):
        funname = sys._getframe().f_code.co_name
        try:
            time.sleep(1)
            self.driver.find_element_by_xpath("//div[@class='x-chat']/div[4]/div/i[2]").click()
            self.clickVideoAllow()
            username = self.driver.find_element_by_xpath("//div[@class='x-chat']/div[4]/div/span").text
            time.sleep(1)
            if username == self.friend:
                self.screenshot("%s_%s_Pass.png" % (funname, time.strftime('%H_%M_%S')))
                print "Agree friend %s Video success" % self.friend
                return True
            else:
                self.screenshot("%s_%s_Failed.png" % (funname, time.strftime('%H_%M_%S')))
                print "Agree friend %s Video failed" % self.friend
                return False
        except Exception, error:
            self.screenshot("%s_%s_Failed.png" % (funname, time.strftime('%H_%M_%S')))
            print "Agree friend %s Video failed" % self.friend, error
            return False

    def agreeAudio(self):
        funname = sys._getframe().f_code.co_name
        try:
            WebDriverWait(self.driver, 50).until(
                lambda x: x.find_element_by_xpath("//div[@class='x-chat']/div[4]/div/i[2]")).click()
            self.clickAudioAllow()
            username = self.driver.find_element_by_xpath("//div[@class='x-chat']/div[4]/div/span").text
            time.sleep(1)
            if username == self.friend:
                self.screenshot("%s_%s_Pass.png" % (funname, time.strftime('%H_%M_%S')))
                print "Agree friend %s Audio success" % self.friend
                return True
            else:
                self.screenshot("%s_%s_Failed.png" % (funname, time.strftime('%H_%M_%S')))
                print "Agree friend %s Audio failed" % self.friend
                return False
        except Exception, error:
            self.screenshot("%s_%s_Failed.png" % (funname, time.strftime('%H_%M_%S')))
            print "Agree friend %s Audio failed" % self.friend, error
            return False

    def refuseAuVid(self):
        funname = sys._getframe().f_code.co_name
        try:
            WebDriverWait(self.driver, 50).until(
                lambda x: x.find_element_by_xpath("//div[@class='x-chat']/div[4]/div/i")).click()
            time.sleep(1)
            self.screenshot("%s_%s_Pass.png" % (funname, time.strftime('%H_%M_%S')))
            try:
                if self.driver.find_element_by_xpath("//video[@class='corner']"):
                    print "refuse friend %s Audio or Video failed" % self.friend
                    return False
            except NoSuchElementException:
                print "refuse friend %s Video or Audio success" % self.friend
                return True
        except Exception, error:
            self.screenshot("%s_%s_Failed.png" % (funname, time.strftime('%H_%M_%S')))
            print "invite friend %s Video or Audio failed" % self.friend, error

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






