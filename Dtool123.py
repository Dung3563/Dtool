import time, datetime, requests, json, os, re
d = '\x1b[1;91m'
xl = '\x1b[1;92m'
v = '\x1b[1;93m'
xb = '\x1b[1;96m'
t = '\x1b[1;97m'
vio = '\x1b[1;95m'
f = """------------------------------------------------------------"""
banner = """
\033[1;96m██████╗  [•] Copyright Axeyed Kha (có của Dũng nữa :))
\033[1;92m██╔══██╗ [•] Tool tính đủ thứ trên đời :v
\033[1;95m██║  ██║ [•] Facebook: Dũng Dũng
\033[1;92m██║  ██║ [•] Phiên bản v1.0
\033[1;96m██████╔╝ [•] Zalo: 0936485851
\033[1;97m╚═════╝  [•] Chúc các bạn dùng tool vui vẻ
"""
def write(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
def login():
    os.system('clear')
    print(banner)
    print(f)
    print('key test')
    print(xl+'namekey: Dtool')
    print(xl+'passkey: v1.0')
    print(f)
    correctkeyname = 'Dtool'
    CorrectPasswordkey = 'v1.0'
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
def main_menu():
  os.system('clear')
  print(banner) 
  print(f) 
  print(v+'Chào mừng bạn tới tool tds token của mình(v1.0 nên còn sơ suất, mình sẽ update nhiều) ')
  print(f) 
  print(t+'[1]Like') 
  print(t+'[2]Follow')
  print(t+'[3]Cmt(bảo trì) ')
  print(t+'[4]Share(bảo trì) ')
  time.sleep(1)
  print(f)
  dung = input(xb+'Chọn chế độ: ')
  if dung == '1' or dung == '01':
    tool_like_function()
  elif dung == '2' or dung == '02':
    tool_follow_function()
  elif dung == '3' or dung == '03':
    tool_comment_function()
  elif dung == '4' or dung == '04':
    tool_share_function()
  else:
    print(d+"Nhập sai")
    time.sleep(3)
    os.system('clear')
def tool_like_function():
    os.system('clear')
    print(banner) 
    print(f) 
    print(v+'[√]Job bạn chọn: Like')
    print(f) 
    tokentds = input('\033[1;93m Enter Token_TDS Here >>')
    print(f)
    tokenfb = input('\033[1;96m Enter Token FB Here >>')
    time.sleep(1)
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
    print(v+'Tên tài khoản:'+user)
    print(v+'Xu trong tài khoản:'+xu) 
    check_token = json.loads(requests.get('https://graph.facebook.com/me/?access_token='+tokenfb).text)
    if "id" in check_token:
        idfb = check_token['id']
        namefb = check_token['name']
        run = json.loads(requests.get('https://traodoisub.com/api/?fields=run&id='+str(idfb)+'&access_token='+tokentds).text)
        if "success" in run:
            print(f)
            print(xl+'ID FB: '+str(idfb)+' | '+str(namefb)+'')
        else:
            print(d+"Nhập lỗi!")
            time.sleep(3)
            os.sys.exit()
    else:
        print(d+"Token lỗi! ")
        time.sleep(3)
        os.sys.exit()
    print(f)
    print(xl+"Tên tài khoản: "+user)
    print(xb+"Xu trong tài khoản: "+xu)
    print(f)
    job=input(v+"Like TDS [y/n] ")
    print(f) 
    dem=0
    if job == 'y' or job == 'Y':
      while True:
            t=datetime.datetime.now().strftime("%X")
            dem=dem+1
            getlike=requests.get('https://traodoisub.com/api/?fields=like&access_token='+tokentds)
            idlike=getlike.json()[0]['id']
            urllike='https://graph.facebook.com/'+str(idlike)+'/likes'
            datalike="access_token="+tokenfb
            like=requests.post(urllike, data=datalike)
            nhan=json.loads(requests.get('https://traodoisub.com/api/coin/?type=LIKE&id='+str(idlike)+'&access_token='+tokentds).text)
            id=idlike[0:15]
            if "success" in nhan:
                write(f'\x1b[1;93m ==>[{dem}] >\x1b[1;92m {t} >\x1b[1;96m Like >\x1b[1;95m {id} >\x1b[1;93m +300 >\x1b[1;94m'+str(nhan['data']['xu'])+" Xu")
                for demtg in range(dl, -1, -1):
                    print(xb+'Đang chạy, xin đợi:   '+str(demtg)+'   ',end='\r')
                    time.sleep(1)
            else:
                print('Lỗi'+id,end='\r')
    elif job == 'n' or job == 'N':
        os.sys.exit()
    else:
        print(d+'[!] Lỗi!! ')
def tool_follow_function():
    os.system('clear')
    print(banner) 
    print(f) 
    print(v+'Job bạn chọn: Follow')
    print(f) 
    tokentds = input(xb+'Nhập token tds: ')
    tokenfb = input(xb+'Nhập token fb: ')
    log=json.loads(requests.get('https://traodoisub.com/api/?fields=profile&access_token='+tokentds).text) 
    if "success" in log:
        user=log['data']['user']
        xu=log['data']['xu']
        print(f) 
        print(vio+'Đăng nhập thành công! ')
        time.sleep(1)
    else:
        print(d+'Token sai! ')
        time.sleep(1)
        os.system('clear')
    print(f)
    print(xl+"Tên tài khoản: "+user)
    print(xb+"Xu trong tài khoản: "+xu)
    print(f)
    job=input(v+"Follow TDS [y/n] ")
    print(f) 
    dem=0
    if job == 'y' or job == 'Y':
      while True:
            t=datetime.datetime.now().strftime("%X")
            dem=dem+1
            getlike=requests.get('https://traodoisub.com/api/?fields=follow&access_token='+tokentds)
            idfollow=getfollow.json()[0]['id']
            urllike='https://graph.facebook.com/'+str(idlike)+'/likes'
            datalike="access_token="+tokenfb
            like=requests.post(urllike, data=datalike)
            nhan=json.loads(requests.get('https://traodoisub.com/api/coin/?type=FOLLOW&id='+str(idlike)+'&access_token='+tokentds).text)
            id=idlike[0:15]
            if "success" in nhan:
                write(f'\x1b[1;93m ==>[{dem}] >\x1b[1;92m {t} >\x1b[1;96m Follow >\x1b[1;95m {id} >\x1b[1;93m +600 >\x1b[1;94m'+str(nhan['data']['xu'])+" Xu")
                for demtg in range(dl, -1, -1):
                    print(xb+'Đang chạy, xin đợi:   '+str(demtg)+'   ',end='\r')
                    time.sleep(1)
            else:
                print('Lỗi'+id,end='\r')
    elif job == 'n' or job == 'N':
        os.sys.exit()
    else:
        print(d+'[!] Lỗi!! ')
def exit():
    print(banner)
    print(f)
    print(xl+'Cảm ơn đã dùng tool của tôi')
login()
            
    