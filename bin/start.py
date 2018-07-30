#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author heaven

import sys,os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))
sys.path.append(BASE_DIR)

from shopping  import shopping
from atm  import atm

while True:
    os.system('clear')
    print("willcome to my first application".center(75))
    print("\n\n\t1.begin shopping!\n\n\t2. Atm\n\n\tq.退出\n")
    choice_1 = str(input("请输入你的选择:  "))
    if choice_1 == "1":
        shopping.login_page();
        break
    elif choice_1 == "2":
        atm.atm_wellcome_page();
        break
    elif choice_1 == "q":
        break
    else:
        print("您的输入有误,请重新输入")
