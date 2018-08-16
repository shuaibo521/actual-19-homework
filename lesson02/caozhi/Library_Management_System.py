#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author emmby,2018-08-15
# 图书管理系统

def login():
    global user_name, password
    if count == 0:
        print('Please try tomorrow!')
        exit(1)
    user_name = input('Please enter your user_name: ')
    password = input('Please enter your password: ')
print('=' * 80, end='')
print('''
\033[31mWelcome to come Liaoning Project Technology University library management system \033[0m
''', end='')
print('=' * 80)
usermessage = ('admin', 'playbook')
userinfo = [
    [1, 'caozhi', 25, '0419', 'liaoyang'],
    [2, 'emmby', 25, '010', 'beijing'],
    [3, 'xiaozhi', 25, '0429', 'huludao'],
    [5, 'xuwei', 50, '029', 'xian'],
    [8, 'pushu', 45, '010', 'beijing'],
]
count = 3
while 1:
    login()
    if user_name == usermessage[0] and password == usermessage[1]:
        print('login success')
        print('=' * 80)
        print('''
Please enter an action
    1、"insert": insert a record.
    2、"select": select someone message.
    3、"update": update someone message.
    4、"delete": delete someone message.
    5、"quit": quit this system.
        ''')
        print('=' * 80)
        print()
        action = input('Please enter your action: ')
        if action == 'insert':
            insert_id = userinfo[-1][0] + 1
            insert_name = input('Please enter add name: ')
            insert_age = int(input('Please enter add age: '))
            insert_tel = input('Please enter add tel: ')
            insert_add = input('Please enter add address: ')
            userinfo.append([insert_id, insert_name, insert_age, insert_tel, insert_add])
        elif action == 'select':
            select_name = input('Please enter select name: ')
            select_flag = 0
            for i in userinfo:
                if select_name == i[1]:
                    print(i)
                    select_flag = 1
            if select_flag == 0:
                print('Sorry, record empty')
        elif action == 'update':
            update_id = int(input('Please enter update student id: '))
            update_flag = 0
            j = 0
            for m in userinfo:
                if update_id == m[0]:
                    update_name = input('Please enter update name: ')
                    update_age = int(input('Please enter update age: '))
                    update_tel = input('Please enter update tel: ')
                    update_add = input('Please enter update address: ')
                    update_flag = 0
                    userinfo[j] = [update_id, update_name, update_age, update_tel, update_add]
                    print(userinfo[j])
                    update_flag = 1
                j += 1
            if update_flag == 0:
                print('Sorry, record empty')
        elif action == 'delete':
            delete_id = int(input('Please enter delete student id: '))
            n = 0
            delete_flag = 0
            for j in userinfo:
                if delete_id == j[0]:
                    userinfo.pop(n)
                    delete_flag = 1
                n += 1
            if delete_flag == 0:
                print('Sorry, record empty')
        elif action == 'exit':
            print('Exit success')
            exit(0)
        else:
            print('Your action is illegal')
    else:
        count -= 1
        print('login error, you have %d left choice' % count)