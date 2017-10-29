#! /Users/chenlianqing/anaconda/bin python3
# -*- coding: utf-8 -*-


from my_friends import *
from bestone import *
import itchat
import arrow
import time


# 微信登录并保持登录状态
itchat.auto_login(hotReload=True)


# 每小时获取一遍股票信息
def get_stock_info():
   my_msg = stock_info()
   return my_msg


# 从昵称获取真实用户ID并发送信息
def send_wechat(nicknames,userNamelist,msg):
    for i in nicknames:
        users = itchat.search_friends(name=i)
        userNamelist.append(users[0]['UserName'])
    nicknames.insert(0,u'陈廉清')
    for j in userNamelist:
        itchat.send(u'%s，您好,今日股票信息如下:%s'%(nicknames[userNamelist.index(j)],msg),toUserName = j)
    time.sleep(60)


# 规定自动运行时间
def auto_send(h1=9,h2=15,m=0):
    while True:
        while True:
            now = arrow.now()
            if (now.weekday()<=4 and (now.hour>=h1 and now.hour<=h2) and now.minute == m):
                break
            time.sleep(60)
        my_msg = get_stock_info()
        print("we have got stock_info.")
        send_wechat(my_nicknames,my_userNamelist,my_msg)

auto_send()


