import requests,os,time,re,json,uuid,random,sys
from concurrent.futures import ThreadPoolExecutor
# lấy dữ liệu người dùng
ban = """\033[1;96m
         
        © Coppyright: Pê Vê Đê Hắt


          ██████╗ ██╗   ██╗██████╗ ██╗  ██╗
          ██╔══██╗██║   ██║██╔══██╗██║  ██║
          ██████╔╝██║   ██║██║  ██║███████║
          ██╔═══╝ ╚██╗ ██╔╝██║  ██║██╔══██║
          ██║      ╚████╔╝ ██████╔╝██║  ██║
          ╚═╝       ╚═══╝  ╚═════╝ ╚═╝  ╚═╝

   

          -----!! TOOL GỘP VIP BY PVDH!!-----
\033[1;34m
#====================================================
# ⚜Admin:Pê Vê Đê Hắt
# ⚜Telegram : @pvdh2304
# ⚜Zalo: zalo.me/pvdhdeptrai123
# ⚜Website: https://pvdhdeptrai.vietnamdev.link/
# ⚜  --  Chúc Bạn Sử Dụng Tool Vui Vẻ  --
#====================================================
"""
def banner():
  os.system("clear")
  for h in ban:
    sys.stdout.write(h)
    sys.stdout.flush()
    time.sleep(0.003)    
banner()
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33m  Auto Roblox    \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m1\033[1;31m] \033[1;32mTool Auto + \033[1;32mRoblox ")
print("\033[1;31m────────────────────────────────────────────────────────────")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║  \033[1;33m  Tool AUTO TDS    \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m2\033[1;31m] \033[1;32mTool Auto Tds TikTok ")
print("\033[1;37m╔═════════════════════╗")
print("\033[1;37m║    \033[1;33m  Tool Khác      \033[1;37m║")
print("\033[1;37m╚═════════════════════╝")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m3\033[1;31m] \033[1;32mTool Buff View TikTok ")
print("\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;31m[\033[1;33m4\033[1;31m] \033[1;32mTool Spam Mess ")
print("\033[1;31m────────────────────────────────────────────────────────────")

chon = int(input('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Số \033[1;37m: \033[1;33m'))
if chon == 1 :
	exec(requests.get('https://raw.githubusercontent.com/Pvdh2304/PvdhGop/main/rejoinpvdh.py').text)
if chon == 2 :
	exec(requests.get('https://raw.githubusercontent.com/Pvdh2304/PvdhGop/main/TDS%20TIKTOK.py').text)
if chon == 3 :
	exec(requests.get('https://raw.githubusercontent.com/Pvdh2304/PvdhGop/main/view.py').text)
if chon == 4 :
	exec(requests.get('https://raw.githubusercontent.com/Pvdh2304/PvdhGop/main/Spam%20Mess.py').text)
else :
	exit()
