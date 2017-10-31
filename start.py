#coding= utf-8

import HTMLTestRunner as htr
import unittest
import sys,os
from execute_friend import TestFriendChat
from execute_group import TestGroupChat
from config import *

os.system("rm -f %s/errorpng/*" %os.getcwd())


if __name__ == "__main__":
    suite = unittest.TestSuite()
    try:
        webim2 = {
                TestFriendChat:["testSignin","testLogin","testLogout","testaddFriend1","testrefuseFriend","testaddFriend2","testagreeFriend",
                                "testsendImage","testsendFile","testMultiMess","testcleanchat","testaddblack","testremoveblack","testdelfriend"

                                ],
                TestGroupChat:["testPublicGroupNo","testInviteMember","testVerifyJoin","testApplyGroup","testsdgrpMess","testgrpMessNum",
                               "testDelMember","testAddBlack","testRemoveBlack","testMute","testRemoveMute","testaddGrpAdmin","testRemoveAdmin",
                               "testModifyGrpName","testcleanGroupMess","testdissolveGroup",
                               "testpublicGrpYES","testRefusejoinGrp","testAgreejoinGrp","testGrpYESmessage",
                               "testGrpYESdissolve","testprivaGrpAllow","testprivaGrpInvite","testGrpAllowSendMess","testGrpAllowDissovle","testPrivateGrpNoAllow",
                               "testPrivateOwnerInvite","testPrivateMemberInvite","testPrivGrpSendMess","testPrivGrpNoDissovle"

                               ]

                }
        for classes,methlist in webim2.items():
            for methods in methlist:
                suite.addTest(classes(methods))

    except ValueError,e:
        print "your methodname is not exist: %s" % e

    filename = '%s/logs/index.html' % os.getcwd()
    fp = file(filename, 'wb')
    runner = htr.HTMLTestRunner(
        stream=fp,
        title='Easemob Test Report',
        description='WebIM2.0 Test Report')
    runner.run(suite)