#coding: utf-8

from selenium import webdriver
import time,sys,requests
from config import *
from chat_friend import AloneChat
import unittest
sys.path.append("..")


class TestFriendChat(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome()
        self.oneuser = AloneChat(driver, user1, passwd1, url, user2)
        options = webdriver.ChromeOptions()
        options.add_argument('disable-infobars')
        browser = webdriver.Chrome(chrome_options=options)
        self.twouser = AloneChat(browser, user2, passwd2, url, user1)

    def testSignin_1(self):
        u'''测试注册用户'''
        self.assertTrue(self.oneuser.sign_in(), True)
        self.oneuser.quitBrowser()
        self.assertTrue(self.twouser.sign_in(), True)
        self.twouser.quitBrowser()
    def testLogin_2(self):
        u'测试登陆用户'
        self.assertTrue(self.oneuser.login(), True)
    def testaddFriend1_3(self):
        u'测试用户1添加好友，此次会被拒绝'
        self.oneuser.login()
        self.assertTrue(self.oneuser.addfirend(), True)
    def testLogout_4(self):
        u'测试用户1登出测试'
        self.oneuser.login()
        self.assertTrue(self.oneuser.logout(), True)
    def testrefuseFriend_5(self):
        u'测试拒绝添加好友'
        self.twouser.login()
        self.assertTrue(self.twouser.refusefriend(), True)
    def testaddFriend2_6(self):
        u'测试用户2添加好友，此次会被同意'
        self.oneuser.login()
        self.assertTrue(self.oneuser.addfirend(), True)
    def testagreeFriend_7(self):
        u'测试同意添加好友'
        self.twouser.login()
        self.assertTrue(self.twouser.agreefriend(), True)
    def testsendImage_8(self):
        u'测试发送图片消息'
        self.oneuser.login()
        self.twouser.login()
        self.twouser.sendimage()
        self.assertTrue(self.oneuser.receiveimage(), True)
    def testsendFile_9(self):
        u'测试发送文件消息'
        self.oneuser.login()
        self.twouser.login()
        self.twouser.sendfile()
        self.assertTrue(self.oneuser.receivefile(), True)
    def testMultiMess_10(self):
        u'测试发送文本，图片，和文件多条消息'
        self.twouser.login()
        self.oneuser.login()
        self.oneuser.sendfile()
        self.oneuser.sendimage()
        self.oneuser.sendMSfirend()
        self.assertTrue(self.twouser.receiveMess(3), True)
    def testAgreeVideo_11(self):
        u'测试同意在线视频聊天的邀请'
        self.oneuser.login()
        onetab = self.oneuser.defineWindows()
        self.twouser.login()
        twotab = self.twouser.defineWindows()
        self.oneuser.sendMSfirend()
        self.twouser.sendMSfirend()
        self.oneuser.goBack(onetab)
        self.oneuser.inviteAuVid(3)
        self.oneuser.clickVideoAllow()
        self.twouser.goBack(twotab)
        self.assertTrue(self.twouser.agreeVideo(), True)
    def testRefuVideo_12(self):
        u'测试拒绝视频聊天的邀请'
        self.oneuser.login()
        onetab = self.oneuser.defineWindows()
        self.twouser.login()
        twotab = self.twouser.defineWindows()
        self.oneuser.sendMSfirend()
        self.twouser.sendMSfirend()
        self.oneuser.goBack(onetab)
        self.oneuser.inviteAuVid(3)
        self.oneuser.clickVideoAllow()
        self.twouser.goBack(twotab)
        self.assertTrue(self.twouser.refuseAuVid(), True)
    def testAgreeAudio_13(self):
        u'测试同意在线音频通话'
        self.oneuser.login()
        onetab = self.oneuser.defineWindows()
        self.twouser.login()
        self.oneuser.sendMSfirend()
        self.twouser.sendMSfirend()
        self.twouser.inviteAuVid(4)
        self.twouser.clickAudioAllow()
        self.oneuser.goBack(onetab)
        self.assertTrue(self.oneuser.agreeAudio(), True)
    def testRefuseAudio_14(self):
        u'测试拒绝在线音频通话'
        self.oneuser.login()
        onetab = self.oneuser.defineWindows()
        self.twouser.login()
        self.oneuser.sendMSfirend()
        self.twouser.sendMSfirend()
        self.twouser.inviteAuVid(4)
        self.twouser.clickAudioAllow()
        self.oneuser.goBack(onetab)
        self.assertTrue(self.oneuser.refuseAuVid(), True)


    def testcleanchat_15(self):
        u'测试清除历史聊天记录'
        self.twouser.login()
        self.oneuser.login()
        self.oneuser.sendfile()
        self.oneuser.sendimage()
        self.oneuser.sendMSfirend()
        self.assertTrue(self.twouser.cleanchat(), True)

    def testaddblack_16(self):
        u'将好友移到黑名单'
        self.twouser.login()
        self.assertTrue(self.twouser.addtoblack(), True)
    def testremoveblack_17(self):
        u'将好友从黑名单中移除'
        self.twouser.login()
        self.assertTrue(self.twouser.removeblack(), True)
    def testdelfriend_18(self):
        u'将好友删除'
        self.twouser.login()
        self.assertTrue(self.twouser.delfriend(), True)

    def tearDown(self):
        self.twouser.quitBrowser()
        self.oneuser.quitBrowser()
        self.oneuser = None
        self.twouser = None







