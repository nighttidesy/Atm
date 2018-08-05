#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author heaven

import sys,os,time,json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))
sys.path.append(BASE_DIR)

#import ATM


#shopping list
shoplist = {
"1":{"pen":10},
"2":{"mp3":100},
"3":{"mp4":500},
"4":{"huaweinova":1500},
"5":{"iphon8":5000}
}
yourshoppingcar = {};
amount = 0
#display the Mall homepage.
def show_shoplist():
    print('\n\n\n{0:^30}'.format("Mall homepage"));
    print('{0:^10}{1:13}{2}'.format("number","name","price(元)\n"));
    for i in shoplist:
        for j in shoplist[i]:
            print('{0:^10}{1:13}{2}'.format(i,j,shoplist[i][j]));

#shopping car.
def add_shoppingcar():
    goodsnumber = int(input("Please input the number of the goods: "));
    global amount
    if serial_number in shoplist:
       for i in list(shoplist[serial_number].keys()):
            yourshoppingcar[i] = goodsnumber;
            amount = amount + int(shoplist[serial_number][i]) * goodsnumber;   #当前添加到购物车中物品总价格
            return amount;
    else:
        print('{}'.format("Input error!,Please input agen!"));
        show_shoplist();

#display goodscar.
def show_goodscarlist():
    print('\n\n\n{}'.format("您的购物情况如下："));
    print('{0:^15}{1}'.format("goodsname","number"));
    for i in yourshoppingcar:
        print('{0:^15}{1:^5}'.format(i,yourshoppingcar[i]));

#print logs
def writelogs(logfilename,logcontent):                       #logfilename 日志文件名称,logcontent 日志内容
    with open(BASE_DIR + '/logs/' + logfilename,'a+',encoding='utf-8') as f:
        f.write('{}'.format(time.ctime() + ":  " + logcontent + "\n"));

def user_invoicing(your_account):  #用户选购完商品后结账接口
    print(your_account);
            

#registered new shopping account.
def registered_account():
    print("用户名只能是数字或者字母，密码长度不能小于5位")
    your_account  = str(input("please input account name: ")).strip();
    your_passwd = str(input("please input your passwd: ")).strip();
    fluge = False;
    if your_account.isalnum() and len(your_passwd) > 4:     #判断用户名是否是字母或者数字并且密码长度不能小于5位
        with open(BASE_DIR + "/data/account.txt",'a+',encoding='utf-8') as f,open(BASE_DIR + "/data/money/" + your_account + ".txt",'a+',encoding='utf-8') as f1:             
            if str(os.path.getsize(BASE_DIR + '/data/account.txt')) == "0":               #判断account.txt文件是否为空文件
                datadic = {};                                                 
                moneydic = {};
                datadic[your_account] = your_passwd;                          #将账户名及密码存储到字典
                f.write(json.dumps(datadic));                                 #将添加后字典写入到文件account.txt
                moneydic[your_account] = "20000";                             #每个账户初始给20000额度
                f1.write(json.dumps(moneydic));                               #将添加后字典写入到文件money.txt
                accountlog = '{}用户添加成功！'.format(your_account);         #拼接添加用户成功的日志信息
                writelogs("account.log",accountlog);                          #将日志写入到account.log 文件中
                print(accountlog);                                            #输出添加账户成功日志到屏幕
            else:
                with open(BASE_DIR + "/data/account.txt",'r+',encoding='utf-8') as f,open(BASE_DIR + "/data/account.txt.bak",'w+',encoding='utf-8') as f_new:  
               #这里使用两个文件是为了实现在account.txt中只保留一个字典,由于遇到使用单个文件在添加账户后字典重复添加到account.txt的问题
                    datadic = json.load(f);                                   #反序列化将文件中的内容转化成字符串传给datadic
                    if your_account in datadic:                               #如果账户存在于字典中,重新注册
                        print("account already exists!");
                        registered_account();
                    else:
                        datadic[your_account] = your_passwd;                 #添加新的账户到字典中
                        f_new.write(json.dumps(datadic));                    #序列化字典到文件data/account.txt.bak中
                        os.rename( BASE_DIR + '/data/account.txt', BASE_DIR + '/data/.account.txt.bak')
                        os.rename( BASE_DIR + '/data/account.txt.bak',BASE_DIR + '/data/account.txt')
                        with f,open(BASE_DIR + "/data/money/" + your_account + ".txt",'a+',encoding='utf-8') as f1:
                            moneydic = {};
                            moneydic[your_account] = "20000";
                            f1.write(json.dumps(moneydic));
                        accountlog = '{}用户添加成功！'.format(your_account);         #拼接添加用户成功的日志信息
                        writelogs("account.log",accountlog);                          #将日志写入到account.log 文件中
                        print(accountlog);                                            #输出添加账户成功日志到屏幕

                                    
    else:
        print("您输入的账号或者密码不符合规范！");
        registered_account();

def settlement(your_account,amount):  #供商户调用结算接口    
    with open( BASE_DIR + "/data/account.txt",'r',encoding='utf-8') as f1:  
        userdata = json.load(f1);
        if your_account in userdata:                               #判断对方账户是否存在
            with open( BASE_DIR + "/data/money/" + your_account + ".txt",'r',encoding='utf-8') as f2:
                currentuserdata = json.load(f2);
                if int(currentuserdata[your_account]) - amount < 0:
                    print("老哥,余额不足，别剁手啦。");
                    return(2)
                else:
                    print('您的账户将支付{}元'.format(amount));
                    your_input = input("确认支付，请输入yes|YES,输入其他任意字符视为取消支付。")
                    if your_input == "yes" or your_input == "YES":
                        your_passwd = str(input("please input your passwd: ")).strip();
                        with open( BASE_DIR + "/data/account.txt",'r+',encoding='utf-8') as f3:
                            datadic = json.load(f3);
                            if datadic[your_account] == your_passwd:
                                print("支付进行中。。。。。。") 
                                time.sleep(2)
                                with open( BASE_DIR + "/data/money/" + your_account + ".txt",'r',encoding='utf-8') as f3,open( BASE_DIR + "/data/money/" + your_account + ".txt.new",'w',encoding='utf-8') as f4:
                                    transferdata = json.load(f3); 
                                    transferdata[your_account] = int(transferdata[your_account]) - amount;
                                    f4.write(json.dumps(transferdata))
                                    logcontent = '\n\n恭喜你,成功支付{}元！'.format(amount)
                                    writelogs("account.log",logcontent);
                                    os.rename(BASE_DIR + "/data/money/" + your_account + ".txt",BASE_DIR + "/data/money/" + your_account + ".txt.bak");
                                    os.rename(BASE_DIR + "/data/money/" + your_account + ".txt.new",BASE_DIR + "/data/money/" + your_account + ".txt");
                                    return 0
                            else:
                                print("您的密码不正确！")
                                return 1
                    else:
                        print("您取消了支付");
                        return 1;
        else:
            print("您的账户不存在,请检查您的账户");
            return 1;

		
		
#login auth
def login(func):
    def login_auth(*args,**kwargs):
        global your_account
        your_account  = str(input("please input account name: ")).strip();
        your_passwd = str(input("please input your passwd: ")).strip();
        with open( BASE_DIR + "/data/account.txt",'r+',encoding='utf-8') as f:
            datadic = json.load(f);
            if your_account in datadic and datadic[your_account] == your_passwd:
                print('登录成功 ^-^,{}欢迎你！\n\n'.format(your_account));
                with open( BASE_DIR + "/data/.currentuser/.account.txt",'w+',encoding='utf-8') as f1:
                    f1.write(your_account);
                    func(*args,**kwargs);
            else:
                print("your name or passwd error!");
                login_page();
    return login_auth

#loging page.
def login_page():
    print('{}'.format("1.login\n2.registered new account\n3.exit"));
    your_input = input("请选择: ");
    if your_input == "1":
        main_shopping();
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
        serial_number = input("\n\n输入car,可以查看购物车;\n输入jiezhang，结账;\n输入q退出;\n选择商品号购买商品，请选择: ");
        if serial_number == "car":
            show_goodscarlist();
        elif serial_number == "jiezhang":
            if settlement(your_account,amount) == 0:
                print("恭喜你，购买成功,购物车已经清空。");
                yourshoppingcar = {};
                print(yourshoppingcar)
            else:
              print("购买失败");
        elif serial_number == "q":
            exit();
        else:
            add_shoppingcar();
