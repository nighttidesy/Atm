#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author heaven

import sys,os

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

#login auth
def login(func):
    def login_auth(*args,**kwargs):
        print('{}'.format("1.login\n2.registered new account\n3.exit"));
        your_input = input("请选择: ");
        if your_input == "1":
            print("1");
            func(*args,**kwargs);
        elif your_input == "2":
            print("2");
        elif your_input == "3":
            exit(1);
        else:
            print("input error!");
            login_auth(*args,**kwargs);
    return login_auth

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





