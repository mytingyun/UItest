#coding: utf-8

from selenium import webdriver
import time,sys,requests
from config import *
from chat_friend import AloneChat
import unittest
sys.path.append("..")

deluser(user1)
deluser(user2)

class TestFriendChat(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('disable-infobars')
        browser = webdriver.Chrome(chrome_options=options)
        self.twouser = AloneChat(browser, user2, passwd2, url, user1)
        driver = webdriver.Chrome()
        self.oneuser = AloneChat(driver, user1, passwd1, url, user2)

    def testSignin(self):
        u'''测试注册用户'''
        self.assertTrue(self.oneuser.sign_in(), True)
        self.oneuser.quitBrowser()
        self.assertTrue(self.twouser.sign_in(), True)
        self.twouser.quitBrowser()
    def testLogin(self):
        u'测试登陆用户'
        self.assertTrue(self.oneuser.login(), True)
    def testaddFriend1(self):
        u'测试用户1添加好友，此次会被拒绝'
        self.oneuser.login()
        self.assertTrue(self.oneuser.addfirend(), True)
    def testLogout(self):
        u'测试用户1登出测试'
        self.oneuser.login()
        self.assertTrue(self.oneuser.logout(), True)
    def testrefuseFriend(self):
        u'测试拒绝添加好友'
        self.twouser.login()
        self.assertTrue(self.twouser.refusefriend(), True)
    def testaddFriend2(self):
        u'测试用户2添加好友，此次会被同意'
        self.oneuser.login()
        self.assertTrue(self.oneuser.addfirend(), True)
    def testagreeFriend(self):
        u'测试同意添加好友'
        self.twouser.login()
        self.assertTrue(self.twouser.agreefriend(), True)
    def testsendImage(self):
        u'测试发送图片消息'
        self.oneuser.login()
        self.twouser.login()
        self.twouser.sendimage()
        self.assertTrue(self.oneuser.receiveMess(1), True)
    def testsendFile(self):
        u'测试发送文件消息'
        self.oneuser.login()
        self.twouser.login()
        self.twouser.sendfile()
        self.assertTrue(self.oneuser.receiveMess(1), True)
    def testMultiMess(self):
        u'测试发送文本，图片，和文件多条消息'
        self.twouser.login()
        self.oneuser.login()
        self.oneuser.sendfile()
        self.oneuser.sendimage()
        self.oneuser.sendMSfirend()
        self.assertTrue(self.twouser.receiveMess(3), True)
    def testcleanchat(self):
        u'测试清除历史聊天记录'
        self.twouser.login()
        self.oneuser.login()
        self.oneuser.sendfile()
        self.oneuser.sendimage()
        self.oneuser.sendMSfirend()
        self.assertTrue(self.twouser.cleanchat(), True)
        time.sleep(2)

    def testaddblack(self):
        u'将好友移到黑名单'
        self.twouser.login()
        self.assertTrue(self.twouser.addtoblack(), True)
        time.sleep(2)
    def testremoveblack(self):
        u'将好友从黑名单中移除'
        self.twouser.login()
        self.assertTrue(self.twouser.removeblack(), True)
    def testdelfriend(self):
        u'将好友删除'
        self.twouser.login()
        self.assertTrue(self.twouser.delfriend(), True)

    def tearDown(self):
        self.twouser.quitBrowser()
        self.oneuser.quitBrowser()
        self.oneuser = None
        self.twouser = None







