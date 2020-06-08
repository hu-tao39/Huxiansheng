import random
secret=random.randint(1,10)
print('...........我爱鱼工作室...........')
temp=input('不妨猜一下我心里想的是哪个数字')
guss=int(temp)
while guss !=secret :
    if guss>secret:
        print('大了大了')
    else :
        print('小了小了')
    temp=input('哎呀，猜错了重新猜猜看吧!')
    guss=int(temp)
    if guss==secret:
        print('我曹，你是我肚子里的蛔虫么？')
        print('哼，猜对了也没有奖励哈哈')
            
print('游戏结束，不玩了')
