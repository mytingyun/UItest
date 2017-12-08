#coding= utf-8


import HTMLTestRunner as htr
import unittest
import sys,os
from execute_friend import TestFriendChat
from execute_group import TestGroupChat
from execute_room import TestChatRoom
from config import *

os.system("del /F /S /Q %s/errorpng/*" %os.getcwd())

deluser(user1)
deluser(user2)
deluser(user3)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    try:
        webim2 = {
                TestFriendChat:["testSignin_1","testLogin_2","testaddFriend1_3","testLogout_4","testrefuseFriend_5","testaddFriend2_6","testagreeFriend_7",
                               "testsendImage_8","testsendFile_9","testMultiMess_10", "testAgreeVideo_11","testRefuVideo_12",
                               "testAgreeAudio_13","testRefuseAudio_14","testcleanchat_15","testaddblack_16","testremoveblack_17","testdelfriend_18"
                ],
                TestGroupChat:["testPublicGroupNo_1","testInviteMember_2","testVerifyJoin_3","testApplyGroup_4","testsdgrpMess_5","testgrpMessNum_6",
                               "testDelMember_7","testAddBlack_8","testRemoveBlack_9","testMute_10","testRemoveMute_11","testaddGrpAdmin_12","testRemoveAdmin_13",
                              "testModifyGrpName_14","testcleanGroupMess_15","testdissolveGroup_16","testpublicGrpYES_17","testRefusejoinGrp_18",
                               "testAgreejoinGrp_19","testGrpYESmessage_20","testGrpYESimage_21","testGrpYESfile_22","testGrpYESdissolve_23","testprivaGrpAllow_24","testprivaGrpInvite_25",
                               "testGrpAllowSendMess_26","testGrpAllowImage_27","testGrpAllowDissovle_28","testPrivateGrpNoAllow_29","testPrivateOwnerInvite_30",
                               "testPrivateMemberInvite_31","testPrivGrpSendMess_32","testPrivGrpfile_33","testPrivGrpNoDissovle_34"],

                TestChatRoom:["testJoinChatroom_1","testSendImage_2","testSendFile_3","testSdMultiMess_4","testCleanMessage_5",],

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