#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：董美迪
日期：2020-4-6
"""
import random #导入random模块

def name_to_number(name): #自定义函数
    """
    将游戏对象对应到不同的整数
    """
    if name == str('石头'):
        number = 0
        return number
    elif name == str('史波克'):
        number = 1
        return number
    elif name == str('纸'):
        number = 2
        return number
    elif name == str('蜥蜴'):
        number = 3
        return number
    elif name == str('剪刀'):
        number = 4
        return number
    else:
        number = 10
        return number

def number_to_name(number): #自定义函数
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if number == 0:
        name = str('石头')
        return name
    elif number == 1:
        name = str('史波克')
        return name
    elif number == 2:
        name = str('纸')
        return name
    elif number == 3:
        name = str('蜥蜴')
        return name
    else:
        name = str('剪刀')
        return name

def rpsls(player_choice): #自定义函数
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
    """
    player_choice_number = name_to_number(player_choice)
    comp_number = random.randint(0,4)
    print('计算机的选择为：',number_to_name(comp_number))
    if comp_number == player_choice_number:
        print('您和计算机出的一样呢')
    elif abs(comp_number - player_choice_number) <= 2:
        if min(comp_number,player_choice_number)== comp_number:
            print('您赢了')
        else:
            print('机器赢了')
    elif abs(comp_number - player_choice_number) <= 4:
        if max(comp_number,player_choice_number)== comp_number:
            print('您赢了')
        else:
            print('机器赢了')
    else:
        print('Error: No Correct Name')

print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
player_choice=input( ) #输入选择
print('您的选择为：',player_choice)
rpsls(player_choice) #调用函数



