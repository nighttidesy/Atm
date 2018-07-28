#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author heaven

import sys,os,time,json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))
sys.path.append(BASE_DIR)

from shopping import shopping


def account_info():
    with open( BASE_DIR + "/data/.currentuser/.account.txt",'r',encoding='utf-8') as f:
        currentuser = f.read()
        with open( BASE_DIR + "/data/money/" + currentuser + ".txt",'r',encoding='utf-8') as f1:
            currentuserdata = json.load(f1)
            print('当前用户信息如下：\n\n\tuser:{}\n\t当前额度:{}'.format(currentuser,currentuserdata[currentuser]));
    atm_mainpage()

@shopping.login
def atm_mainpage():
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
        print("2")
#        get_money();
    elif your_input == "3":
        print("3")
#        reimbursement();
    elif your_input == "4":
        print("4")
#       transfer_money();
    elif your_input == "5":
        shopping.login_page();

