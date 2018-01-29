#-*-coding:utf-8-*-

from random import randint
from time import sleep
import os

__metaclass__=type

openTime = 0
randNum = 0
nowTime = openTime
randNum = 0
sum = 0
lastRefresh = openTime
class BIZ:
    def __init__(self):
        self.num = 0
        self.time = 0
class USER:
    def __init__(self):
        self.num = 0
        self.inTime = 0
        self.outTime = 0
        self.deltaTime = 0
        self.biz = [-1,-1,-1]
        self.next = None

class WIN:
    def __init__(self):
        self.num = 0
        self.sumTime = 0
        self.userList = None

def Print():
    print "******当前时间{time}*******".format(time=nowTime)
    for i in winList:
        print "窗口{num}:".format(num=i.num)
        if i.userList == None:
            print "无用户"
        else:
            p=i.userList
            while p!= None:
                print "用户{num} 在办理".format(num=p.num),
                for i in p.biz:
                    if i == -1:
                        break
                    else:
                        print "业务{num}".format(num=bizList[i].num),
                print "\n",
                p = p.next

def OUT():
    global lastRefresh
    while True:
        flag = []
        for i in winList:
            if i.userList == None:
                flag.append(0)
            elif i.userList.outTime > nowTime:
                flag.append(0)
            else:
                flag.append(1)
        min = winList[0]
        j=0
        for i in flag:
            if i == 1:
                j = i
                break
        if j == 0:
            return
        else:
            for j in winList:
                if j.userList != None:
                    min = j
                    break
            for m in winList:
                if m.userList == None:
                    continue
                elif min.userList.outTime > m.userList.outTime:
                    min = m
            p = min.userList
            min.userList = p.next
            min.sumTime = min.sumTime-p.deltaTime
            sleep(nowTime-lastRefresh)
            lastRefresh=nowTime
            os.system("clear")
            Print()

def IN():
    global sum
    global lastRefresh
    randNum = randint(0, 3)
    while randNum > 0:
        sum = sum+1
        user = USER()
        user.num = sum
        user.inTime = nowTime

        bizNum=randint(0,2)
        user.biz[0]=bizNum
        bizNum=randint(0,2)
        if bizNum == user.biz[0]:
            user.biz[0] = bizNum
        else:
            user.biz[1] = bizNum

        for i in user.biz:
            if i == -1:
                break
            else:
                user.deltaTime = user.deltaTime + bizList[i].time

        user.ouTime = nowTime + user.deltaTime

        min = winList[0]

        for i in winList:
            if min.sumTime > i.sumTime:
                min = i

        p = min.userList

        if p == None:
            min.userList = user
        else:
            while p.next!=None:
                p = p.next
            p.next = user

        min.sumTime = min.sumTime + user.deltaTime

        sleep(nowTime-lastRefresh)
        lastRefresh = nowTime
        os.system("clear")

        Print()

        randNum = randNum - 1


winList=[]
for i in range(3):
    winList.append(WIN())
    winList[i].num = i+1

bizList=[]
for i in range(3):
    bizList.append(BIZ())
    bizList[i].num = i+1
    bizList[i].time = (i+1)*2



endTime = int(input("请输入结束时间:"))

os.system("clear")
print "时间为{time}时结束模拟，系统正在刷新，请稍后……".format(time=endTime)

randTime = randint(0,10)
nowTime = nowTime + randTime

while nowTime<endTime:
    OUT()
    IN()

    randTime = randint(0,10)
    nowTime = nowTime +randTime

OUT()
print "结束营业"









