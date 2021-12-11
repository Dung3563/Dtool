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
os.system("clear")
rf_acc='https://traodoisub.com/view/cauhinh'
sr="\033[1;31m [\033[1;92m●\033[1;31m]\033[1;97m"
logo = """
\033[1;32m╔═════════════════════════════════════════════════════════╗
\033[1;32m\033[1;96m\033[1;91m  \033[1;95m  [√]Facebook : Dũng Dũng    \033[1;32m   
\033[1;32m \033[1;96m \033[1;91m\033[1;94m  [√]Zalo : 0936485851          \033[1;32m      
\033[1;32m \033[1;96m\033[1;91m\033[0;33m   [√]Tsr : 0936485851        \033[1;32m       
\033[1;32m \033[1;96m\033[1;91m   \033[1;92m[√]Tool tđs python token v1.0          \033[1;32m    
\033[1;32m \033[1;96m\033[1;91m\033[1;97m   [√]Support: Axeyed Kha  \033[1;32m   
\033[1;32m╚═════════════════════════════════════════════════════════"""
vs='================⟩⟩⟩⟩⟩⟩⟩ Vesion 1.0 ⟨⟨⟨⟨⟨⟨================='
def write(z):
  for e in z + '\n':
    sys.stdout.write(e) 
    sys.stdout.flush()
    time.sleep(0.01)
print(logo)
os.system("clear")
print(logo)
print(vs)
h=open('tktds.txt',mode='a+')
h=open('tktds.txt',mode='r')

hung=h.read()
print(sr+'Tài Khoản  : '+hung)
h.close()
k=open('mktds.txt',mode='a+')
k=open('mktds.txt',mode='r')
hai=k.read()
print(sr+'Mật Khẩu : '+hai)
k.close()
hdoi=input(sr+'Bạn Muốn Đổi Tài Khoản TDS Không (y/n) : ')
if hdoi=='y' or hdoi=="Y":
 h=open('tktds.txt',mode='w')
 os.system('clear')
 print(logo)
 tkm=input(sr+'Nhập Tài Khoản TDS Mới : ')
 h.write(tkm)
 h.close()
 k=open('mktds.txt',mode='w')
 mkm=input(sr+'Nhập Mật Khẩu TDS Mới : ')
 k.write(mkm)
 k.close()
 tk=tkm
 mk=mkm
else:
 tk=hung
 mk=hai
rf_login='https://traodoisub.com/home/'
head_login={
'Host':'traodoisub.com',
'accept':'*/*',
'content-length':'28',
'accept':'application/json, text/javascript, */*; q=0.01',
'user-agent':'Mozilla/5.0 (Linux; Android 10; Star 3 Build/QKQ1.200311.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36',
'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
'x-requested-with':'XMLHttpRequest',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://traodoisub.com/',
'accept-encoding':'gzip, deflate',
'accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
}
data_login={
'username':tk,
'password':mk,
}
log=session.post(url='https://traodoisub.com/scr/login.php', headers=head_login, data=data_login).text
if "success" in log:
    print(sr+'Login Thành Công ')
else:
    print(sr+'Login Thất Bại ')
    exit()
sleep(0.2)
reg = log
m = session.cookies.get_dict()
ph = m['PHPSESSID']
cktds='PHPSESSID='+ph
os.system('clear')
print(logo)
print(vs)
head={
'Host':'traodoisub.com',
'accept':'application/json, text/javascript, */*; q=0.01',
'user-agent':'Mozilla/5.0 (Linux; Android 10; Star 3 Build/QKQ1.200311.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36',
'x-requested-with':'XMLHttpRequest',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':rf_login,
'accept-encoding':'gzip, deflate',
'accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie':cktds,
}
check_tk=requests.get(url='https://traodoisub.com/scr/user.php', headers=head)
xu=check_tk.json()['xu']
print(sr+'Username : '+tk)
print(sr+'Xu Hiện Tại : '+xu)
print('-'*60)
while True:
 Token_fb=input(sr+'Nhập Token Facebook : ')
 check_token=json.loads(requests.get('https://graph.facebook.com/me/?access_token='+Token_fb).text)
 try:
    idfb = check_token['id']
    namefb = check_token['name']
    sleep(0.1)
    print(sr+'Token Đúng !!! Chờ Chút 🤧🤧')
    try:
      head_acc={
'Host':'traodoisub.com',
'accept':'application/json, text/javascript, */*; q=0.01',
'user-agent':'Mozilla/5.0 (Linux; Android 10; Star 3 Build/QKQ1.200311.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36',
'x-requested-with':'XMLHttpRequest',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':rf_acc,
'accept-encoding':'gzip, deflate',
'accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie':cktds,
    }
      data_acc={
       "iddat":idfb
      }
      dat_acc=requests.post(url='https://traodoisub.com/scr/datnick.php', headers=head_acc, data=data_acc)
    except:
        idfb = check_token['id']
        print(sr+'Vui Lòng Thêm '+idfb+' Vào Traodoisub')
        exit()
    sleep(0.1)
    break
 except:
    print(sr+'Token Die Hoặc Bị Văng Khỏi Web')
os.system('clear')
print(logo)
print(vs)
print(sr+'Username : '+tk)
print(sr+'Xu Hiện Tại : '+xu)
print('-'*60)
print("\033[1;92m Chạy FB : " + str(namefb) +" | ID " + str(idfb))
print('-'*60)
print(f"{sr}\033[1;92m Nhập [1] Chạy Nhiệm Vụ Like")
print(f"{sr}\033[1;92m Nhập [2] Chạy Nhiệm Vụ Follow")
print(f"{sr}\033[1;92m Nhập [3] Chạy Nhiệm Vụ Comments ( Đang Bảo Trì )")
print(f"{sr}\033[1;92m Nhập [4] Chạy Nhiệm Vụ Share")
print(f"{sr}\033[1;92m Nhập [5] Chạy Nhiệm Vụ Like + Follow")
print(f"{sr}\033[1;92m Nhập [6] Chạy Nhiệm Vụ Like + Follow + Share")
print(f"{sr}\033[1;92m Nhập [7] Chạy Nhiệm Vụ Like + Share")
print("-"*60)
ls=int(input(f"{sr} Nhập Số : "))
delay=int(input(f"{sr} Nhập Delay Job : "))
nvdl=int(input(f"{sr} Sau Bao Nhiêu Nhiệm Vụ Thì Tránh Block: "))
dlnv=int(input(f"{sr} Sau {nvdl} Nhiệm Vụ Nghỉ Bao Nhiêu Giây : "))
if ls==1:
 while True:
    head_job={
'Host':'traodoisub.com',
'accept':'application/json, text/javascript, */*; q=0.01',
'user-agent':'Mozilla/5.0 (Linux; Android 10; Star 3 Build/QKQ1.200311.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36',
'x-requested-with':'XMLHttpRequest',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://traodoisub.com/ex/like/',
'accept-encoding':'gzip, deflate',
'accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie':cktds,
  }
    try:
             get_job=requests.get(url='https://traodoisub.com/ex/like/load.php', headers=head_job)
             id_like=get_job.json()['data'][0]['id']
             urllike='https://graph.facebook.com/'+str(id_like)+'/likes'
             datalike="access_token="+Token_fb
             lam_job_like=requests.post(urllike, data=datalike)
             nhan_like={
'Host':'traodoisub.com',
'accept':'*/*',
'content-length':'28',
'accept':'application/json, text/javascript, */*; q=0.01',
'user-agent':'Mozilla/5.0 (Linux; Android 10; Star 3 Build/QKQ1.200311.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36',
'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
'x-requested-with':'XMLHttpRequest',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://traodoisub.com/ex/like/',
'accept-encoding':'gzip, deflate',
'accept-language':'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
'Cookie':cktds,
             }
             data_nhan={
              "id":id_like,
              "type":"like"
             }
             nhan=requests.post(url='https://traodoisub.com/ex/like/nhantien.php', headers=nhan_like, data=data_nhan).text
             if nhan=='2':
               dem=dem+1
               t=datetime.now().strftime("%H:%M:%S")
               check_tk=requests.get(url='https://traodoisub.com/scr/user.php', headers=head)
               print(f"\033[1;93m[\033[1;93m{dem}\033[1;93m]\033[1;91|\033[1;96m{t}\033[1;91m • \033[1;92mLIKE\033[1;91m •\033[1;96m {id_like} \033[1;91m •\033[1;92m+300\033[1;91m • \033[1;93m{int(check_tk.json()['xu'])}\033[1;91m •")
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
                print(sr+'Có Thể Là Do Hết nv ,Đợi ',a,end='\r')
                sleep(1)