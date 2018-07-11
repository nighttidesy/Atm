#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author heaven

import sys,os,time,json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))
sys.path.append(BASE_DIR)


#shopping list
shoplist = {
"1":{"pen":10},
"2":{"mp3":100},
"3":{"mp4":500},
"4":{"huaweinova":1500},
"5":{"iphon8":5000}
}
yourshoppingcar = {};
#display the Mall homepage.
def show_shoplist():
    print('{0:^30}'.format("Mall homepage"));
    print('{0:^10}{1:13}{2}'.format("number","name","price\n"));
    for i in shoplist:
        for j in shoplist[i]:
            print('{0:^10}{1:13}{2}'.format(i,j,shoplist[i][j]));

#shopping car.
def add_shoppingcar():
    goodsnumber = input("Please input the number of the goods: ");
    if serial_number in shoplist:
       for i in list(shoplist[serial_number].keys()):
            yourshoppingcar[i] = goodsnumber;
        
    else:
        print('{}'.format("Input error!,Please input agen!"));
        show_shoplist();

#display goodscar.
def show_goodscarlist():
    print('{}'.format("您的购物情况如下："));
    print('{0:^15}{1}'.format("goodsname","number"));
    for i in yourshoppingcar:
        print('{0:^15}{1:^5}'.format(i,yourshoppingcar[i]));

#print logs
def writelogs(logfilename,logcontent):                       #logfilename 日志文件名称,logcontent 日志内容
    with open(BASE_DIR + '/logs/' + logfilename,'a+',encoding='utf-8') as f:
        f.write('{}'.format(time.ctime() + ":  " + logcontent + "\n"));
            

#registered new shopping account.
def registered_account():
    print("用户名只能是数字或者字母，密码长度不能小于5位")
    your_account  = str(input("please input account name: ")).strip();
    your_passwd = str(input("please input your passwd: ")).strip();
    fluge = False;
    if your_account.isalnum() and len(your_passwd) > 4:     #判断用户名是否是字母或者数字并且密码长度不能小于5位
        with open("data/account.txt",'a+',encoding='utf-8') as f:             
            if str(os.path.getsize('data/account.txt')) == "0":               #判断account.txt文件是否为空文件
                datadic = {};                                                 
                datadic[your_account] = your_passwd;                          #将账户名及密码存储到字典
                f.write(json.dumps(datadic));                                 #将添加后字典写入到文件account.txt
                accountlog = '{}用户添加成功！'.format(your_account);         #拼接添加用户成功的日志信息
                writelogs("account.log",accountlog);                          #将日志写入到account.log 文件中
                print(accountlog);                                            #输出添加账户成功日志到屏幕
            else:
                with open("data/account.txt",'r+',encoding='utf-8') as f,open("data/account.txt.bak",'w+',encoding='utf-8') as f_new:       #这里使用两个文件是为了实现在account.txt中只保留一个字典,由于遇到使用单个文件在添加账户后字典重复添加到account.txt的问题
                    datadic = json.load(f);                                   #反序列化将文件中的内容转化成字符串传给datadic
                    if your_account in datadic:                               #如果账户存在于字典中,重新注册
                        print("account already exists!");
                        registered_account();
                    else:
                        datadic[your_account] = your_passwd;                 #添加新的账户到字典中
                        f_new.write(json.dumps(datadic));                    #序列化字典到文件data/account.txt.bak中
                        os.rename('data/account.txt','data/.account.txt.bak')
                        os.rename('data/account.txt.bak','data/account.txt')
                        accountlog = '{}用户添加成功！'.format(your_account);         #拼接添加用户成功的日志信息
                        writelogs("account.log",accountlog);                          #将日志写入到account.log 文件中
                        print(accountlog);                                            #输出添加账户成功日志到屏幕

                                    
    else:
        print("您输入的账号或者密码不符合规范！");
        registered_account();


#login auth
def login(func):
    def login_auth(*args,**kwargs):
        your_account  = str(input("please input account name: ")).strip();
        your_passwd = str(input("please input your passwd: ")).strip();
        
        func(*args,**kwargs);
    return login_auth

#loging page.
def login_page():
    print('{}'.format("1.login\n2.registered new account\n3.exit"));
    your_input = input("请选择: ");
    if your_input == "1":
        print("1");
    elif your_input == "2":
        registered_account();
        login_page();
    elif your_input == "3":
        exit(1);
    else:
        print("input error!");

#main shopping program.
@login
def main_shopping():
    while True:
        show_shoplist();
        global serial_number;
        serial_number = input("Please choice the goods serial number(输入car,可以查看购物车): ");
        if serial_number == "car":
            show_goodscarlist();
        else:
            add_shoppingcar();






