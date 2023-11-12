import os
try:
	import requests,colorama,prettytable
except:
	os.system("pip install requests")
	os.system("pip install colorama")
	os.system("pip install prettytable")
	os.system("pip install requests")
	os.system("pip install time")
from os import system
import time
import requests

def clear_screen():
    system("clear")

def validate_key(key):
    valid_keys = ["pvdh2304"]
    if key in valid_keys:
        return True
    else:
        return False

clear_screen()

while True:
    haha = print("Tool Được Tạo Bởi Pvdh")
    kaka = print("Nếu Cần Bạn Có Thể Thuê 15k/1 Tháng")
    getkey = print("Link Get Key Bạn Là: https://link4m.com/zOwSyCF")
    hahaha = print("Key Có Thời Hạn 1 Ngày")
    key = input("Vui Lòng Nhập Key: ")
    if validate_key(key):
        break
    else:
        print("Key Không Hợp Lệ. Vui lòng thử lại.")
        time.sleep(1)
clear_screen()

def phone_blocker(phone):
    blocked_numbers = ["0833551113", "0823551113"]
    
    if phone in blocked_numbers:
        print("Địt Mẹ Mày Béo. Dám Spam Số Tao!!!!")
        return False
    
    if not phone.isdigit() or len(phone) != 10:
        print("Vui Lòng Nhập Số Có 10 Chữ Số")

admin = print("Tool Được Tạo Bởi Pvdh")
choice1 = print("1: Để Spam Sms+Call")
choice = input("Vui Lòng Chọn Lệnh Bạn Cần: ")

if choice == "1":
    phone = input("Vui Lòng Nhập Số Điện Thoại Để Spam: ")
    phone_blocker(phone)