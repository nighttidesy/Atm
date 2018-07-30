#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author heaven

import sys,os,time,json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))
sys.path.append(BASE_DIR)

from shopping import shopping


def account_info():  #corrent user account information. 
    with open( BASE_DIR + "/data/money/" + shopping.your_account + ".txt",'r',encoding='utf-8') as f1:
        currentuserdata = json.load(f1)
        print('当前用户信息如下：\n\n\tuser:{}\n\t当前额度:{}\n\n\n'.format(shopping.your_account,currentuserdata[shopping.your_account]));
        atm_mainpage();

def get_cash():  #用户取现功能
    cash_number = int(input("请输入要取现的金额："))    #获取用户取现金额
    your_passwd = str(input("please input your passwd: ")).strip();       
    with open( BASE_DIR + "/data/account.txt",'r+',encoding='utf-8') as f:
        datadic = json.load(f);
        if  datadic[shopping.your_account] == your_passwd:
            with open( BASE_DIR + "/data/money/" + shopping.your_account + ".txt",'r',encoding='utf-8') as f1,open( BASE_DIR + "/data/money/" + shopping.your_account + ".txt.new",'w',encoding='utf-8') as f2:
                currentuserdata = json.load(f1);
                if int(currentuserdata[shopping.your_account]) - cash_number < 0:   #判断余额是否充足
                    print("\n\n老哥,余额不足。");
                    atm_mainpage();
                else:
                    currentuserdata[shopping.your_account] = int(currentuserdata[shopping.your_account]) - cash_number; #取钱后用户剩余额度
                    print("正在出款，老板请稍等......")
                    time.sleep(2)
                    logcontent = '\n\n恭喜{}，取现 {} 元成功!\n您当前用户的剩余额度为：{}元\n\n\n'.format(shopping.your_account,cash_number,currentuserdata[shopping.your_account])
                    print(logcontent)
                    shopping.writelogs("account.log",logcontent)
                    f2.write(json.dumps(currentuserdata));
                    os.rename(BASE_DIR + "/data/money/" + shopping.your_account + ".txt",BASE_DIR + "/data/money/" + shopping.your_account + ".txt.bak");
                    os.rename(BASE_DIR + "/data/money/" + shopping.your_account + ".txt.new",BASE_DIR + "/data/money/" + shopping.your_account + ".txt");
                    atm_mainpage();
        else:
            print("您输入的密码不正确，请重新输入。");
            get_cash();

@shopping.login
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
        print("3")
#        reimbursement();
    elif your_input == "4":
        print("4")
#       transfer_money();
    elif your_input == "5":
        shopping.login_page();

