
login_username = ['123']#账号表
login_password = ['123']#密码表
#员工信息
#序号、姓名、年龄、电话、城市
userinfo = [
    [1,'zhangjinqi','25','13240145401','beijing']
]

find_name = [arr[1] for arr in userinfo]
while True:
    new_old = input('您好，您是新用户还是老用户？(n/o)')
    if new_old == 'n':
        new_username = input('请输入您的新用户名：')
        new_password = input('请输入您的密码：')
        if new_username not in login_username:
            login_username.append(new_username)
            login_password.append(new_password)
            print('注册成功!')
            print('欢迎进入员工资料信息管理系统，欢迎您{}'.format(new_username))
            break
        else:
            print('用户名已存在，请直接选择老用户登陆')
    elif new_old == 'o':
        count = 0
        if count < 3:
            old_username = input('请输入您的用户名：')
            old_password = input('请输入您的密码：')
            if old_username in login_username and old_password in login_password:
                print('登陆成功！')
                print('欢迎进入员工资料信息管理系统，欢迎您{}'.format(old_username))
                break
            else:
                print('登录失败！用户名或密码错误！请重新选择')
            count += 1
        else:
            print('失败已超过三次，请重新选择！')
    else:
        print('输入错误，请重新输入')
while True:
    # 在输入指令之前，你需要先提示都有些什么指令
    op = input('请输入指令：')
    if op == 'add':
        while True:
            userinfo_new = input('请按顺序录入员工信息（姓名、年龄、电话、城市）并按空格键隔开:')
            if len(userinfo_new.split()) == 4:
                if userinfo == []:
                    userinfo_new = userinfo_new.split()
                    userinfo_new.insert(0,1)
                    userinfo.append(userinfo_new)
                    print('已成功添加员工信息！{}'.format(userinfo_new))
                    break
                else:
                    userinfo_new = userinfo_new.split()
                    userinfo_new.insert(0, len(userinfo)+1)
                    userinfo.append(userinfo_new)
                    find_name.append(userinfo_new[1])
                    break
            else:
                print('输入错误请重新输入')
    elif op == 'delete':
        del_list = []
        while True:
            user_name = input('请输入要删除的员工姓名：')
            for user in userinfo:
                if user_name in user:
                    print(user)
                    del_list.append(user[0])
                    user_num = int(input('请确认要删除的员工序号：'))
                    if user_num in del_list:
                        print('已成功删除员工{}'.format(userinfo[user_num-1][1]))
                        userinfo.remove(userinfo[user_num-1])
                        find_name.remove(find_name[user_num-1])
                        break
                    else:
                        print('输入有误,请重新输入')
                else:
                    print('员工姓名输入有误，请重新输入')
    elif op == 'update':
        update_list = []
        while True:
            update_name = input('请输入要修改的员工名称')
            for user in userinfo:
                if update_name in user:
                    print(user)
                    update_list.append(user[0])
                    update_num = int(input('请确认要修改的员工序号：'))
                    if update_num in update_list:
                        update_sub = input('请输入要修改的员工信息(n,a,p,c):')
                        if update_sub == 'n':
                            update_n = input('要改成什么名字：')
                            userinfo[update_num-1][1] = update_n
                            find_name[update_num-1] = update_n
                        elif update_sub == 'a':
                            update_a = int(input('要改成多大年龄：'))
                            if type(update_a) == int and update_a >= 0:
                                userinfo[update_num-1][2] = update_a
                            else:
                                print('输入有误，请重新输入：')
                        elif update_sub == 'f':
                            update_p = int(input('请输入最新的手机号码：'))
                            if type(update_p) == int and len(str(update_p)) == 11:
                                userinfo[update_num - 1][3] = str(update_p)
                            else:
                                print('输入有误，请重新输入：')
                        elif update_sub == 'c':
                            update_c = input('请输入该员工的城市名称：')
                            if type(int(update_c)) != int:
                                userinfo[update_num - 1][4] = str(update_c)
                            else:
                                print('城市名称输入有误，请重新输入：')
                        else:
                            print('修改项目名称输入有误，请重新输入：')
                    else:
                        print('序号输入有误，请重新输入：')
                else:
                    print('没有这个员工，请重新输入：')
    elif op == 'find':
        find_num = input('请输入要查询的员工编号或姓名：')
        if type(int(find_num)) == int:
            if int(find_num) <= len(userinfo):
                print(userinfo[int(find_num)-1])
            else:
                print('超出查找范围，请重新输入')
        elif find_num in find_name:
            find_p = [find_list for find_list in userinfo if find_list[1] == find_num]
            print(find_p)
        else:
            print('输入有误，请输入正确的员工编号或姓名')
    elif op == 'exit':
        break
