#coding:gbk
'''
����Ŀ�꣺ʵ�����ü�����������3��������Ļ���������Լ�ƽ��ֵ��
�������ߣ�ֲ��һ�� ������
'''
def sum(num1,num2,num3):
    summation=num1+num2+num3
    return summation
def average(num1,num2,num3):
    ave = (num1+num2+num3)/3
    return ave
a=float(input("�������һ������"))
b=float(input("������ڶ�������"))
c=float(input("���������������"))
summation=sum(a,b,c)
aver=average(a,b,c)
print("�������ĺ�Ϊ��"+str(summation))
print("��������ƽ����Ϊ��"+str(aver))
