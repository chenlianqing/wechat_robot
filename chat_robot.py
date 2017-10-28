#! /Users/chenlianqing/anaconda/bin python3
# -*- coding: utf-8 -*-


import itchat


# 用自己的微信账号登录
itchat.auto_login()


my_nicknames = [u'能小逗',u'陈晚清']
my_userNamelist = [u'filehelper']

def get_realid(nicknames,userNamelist):
    for i in nicknames:
        users = itchat.search_friends(name=i)
        userNamelist.append(users[0]['UserName'])
        nicknames.insert(0,u'陈廉清')

get_realid(my_nicknames,my_userNamelist)


my_nicknames.insert(0,u'陈廉清')

print(my_nicknames)
print(my_userNamelist)

for j in userNamelist:
    itchat.send(u'%s，您好，我是陈廉清的微信机器人。'%nicknames[userNamelist.index(j)],toUserName = j)







# ===================================================================
# 想给谁发信息，先查找到这个朋友
# users = itchat.search_friends(name=u'通讯录备注名')
# 找到UserName
# userName = users[0]['UserName']
# 然后给他发消息
# itchat.send('hello',toUserName = userName)
