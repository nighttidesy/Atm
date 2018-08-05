#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author heaven

import sys,os,time,json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))
sys.path.append(BASE_DIR)

import SHOPPING

@SHOPPING.testh.login
def testa_atm():
	print("atm")

testa_atm()
SHOPPING.testh.test_shop()
