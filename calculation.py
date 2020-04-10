#coding:gbk
'''
程序目标：实现利用键盘任意输入3个数，屏幕上输出其和以及平均值。
程序作者：植产一班 郝子轩
'''
def sum(num1,num2,num3):
    summation=num1+num2+num3
    return summation
def average(num1,num2,num3):
    ave = (num1+num2+num3)/3
    return ave
a=float(input("请输入第一个数："))
b=float(input("请输入第二个数："))
c=float(input("请输入第三个数："))
summation=sum(a,b,c)
aver=average(a,b,c)
print("三个数的和为："+str(summation))
print("三个数的平均数为："+str(aver))
