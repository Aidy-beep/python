#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�������
���ڣ�2020-4-6
"""
import random #����randomģ��

def name_to_number(name): #�Զ��庯��
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name == str('ʯͷ'):
        number = 0
        return number
    elif name == str('ʷ����'):
        number = 1
        return number
    elif name == str('ֽ'):
        number = 2
        return number
    elif name == str('����'):
        number = 3
        return number
    elif name == str('����'):
        number = 4
        return number
    else:
        number = 10
        return number

def number_to_name(number): #�Զ��庯��
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number == 0:
        name = str('ʯͷ')
        return name
    elif number == 1:
        name = str('ʷ����')
        return name
    elif number == 2:
        name = str('ֽ')
        return name
    elif number == 3:
        name = str('����')
        return name
    else:
        name = str('����')
        return name

def rpsls(player_choice): #�Զ��庯��
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
    """
    player_choice_number = name_to_number(player_choice)
    comp_number = random.randint(0,4)
    print('�������ѡ��Ϊ��',number_to_name(comp_number))
    if comp_number == player_choice_number:
        print('���ͼ��������һ����')
    elif abs(comp_number - player_choice_number) <= 2:
        if min(comp_number,player_choice_number)== comp_number:
            print('��Ӯ��')
        else:
            print('����Ӯ��')
    elif abs(comp_number - player_choice_number) <= 4:
        if max(comp_number,player_choice_number)== comp_number:
            print('��Ӯ��')
        else:
            print('����Ӯ��')
    else:
        print('Error: No Correct Name')

print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
player_choice=input( ) #����ѡ��
print('����ѡ��Ϊ��',player_choice)
rpsls(player_choice) #���ú���



