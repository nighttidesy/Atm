#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author heaven

import sys,os,time,json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))
sys.path.append(BASE_DIR)


import SHOPPING

def account_info():  #corrent user account information. 
    with open( BASE_DIR + "/data/money/" + SHOPPING.shopping.your_account + ".txt",'r',encoding='utf-8') as f1:
        currentuserdata = json.load(f1)
        print('当前用户信息如下：\n\n\tuser:{}\n\t当前额度:{}\n\n\n'.format(SHOPPING.shopping.your_account,currentuserdata[SHOPPING.shopping.your_account]));
        atm_mainpage();

def get_cash():  #用户取现功能
    cash_number = int(input("请输入要取现的金额："))    #获取用户取现金额
    your_passwd = str(input("please input your passwd: ")).strip();       
    with open( BASE_DIR + "/data/account.txt",'r+',encoding='utf-8') as f:
        datadic = json.load(f);
        if  datadic[SHOPPING.shopping.your_account] == your_passwd:
            with open( BASE_DIR + "/data/money/" + SHOPPING.shopping.your_account + ".txt",'r',encoding='utf-8') as f1,open( BASE_DIR + "/data/money/" + SHOPPING.shopping.your_account + ".txt.new",'w',encoding='utf-8') as f2:
                currentuserdata = json.load(f1);
                if int(currentuserdata[SHOPPING.shopping.your_account]) - cash_number < 0:   #判断余额是否充足
                    print("\n\n老哥,余额不足。");
                    atm_mainpage();
                else:
                    currentuserdata[SHOPPING.shopping.your_account] = int(currentuserdata[SHOPPING.shopping.your_account]) - cash_number; #取钱后用户剩余额度
                    print("正在出款，老板请稍等......")
                    time.sleep(2)
                    logcontent = '\n\n恭喜{}，取现 {} 元成功!\n您当前用户的剩余额度为：{}元\n\n\n'.format(SHOPPING.shopping.your_account,cash_number,currentuserdata[SHOPPING.shopping.your_account])
                    print(logcontent)
                    SHOPPING.shopping.writelogs("account.log",logcontent)
                    f2.write(json.dumps(currentuserdata));
                    os.rename(BASE_DIR + "/data/money/" + SHOPPING.shopping.your_account + ".txt",BASE_DIR + "/data/money/" + SHOPPING.shopping.your_account + ".txt.bak");
                    os.rename(BASE_DIR + "/data/money/" + SHOPPING.shopping.your_account + ".txt.new",BASE_DIR + "/data/money/" + SHOPPING.shopping.your_account + ".txt");
                    atm_mainpage();
        else:
            print("您输入的密码不正确，请重新输入。");
            get_cash();

def also_cash(): #用户还款功能
    cash_number = int(input("请输入要还款的金额："))    #获取用户还款金额
    your_passwd = str(input("please input your passwd: ")).strip();
    with open( BASE_DIR + "/data/account.txt",'r+',encoding='utf-8') as f:
        datadic = json.load(f);
        if  datadic[SHOPPING.shopping.your_account] == your_passwd:
            with open( BASE_DIR + "/data/money/" + SHOPPING.shopping.your_account + ".txt",'r',encoding='utf-8') as f1,open( BASE_DIR + "/data/money/" + SHOPPING.shopping.your_account + ".txt.new",'w',encoding='utf-8') as f2:
                currentuserdata = json.load(f1);
                currentuserdata[SHOPPING.shopping.your_account] = int(currentuserdata[SHOPPING.shopping.your_account]) + cash_number;  #还款后额度
                print("正在还款，老板请稍等......")
                time.sleep(2)
                logcontent = '\n\n恭喜{}，还款 {} 元成功!\n您当前用户的剩余额度为：{}元\n\n\n'.format(SHOPPING.shopping.your_account,cash_number,currentuserdata[SHOPPING.shopping.your_account]);
                print(logcontent)
                SHOPPING.shopping.writelogs("account.log",logcontent)
                f2.write(json.dumps(currentuserdata));
                os.rename(BASE_DIR + "/data/money/" + SHOPPING.shopping.your_account + ".txt",BASE_DIR + "/data/money/" + SHOPPING.shopping.your_account + ".txt.bak");
                os.rename(BASE_DIR + "/data/money/" + SHOPPING.shopping.your_account + ".txt.new",BASE_DIR + "/data/money/" + SHOPPING.shopping.your_account + ".txt");
                atm_mainpage();
        else:
            print("您输入的密码不正确，请重新输入。");
            also_cash();

def transfer_money():  #用户转账功能
    transfer_user = str(input("请输入对方用户账号: "));
    transfer_number = int(input("请输入要转账的金额："));
    with open( BASE_DIR + "/data/account.txt",'r',encoding='utf-8') as f1:
        userdata = json.load(f1);
        if transfer_user in userdata:                  #判断对方账户是否存在
            with open( BASE_DIR + "/data/money/" + SHOPPING.shopping.your_account + ".txt",'r',encoding='utf-8') as f1:
                currentuserdata = json.load(f1);
                if int(currentuserdata[SHOPPING.shopping.your_account]) - transfer_number < 0:
                    print("老哥,余额不足。");
                    atm_mainpage();
                else:
                    with open( BASE_DIR + "/data/money/" + SHOPPING.shopping.your_account + ".txt",'r',encoding='utf-8') as f3,open( BASE_DIR + "/data/money/" + SHOPPING.shopping.your_account + ".txt.new",'w',encoding='utf-8') as f4:
                        currentuserdata = json.load(f3);
                        currentuserdata[SHOPPING.shopping.your_account] = int(currentuserdata[SHOPPING.shopping.your_account]) - transfer_number;  #转款方剩余额度
                        f4.write(json.dumps(currentuserdata));                                                               #将变更后的金额存到txt.new文件中
                        print("转账中。。。。。。")
                        time.sleep(2)
                        logcontent = '\n\n{}用户成功向{}用户转账{}元，当前额度为{}'.format(SHOPPING.shopping.your_account,transfer_user,transfer_number,currentuserdata[SHOPPING.shopping.your_account])  #日志信息
                        print(logcontent)
                        SHOPPING.shopping.writelogs("account.log",logcontent)
                        os.rename(BASE_DIR + "/data/money/" + SHOPPING.shopping.your_account + ".txt",BASE_DIR + "/data/money/" + SHOPPING.shopping.your_account + ".txt.bak");
                        os.rename(BASE_DIR + "/data/money/" + SHOPPING.shopping.your_account + ".txt.new",BASE_DIR + "/data/money/" + SHOPPING.shopping.your_account + ".txt");
                        with open( BASE_DIR + "/data/money/" + transfer_user + ".txt",'r',encoding='utf-8') as f5,open( BASE_DIR + "/data/money/" + transfer_user + ".txt.new",'w',encoding='utf-8') as f6:  #转入方录入额度
                            transferdata = json.load(f5);
                            transferdata[transfer_user] = int(transferdata[transfer_user]) + transfer_number;  #转入方转入资金后额度
                            f6.write(json.dumps(transferdata))
                            logcontent = '{}用户成功向您的账户{}转账{}元'.format(SHOPPING.shopping.your_account,transfer_user,transfer_number)
                            SHOPPING.shopping.writelogs("account.log",logcontent)
                            os.rename(BASE_DIR + "/data/money/" + transfer_user + ".txt",BASE_DIR + "/data/money/" + transfer_user + ".txt.bak");
                            os.rename(BASE_DIR + "/data/money/" + transfer_user + ".txt.new",BASE_DIR + "/data/money/" + transfer_user + ".txt");
                        atm_mainpage();
 
                
        else:
            logcontent = '转账失败，{}账号不存在!.format(transfer_user)'
            print(logcontent)
            SHOPPING.shopping.writelogs("account.log",logcontent)
            atm_mainpage();
    



@SHOPPING.shopping.login
def atm_wellcome_page():   #atm进入后显示页面
    while True:
        print('{0:^30}'.format("WILLCOME  TO  ATM!\n  祝老板使用愉快"))
        pagecontent = '''
        输入1进入主功能界面
        输入q退出 
    
    '''
        print('{}'.format(pagecontent));
        your_input = str(input("Please input your choice:  ")).strip();
        if your_input == "1":
            atm_mainpage();
        elif your_input == "q":
            break;
        else:
            print("您的输入有误！请重新选择。")  




def atm_mainpage():  #atm主功能界面
    print('{0:^30}'.format("WILLCOME  TO  ATM!\n"))
    atmpagecontent = '''
    1。查看当前账户信息。
    2。取现。
    3. 还款。
    4. 转账。
    5. 退出登录


'''
    print('{}'.format(atmpagecontent))
    your_input = str(input("Please input your choice:  ")).strip()    
    if your_input == "1":
        print("1")
        account_info();
    elif your_input == "2":
        get_cash();
    elif your_input == "3":
        also_cash();
    elif your_input == "4":
       transfer_money();
    elif your_input == "5":
        SHOPPING.shopping.login_page();


