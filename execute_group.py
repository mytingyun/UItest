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
        #driver2 = webdriver.Chrome()
        options = webdriver.ChromeOptions()
        options.add_argument('disable-infobars')
        browser = webdriver.Chrome(chrome_options=options)
        self.twouser = ChatGroup(browser, user2, gpasswd, url, user1, groupname)
        driver3 = webdriver.Chrome()
        self.threeuser = ChatGroup(driver3, user3, gpasswd, url, user1, groupname)

    def testPublicGroupNo(self):
        self.oneuser.sign_in()
        self.twouser.sign_in()
        self.threeuser.sign_in()

        self.oneuser.login()
        self.assertTrue(self.oneuser.publicgroup(), True)
        self.oneuser.quitBrowser()
        self.twouser.quitBrowser()
        self.threeuser.quitBrowser()
    def testInviteMember(self):
        self.oneuser.login()
        self.assertTrue(self.oneuser.invitemember(user2), True)
        time.sleep(2)
        self.oneuser.quitBrowser()
        self.twouser.quitBrowser()
        self.threeuser.quitBrowser()
    def testVerifyJoin(self):
        self.twouser.login()
        self.judge, self.groupnum = self.twouser.verifyjoin()
        self.assertTrue(self.judge, True)
        self.twouser.quitBrowser()
        self.oneuser.quitBrowser()
        self.threeuser.quitBrowser()

    def tearDown(self):
        self.oneuser = None
        self.twouser = None
        self.threeuser = None