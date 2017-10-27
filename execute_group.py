#coding: utf-8

from selenium import webdriver
import time,sys,requests
from config import *
from chat_group import ChatGroup
import unittest
sys.path.append("..")

deluser(user1)
deluser(user2)
deluser(user3)

class TestGroupChat(unittest.TestCase):
    def setUp(self):
        driver1 = webdriver.Chrome()
        self.oneuser = ChatGroup(driver1, user1, gpasswd, url, user2, groupname)

        options = webdriver.ChromeOptions()
        options.add_argument('disable-infobars')
        self.browser = webdriver.Chrome(chrome_options=options)
        self.twouser = ChatGroup(self.browser, user2, gpasswd, url, user1, groupname)

        self.driver3 = webdriver.Chrome()
        self.threeuser = ChatGroup(self.driver3, user3, gpasswd, url, user1, groupname)

    def testPublicGroupNo(self):
        u'验证创建群组'
        self.oneuser.sign_in()
        self.twouser.sign_in()
        self.threeuser.sign_in()
        self.oneuser.login()
        self.assertTrue(self.oneuser.publicgroup(), True)
        self.oneuser.quitBrowser()
        self.twouser.quitBrowser()
        self.threeuser.quitBrowser()
    def testInviteMember(self):
        u'验证邀请其他人员加入群聊'
        self.oneuser.login()
        self.assertTrue(self.oneuser.invitemember(user2), True)
        time.sleep(2)
        self.oneuser.quitBrowser()
        self.twouser.quitBrowser()
        self.threeuser.quitBrowser()
    def testVerifyJoin(self):
        u'验证是否加入成功'
        self.twouser.login()
        global groupnum
        self.judge, groupnum = self.twouser.verifyjoin()
        self.assertTrue(self.judge, True)
        self.twouser.quitBrowser()
        self.oneuser.quitBrowser()
        self.threeuser.quitBrowser()
    def testApplyGroup(self):
        u'验证申请加入群聊'
        self.threeuser.login()
        self.assertTrue(self.threeuser.applyjoin(groupnum), True)
        self.twouser.quitBrowser()
        self.oneuser.quitBrowser()
        self.threeuser.quitBrowser()
    def testsdgrpMess(self):
        u'验证发送一定数量的群消息'
        self.oneuser.login()
        self.assertTrue(self.oneuser.sendgroupMess(groupmess_num), True)
        self.twouser.quitBrowser()
        self.oneuser.quitBrowser()
        self.threeuser.quitBrowser()
    def testgrpMessNum(self):
        u'验证发送的群消息和数量其他成员是否收到'
        self.twouser.login()
        self.oneuser.login()
        self.oneuser.sendgroupMess(groupmess_num)
        self.assertTrue(self.twouser.groupMessNum(groupmess_num), True)
        self.twouser.quitBrowser()
        self.oneuser.quitBrowser()
        self.threeuser.quitBrowser()
    def testDelMember(self):
        u'验证删除群成员'
        self.oneuser.login()
        global nowuser
        result, nowuser = self.oneuser.operateMember(4)
        self.four = ChatGroup(self.browser, nowuser, gpasswd, url, user1, groupname)
        self.four.login()
        self.assertTrue(self.four.verifyDelete(nowuser), True)
        self.four.applyjoin(groupnum)
        self.twouser.quitBrowser()
        self.oneuser.quitBrowser()
        self.threeuser.quitBrowser()
        self.four.quitBrowser()
    def testAddBlack(self):
        u'验证将成员加入黑名单'
        self.oneuser.login()
        global blackuser
        result, blackuser = self.oneuser.operateMember(3)
        self.assertTrue(self.oneuser.verifyBlkList(blackuser), True)
        self.twouser.quitBrowser()
        self.oneuser.quitBrowser()
        self.threeuser.quitBrowser()
    def testRemoveBlack(self):
        u'验证将黑名单的成员移除'
        self.oneuser.login()
        self.assertTrue(self.oneuser.groupRemoveblack(), True)
        self.twouser.quitBrowser()
        self.oneuser.quitBrowser()
        self.threeuser.quitBrowser()
    def testMute(self):
        u'验证对某群成员禁言'
        self.other = ChatGroup(self.browser, blackuser, gpasswd, url, user1, groupname)
        self.other.login()
        self.other.applyjoin(groupnum)
        self.other.quitBrowser()
        self.oneuser.login()
        a, muteuser = self.oneuser.operateMember(2)
        self.four = ChatGroup(self.driver3, muteuser, gpasswd, url, user1, groupname)
        self.four.login()
        self.four.sendgroupMess(groupmess_num)
        self.assertFalse(self.oneuser.groupMessNum(groupmess_num), False)
        self.oneuser.quitBrowser()
        self.four.quitBrowser()
        self.threeuser.quitBrowser()
        self.twouser.quitBrowser()
    def testRemoveMute(self):
        u'验证对禁言的成员解除禁言'
        self.oneuser.login()
        a, muteuser = self.oneuser.operateMember(2)
        self.four = ChatGroup(self.browser, muteuser, gpasswd, url, user1, groupname)
        self.four.login()
        self.four.sendgroupMess(groupmess_num)
        self.assertTrue(self.oneuser.groupMessNum(groupmess_num), True)
        self.oneuser.quitBrowser()
        self.four.quitBrowser()
        self.threeuser.quitBrowser()
        self.twouser.quitBrowser()
    def testaddGrpAdmin(self):
        u'验证将成员转为管理员'
        self.oneuser.login()
        a, adminuser = self.oneuser.operateMember(1)
        self.assertTrue(self.oneuser.groupadmin(groupnum,adminuser), True)
        self.oneuser.quitBrowser()
        self.threeuser.quitBrowser()
        self.twouser.quitBrowser()
    def testRemoveAdmin(self):
        u'验证解除管理员权限'
        self.oneuser.login()
        a, adminuser = self.oneuser.operateMember(1)
        self.assertFalse(self.oneuser.groupadmin(groupnum, adminuser), False)
        self.oneuser.quitBrowser()
        self.threeuser.quitBrowser()
        self.twouser.quitBrowser()


    def tearDown(self):
        self.oneuser = None
        self.twouser = None
        self.threeuser = None