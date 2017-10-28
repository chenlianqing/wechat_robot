#! /Users/chenlianqing/anaconda/bin python3
# -*- coding: utf-8 -*-


import itchat


# 用自己的微信账号登录
itchat.auto_login()


# 从昵称获取真实用户ID并发送信息
def send_wechat(nicknames,userNamelist):
    for i in nicknames:
        users = itchat.search_friends(name=i)
        userNamelist.append(users[0]['UserName'])
    nicknames.insert(0,u'陈廉清')
    for j in userNamelist:
        itchat.send(u'%s，您好，我是陈廉清的微信机器人。'%nicknames[userNamelist.index(j)],toUserName = j)


send_wechat(my_nicknames,my_userNamelist)







# ===================================================================
# 想给谁发信息，先查找到这个朋友
# users = itchat.search_friends(name=u'通讯录备注名')
# 找到UserName
# userName = users[0]['UserName']
# 然后给他发消息
# itchat.send('hello',toUserName = userName)
