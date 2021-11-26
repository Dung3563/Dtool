import time, datetime, requests, json, os, re
try:
    import os, sys, time, datetime, random, requests
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
except ImportError:
    os.system('pip2 install requests')
    os.system('pip install requests')
    time.sleep(1)
#======color======#
d = '\x1b[1;91m'
xl = '\x1b[1;92m'
v = '\x1b[1;93m'
xb = '\x1b[1;96m'
t = '\x1b[1;97m'
vio = '\x1b[1;95m'
#=====Logo && Banner=====#
banner = """
\033[1;92m          ████████╗██████╗ ███████╗
\033[1;93m          ╚══██╔══╝██╔══██╗██╔════╝
\033[1;96m             ██║   ██║  ██║███████╗
\033[1;92m             ██║   ██║  ██║╚════██║
\033[1;93m             ██║   ██████╔╝███████║
\033[1;96m             ╚═╝   ╚═════╝ ╚══════╝
\033[1;97m          Tool TDS 100% Working (Version > Pro)
\033[1;97m          Copyright > AxeyedKha

        ╔═════════════════════════════════════════════╗
        ║\033[1;97m[\033[1;92m+\033[1;97m]Coder    :\033[1;96m Axeyed Kha \033[1;97m                    ║
        ║\033[1;97m[\033[1;92m+\033[1;97m]Github   :\033[93m https://github.com/AXEYEDKHA\033[1;97m   ║
        ║\033[1;97m[\033[1;92m+\033[1;97m]Tools    :\033[1;95m TDS PRO   \033[97m                     ║
        ║\033[1;97m[\033[1;92m+\033[1;97m]Create   :\033[1;91m 03 - 09 - 2021\033[1;97m                 ║
        ╚═════════════════════════════════════════════╝
"""
f = """\033[1;97m=========================================================================="""
#=====Animation=====#
def write(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
#=====Login Tool=====#
def login():
    os.system('clear')
    print(banner)
    print(f)
    write(t+'Get API Key at > https://bitly.com.vn/kx7xqd')
    print(f)
    correctkeyname = 'TDSPRO'
    CorrectPasswordkey = 'axeyedkhatds'
    loop = 'true'
    while loop == 'true':
        username = input('\x1b[1;96m Key Name >> ')
        if username == correctkeyname:
            password = input('\x1b[1;96m Key Password >> ')
            if password == CorrectPasswordkey:
                main_menu()
                loop = 'false'
            else:
                print ('Wrong Key')
        else:
            print ('Wrong Username Key')
#======Menu Tool=====#
def main_menu():
    os.system('clear')
    write(banner)
    print(f)
    write(v+'WELCOME TO MY TOOL. Tool Tds Pro. Token Multithreading')
    print(f)
    write(t+'[1] Folow')
    write(t+'[2] Like')
    write(t+'[3] Comment')
    write(t+'[4] Share')
    write(t+'[5] Reaction')
    write(t+'Exit or Stop Program, Ctrl + Z')
    print(f)
    kali = input(xl+'Choose Option >> ')
    if kali == '1' or kali == '01':
        tool_folow_function()
    elif kali == '2' or kali == '02':
        tool_like_function()
    elif kali == '3' or kali == '03':
        tool_comment_function()
    elif kali == '4' or kali == '04':
        tool_share_function()
    else:
        print(d+'[!] Wrong')
        os.sys.exit()
#====Tool_Main_Funtion=====#
def tool_folow_function():
    os.system('clear')
    print(banner)
    print(f)
    write(xl+'Job You Was Choosed > FOLOW')
    print(f)
    tokentds = input('\033[1;93m Enter Token_TDS Here >>')
    print(f)
    tokenfb = input('\033[1;96m Enter Token FB Here >>')
    log=json.loads(requests.get('https://traodoisub.com/api/?fields=profile&access_token='+tokentds).text)
    if "success" in log:
        user=log['data']['user']
        xu=log['data']['xu']
        print(f)
        print(xl+"Login Succesfully")
    else:
        print(d+"Token Invalid")
        time.sleep(3)
        os.sys.exit()
    print(f)
    write(xl+"Username Traodoisub > "+user)
    write(xb+"Coin in Account Is  > "+xu)
    check_token = json.loads(requests.get('https://graph.facebook.com/me/?access_token='+tokenfb).text)
    if "id" in check_token:
        idfb = check_token['id']
        namefb = check_token['name']
        run = json.loads(requests.get('https://traodoisub.com/api/?fields=run&id='+str(idfb)+'&access_token='+tokentds).text)
        if "success" in run:
            print(f)
            print(xl+'ID FB > '+str(idfb)+' | '+str(namefb)+'')
        else:
            print(d+"Configuration Invalid")
            time.sleep(3)
            os.sys.exit()
    else:
        print(d+"Token Invalid")
        time.sleep(3)
        os.sys.exit()
    print(f)
    write(xl+"Username Traodoisub > "+user)
    write(xb+"Coin in Account Is  > "+xu)
    print(f)
    job=input(v+"Folow TDS [y/n] ")
    print(f)
    dl=int(input(xb+"Time Delay >> "))
    print(f)
    dem=0
    if job=="y" or job == "Y":
        while True:
            t=datetime.datetime.now().strftime("%X")
            dem=dem+1
            getfolow=requests.get('https://traodoisub.com/api/?fields=follow&access_token='+tokentds)
            idfolow=getfolow.json()[0]['id']
            urllike='https://graph.facebook.com/'+str(idfolow)+'/likes'
            datalike="access_token="+tokenfb
            like=requests.post(urllike, data=datalike)
            nhan=json.loads(requests.get('https://traodoisub.com/api/coin/?type=FOLLOW&id='+str(idfolow)+'&access_token='+tokentds).text)
            id=idfolow[0:15]
            if "success" in nhan:
                write(f'\x1b[1;93m ==>[{dem}] >\x1b[1;92m {t} >\x1b[1;96m Folow >\x1b[1;95m {id} >\x1b[1;93m +600 >\x1b[1;94m'+str(nhan['data']['xu'])+" Xu")
                for demtg in range(dl, -1, -1):
                    print(xb+'Processing, Please Wait >   '+str(demtg)+'   ',end='\r')
                    time.sleep(1)
            else:
                print('ERROR'+id,end='\r')
    elif job == 'n' or job == 'N':
        os.sys.exit()
    else:
        print(d+'[!] Wrong')


def tool_like_function():
    os.system('clear')
    print(banner)
    print(f)
    write(xl+'Job You Was Choosed > LIKE')
    print(f)
    tokentds = input('\033[1;93m Enter Token_TDS Here >>')
    print(f)
    tokenfb = input('\033[1;96m Enter Token FB Here >>')
    log=json.loads(requests.get('https://traodoisub.com/api/?fields=profile&access_token='+tokentds).text)
    if "success" in log:
        user=log['data']['user']
        xu=log['data']['xu']
        print(f)
        print(xl+"Login Succesfully")
    else:
        print(d+"Token Invalid")
        time.sleep(3)
        os.sys.exit()
    print(f)
    write(xl+"Username Traodoisub > "+user)
    write(xb+"Coin in Account Is  > "+xu)
    check_token = json.loads(requests.get('https://graph.facebook.com/me/?access_token='+tokenfb).text)
    if "id" in check_token:
        idfb = check_token['id']
        namefb = check_token['name']
        run = json.loads(requests.get('https://traodoisub.com/api/?fields=run&id='+str(idfb)+'&access_token='+tokentds).text)
        if "success" in run:
            print(f)
            print(xl+'ID FB > '+str(idfb)+' | '+str(namefb)+'')
        else:
            print(d+"Configuration Invalid")
            time.sleep(3)
            os.sys.exit()
    else:
        print(d+"Token Invalid")
        time.sleep(3)
        os.sys.exit()
    print(f)
    write(xl+"Username Traodoisub > "+user)
    write(xb+"Coin in Account Is  > "+xu)
    print(f)
    job=input(v+"Like TDS [y/n] ")
    print(f)
    dl=int(input(xb+"Time Delay >> "))
    print(f)
    dem=0
    if job=="y" or job == "Y":
        while True:
            t=datetime.datetime.now().strftime("%X")
            dem=dem+1
            getfolow=requests.get('https://traodoisub.com/api/?fields=like&access_token='+tokentds)
            idfolow=getfolow.json()[0]['id']
            urllike='https://graph.facebook.com/'+str(idfolow)+'/likes'
            datalike="access_token="+tokenfb
            like=requests.post(urllike, data=datalike)
            nhan=json.loads(requests.get('ttps://traodoisub.com/api/coin/?type=LIKE&id='+str(idfolow)+'&access_token='+tokentds).text)
            id=idfolow[0:15]
            if "success" in nhan:
                write(f'\x1b[1;93m ==>[{dem}] >\x1b[1;92m {t} >\x1b[1;96m LIKE >\x1b[1;95m {id} >\x1b[1;93m +300 >\x1b[1;94m'+str(nhan['data']['xu'])+" Xu")
                for demtg in range(dl, -1, -1):
                    print(xb+'Processing, Please Wait >   '+str(demtg)+'   ',end='\r')
                    time.sleep(1)
            else:
                print('ERROR'+id,end='\r')
    elif job == 'n' or job == 'N':
        os.sys.exit()
    else:
        print(d+'[!] Wrong')


def tool_comment_function():
    os.system('clear')
    print(banner)
    print(f)
    write(xl+'Job You Was Choosed > COMMENT')
    print(f)
    tokentds = input('\033[1;93m Enter Token_TDS Here >>')
    print(f)
    tokenfb = input('\033[1;96m Enter Token FB Here >>')
    log=json.loads(requests.get('https://traodoisub.com/api/?fields=profile&access_token='+tokentds).text)
    if "success" in log:
        user=log['data']['user']
        xu=log['data']['xu']
        print(f)
        print(xl+"Login Succesfully")
    else:
        print(d+"Token Invalid")
        time.sleep(3)
        os.sys.exit()
    print(f)
    write(xl+"Username Traodoisub > "+user)
    write(xb+"Coin in Account Is  > "+xu)
    check_token = json.loads(requests.get('https://graph.facebook.com/me/?access_token='+tokenfb).text)
    if "id" in check_token:
        idfb = check_token['id']
        namefb = check_token['name']
        run = json.loads(requests.get('https://traodoisub.com/api/?fields=run&id='+str(idfb)+'&access_token='+tokentds).text)
        if "success" in run:
            print(f)
            print(xl+'ID FB > '+str(idfb)+' | '+str(namefb)+'')
        else:
            print(d+"Configuration Invalid")
            time.sleep(3)
            os.sys.exit()
    else:
        print(d+"Token Invalid")
        time.sleep(3)
        os.sys.exit()
    print(f)
    write(xl+"Username Traodoisub > "+user)
    write(xb+"Coin in Account Is  > "+xu)
    print(f)
    job=input(v+"Comment TDS [y/n] ")
    print(f)
    dl=int(input(xb+"Time Delay >> "))
    print(f)
    dem=0
    if job=="y" or job == "Y":
        while True:
            t=datetime.datetime.now().strftime("%X")
            dem=dem+1
            getfolow=requests.get('https://traodoisub.com/api/?fields=comment&access_token='+tokentds)
            idfolow=getfolow.json()[0]['id']
            urllike='https://graph.facebook.com/'+str(idfolow)+'/likes'
            datalike="access_token="+tokenfb
            like=requests.post(urllike, data=datalike)
            nhan=json.loads(requests.get('https://traodoisub.com/api/coin/?type=COMMENT&id='+str(idfolow)+'&access_token='+tokentds).text)
            id=idfolow[0:15]
            if "success" in nhan:
                write(f'\x1b[1;93m ==>[{dem}] >\x1b[1;92m {t} >\x1b[1;96m Comment >\x1b[1;95m {id} >\x1b[1;93m +600 >\x1b[1;94m'+str(nhan['data']['xu'])+" Xu")
                for demtg in range(dl, -1, -1):
                    print(xb+'Processing, Please Wait >   '+str(demtg)+'   ',end='\r')
                    time.sleep(1)
            else:
                print('ERROR'+id,end='\r')
    elif job == 'n' or job == 'N':
        os.sys.exit()
    else:
        print(d+'[!] Wrong')
    

def tool_share_function():
    os.system('clear')
    print(banner)
    print(f)
    write(xl+'Job You Was Choosed > SHARE')
    print(f)
    tokentds = input('\033[1;93m Enter Token_TDS Here >>')
    print(f)
    tokenfb = input('\033[1;96m Enter Token FB Here >>')
    log=json.loads(requests.get('https://traodoisub.com/api/?fields=profile&access_token='+tokentds).text)
    if "success" in log:
        user=log['data']['user']
        xu=log['data']['xu']
        print(f)
        print(xl+"Login Succesfully")
    else:
        print(d+"Token Invalid")
        time.sleep(3)
        os.sys.exit()
    print(f)
    write(xl+"Username Traodoisub > "+user)
    write(xb+"Coin in Account Is  > "+xu)
    check_token = json.loads(requests.get('https://graph.facebook.com/me/?access_token='+tokenfb).text)
    if "id" in check_token:
        idfb = check_token['id']
        namefb = check_token['name']
        run = json.loads(requests.get('https://traodoisub.com/api/?fields=run&id='+str(idfb)+'&access_token='+tokentds).text)
        if "success" in run:
            print(f)
            print(xl+'ID FB > '+str(idfb)+' | '+str(namefb)+'')
        else:
            print(d+"Configuration Invalid")
            time.sleep(3)
            os.sys.exit()
    else:
        print(d+"Token Invalid")
        time.sleep(3)
        os.sys.exit()
    print(f)
    write(xl+"Username Traodoisub > "+user)
    write(xb+"Coin in Account Is  > "+xu)
    print(f)
    job=input(v+"Share TDS [y/n] ")
    print(f)
    dl=int(input(xb+"Time Delay >> "))
    print(f)
    dem=0
    if job=="y" or job == "Y":
        while True:
            t=datetime.datetime.now().strftime("%X")
            dem=dem+1
            getfolow=requests.get('https://traodoisub.com/api/?fields=share&access_token='+tokentds)
            idfolow=getfolow.json()[0]['id']
            urllike='https://graph.facebook.com/'+str(idfolow)+'/likes'
            datalike="access_token="+tokenfb
            like=requests.post(urllike, data=datalike)
            nhan=json.loads(requests.get('https://traodoisub.com/api/coin/?type=SHARE&id='+str(idfolow)+'&access_token='+tokentds).text)
            id=idfolow[0:15]
            if "success" in nhan:
                write(f'\x1b[1;93m ==>[{dem}] >\x1b[1;92m {t} >\x1b[1;96m Share >\x1b[1;95m {id} >\x1b[1;93m +800 >\x1b[1;94m'+str(nhan['data']['xu'])+" Xu")
                for demtg in range(dl, -1, -1):
                    print(xb+'Processing, Please Wait >   '+str(demtg)+'   ',end='\r')
                    time.sleep(1)
            else:
                print('ERROR'+id,end='\r')


def tool_reaction_funtion():
    os.system('clear')
    print(banner)
    print(f)
    write(xl+'Job You Was Choosed > COMMENT')
    print(f)
    tokentds = input('\033[1;93m Enter Token_TDS Here >>')
    print(f)
    tokenfb = input('\033[1;96m Enter Token FB Here >>')
    log=json.loads(requests.get('https://traodoisub.com/api/?fields=profile&access_token='+tokentds).text)
    if "success" in log:
        user=log['data']['user']
        xu=log['data']['xu']
        print(f)
        print(xl+"Login Succesfully")
    else:
        print(d+"Token Invalid")
        time.sleep(3)
        os.sys.exit()
    print(f)
    write(xl+"Username Traodoisub > "+user)
    write(xb+"Coin in Account Is  > "+xu)
    check_token = json.loads(requests.get('https://graph.facebook.com/me/?access_token='+tokenfb).text)
    if "id" in check_token:
        idfb = check_token['id']
        namefb = check_token['name']
        run = json.loads(requests.get('https://traodoisub.com/api/?fields=run&id='+str(idfb)+'&access_token='+tokentds).text)
        if "success" in run:
            print(f)
            print(xl+'ID FB > '+str(idfb)+' | '+str(namefb)+'')
        else:
            print(d+"Configuration Invalid")
            time.sleep(3)
            os.sys.exit()
    else:
        print(d+"Token Invalid")
        time.sleep(3)
        os.sys.exit()
    print(f)
    write(xl+"Username Traodoisub > "+user)
    write(xb+"Coin in Account Is  > "+xu)
    print(f)
    job=input(v+"Comment TDS [y/n] ")
    print(f)
    dl=int(input(xb+"Time Delay >> "))
    print(f)
    dem=0
    if job=="y" or job == "Y":
        while True:
            t=datetime.datetime.now().strftime("%X")
            dem=dem+1
            getfolow=requests.get('https://traodoisub.com/api/?fields=comment&access_token='+tokentds)
            idfolow=getfolow.json()[0]['id']
            urllike='https://graph.facebook.com/'+str(idfolow)+'/likes'
            datalike="access_token="+tokenfb
            like=requests.post(urllike, data=datalike)
            nhan=json.loads(requests.get('https://traodoisub.com/api/coin/?type=COMMENT&id='+str(idfolow)+'&access_token='+tokentds).text)
            id=idfolow[0:15]
            if "success" in nhan:
                write(f'\x1b[1;93m ==>[{dem}] >\x1b[1;92m {t} >\x1b[1;96m Comment >\x1b[1;95m {id} >\x1b[1;93m +600 >\x1b[1;94m'+str(nhan['data']['xu'])+" Xu")
                for demtg in range(dl, -1, -1):
                    print(xb+'Processing, Please Wait >   '+str(demtg)+'   ',end='\r')
                    time.sleep(1)
            else:
                print('ERROR'+id,end='\r')
    elif job == 'n' or job == 'N':
        os.sys.exit()
    else:
        print(d+'[!] Wrong')
#=====Exit=====#
def exit():
    print(banner)
    print(f)
    print(xl+'Thank You was Used My tool')
#=====Important_Main=====#
login()
#=====Axeyedkha=====#