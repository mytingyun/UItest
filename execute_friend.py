#coding: utf-8

from selenium import webdriver
import time
from config import *
from chat_friend import AloneChat

#启动一个浏览器，用户1注册，登陆，添加好友
driver = webdriver.Chrome()
oneuser = AloneChat(driver,user1,passwd1,url,user2)
#oneuser.sign_in()
oneuser.login()
oneuser.addfirend()
#oneuser.logout()


#启动另一个浏览器，用户2注册，登陆，同意添加好友，发送消息
options = webdriver.ChromeOptions()
options.add_argument('disable-infobars')
browser = webdriver.Chrome(chrome_options=options)
twouser = AloneChat(browser,user2,passwd2,url,user1)
twouser.login()
twouser.agreefriend()
twouser.sendMSfirend()
twouser.sendfile()
twouser.sendimage()
twouser.logout()

'''
twouser.sign_in()
twouser.refresh()
time.sleep(2)

twouser.quitBrowser()

#用户1接收消息
oneuser.receiveMess()
oneuser.addtoblack()
oneuser.removeblack()
oneuser.delfriend()
oneuser.sendMSfirend()
oneuser.sendimage()
oneuser.sendfile()
'''
time.sleep(2)
oneuser.receiveMess()
oneuser.cleanchat()




#time.sleep(3)
