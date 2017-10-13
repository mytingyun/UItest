#coding: utf-8

from selenium import webdriver
import time
from config import *

options = webdriver.ChromeOptions()
options.add_argument('disable-infobars')
browser = webdriver.Chrome(chrome_options=options)

class AloneChat:

    def __init__(self,user,passwd,url,friend):
        self.user = user
        self.passwd = passwd
        self.url = url
        self.friend = friend
    def login(self):
        browser.get(self.url)
        browser.find_element_by_id("username").send_keys(self.user)
        browser.find_element_by_id("password").send_keys(self.passwd)
        browser.find_element_by_xpath("//div[@class='ant-row']/button").click()
    def addfirend(self):
        time.sleep(2)
        browser.find_element_by_xpath("//div[@class='fr']/i").click()
        browser.find_element_by_xpath("//i[@class='anticon anticon-user-add']").click()
        time.sleep(1)
        browser.find_element_by_xpath("//div[@class='ant-col-20']/input").send_keys(self.friend)
        browser.find_element_by_xpath("//div[@class='ant-col-4']/button").click()

    def refusefriend(self):
        time.sleep(3)
        browser.find_element_by_xpath("//div[@class='ant-col-10']/button[2]").click()

    def agreefriend(self):
        time.sleep(3)
        browser.find_element_by_xpath("//div[@class='ant-col-10']/button").click()

    def sendMSfirend(self):
        time.sleep(2)
        browser.find_element_by_xpath("//div[@class='nav-text']/div").click()
        time.sleep(1)
        browser.find_element_by_class_name("ant-input").send_keys(message)
        browser.find_element_by_xpath("//span[@class='ant-input-group-addon']/i").click()

    def receiveMess(self):


        time.sleep(5)
        #browser.quit()
twouser = AloneChat(user2,passwd2,url,user1)
twouser.login()


options = webdriver.ChromeOptions()
options.add_argument('disable-infobars')
browser = webdriver.Chrome(chrome_options=options)
oneuser = AloneChat(user1,passwd1,url,user2)
oneuser.login()
oneuser.sendMSfirend()






