import sys,os,time,json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0])))
sys.path.append(BASE_DIR)

#import ATM

def test_shop():
    print("shopping")
	
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
