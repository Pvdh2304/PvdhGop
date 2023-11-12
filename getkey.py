import random
from atexit import register
from time import sleep
import os,json,re,sys
import threading,base64
import os,time,re,json,random
from datetime import datetime
from time import sleep,strftime
import requests
os.system("clear")
dau="\033[1;31m[\033[1;37m×.×\033[1;31m] \033[1;37m➩"
banner = f"""\033[1;32m
\033[1;36m          ██████╗ ██╗   ██╗██████╗ ██╗  ██╗
\033[1;35m          ██╔══██╗██║   ██║██╔══██╗██║  ██║
\033[1;33m          ██████╔╝██║   ██║██║  ██║███████║
\033[1;31m          ██╔═══╝ ╚██╗ ██╔╝██║  ██║██╔══██║
\033[1;37m          ██║      ╚████╔╝ ██████╔╝██║  ██║
\033[1;32m          ╚═╝       ╚═══╝  ╚═════╝ ╚═╝  ╚═╝
\033[1;31m────────────────────────────────────────────────────────────
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;33mVUI LÒNG GETKEY
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> ADMIN: \033[1;36mPê Vê Đê Hắt
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> Telegram: \033[1;36m@pvdh2304
\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mBOX SUPPORT: \033[1;37mhttps://zalo.me/g/ehvwqu714
\033[1;31m────────────────────────────────────────────────────────────
"""
for h in banner:
       sys.stdout.write(h)
       sys.stdout.flush()
       sleep(0.0003)

ngay=int(strftime('%d'))
key1=str(ngay*1246881818+2888181472) 
key = 'Pvdh'+key1
keyv1 = 'Key Víp Tùy Chỉnh'

api_url = f"https://link4m.co/api-shorten/v2?api=6513ea0e5fff14347929b322&url=https://pvdh.vinaddns.com/key/key?key={key}"

response = requests.get(api_url)
result = json.loads(response.text)

if result["status"] != 'success':
    print(result["message"])

link_key = result["shortenedUrl"]

h = open('pvdh.txt', mode='a+')
h = open('pvdh.txt', mode='r')
thien = h.read()
h.close()
print()
if thien== keyv1 or thien== key:
    exec(requests.get('https://raw.githubusercontent.com/Pvdh2304/PvdhGop/main/main.py').text)
else:
     print('\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ')
     print(dau,'\033[1;32mKEY CÓ THỜ HẠN LÀ 1 NGÀY.SAU 1 NGÀY KEY SẼ RESET')
     print('\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ')
print(dau,'\033[1;33mLINK LẤY KEY LÀ:\033[1;31m '+link_key)
print('\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ')
keynhap = input('\033[1;31m[\033[1;37m×.×\033[1;31m] \033[1;37m➩ \033[1;32mNHẬP KEY VỪA GETKEY CỦA BẠN VÀO\033[1;33m ~>\033[1;36m ')
print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
if keynhap == key or keynhap== keyv1:
    print(dau,'\033[1;32mKEY ĐÚNG ĐANG MỞ TOOL !')
    print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
    sleep(2)
    h=open('pvdh.txt',mode='w')
    h.write(keynhap)
    h.close()
    exec(requests.get('https://raw.githubusercontent.com/Pvdh2304/PvdhGop/main/main.py').text)
else:
    print(dau,'\033[1;33m KEY SAI !')
    print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
    
