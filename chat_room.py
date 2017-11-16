#coding: utf-8

import selenium,os,sys
import time,logging
from config import *
from chat_friend import AloneChat
from chat_group import ChatGroup
from selenium.webdriver.support.ui import WebDriverWait

sys.path.append(os.getcwd())

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(pathName)s [line: %(lineno)d] %(levelname)s %(message)s',
                    datefmt='%A, %Y-%m-%d %H:%M:%s',
                    filename='logs/chat.log',
                    filemode='a'
                    )

class ChatRoom(ChatGroup):
    def __init__(self,driver,user,passwd,url,friend,groupname):
        super(ChatRoom, self).__init__(driver, user, passwd, url, friend,groupname)

    def JoinChatroom(self):
        funname = sys._getframe().f_code.co_name
        try:
            self.driver.find_element_by_xpath(
                "//ul[@class='ant-menu ant-menu-horizontal x-header-tab__menu ant-menu-light ant-menu-root']/li[3]").click()
            WebDriverWait(self.driver, 5).until(
                lambda x: x.find_element_by_xpath("//div[@class='nav-text']/div")).click()
            try:
                if self.driver.find_element_by_xpath("//div[@class='x-list-item x-chat-header']/div"):
                    roomnumID = self.driver.find_element_by_xpath("//div[@class='x-list-item x-chat-header']/div").text
                    logging.info("join chat room success, chatroom id is: ",roomnumID)
                    print "join chat room success, chatroom id is: ",roomnumID
                    return True,roomnumID
                else:
                    self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
                    logging.debug("join chat room failed")
                    print "join chat room failed"
                    return False,None
            except Exception,error:
                self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
                logging.debug("join chat room failed",error)
                print "join chat room failed",error
                return False, None
        except Exception,error:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            logging.debug("join chat room failed", error)
            print "join chat room failed", error
            return False, None

    def JoinAssignRoom(self,roomnumID):
        funname = sys._getframe().f_code.co_name
        try:
            WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath(
                "//ul[@class='ant-menu ant-menu-horizontal x-header-tab__menu ant-menu-light ant-menu-root']/li[3]")).click()
            WebDriverWait(self.driver, 5).until(
                lambda x: x.find_element_by_xpath("//div[@class='nav-text']/div")).click()
            nownum = self.driver.find_element_by_xpath("//div[@class='x-list-item x-chat-header']/div").text
            for i in range(1, 10):
                if str(nownum) != roomnumID:
                    self.driver.find_element_by_xpath(
                        "//ul[@class='ant-menu ant-menu-inline ant-menu-light ant-menu-root']/li[%d]" % i).click()
                    nownum = self.driver.find_element_by_xpath("//div[@class='x-list-item x-chat-header']/div").text
                    if i == 10:
                        logging.debug("%s is not found" % roomnumID)
                        print "%s is not found" % roomnumID
                        exit(100)
                else:
                    logging.info("Join chatroom %s success" % roomnumID)
                    print "Join chatroom %s success" % roomnumID
                    break
            return True
        except Exception,err:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            logging.debug("join chatroom %s failed" % roomnumID, err)
            print "join chatroom %s failed" % roomnumID, err
            return False
    def sendroomMess(self,groupmess_num):
        funname = sys._getframe().f_code.co_name
        try:
            time.sleep(0.5)
            WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath(
                "//ul[@class='ant-menu ant-menu-horizontal x-header-tab__menu ant-menu-light ant-menu-root']/li[3]")).click()
            WebDriverWait(self.driver, 5).until(
                lambda x: x.find_element_by_xpath("//div[@class='nav-text']/div")).click()
            self.sendimage()
            self.sendfile()
            for num in range(groupmess_num-2):
                self.sendMSfirend()
            return True
        except Exception, error:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            logging.debug("%s Failed" % funname, error)
            print u"%s Failed" % funname, error
            return False

    def RoomMessNum(self,groupmess_num):
        funname = sys._getframe().f_code.co_name
        try:
            time.sleep(0.5)
            WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath(
                "//ul[@class='ant-menu ant-menu-horizontal x-header-tab__menu ant-menu-light ant-menu-root']/li[3]")).click()
            WebDriverWait(self.driver, 5).until(
                lambda x: x.find_element_by_xpath("//div[@class='nav-text']/div")).click()
            try:
                WebDriverWait(self.driver, 5).until(
                    lambda x: x.find_element_by_xpath("//div[@class='x-chat-content']/div[%d]" % groupmess_num))
                if self.driver.find_element_by_xpath("//div[@class='x-chat-content']/div[%d]" %groupmess_num):
                    logging.info("Verify chatroom message OK, number is: ", groupmess_num)
                    print u"Verify chatroom message OK, number is: ", groupmess_num
                    return True
            except Exception, error:
                self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
                logging.debug("Verify chatroom message failed, number is not %d" %groupmess_num, error)
                print u"Verify chatroom message failed, number is not %d" %groupmess_num, error
                return False
        except Exception, error:
            self.screenshot("%s_%s.png" % (funname, time.strftime('%H_%M_%S')))
            logging.debug("%s Failed" % funname, error)
            print u"%s Failed" % funname, error
            return False