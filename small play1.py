print('...........我爱鱼工作室...........')
temp = input('不妨猜一下我心里想的是哪个数字')
guss = int(temp)
while guss != 8:
    temp = input('哎呀，猜错了重新再猜一次吧！')
    guss = int(temp)
    if guss == 8:
        print('我曹，你是我肚子里的蛔虫么')
        print('哼，猜中了也没有奖励')
    else:
        if guss > 8:
            print('大了大了')
        else:
            print('小了小了')
print('游戏结束，不玩了')

print('你电脑Python怎么运行？')
