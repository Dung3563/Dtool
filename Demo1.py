import requests
import os, sys, json, re
from time import sleep
session = requests.Session()
import os, sys, re, json
from time import sleep
import random
from datetime import datetime
import requests 
dem=0
stop=1
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
def menu():
  os.system('clear')
  print(banner) 
  write(f) 
  write("chào mừng tới tool tds token v1.0 by Dũng")
  print(xb+"mời chọn 1 job để chạy ")
  print(f) 
  time.sleep(0.1)
  write("[1]Like")
  write("[2]Follow")
  nhap = input("nhập job muốn chạy: ")
  if nhap == '1' or nhap == '01':
    tool_like_function()
  elif nhap == '2' or nhap == '02':
    tool_follow_function()
  else:
    print(d+"Nhập sai!")
    time.sleep(3)
    os.system('clear')
#tool Like 
def tool_like_function():
  os.system('clear')
  print(banner)
  print(f)
  print(v+"Job bạn chọn: Like")
  tokentds = input(vio+"nhập token TDS: ")
  tokenfb = input(vio+"Nhập token FB: ")
  time.sleep(1)
  log = json.loads(requests.get('https://traodoisub.com/api/?fields=profile&access_token='+tokentds).text)
  if 'success'in log:
    user=log['data']['user']
    xu=log['data']['xu']
    print(f) 
    print(xl+"Đăng nhập thành công")
  else:
    print(d+"Nhập sai")
    os.system('clear')
  print(f) 
  write(v+"Tên tài khoản: "+user)
  write(v+"Xu trong tài khoản: "+xu)
  print(f) 
  dl=int(input(xb+"Time Delay >> "))
  check_token = json.loads(requests.get('https://graph.facebook.com/me/?access_token='+tokenfb).text)
  if "id" in check_token:
        idfb = check_token['id']
        namefb = check_token['name']
        run = json.loads(requests.get('https://traodoisub.com/api/?fields=run&id='+str(idfb)+'&access_token='+tokentds).text)
        if "success" in run:
            print(f)
            print(xl+'Đang cấu hình id: '+str(idfb)+' | '+str(namefb)+'')
        else:
            print(d+"Nhập lỗi!")
            time.sleep(3)
            os.sys.exit()
  else:
        print(d+"Token lỗi! ")
        time.sleep(3)
        os.sys.exit()
  print(f)
  dem=0
  t=datetime.datetime.now().strftime("%X")
  dem=dem+1 
  while True:
    getlike=requests.get('https://traodoisub.com/api/?fields=like&access_token='+tokentds)
    
    idlike=getlike.json()[0]['id']
    urllike='https://graph.facebook.com/'+str(idlike)+'/likes'
    datalike="access_token="+tokenfb
    like=requests.post(urllike, data=datalike)
    nhan=json.loads(requests.get('https://traodoisub.com/api/coin/?type=LIKE&id='+str(idlike)+'&access_token='+tokentds).text)
    id=idlike[0:15]
    if "success" in nhan:
                print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mLIKE\033[1;97m]\033[1;92m {id_like} \033[1;97m[\033[1;92m+300\033[1;97m] \033[1;97m[\033[1;92m{int(check_tk.json()['xu'])}\033[1;97m]")
               if dem==stop*nvdl:
                                    stop+=1
                                    for demtg in range(dlnv, -1,-1):
                                        print(" [-]  Đang Delay Tránh Block ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [\]  Đang Delay Tránh Block ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [|]  Đang Delay Tránh Block ",demtg,end='\r')
                                        sleep(0.25)
                                        print(" [/]  Đang Delay Tránh Block ",demtg,end='\r')
                                        sleep(0.25)
               if delay==0:
                print('            ',end='\r')
               else:
                            for demtg in range(delay, -1, -1):
                                print(" [-]  Đang Delay ",demtg,end='\r')
                                sleep(0.25)
                                print(" [\]  Đang Delay ",demtg,end='\r')
                                sleep(0.25)
                                print(" [|]  Đang Delay ",demtg,end='\r')
                                sleep(0.25)
                                print(" [/]  Đang Delay ",demtg,end='\r')
                                sleep(0.25)
             else:
              t=datetime.now().strftime("%H:%M:%S")
              print(f"\033[1;97m[\033[1;92m{dem}\033[1;97m] [\033[1;92m{t}\033[1;97m] [\033[1;92mLIKE\033[1;97m]\033[1;92m {id_like}",end=' \r')
              sleep(2)
    except:
            for a in range(5, -1, -1):
                print(sr+'Có Thể Là Do Hết nv ,Đơi ',a,end='\r')
                sleep(1)
#tool follow
def tool_follow_function():
  os.system('clear')
  print(banner) 
  print(f) 
  print(v+"Job bạn chọn: Follow")
  tokentds = input(vio+"nhập token TDS: ")
  tokenfb = input(vio+"Nhập token FB: ")
  time.sleep(1)
  log = json.loads(requests.get('https://traodoisub.com/api/?fields=profile&access_token='+tokentds).text)
  if 'success'in log:
    user=log['data']['user']
    xu=log['data']['xu']
    print(xl+"Đăng nhập thành công!! ")
  else:
    print(d+"Lỗi token")
    os.system('clear')
  write(v+"Tên tài khoản: "+user) 
  write(v+"Xu trong tài khoản: "+xu) 
  print(f) 
  dl=int(input(xb+"Time Delay >> "))
  check_token = json.loads(requests.get('https://graph.facebook.com/me/?access_token='+tokenfb).text)
  if "id" in check_token:
        idfb = check_token['id']
        namefb = check_token['name']
        run = json.loads(requests.get('https://traodoisub.com/api/?fields=run&id='+str(idfb)+'&access_token='+tokentds).text)
        if "success" in run:
            print(f)
            print(xl+'Đang cấu hình id: '+str(idfb)+' | '+str(namefb)+'')
        else:
            print(d+"Nhập lỗi!")
            time.sleep(3)
            os.sys.exit()
  else:
        print(d+"Token lỗi! ")
        time.sleep(3)
        os.sys.exit()
  print(f)
  dem=0
  t=datetime.datetime.now().strftime("%X")
  dem=dem+1 
  while True:
    getfollow=requests.get('https://traodoisub.com/api/?fields=follow&access_token='+tokentds) 
    idfollow=getfollow.json()[0]['id']
    urlfollow='https://graph.facebook.com/'+str(idfollow)+'/likes'
    datafollow="access_token="+tokenfb
    follow=requests.post(urlfollow, data=datafollow)
    nhan=json.loads(requests.get('https://traodoisub.com/api/coin/?type=FOLLOW&id='+str(idfollow)+'&access_token='+tokentds).text)
    id=idfollow[0:15]
    if "success" in nhan:
                write(f'\x1b[1;93m ==>[{dem}] >\x1b[1;92m {t} >\x1b[1;96m Folow >\x1b[1;95m {id} >\x1b[1;93m +600 >\x1b[1;94m'+str(nhan['data']['xu'])+" Xu")
                for demtg in range(dl, -1, -1):
                    print(xb+'Làm job tiếp sau -->   '+str(demtg)+'   ',end='\r')
                    time.sleep(1)
    else:
        print(d+'Lỗi '+id,end='\r')
menu()
  