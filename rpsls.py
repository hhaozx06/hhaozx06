#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�ֲ��һ�������
���ڣ�2020.4.2
"""

import random


# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
   if name=='ʯͷ':
	   a=input = 0
   elif name=='ʷ����':
	   a=input = 1
   elif name=='ֽ':
	   a=input = 2
   elif name=='����':
	   a=input = 3
   elif name=='����':
	   a=input = 4
   else:
	   print("Error: No Correct Name")
   return a


def number_to_name(number):
   if number==0:
       b='ʯͷ'
   elif number==1:
	   b='ʷ����'
   elif number==2:
	   b='ֽ'
   elif number==3:
	   b='����'
   else:
	   b='����'
   return b   
	   
	   
	   
	  
def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    print("����ѡ��Ϊ��",choice_name)
    pc = name_to_number(player_choice)
    computer_choice=random.randrange(0,4)
    cc = number_to_name(computer_choice)
    print("�������ѡ��Ϊ��",cc)
    d=computer_choice - int(pc)
    if d == 0:
	    print("���ͼ��������һ����")
    elif d == -1 or d == -2 or d ==3 or d ==4:
        print("��Ӯ�ˣ�")
    else:
	    print("����Ӯ�ˣ�")
    return 0

print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)

