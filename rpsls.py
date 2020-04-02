#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：植产一班郝子轩
日期：2020.4.2
"""

import random


# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
   if name=='石头':
	   a=input = 0
   elif name=='史波克':
	   a=input = 1
   elif name=='纸':
	   a=input = 2
   elif name=='蜥蜴':
	   a=input = 3
   elif name=='剪刀':
	   a=input = 4
   else:
	   print("Error: No Correct Name")
   return a


def number_to_name(number):
   if number==0:
       b='石头'
   elif number==1:
	   b='史波克'
   elif number==2:
	   b='纸'
   elif number==3:
	   b='蜥蜴'
   else:
	   b='剪刀'
   return b   
	   
	   
	   
	  
def rpsls(player_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

    """
    print("您的选择为：",choice_name)
    pc = name_to_number(player_choice)
    computer_choice=random.randrange(0,4)
    cc = number_to_name(computer_choice)
    print("计算机的选择为：",cc)
    d=computer_choice - int(pc)
    if d == 0:
	    print("您和计算机出的一样呢")
    elif d == -1 or d == -2 or d ==3 or d ==4:
        print("您赢了！")
    else:
	    print("机器赢了！")
    return 0

print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)


