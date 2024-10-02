# Code By Alexander Axl Montreal
# Facebook Boost By Alexander Axl Montreal
# Facebook By Alexander Axl Montreal
# Tool Owner KAREN-BOOST




# ────────────────[Imports]─────────────────
import lzma
import zlib
import codecs
import base64
_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));

import requests
import re
import uuid
import random
import os
import time
import threading
import json
import base64
import platform
import logging
from datetime import datetime
from time import sleep
import random
import json
import requests
import uuid
import string
import base64
import urllib
import urllib3
import re
import os
import time
import sys
from datetime import datetime
from urllib.request import urlopen
from time import sleep as slp
import re
import requests
import json
import json


import requests
import re
import os
from bs4 import BeautifulSoup as bs
import random
import urllib3
import random
from atexit import register
from time import sleep
import os,json,re,sys
import threading,base64
import os,time,re,json,random
from datetime import datetime
from time import sleep,strftime
import requests
from time import sleep
from concurrent.futures import ThreadPoolExecutor
import threading 
from concurrent.futures import ThreadPoolExecutor as loda
from bs4 import BeautifulSoup
import requests
from time import strftime

def check_install_requests():
    try:
        import requests
    except ModuleNotFoundError:
        os.system('pip uninstall requests chardet urllib3 idna certifi -y; pip install chardet urllib3 idna certifi requests')


check_install_requests()
# ────────────────[USERAGENT]─────────────────
def W_ueragnt():
    chrome_version = random.randint(80, 99)
    webkit_version = random.randint(500, 599)
    safari_version = random.randint(400, 499)
    windows_version = random.randint(8, 10)
    is_win64 = random.choice([
        True,
        False])
    if is_win64:
        if not 'WOW64;':
            user_agent = f'''Mozilla/5.0 (Windows NT {windows_version}.{''}Win64; x64) AppleWebKit/{webkit_version}.0 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/{safari_version}.0'''
            return user_agent

headers = {
    'user-agent': W_ueragnt(),
    'viewport-width': '847',
    'x-asbd-id': '129477',
    'x-fb-friendly-name': 'GroupCometJoinForumMutation',
    'x-fb-lsd': 'wGh6ACr3OJ2v2rPBdXy-1o' }
headersccc = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'viewport-width': '546',
    'x-asbd-id': '129477',
    'x-fb-friendly-name': 'CometProfilePlusLikeMutation',
    'x-fb-lsd': 'KA9qtqSd7hV8150DnYqqmy' }
# ────────────────[Gitpull]─────────────────

try:
    os.system('clear')
    print("\033[1;36mCHECKING UPDATES....")
    time.sleep(5)
    os.system("git pull > /dev/null 2>&1")
except:
    pass
    
# ────────────────[Colours]─────────────────
red = '\033[1;91m'
ye = '\033[1;93m'
blue = '\033[1;94m'
mage = '\033[1;95m'
cyan = '\033[1;96m'
c = '\033[1;96m'
w = '\033[1;97m'
wh = '\033[1;97m'
reset = '\033[0m'
r = '\033[0m'
redd = '\x1b[1;31m'
green = '\x1b[1;32m'
yellow = '\x1b[1;33m'
bluee = '\x1b[1;34m'
cyann = '\x1b[1;36m'
white = '\x1b[1;37m'
black = '\x1b[1;30m'
magenta = '\x1b[1;35m'
grey = '\x1b[1;90m'
orange = '\x1b[1;91m'
lime = '\x1b[1;92m'
sky_blue = '\x1b[1;94m'
purple = '\x1b[1;95m'
turquoise = '\x1b[1;96m'
# ────────────────[Logo]─────────────────

logo = (f''' 
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
       \033[1;96m   ╦╔═╔═╗╦═╗╔═╗╔╗╔   ╔╗ ╔═╗╔═╗╔═╗╔╦╗
       \033[1;96m   ╠╩╗╠═╣╠╦╝║╣ ║║║───╠╩╗║ ║║ ║╚═╗ ║ 
       \033[1;97m   ╩ ╩╩ ╩╩╚═╚═╝╝╚╝   ╚═╝╚═╝╚═╝╚═╝ ╩  {c}「{red}V•2{c}」{r} 
        {r} 「OWNER    : ALEXANDER  AXL MONTREAL」{r} 
        {r} 「FACEBOOK : ALEXANDER  AXL MONTREAL」{r} 
        {r} 「TOOLTYPE : FACEBOOK BOOST PHILIPPINE」{r}
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ \n''')



# ────────────────[Linex]─────────────────

def linex():
    print(f'  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

# ────────────────[Clear]─────────────────
def clear():
    os.system('clear')
    print(logo)
    
    
# ────────────────[Create Direc]─────────────────


import os

folder_name = "/sdcard/KAREN-BOOST"
file_names = ["toka.txt", "tokaid.txt", "tokp.txt", "tokpid.txt", "cok.txt", "cokid.txt"]


if not os.path.exists(folder_name):
    try:
        os.makedirs(folder_name)
        print(f"FOLDER '{folder_name}' CREATED.")
    except Exception as e:
        print(f"FAILED TO CREATE FOLDER '{folder_name}': {e}")
else:
    print(f"FOLDER '{folder_name}' ALREADY EXISTS.")


for file_name in file_names:
    file_path = os.path.join(folder_name, file_name)
    if not os.path.exists(file_path):  
        try:
            with open(file_path, 'w') as file:
                pass  
            print(f"FILE '{file_path}' CREATED.")
        except Exception as e:
            print(f"FAILED TO CREATE FILE '{file_path}': {e}")
    else:
        print(f"FILE '{file_path}' ALREADY EXISTS.")
        
# ────────────────[Setup - Data]─────────────────

def setup_user_data():
    os.makedirs("data", exist_ok=True)
    
    def create_file_if_not_exists(file_path):
        if not os.path.exists(file_path):
            open(file_path, "w").close()
    
    create_file_if_not_exists("data/namekar.xml")
    create_file_if_not_exists("data/passwordkar.xml")
    create_file_if_not_exists("data/agekar.xml")
    create_file_if_not_exists("data/locationkar.xml")


    
    def get_user_input(file_path, prompt_message):
        if os.path.getsize(file_path) > 0:
            with open(file_path, "r") as file_obj:
                return file_obj.readline().strip()
        else:
            user_input = input(prompt_message)
            with open(file_path, "w") as file_obj:
                file_obj.write(user_input)
            return user_input
    
    clear()
    uname = get_user_input("data/namekar.xml", f"  {c}     「{r}•{c}」{r}  ENTER YOUR NAME » ")
    upass = get_user_input("data/passwordkar.xml", f" {c}     「{r}•{c}」{r}   ENTER YOUR PASSWORD » ")

    uage = get_user_input("data/agekar.xml", f" {c}     「{r}•{c}」{r}   ENTER YOUR AGE » ")

    ulocation = get_user_input("data/locationkar.xml", f" {c}     「{r}•{c}」{r}   ENTER YOUR LOCATION » ")

setup_user_data()

# ────────────────[User-Name-Age-Location]─────────────────

def get_user_name():
    with open("data/namekar.xml", "r") as file_obj:
        return file_obj.readline().strip()

def get_user_password():
    with open("data/passwordkar.xml", "r") as file_obj:
        return file_obj.readline().strip()

def get_user_age():
    with open("data/agekar.xml", "r") as file_obj:
        return file_obj.readline().strip()

def get_user_location():
    with open("data/locationkar.xml", "r") as file_obj:
        return file_obj.readline().strip()
# ────────────────[Approval]─────────────────

user_id = str(os.geteuid())
user_name = get_user_name()
uuid = f"{user_id}BERSBOOATING{user_id}"
key = f"{user_name}-KAREN-BOOST-{uuid}"

def get_approval_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def approval():
    clear()
    try:
        user_id = str(os.geteuid())
        user_name = get_user_name()
        uuid = f"{user_id}BERSBOOATING{user_id}"
        key = f"{user_name}-KAREN-BOOST-{uuid}"

        clear()
        print("\033[1;37m [\u001b[36m•\033[1;37m] YOU NEED APPROVAL TO USE THIS TOOL   \033[1;37m")
        print("\033[1;37m [\u001b[36m•\033[1;37m] I AIN'T RESPONSIBLE IF ANYTHING HAPPENS WHILE YOU TRY TO BYPASS.  \033[1;37m")
        print(f"\033[1;37m [\u001b[36m•\033[1;37m] YOUR KEY :\u001b[36m {key}")
        linex()

        urls = [
            "https://github.com/ALEXANDERAXLMONTREAL/06f27/blob/main/5.txt",
            "https://github.com/ALEXANDERAXLMONTREAL/06f27/blob/main/6.txt",
            "https://github.com/ALEXANDERAXLMONTREAL/06f27/blob/main/7.txt",
            "https://github.com/ALEXANDERAXLMONTREAL/06f27/blob/main/8.txt"
        ]
        
        key_found = False
        for url in urls:
            approval_data = get_approval_data(url)
            
            if key in approval_data:
                key_found = True
                break

        if key_found:
            print(f"\033[1;97m >> YOUR KEY HAS BEEN APPROVED!!!")
            time.sleep(3)
            return key
        else:
            print("\x1b[1;97m >> SEND IF YOU WANT TO PURCHASE! ")
            time.sleep(0.1)
            input(' >> CLICK ENTER TO SEND YOUR KEY ')
            os.system('xdg-open https://www.facebook.com/AlexanderAxlMontreal.IAmLimitless')
            time.sleep(1)
            exit()
    except requests.RequestException as e:
        logging.error(f"UNABLE TO FETCH DATA FROM SERVER.")
        return logging.error
        print(f" >> UNABLE TO FETCH DATA FROM SERVER.")
        time.sleep(2)
        exit()
    except Exception as e:
        logging.error(f"AN UNEXPECTED ERROR OCCURRED.")
        return logging.error
        print(f" >> AN UNEXPECTED ERROR OCCURRED.")
        time.sleep(2)
        exit()

# ────────────────[Count line]─────────────────

def count_lines(file_path):
   
    try:
        with open(file_path, 'r') as file:
            return sum(1 for line in file)
    except FileNotFoundError:
        return 0

# ────────────────[PSB to post ID]─────────────────

def linktradio(post_link):
    def extract_postid_from_link(post_link):
        pattern = r'https://www\.facebook\.com/\d+/posts/(\d+)/?'
        match = re.match(pattern, post_link)
        if match:
            return match.group(1)
        else:
            return None

    def convert_to_traodoisub(url):
        try:
            response = requests.post('https://id.traodoisub.com/api.php', data={'link': url})
            if response.status_code == 200:
                result = response.json().get('id')
                return result
            else:
                return None
        except Exception as e:
            print(f'AN ERROR OCCURRED: {e}')
            return None

    if re.search(r'/posts/\d+', post_link):
        post_id = extract_postid_from_link(post_link)
        if post_id:
            return post_id
    elif 'pfbid' in post_link:
        post_id = convert_to_traodoisub(post_link)
        if post_id:
            return post_id

    return 'INVALID LINK FORMAT OR UNABLE TO PROCESS THE LINK.'

# ────────────────[START TOOL]─────────────────
def start_tool():
    clear()
    print(f'''{yellow}  [1] {cyan}EXTRACT NORMAL ACCOUNT PAGES     {yellow}-  {green}[UID AND PASSWORD]''')
    print(f'''{yellow}  [2] {cyan}EXTRACT SINGLE NORMAL ACCOUNT    {yellow}-  {green}[NO DUPLICATE CHECKER]''')
    print(f'''{yellow}  [3] {cyan}EXTRACT BULK NORMAL ACCOUNTS M1  {yellow}-  {green}[THRU TXT FILE]''')
    print(f'''{yellow}  [4] {cyan}EXTRACT BULK NORMAL ACCOUNTS M2  {yellow}-  {green}[THRU TXT FILE]''')
    print(f'''{yellow}  [5] {cyan}EXTRACT BULK ACCOUNTS PAGES      {yellow}-  {green}[THRU TXT FILE]''')
    print(f'''{yellow}  [0] {red}RETURN TO MAIN MENU''')
    linex()
    choice = input(f'''{yellow}  CHOOSE : {green}''')
    if choice == '1':
        get_facebook_pages()
        return None
    if None == '2':
        get_facebook_account()
        return None
    if None == '3':
        bgraph_bulk_account()
        return None
    if None == '4':
        datr()
        return None
    if None == '5':
        bgraph_bulk_pages()
        return None
    if None == '0':
        menu()
        return None
    None(f'''{red}  INVALID CHOICE. PLEASE PICK A NUMBER FROM 1 TO 6.''')
# ────────────────[NOT ONE]─────────────────
def get_facebook_pages():
    ses = requests.Session()
    clear()
    print(f'''{green}  METHOD 1 {white}---> {yellow}KAREN-BOOST NORMAL ACCOUNT PAGES''')
    linex()
    ids = input(f'''{yellow}ENTER FACEBOOK ID: {green}''')
    linex()
    pas = input(f'''{yellow}ENTER FACEBOOK PASSWORD: {green}''')
    linex()
    fbav = f'''{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'''
    fbbv = str(random.randint(111111111, 999999999))
    fbrv = '0'
    random_seed = random.Random()
    adid = str(''.join(random_seed.choices(string.hexdigits, k = 16)))
    ua_bgraph = f'''[FBAN/FB4A;FBAV/{str(random.randint(49, 66))}.0.0.{str(random.randrange(20, 49))}{str(random.randint(11, 99))};FBBV/{str(random.randint(11111111, 77777777))};[FBAN/FB4A;FBAV/{fbav};FBPN/com.facebook.katana;FBLC/pt_BR;FBBV/{fbbv};FBCR/CLARO BR;FBMF/Xiaomi;FBBD/Redmi;FBDV/M1908C3JGG;FBSV/11;FBCA/arm64-v8a:null;FBDM/{{density=2.75,width=1080,height=2216}};FB_FW/1;FBRV/470765339;] FBBK/1'''
    data = {
        'locale': 'en_SV',
        'client_country_code': 'SV',
        'fb_api_req_friendly_name': 'authenticate',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
        'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32' }
    head = {
        'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32' }
    url = 'https://graph.facebook.com/auth/login'
    po = requests.post(url, data = data, headers = head).json()
    if 'session_key' in po:
        poo = po.get('access_token', '')
        token = str(poo)
        cookie = po.get('session_cookies', [])()
        return get_facebook_pages_with_token(token)
    if Exception:
        e = 'True'
        print(f'''ERROR: {e}''')
        e = None
        del e
        e = None
        del e

import requests
import random
import string
import uuid

def get_facebook_account():
    clear()
    print(f'''{green}  METHOD 2 {white}---> {yellow}KAREN-BOOST SINGLE NORMAL ACCOUNT''')
    linex()
    print(f'''{white}  CHOOSE WHERE TO SAVE:''')
    print(f'''{yellow}  [1] {blue}ON YOUR FRA LIST''')
    print(f'''{yellow}  [2] {blue}ON YOUR RPA LIST''')
    print(f'''{yellow}  [3] {blue}ON YOUR FRA PAGES LIST''')
    print(f'''{yellow}  [4] {blue}ON YOUR RPA PAGES LIST''')
    print(f'''{red}  [0] {red}RETURN''')
    linex()
    account_choose = input(f'''{yellow}  CHOOSE : {green}''')
    linex()
    if account_choose == '1':
        path_file = '/sdcard/.KAREN-BOOST-TOKEN-FRA-ACCOUNT.txt'
        check_path = '/sdcard/.KAREN-BOOST-TOKEN-FRA-ACCOUNT-NAME-ID.txt'
    if account_choose == '2':
        path_file = '/sdcard/.KAREN-BOOST-TOKEN-RP-ACCOUNT.txt'
        check_path = '/sdcard/.KAREN-BOOST-TOKEN-RP-ACCOUNT-NAME-ID.txt'
    if account_choose == '3':
        path_file = '/sdcard/.KAREN-BOOST-TOKEN-FRA-PAGES.txt'
        check_path = '/sdcard/.KAREN-BOOST-TOKEN-FRA-PAGES-NAME-ID.txt'
    if account_choose == '4':
        path_file = '/sdcard/.KAREN-BOOST-TOKEN-RP-PAGES.txt'
        check_path = '/sdcard/.KAREN-BOOST-TOKEN-RP-PAGES-NAME-ID.txt'
    if account_choose == '0':
        start_tool()
        return None
    None('INVALID CHOICE')
    return None
    uid = input(f'''{yellow}ENTER FACEBOOK ID: {green}''')
    linex()
    pas = input(f'''{yellow}ENTER FACEBOOK PASSWORD: {green}''')
    linex()
    fbav = f'''{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'''
    fbbv = str(random.randint(111111111, 999999999))
    fbrv = '0'
    random_seed = random.Random()
    adid = ''.join(random_seed.choices(string.hexdigits, k = 16))
    ua_bgraph = '[FBAN/FB4A;FBAV/' + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ';FBBV/' + str(random.randint(11111111, 77777777)) + ';' + '[FBAN/FB4A;FBAV/' + fbav + ';FBBV/' + fbbv + ';FBDM/{density=3.0,width=1080,height=2107};FBLC/fr_FR;FBRV/' + fbrv + ';FBCR/Ooredoo TN;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1M;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]'
    data = {
        'locale': 'en_SV',
        'client_country_code': 'SV',
        'fb_api_req_friendly_name': 'authenticate',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
        'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32' }
    head = {
        'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32' }
    url = 'https://graph.facebook.com/auth/login'
    po = requests.post(url, headers = head, data = data).json()
    if 'session_key' in po:
        cookie = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
        poo = po.get('access_token', '')
        token = str(poo)
        open('/sdcard/.KAREN-BOOST-COOKIE-ACCOUNT-NAME-ID.txt', 'a').write('')
        print(f'''  {white}ID : {yellow}{uid} {white}---> {green}SUCCESSFULLY EXTRACT!''')
        open(check_path, 'a').write(uid + '\n')
        open(path_file, 'a').write('%s\n' % poo)
    print(f'''  {red}ID : {red}{uid} {white}---> {red} FAILED TO EXTRACT!''')
    if Exception:
        e = ';'.join
        print(f'''{red}AN ERROR OCCURRED!''')
        e = None
        del e
        e = None
        del e

ok = []
checkpoint = []
loop = 0
import uuid
import requests
import random
import sys
from concurrent.futures import ThreadPoolExecutor as thread

def bgraph_bulk_account():
    clear()
    print(f'''{green}  METHOD 3 {white}---> {yellow}KAREN-BOOST BULK NORMAL ACCOUNTS M1''')
    print(f'''{red}  FILE FORMAT : {green}uid|password''')
    linex()
    print(f'''{white}  CHOOSE WHERE TO SAVE:''')
    print(f'''{yellow}  [1] {blue}ON YOUR FRA LIST''')
    print(f'''{yellow}  [2] {blue}ON YOUR RPA LIST''')
    print(f'''{yellow}  [3] {blue}ON YOUR FRA PAGES LIST''')
    print(f'''{yellow}  [4] {blue}ON YOUR RPA PAGES LIST''')
    print(f'''{red}  [0] {red}RETURN''')
    linex()
    account_choose = input(f'''{yellow}  CHOOSE : {green}''')
    linex()
    if account_choose == '1':
        open('/sdcard/.KAREN-BOOST-TOKEN-FRA-ACCOUNT.txt', 'a').write('')
        open('/sdcard/.KAREN-BOOST-TOKEN-FRA-ACCOUNT-NAME-ID.txt', 'a').write('')
        path_file = '/sdcard/.KAREN-BOOST-TOKEN-FRA-ACCOUNT.txt'
        check_path = '/sdcard/.KAREN-BOOST-TOKEN-FRA-ACCOUNT-NAME-ID.txt'
    if account_choose == '2':
        open('/sdcard/.KAREN-BOOST-TOKEN-RP-ACCOUNT.txt', 'a').write('')
        open('/sdcard/.KAREN-BOOST-TOKEN-RP-ACCOUNT-NAME-ID.txt', 'a').write('')
        path_file = '/sdcard/.KAREN-BOOST-TOKEN-RP-ACCOUNT.txt'
        check_path = '/sdcard/.KAREN-BOOST-TOKEN-RP-ACCOUNT-NAME-ID.txt'
    if account_choose == '3':
        open('/sdcard/.KAREN-BOOST-TOKEN-FRA-PAGES.txt', 'a').write('')
        open('/sdcard/.KAREN-BOOST-TOKEN-FRA-PAGES-NAME-ID.txt', 'a').write('')
        path_file = '/sdcard/.KAREN-BOOST-TOKEN-FRA-PAGES.txt'
        check_path = '/sdcard/.KAREN-BOOSTKAREN-BOOST-TOKEN-FRA-PAGES-NAME-ID.txt'
    if account_choose == '4':
        open('/sdcard/.KAREN-BOOST-TOKEN-RP-PAGES.txt', 'a').write('')
        open('/sdcard/.KAREN-BOOST-TOKEN-RP-PAGES-NAME-ID.txt', 'a').write('')
        path_file = '/sdcard/.KAREN-BOOST-TOKEN-RP-PAGES.txt'
        check_path = '/sdcard/.KAREN-BOOST-TOKEN-RP-PAGES-NAME-ID.txt'
    if account_choose == '0':
        start_tool()
        return None
    None('INVALID CHOICE')
    return None
    filee = input(f'''{yellow}INPUT FILE PATH : {green}''')
    linex()
    fo = open(filee, 'r').read().splitlines()
    if FileNotFoundError:
        print(f'''{red}FILE NOT FOUND''')
        slp(5)
        menu()
    cook = thread(max_workers = 30)
    for i in fo:
        (uid, pw) = i.split('|')
        cook.submit(graph, uid, pw, path_file, check_path)
        None(None, None)
        return None
        if not None:
            pass


def graph(uid, pw, path_file, check_path):
    global loop
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    data = {
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32' }
    simm3 = random.choice([
        'GLOBE',
        'SMART'])
    headers = '62f8ce9f74b12f84c123cc23437a4a32'
    url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
    po = requests.post(url, headers = headers, data = data).json()
    if 'session_key' in po:
        cookie = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
        poo = po.get('access_token', '')
        token = str(poo)
        open('/sdcard/.KAREN-BOOST-COOKIE-ACCOUNT-NAME-ID.txt', 'a').write('')
        if uid in open(check_path, 'r').read():
            print(f'''{red}  ACCOUNT ALREADY EXIST IN TOOL{yellow}---> {red}{uid}''')
            linex()
        print(f'''  {white}ID : {yellow}{uid} {white}---> {green}SUCCESSFULLY EXTRACT!''')
        linex()
        open(check_path, 'a').write(uid + '\n')
        open(path_file, 'a').write('%s\n' % poo)
        ok.append(uid)
    if Exception:
        e = ';'.join
        print(f'''{red}AN ERROR OCCURRED!''')
        e = None
        del e
        e = None
        del e
    loop += 1


def get_facebook_pages_with_token3(uid, poo, path_file, check_path):
    url = 'https://graph.facebook.com/v18.0/me/accounts'
    headers = {
        'Authorization': f'''Bearer {poo}''' }
    response = requests.get(url, headers = headers)
    if response.status_code != 200:
        print(f'''  {red}ACCOUNT : {red}{uid} {white}---> {red}FAILED!''')
        linex()
        return None
    data = None.json()
    pages_data = data['data']()
    total_accounts = 0
    new_accounts = 0
    print(f'''  {white}ACCOUNT : {yellow}{uid}{white} ---> TOTAL PAGES KAREN-BOOST: ''', end = ' ')
    file = open(check_path, 'r')
    existing_pages = file.readlines()
    existing_page_ids = existing_pages()
    None(None, None)
    lines = [
        "token1|value1",
        "token2|value2",
    ]

    tokens = [line.strip().split('|')[0] for line in lines]

    pages = [
        {"access_token": "token1", "id": "1", "name": "Page One"},
        {"access_token": "token2", "id": "2", "name": "Page Two"},
    ]

    page_info = [{
        'accessToken': page['access_token'],
        'id': page['id'],
        'name': page['name']
    } for page in pages]

    print(tokens)
    print(page_info)

    if FileNotFoundError:
        existing_page_ids = set()
    for page in pages_data:
        pages_access_token = page['accessToken']
        pages_name = page['name']
        pages_id = page['id']
        if pages_id in existing_page_ids:
            print(f'''\n{red}  PAGES ALREADY EXIST IN TOOL{yellow}---> {red}''' + pages_id + '|' + pages_name)
        new_accounts += 1
        total_accounts += 1
        file = open(check_path, 'a')
        file.write(pages_id + '|' + pages_name + '\n')
        None(None, None)
        if not None:
            pass
        if Exception:
            e = None
            print(f'''{red}ERROR WRITING: {e}''')
            e = None
            del e
            e = None
            del e
        file = open(path_file, 'a')
        file.write(pages_access_token + '\n')
        None(None, None)
        if not None:
            pass
        if Exception:
            e = None
            print(f'''{red}ERROR WRITING: {e}''')
            e = None
            del e
            e = None
            del e
        print(f'''{green}[{total_accounts}]''')
        linex()
        return pages_data


def bgraph_bulk_pages():
    clear()
    print(f'''{green}  METHOD 5 {white}---> {yellow}KAREN-BOOST BULK ACCOUNTS PAGES''')
    print(f'''{red}  FILE FORMAT : {green}uid|password''')
    linex()
    print(f'''{white}  CHOOSE WHERE TO SAVE:''')
    print(f'''{yellow}  [1] {blue}ON YOUR FRA LIST''')
    print(f'''{yellow}  [2] {blue}ON YOUR RPA LIST''')
    print(f'''{yellow}  [3] {blue}ON YOUR FRA PAGES LIST''')
    print(f'''{yellow}  [4] {blue}ON YOUR RPA PAGES LIST''')
    print(f'''{red}  [0] {red}RETURN''')
    linex()
    account_choose = input(f'''{yellow}  CHOOSE : {green}''')
    linex()
    if account_choose == '1':
        open('/sdcard/.KAREN-BOOST-TOKEN-FRA-ACCOUNT.txt', 'a').write('')
        open('/sdcard/.KAREN-BOOST-TOKEN-FRA-ACCOUNT-NAME-ID.txt', 'a').write('')
        path_file = '/sdcard/.KAREN-BOOST-TOKEN-FRA-ACCOUNT.txt'
        check_path = '/sdcard/.KAREN-BOOST-TOKEN-FRA-ACCOUNT-NAME-ID.txt'
    if account_choose == '2':
        open('/sdcard/.KAREN-BOOST-TOKEN-RP-ACCOUNT.txt', 'a').write('')
        open('/sdcard/.KAREN-BOOST-TOKEN-RP-ACCOUNT-NAME-ID.txt', 'a').write('')
        path_file = '/sdcard/.KAREN-BOOST-TOKEN-RP-ACCOUNT.txt'
        check_path = '/sdcard/.KAREN-BOOST-TOKEN-RP-ACCOUNT-NAME-ID.txt'
    if account_choose == '3':
        open('/sdcard/.KAREN-BOOST-TOKEN-FRA-PAGES.txt', 'a').write('')
        open('/sdcard/.KAREN-BOOST-TOKEN-FRA-PAGES-NAME-ID.txt', 'a').write('')
        path_file = '/sdcard/.KAREN-BOOST-TOKEN-FRA-PAGES.txt'
        check_path = '/sdcard/.KAREN-BOOST-TOKEN-FRA-PAGES-NAME-ID.txt'
    if account_choose == '4':
        open('/sdcard/.KAREN-BOOST-TOKEN-RP-PAGES.txt', 'a').write('')
        open('/sdcard/.KAREN-BOOST-TOKEN-RP-PAGES-NAME-ID.txt', 'a').write('')
        path_file = '/sdcard/.KAREN-BOOST-TOKEN-RP-PAGES.txt'
        check_path = '/sdcard/.KAREN-BOOST-TOKEN-RP-PAGES-NAME-ID.txt'
    if account_choose == '0':
        start_tool()
        return None
    None('Invalid choice')
    return None
    linex()
    filee = input(f'''{yellow}INPUT FILE PATH : {green}''')
    linex()
    fo = open(filee, 'r').read().splitlines()
    if FileNotFoundError:
        print(f'''{red}FILE NOT FOUND''')
        slp(5)
        menu()
    cook = thread(max_workers = 30)
    for i in fo:
        (uid, pw) = i.split('|')
        cook.submit(graph2, uid, pw, path_file, check_path)
        None(None, None)
        return None
        if not None:
            pass

def graph4(uid, pw, path_file, check_path):
    fbav = f'''{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'''
    fbbv = str(random.randint(111111111, 999999999))
    fbrv = '0'
    random_seed = random.Random()
    adid = ''.join(random_seed.choices(string.hexdigits, k = 16))
    ua_bgraph = '[FBAN/FB4A;FBAV/' + str(random.randint(49, 66)) + '.0.0.' + str(random.randrange(20, 49)) + str(random.randint(11, 99)) + ';FBBV/' + str(random.randint(11111111, 77777777)) + ';' + '[FBAN/FB4A;FBAV/' + fbav + ';FBBV/' + fbbv + ';FBDM/{density=3.0,width=1080,height=2107};FBLC/fr_FR;FBRV/' + fbrv + ';FBCR/Ooredoo TN;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/MAR-LX1M;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]'
    data = {
        'locale': 'en_SV',
        'client_country_code': 'SV',
        'fb_api_req_friendly_name': 'authenticate',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
        'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32' }
    head = {
        'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32' }
    url = 'https://graph.facebook.com/auth/login'
    po = requests.post(url, headers = head, data = data).json()
    if 'session_key' in po:
        cookie = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
        poo = po.get('access_token', '')
        token = str(poo)
        return get_facebook_pages_with_token3(uid, token, path_file, check_path)
    if Exception:
        e = 'True'
        print(f'''{red}AN ERROR OCCURRED!''')
        e = None
        del e
        e = None
        del e

def graph2(uid, pw, path_file, check_path):
    global loop
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    pas = pw
    data = {
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32' }
    simm3 = random.choice([
        'GLOBE',
        'SMART'])
    headers = '62f8ce9f74b12f84c123cc23437a4a32'
    url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
    po = requests.post(url, headers = headers, data = data).json()
    if 'session_key' in po:
        cookie = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
        poo = po.get('access_token', '')
        token = str(poo)
        return get_facebook_pages_with_token3(uid, token, path_file, check_path)
    if Exception:
        e = 'x-fb-connection-token'
        print(f'''AN ERROR OCCURRED: {e}''')
        e = None
        del e
        e = None
        del e
    loop += 1

ids = []
OK = []
CP = []
loop = 0

def get_ua():
    return f'''Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S{random.randrange(100, 9999)}/{random.randrange(100, 9999)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{random.randrange(1, 9)}; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/{random.randrange(1, 9)}.{random.randrange(1, 9)} Mobile WVGA SMM-MMS/1.2.0 OPN-B'''

def datr():
    global loop
    ids.clear()
    OK.clear()
    CP.clear()
    loop = loop * 0
    clear()
    print(f'''{green}  METHOD 4 {white}---> {yellow}KAREN-BOOST BULK NORMAL ACCOUNTS M2''')
    linex()
    file_name = input(f'''{yellow}PUT FILE PATH : {green}''')
    linex()
    ids.extend(open(file_name, 'r').read().splitlines())
    if Exception:
        e = None
        print(f''' {str(e)}''')
        sleep(0.8)
        main()
        e = None
        del e
        e = None
        del e
    checker = thread(max_workers = 30)
    for id in ids:
        checker.submit(_Cookies, id)
        None(None, None)
        if not None:
            pass
    exit()

def getCookies(uid, password):
    session = requests.Session()
    _ua = get_ua()
    _fb = session.get('https://m.facebook.com').text
    _data = {
        'lsd': re.search('name="lsd" value="(.*?)"', str(_fb)).group(1),
        'jazoest': re.search('name="jazoest" value="(.*?)"', str(_fb)).group(1),
        'm_ts': re.search('name="m_ts" value="(.*?)"', str(_fb)).group(1),
        'li': re.search('name="li" value="(.*?)"', str(_fb)).group(1),
        'try_number': '0',
        'unrecognized_tries': '0',
        'email': uid,
        'pass': password,
        'login': 'Log In' }
    _header = {
        'authority': 'm.facebook.com',
        'upgrade-insecure-requests': '1',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-PK,en-GB,en-US;q=0.9,en;q=0.8,en;q=0.7',
        'dnt': '1',
        'x-requested-with': 'mark.via.gp',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'user-agent': _ua }
    _res = session.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100', data = _data, headers = _header).text
    cookies = ";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
    return cookies

def _Cookies(id):
    global loop
    (uid, psw) = id.split('|')
    _cookies = getCookies(uid, psw)
    if 'c_user' in _cookies:
        print(f'''  {white}ID : {yellow}{uid} {white}---> {green}Successfully Extract!''')
        line()
        open('/sdcard/.KAREN-BOOST-COOKIE-ACCOUNT.txt', 'a').write(_cookies + '\n')
    if 'checkpoint' in _cookies:
        print(f'''  {red}ID : {red}{uid} {white}---> {red}FAILED!''')
        linex()
    loop += 1
    return None
# ────────────────[Not One]─────────────────
def count_lines_in_files(*file_paths):
    for i, file_path in enumerate(file_paths, start = 1):
        file = open(file_path, 'r')
# ────────────────[Overview]─────────────────

def overview():
    open('/sdcard/.KAREN-BOOST-TOKEN-FRA-ACCOUNT.txt', 'a').write('')
    open('/sdcard/.KAREN-BOOST-TOKEN-FRA-ACCOUNT-NAME-ID.txt', 'a').write('')
    open('/sdcard/.KAREN-BOOST-TOKEN-RP-ACCOUNT.txt', 'a').write('')
    open('/sdcard/.KAREN-BOOST-TOKEN-RP-ACCOUNT-NAME-ID.txt', 'a').write('')
    open('/sdcard/.KAREN-BOOST-TOKEN-FRA-PAGES.txt', 'a').write('')
    open('/sdcard/.KAREN-BOOST-TOKEN-FRA-PAGES-NAME-ID.txt', 'a').write('')
    open('/sdcard/.KAREN-BOOST-TOKEN-RP-PAGES.txt', 'a').write('')
    open('/sdcard/.KAREN-BOOST-TOKEN-RP-PAGES-NAME-ID.txt', 'a').write('')
    print(f'''\t\t{cyan}YOUR BOOSTING TOOL OVERVIEW''')
    count_lines_in_files(path_file1, path_file2, path_file3, path_file4)
    print(f"\033[1;96m  ━━━━━━━━━━━━━━━━━━━━━━━[{red}OVERVIEW{c}]━━━━━━━━━━━━━━━━━━━━━")
    total_accounts = count_lines("/sdcard/KAREN-BOOST/toka.txt")
    total_pages = count_lines("/sdcard/KAREN-BOOST/tokp.txt")
    total_pagees = count_lines("/sdcard/KAREN-BOOST/tokp1.txt")
    total_pageees = count_lines("/sdcard/KAREN-BOOST/tokp2.txt")
    print(f"  {r}     TOTAL ACCOUNTS: {c} {total_accounts}{r} | TOTAL PAGES:     {c}{total_pages} {r}")
    print(f"  {r}     TOTAL FRA PAGES: {c}{total_pagees}{r} | TOTAL RPA PAGES: {c}{total_pageees} {r}")
    print(f'{c}  ══════════════════════════════════════════════════════{wh}')
# ────────────────[Path Files]─────────────────
path_file1 = '/sdcard/.KAREN-BOOST-TOKEN-FRA-ACCOUNT.txt'
path_file2 = '/sdcard/.KAREN-BOOST-TOKEN-RP-ACCOUNT.txt'
path_file3 = '/sdcard/.KAREN-BOOST-TOKEN-FRA-PAGES.txt'
path_file4 = '/sdcard/.KAREN-BOOST-TOKEN-RP-PAGES.txt'
path_file5 = '/sdcard/.KAREN-BOOST-TOKEN-FRA-ACCOUNT.txt'
path_file6 = '/sdcard/.KAREN-BOOST-TOKEN-RP-ACCOUNT.txt'
path_file7 = '/sdcard/.KAREN-BOOST-TOKEN-FRA-PAGES.txt'
path_file8 = '/sdcard/.KAREN-BOOST-TOKEN-RP-PAGES.txt'
path_file9 = '/sdcard/.KAREN-BOOST-TOKEN-FRA-ACCOUNT.txt'
path_file10 = '/sdcard/.KAREN-BOOST-TOKEN-RP-ACCOUNT.txt'
path_file11 = '/sdcard/.KAREN-BOOST-TOKEN-FRA-PAGES.txt'
path_file12 = '/sdcard/.KAREN-BOOST-TOKEN-RP-PAGES.txt'
# ────────────────[Setup - Data]─────────────────

def setup_user_data():
    os.makedirs("data", exist_ok=True)
    
    def create_file_if_not_exists(file_path):
        if not os.path.exists(file_path):
            open(file_path, "w").close()
    
    create_file_if_not_exists("data/namekar.xml")
    create_file_if_not_exists("data/passwordkar.xml")
    create_file_if_not_exists("data/agekar.xml")
    create_file_if_not_exists("data/locationkar.xml")


    
    def get_user_input(file_path, prompt_message):
        if os.path.getsize(file_path) > 0:
            with open(file_path, "r") as file_obj:
                return file_obj.readline().strip()
        else:
            user_input = input(prompt_message)
            with open(file_path, "w") as file_obj:
                file_obj.write(user_input)
            return user_input
    
    clear()
    uname = get_user_input("data/namekar.xml", f"  {c}     「{r}•{c}」{r}  ENTER YOUR NAME » ")
    upass = get_user_input("data/passwordkar.xml", f" {c}     「{r}•{c}」{r}   ENTER YOUR PASSWORD » ")

    uage = get_user_input("data/agekar.xml", f" {c}     「{r}•{c}」{r}   ENTER YOUR AGE » ")

    ulocation = get_user_input("data/locationkar.xml", f" {c}     「{r}•{c}」{r}   ENTER YOUR LOCATION » ")

setup_user_data()

# ────────────────[User-Name-Age-Location]─────────────────

def get_user_name():
    with open("data/namekar.xml", "r") as file_obj:
        return file_obj.readline().strip()

def get_user_password():
    with open("data/passwordkar.xml", "r") as file_obj:
        return file_obj.readline().strip()

def get_user_age():
    with open("data/agekar.xml", "r") as file_obj:
        return file_obj.readline().strip()

def get_user_location():
    with open("data/locationkar.xml", "r") as file_obj:
        return file_obj.readline().strip()

# ────────────────[Greet -User]─────────────────

def greet_user():
    current_time = datetime.now()
    user_name = get_user_name()
    if current_time.hour < 12:
        print(f"    「GOOD MORNING」 {c}{user_name}!{wh}")
    elif current_time.hour < 18:
        print(f"    「GOOD AFTERNOON」 {c}{user_name}!{r}")
    elif current_time.hour < 8:
        print(f"    「GOOD EVENING」 {c}{user_name}!{w}")
    #else:
    elif current_time.hour < 12:
        print(f"    「GOOD NIGHT」 {c}{user_name}!{w}")

# ────────────────[IP]─────────────────

def ip(key):
    urls = {
        "TRIAL" : "https://github.com/ALEXANDERAXLMONTREAL/06f27/blob/main/5.txt",
        "PREMIUM「1」": "https://github.com/ALEXANDERAXLMONTREAL/06f27/blob/main/6.txt",
        "PREMIUM「3」": "https://github.com/ALEXANDERAXLMONTREAL/06f27/blob/main/7.txt",
        "PREMIUM「3」": "https://github.com/ALEXANDERAXLMONTREAL/06f27/blob/main/8.txt"
    }

    statee = "PAID"
    for state, url in urls.items():
        response = requests.get(url)
        if response.status_code == 200:
            content = response.text
            if key in content:
                statee = state
                break

    ip_response = requests.get(
        "http://ip-api.com/json/",
        headers={
            "Referer": "http://ip-api.com/",
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) "
                           "AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 "
                           "Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
        }
    ).json()

    
    
    print(f" {c}  「{w}STATE{c}」{w}:{c}{statee}")
    print(f" {c}  「{w}IP{c}」{w}:{c}{ip_response.get('query', ' ')}")
    print(f"{c}   「{w}COUNTRY{c}」{w}:{c}{ip_response.get('country', ' ')}")
    print(f"{c}   「{w}ISP{c}」{w}:{c}{ip_response.get('isp', ' ')}")
    print(f"{c}   「{w}S-KEY{c}」{w}:{c}{key}")
    linex()

# ────────────────[Clr]─────────────────
    
def clr():
    os.system('clear')
    print(logo)  
    overview()
    greet_user()
    ip(key)

# ────────────────[Menu]─────────────────
def enc(txt):
    encoded_bytes = base64.b64encode(txt.encode('utf-8'))
    encoded_string = encoded_bytes.decode('utf-8')
    return encoded_string

def menu():
    approval()
    clr()
    left_options = [
        ("10", f"AUTO-SHARE{r}           "),
        ("11", f"{c}AUTO-REACT-W/O-CARE{r}  "),
        ("12", f"{c}AUTO-REACT-WITH-CARE{r} "),
        ("13", f"{c}AUTO-REACT-TO-COMMENT{r}"),
        ("14", f"{c}AUTO-REACT-TO-COVER{r}  "),
        ("15", f"{c}AUTO-REACT-TO-REELS{r}  "),
        ("16", f"{c}AUTO-RESET{r}           "),
        ("0", f" {red}AUTO-EXIT{r}            ")
    ]
    right_options = [
        ("1", f"{c}AUTO-START{r}"), 
        ("2", f"AUTO-REACT"), 
        ("3", f"AUTO-CREATE-PAGE"), 
        ("4", f"AUTO-FOLLOW"), 
        ("5", f"AUTO-COMMENT"), 
        ("6", f"AUTO-SHARE"), 
        ("7", f"AUTO-LIKE-FOLLOW-PAGE"),
        ("8", f"AUTO-GROUP-JOIN"),
        ("9", f"{c} AUTO-START-TOOL{r}"),
    ]
    for (left_option, left_desc), (right_option, right_desc) in zip(left_options, right_options):
        print(f"{c}   「{r}{left_option}{c}」{r} {left_desc:<14}     {c}   「{r}{right_option}{c}」{r} {right_desc}")
    linex()
    choice = input(f'   {c}「{r}CHOOSE {c}」{r}»  ')
    menu_actions = {
        '1': Initialize,
        '2': QuickReact,
        '3': C_page,
        '4': follow,
        '5': comment_on_facebook_post,
        '6': AutomaticSharing,
        '7': p_like,
        '8': g_join,
        '9': start_tool,
        '10': auto_share,
        '11': react,
        '12': react_with_care,
        '13': react_comment,
        '14': react_dp_cover,
        '15': react_reels,
        '16': lambda: reset(),
        '0': lambda: print(' 「✓」 DONE LOGOUT ') or exit()
    }
    menu_actions.get(choice, lambda: print(' 「!」INVALID OPTION. '))()

# ────────────────[Manual]─────────────────

def Manual():
    user_choice = input(f" {wh}INPUT Y OR LEAVE BLANK if ITS ACCOUNT.IF ITS A PAGE THEN INPUT (y/Y/yes/Yes or n/N/no/No or d/D/default/Default): {r}")
    #linex()
    user = input(f"{c}USER ID/EMAIL:{wh} ")
    #linex()
    passw = input(f"{c}PASSWORD:{wh} ")
    linex()
    cuser(user, passw, user_choice)

# ────────────────[Automatic file]─────────────────

def Auto():
    directory = '/sdcard'
    txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]
    
    if not txt_files:
        print(f'\033[1;31m「!」NO . TXT FILES FOUND IN {directory}')
        return
    
    for i, filename in enumerate(txt_files, start=1):
        print(f"    {c}「{r}{i}{c}」{wh}  {filename}")
    
    try:
        linex()
        choice = int(input('   CHOOSE: '))
        if 1 <= choice <= len(txt_files):
            selected_file = os.path.join(directory, txt_files[choice - 1])
            if os.path.isfile(selected_file):
                try:
                    user_choice = input(f"{ye}INPUT Y OR LEAVE BLANK IF IT'S AN ACCOUNT. IF IT'S A PAGE, INPUT (y/Y/yes/Yes or n/N/no/No or d/D/default/Default): {r}")
                    with open(selected_file, 'r') as file:
                        for line in file:
                            user_pass = line.strip().split('|')
                            process_users([user_pass], user_choice)
                except Exception as e:
                    print(f'\033[1;31m「!」ERROR READING THE FILE: {e}')
            else:
                print(f'\033[1;31m「!」FILE NOT FOUND ')
        else:
            print(f'{red}「!」INVALID OPTION.{r}')
    except ValueError:
        print(f'{red}「!」INVALID INPUT.{r}')


# ────────────────[Manually using file]─────────────────

def ManFile():
    file = input(' 「?」PUT FILE PATH: ')
    if os.path.isfile(file):
        try:
            user_choice = input(f" {ye}INPUT Y OR LEAVE BLANK IF IT'S AN ACCOUNT. IF IT'S A PAGE, INPUT (y/Y/yes/Yes or n/N/no/No or d/D/default/Default): {r}")
            with open(file, 'r') as file:
                for line in file:
                    user_pass = line.strip().split('|')
                    process_users([user_pass], user_choice)
        except Exception as e:
            print(f' \033[1;31m「!」ERROR READING THE FILE: {e}')
    else:
        print(f' \033[1;31m「!」FILE LOCATION NOT FOUND ')


def process_users(user_list, user_choice):
    for user_pass in user_list:
        if len(user_pass) == 2:
            user, passw = user_pass
            cuser(user, passw, user_choice)
            approvalf()
        else:
            print(f"INVALID FORMAT IN LINE: {user_pass}")

# ────────────────[Tok+cookie extract]─────────────────

import requests
import uuid
import random

def cuser(user, passw, user_choice):
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    data = {
        'adid': f'{uuid.uuid4()}',
        'format': 'json',
        'device_id': f'{uuid.uuid4()}',
        'cpl': 'true',
        'family_device_id': f'{uuid.uuid4()}',
        'credentials_type': 'device_based_login_password',
        'error_detail_type': 'button_with_disabled',
        'source': 'device_based_login',
        'email': user,
        'password': passw,
        'access_token': accessToken,
        'generate_session_cookies': '1',
        'meta_inf_fbmeta': '',
        'advertiser_id': f'{uuid.uuid4()}',
        'currently_logged_in_userid': '0',
        'locale': 'en_US',
        'client_country_code': 'US',
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
    }
    headers = {
        'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/en_US;FBBV/135374479;FBCR/SMART;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'graph.facebook.com',
        'X-FB-Net-HNI': str(random.randint(10000, 99999)),
        'X-FB-SIM-HNI': str(random.randint(10000, 99999)),
        'X-FB-Connection-Type': 'MOBILE.LTE',
        'X-Tigon-Is-Retry': 'False',
        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
        'x-fb-device-group': str(random.randint(1000, 9999)),
        'X-FB-Friendly-Name': 'ViewerReactionsMutation',
        'X-FB-Request-Analytics-Tags': 'graphservice',
        'X-FB-HTTP-Engine': 'Liger',
        'X-FB-Client-IP': 'True',
        'X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
        'X-FB-Server-Cluster': 'True',
        'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'
    }
    
    pos = requests.post("https://b-graph.facebook.com/auth/login", headers=headers, data=data, allow_redirects=False).json()
    
    if "session_key" in pos:
        print(f"   {c}「SUCCESSFULLY」--> {user} EXTRACTED SUCCESSFULLY.{wh}")
        
        cookie = ';'.join(i['name'] + '=' + i['value'] for i in pos['session_cookies'])
        c_user_value = [i['value'] for i in pos['session_cookies'] if i['name'] == 'c_user'][0]
        
        if user_choice.lower() in ['n', 'no']:
            with open('/sdcard/KAREN-BOOST/tokpid.txt', 'a') as f:
                f.write(f'{c_user_value}\n')
            with open('/sdcard/KAREN-BOOST/tokp.txt', 'a') as f:
                f.write(f'{pos["access_token"]}\n')
        else:
            with open('/sdcard/KAREN-BOOST/toka.txt', 'a') as f:
                f.write(f'{pos["access_token"]}\n')
            with open('/sdcard/KAREN-BOOST/tokaid.txt', 'a') as f:
                f.write(f'{c_user_value}\n')
        
        with open('/sdcard/KAREN-BOOST/cok.txt', 'a') as f:
            f.write(f'{cookie}\n')
        
        with open('/sdcard/KAREN-BOOST/cokid.txt', 'a') as f:
            f.write(f'{c_user_value}\n')
    else:
        print(f"   {red}「FAILED」--> {user} ISN'T EXTRACTED. {w} ")



# ────────────────[1• Initizalize]─────────────────

def Initialize():
    print(f"  {red} PLEASE CHOOSE HOW YOU WANT TO EXTRACT.\n")
    print(f"{c}     「{r}1{c}」{r} MANUAL THROUGH INPUT")
    print(f"{c}     「{r}2{c}」{r} MANUAL THROUGH FILE")
    print(f"{c}     「{r}3{c}」{r} AUTOMATIC THROUGH OPTION")
    
    me = input(f'   {c}「{r}CHOOSE {c}」{r}»  ')
    if me == '1':
        Manual()
    if me == '2':
    	ManFile()
    elif me == '3':
        Auto()
    else:
        print(f' {red}「!」INVALID OPTION. ')

# ────────────────[2• React]─────────────────

def Reaction(actor_id:str, post_id:str, react:str, token:str):
    rui    = requests.Session()
    var  = {"input":{"feedback_referrer":"native_newsfeed","tracking":[None],"feedback_id":str(base64.b64encode(('feedback:{}'.format(post_id)).encode('utf-8')).decode('utf-8')),"client_mutation_id":str(uuid.uuid4()),"nectar_module":"newsfeed_ufi","feedback_source":"native_newsfeed","attribution_id_v2":"NewsFeedFragment,native_newsfeed,cold_start,1710331848.276,264071715,4748854339,,","feedback_reaction_id":react,"actor_id":actor_id,"action_timestamp":str(time.time())[:10]}}
    data = {'access_token':token,'method':'post','pretty':False,'format':'json','server_timestamps':True,'locale':'id_ID','fb_api_req_friendly_name':'ViewerReactionsMutation','fb_api_caller_class':'graphservice','client_doc_id':'2857784093518205785115255697','variables':json.dumps(var),'fb_api_analytics_tags':["GraphServices"],'client_trace_id':str(uuid.uuid4())}
    pos  = rui.post('https://graph.facebook.com/graphql', data=data).json()
    try:
        if react in str(pos): print(f"{c}「SUCCESSFULLY」»  {w} REACTED WITH » {c}{actor_id} TO {c}{post_id} ")
        else: print(f"{red}「FAILED」»  {red} REACTED WITH » {red}{actor_id} TO {red}{post_id} ")
    except Exception: print('')

def choose_reaction():
    print(f"{red}PLEASE CHOOSE THE REACTION YOU WANT TO USE.\n")
    print(f"{c}     「{r}1{c}」{r} LIKE")
    print(f"{c}     「{r}2{c}」{r} LOVE")
    print(f"{c}     「{r}3{c}」{r} HAHA")
    print(f"{c}     「{r}4{c}」{r} WOW")
    print(f"{c}     「{r}5{c}」{r} CARE")
    print(f"{c}     「{r}6{c}」{r} SAD")
    print(f"{c}     「{r}7{c}」{r} ANGRY")

    rec = input(f'   {c}「{r}CHOOSE {c}」{r}»  ')
    reactions = {
        '1': '1635855486666999',  # LIKE 
        '2': '1678524932434102',  # LOVE 
        '3': '115940658764963',   # HAHA 
        '4': '478547315650144',   # WOW 
        '5': '613557422527858',   # CARE 
        '6': '908563459236466',   # SAD 
        '7': '444813342392137'    # ANGRY 
    }
    return reactions.get(rec, None)

def QuickReact():
    def get_ids_tokens(file_path):
        with open(file_path, 'r') as file:
            return [line.strip() for line in file]

    actor_ids = get_ids_tokens('/sdcard/KAREN-BOOST/tokaid.txt')
    tokens = get_ids_tokens('/sdcard/KAREN-BOOST/toka.txt')
    post_link = input('ENTER THE FACEBOOK POST LINK: ')
    post_id = linktradio(post_link)

    react = choose_reaction()
    if react:
        for actor_id, token in zip(actor_ids, tokens):
            Reaction(actor_id=actor_id, post_id=post_id, react=react, token=token)
    else:
        print(' 「!」INVALID OPTION. ')


# ────────────────[3•Create-pages]─────────────────

class reg_pro5():
    def __init__(self, cookies, name) -> None:
        self.cookies = cookies
        self.name = name  
        self.id_acc = self.cookies.split('c_user=')[1].split(';')[0]
        headers = {
            'authority': 'www.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'vi',
            'cookie': self.cookies,
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'viewport-width': '980',
        }
        url_profile = requests.get('https://www.facebook.com/me', headers=headers).url
        profile = requests.get(url_profile, headers=headers).text
        try:
            self.fb_dtsg = profile.split('{"name":"fb_dtsg","value":"')[1].split('"},')[0]
        except:
            self.fb_dtsg = profile.split(',"f":"')[1].split('","l":null}')[0]

    def Reg(self):
        headers = {
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            # Requests sorts cookies= alphabetically
            'cookie': self.cookies,
            'origin': 'https://www.facebook.com',
            'referer': 'https://www.facebook.com/pages/creation?ref_type=launch_point',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'viewport-width': '980',
            'x-fb-friendly-name': 'AdditionalProfilePlusCreationMutation',
            'x-fb-lsd': 'ZM7FAk6cuRcUp3imwqvHTY',
        }

        data = {
            'av': self.id_acc,
            '__user': self.id_acc,
            '__a': '1',
            '__dyn': '7AzHxq1mxu1syUbFuC0BVU98nwgU29zEdEc8co5S3O2S7o11Ue8hw6vwb-q7oc81xoswIwuo886C11xmfz81sbzoaEnxO0Bo7O2l2Utwwwi831wiEjwZwlo5qfK6E7e58jwGzE8FU5e7oqBwJK2W5olwuEjUlDw-wUws9ovUaU3qxWm2Sq2-azo2NwkQ0z8c84K2e3u362-2B0oobo',
            '__csr': 'gP4ZAN2d-hbbRmLObkZO8LvRcXWVvth9d9GGXKSiLCqqr9qEzGTozAXiCgyBhbHrRG8VkQm8GFAfy94bJ7xeufz8jK8yGVVEgx-7oiwxypqCwgF88rzKV8y2O4ocUak4UpDxu3x1K4opAUrwGx63J0Lw-wa90eG18wkE7y14w4hw6Bw2-o069W00CSE0PW06aU02Z3wjU6i0btw3TE1wE5u',
            '__req': 't',
            '__hs': '19296.HYP:comet_pkg.2.1.0.2.1',
            'dpr': '1',
            '__ccg': 'EXCELLENT',
            '__rev': '1006496476',
            '__s': '1gapab:y4xv3f:2hb4os',
            '__hsi': '7160573037096492689',
            '__comet_req': '15',
            'fb_dtsg': self.fb_dtsg,
            'jazoest': '25404',
            'lsd': 'ZM7FAk6cuRcUp3imwqvHTY',
            '__aaid': '800444344545377',
            '__spin_r': '1006496476',
            '__spin_b': 'trunk',
            '__spin_t': '1667200829',
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'AdditionalProfilePlusCreationMutation',
            'variables': '{"input":{"bio":"","categories":["181475575221097"],"creation_source":"comet","name":"'+self.name+'","page_referrer":"launch_point","actor_id":"'+self.id_acc+'","client_mutation_id":"1"}}',
            'server_timestamps': 'true',
            'doc_id': '5903223909690825',
        }

        response = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data).json()
        try:
            return response['data']['additional_profile_plus_create']['additional_profile']['id']
        except:
            return (f'「FAILED  」TO CREATE PAGE.')

# ────────────────[4•Auto-Follow]─────────────────
def follow():
    clear()
    print(f'''{white}  CHOOSE FACEBOOK TO FOLLOW:''')
    print(f'''{yellow}  [1] {blue}YOUR FRA LIST''')
    print(f'''{yellow}  [2] {blue}YOUR RPA LIST''')
    print(f'''{yellow}  [3] {blue}YOUR FRA PAGES LIST''')
    print(f'''{yellow}  [4] {blue}YOUR RPA PAGES LIST''')
    print(f'''{red}  [0] {red}RETURN TO MAIN MENU''')
    linex()
    account_choose = input(f'''{yellow}  CHOOSE : {green}''')
    linex()
    if account_choose == '1' or account_choose == '01':
        file_path = '/sdcard/.KAREN-BOOST-TOKEN-FRA-ACCOUNT.txt'
    if account_choose == '2' or account_choose == '02':
        file_path = '/sdcard/.KAREN-BOOST-TOKEN-RP-ACCOUNT.txt'
    if account_choose == '3' or account_choose == '03':
        file_path = '/sdcard/.KAREN-BOOST-TOKEN-FRA-PAGES.txt'
    if account_choose == '4' or account_choose == '04':
        file_path = '/sdcard/.KAREN-BOOST-TOKEN-RP-PAGES.txt'
    if account_choose == '0' or account_choose == '00':
        main()
    print(f'''{red}INVALID INPUT!''')
    sleep(1.5)
    follow()
    access_tokens = get_access_token_from_file(file_path)
    if not access_tokens:
        return None
    user_id = None(f'''{yellow}ENTER TARGET UID : {green}''')
    linex()
    limit = int(input(f'''{yellow}INPUT QUANTITY of FOLLOWS, LIMIT IS {green}{len(access_tokens)} : '''))
    if ValueError:
        print(f'''{red}ERROR: PLEASE ENTER A VALID NUMBER FOR THE LIMIT.''')
        return None
    if limit > len(access_tokens):
        print(f'''{red}ERROR: THE SPECIFIED LIMIT EXCEEDS THE NUMBER OF AVAILABLE FOLLOWERS.''')
        return None
    success_count = None
    failure_count = 0
    for i, access_token in enumerate(access_tokens[:limit]):
        auto_follow_url = f'''https://graph.facebook.com/v19.0/{user_id}/subscribers'''
        time.sleep(1)
        headers = {
            'Authorization': f'''Bearer {access_token}''',
            'user-agent': W_ueragnt() }
        response = requests.post(auto_follow_url, headers = headers)
        if response.ok:
            line()
            print(f'''{green}  FOLLOWER {i + 1} ---> SUCCESSFULLY FOLLOW!''')
            success_count += 1
        linex()
        print(f'''{red}  FOLLOWER {i + 1} ---> FAILED TO FOLLOW!''')
        failure_count += 1
        linex()
        print(f'''{yellow}  TOTAL : \n''')
        print(f'''{green}  COMPLETED : {white}{success_count}''')
        print(f'''{red}  FAILED : {white}{failure_count}''')
        return None
# ────────────────[5•Comment]─────────────────
def get_ids_tokens(file_path):
        with open(file_path, 'r') as file:
            return [line.strip() for line in file]

def comment_on_facebook_post():
    user_ids = get_ids_tokens('/sdcard/KAREN-BOOST/tokaid.txt')
    access_tokens = get_ids_tokens('/sdcard/KAREN-BOOST/toka.txt')
    current_time = datetime.now()
    user_name = get_user_name()
    post_link = input('ENTER THE FACEBOOK POST LINK: ')
    post_id = linktradio(post_link)
    comment_text = input('ENTER THE COMMENT TEXT (OR LEAVE BLANK FOR AUTO COMMENT): ')
    num_comments = int(input('ENTER THE NUMBER OF COMMENTS TO MAKE: '))

    if not comment_text:
        current_time = datetime.now().strftime("%I:%M %p")
        current_date = datetime.now().strftime("%Y-%m-%d")
        comment_text = f'TIME:「{current_time}」「{current_date}」\n-「AUTO COMMENT BY {user_name}」'

    def has_commented(post_id, access_token, user_id):
        try:
            url = f'https://graph.facebook.com/v18.0/{user_id}_{post_id}/comments'
            params = {'access_token': access_token}
            response = requests.get(url, params=params)
            response.raise_for_status()
            comments = response.json().get('data', [])
            
            for comment in comments:
                if comment.get('from', {}).get('id') == user_id:
                    return True
        except requests.exceptions.RequestException as error:
            print(f" {red}「FAILED  」TO COMMENT ON {post_id}")
        return False

    comments_count = 0
    user_count = len(user_ids)

    for _ in range(num_comments):
        for i in range(user_count):
            user_id = user_ids[i]
            access_token = access_tokens[i]

            try:
                if not has_commented(post_id, access_token, user_id):
                    url = f'https://graph.facebook.com/v19.0/{user_id}_{post_id}/comments'
                    params = {'access_token': access_token, 'message': comment_text}
                    response = requests.post(url, params=params)
                    
                    if response.status_code == 200:
                        comments_count += 1
                        print(f"{c}「SUCCESSFULLY 」{w} COMMENTED ON {c} {post_id}")
                        if comments_count >= num_comments:
                            print(f"{c}「SUCCESSFULLY  」{w} COMMENTED {c} {num_comments} {w}times.")
                            return
                    else:
                        print(f"{red}「FAILED  」TO COMMENT ON {post_id}")
            except requests.exceptions.RequestException as error:
                print(f"{red}「FAILED  」TO COMMENT ON {post_id}")


def C_page():
    print("WAIT FOR UPDATE FACEBOOK")

# ────────────────[6•Share]─────────────────

def AutomaticSharing():
    access_token = input('ENTER THE ACCESS TOKEN: ') # ACCESS TOKEN HERE
    share_url = input('ENTER THE FACEBOOK POST LINK: ')
    share_count = 22200
    time_interval = 1.5
    delete_after = 60 * 60

    shared_count = 0
    timer = None

    headers = {
        'authority': 'graph.facebook.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
    }

    def share_post():
        nonlocal shared_count, timer

        try:
            response = requests.post(
                f'https://graph.facebook.com/me/feed?access_token={access_token}&fields=id&limit=1&published=0',
                json={
                    'link': share_url,
                    'privacy': {'value': 'SELF'},
                    'no_story': True,
                },
                headers=headers
            )

            shared_count += 1
            post_id = response.json().get('id')
            print(f' {c}「SUCCESSFULLY」»  {c}「{wh}{shared_count}{c}」» {wh} ID:{c}{post_id or "Unknown"}{wh}')

            if shared_count == share_count:
                timer.cancel()
                print('FINISHED SHARING POSTS.')

                if post_id:
                    threading.Timer(delete_after, delete_post, args=(post_id,)).start()

        except requests.exceptions.RequestException as error:
            print('FAILED TO SHARE POST:', error.response.json() if error.response else str(error))

    def delete_post(post_id):
        try:
            requests.delete(f'https://graph.facebook.com/{post_id}?access_token={access_token}')
            print(f'POST DELETED: {post_id}')
        except requests.exceptions.RequestException as error:
            print('FAILED TO DELETE POST:', error.response.json() if error.response else str(error))

    def start_sharing():
        nonlocal timer
        timer = threading.Timer(time_interval, share_post)
        timer.start()

    for _ in range(share_count):
        start_sharing()
        time.sleep(time_interval)

    
    time.sleep(share_count * time_interval)
    if timer:
        timer.cancel()
        print('LOOP STOPPED.')
# ────────────────[7•Auto Like & Follow Page]─────────────────
def p_like():
    clear()
    ses = requests.Session()
    cokix = input(f'''{yellow}COOKIE : {green}''')
    linex()
    ids_coki = input(f'''{yellow}INPUT FILE PATH :{green} ''')
    page_id = open(ids_coki).read().splitlines()
    print('FILE NOT FOUND')
    sleep(3)
    linex()
    page_ids = input(f'''{yellow}INPUT TARGET PAGE ID : {green}''')
    linex()
    limitx = int(input(f'''{yellow}QUANTITY : {green}'''))
    headersccc['user-agent'] = W_ueragnt()
    mbasic_url = 'https://mbasic.facebook.com/' + page_ids
    reqx = bs(ses.get(mbasic_url, headers = headersccc, cookies = {
        'cookie': cokix }).content, 'html.parser')
    reqxx = reqx.find_all('a', string = 'Message')
    d_pa_id = str(reqxx).split('href="/messages/thread/')[1].split('/')[0]
    clear()
    print(f'''{yellow}TOTAL PAGE : {green}{len(page_id)}''')
    print(f'''{yellow}TARGET     : {green}{page_ids}''')
    linex()
    for i in range(min(len(page_id), limitx)):
        pageid = page_id[i]
        page_uidz = 'i_user=' + pageid
        cookies_page = {
            'cookie': cokix + page_uidz }
        mylove = ThreadPoolExecutor(max_workers = 30)
        mylove.submit(likepage, cookies_page, pageid, page_ids, d_pa_id)
        None(None, None)
        if not None:
            pass
        linex()
        linex()
        print('{red}FAILED')
        print(cokix)
        print(linex())
        open('failed.txt', 'a', encoding = 'utf8').write(f'''{cokix}\n''')
        exit()
        return None

def likepage(cookies_page, pageid, page_ids, d_pa_id):
    headers['user-agent'] = W_ueragnt()
    web_url = 'https://www.facebook.com/profile.php?id=' + page_ids
    req = bs(ses.get(web_url, headers = headers, cookies = cookies_page).content, 'html.parser')
    uidx = re.search('__user=(.*?)&', str(req)).group(1)
    data_post = {
        'av': uidx,
        'dpr': re.search('"pr":(.*?),', str(req)).group(1),
        'fb_dtsg': re.search('"DTSGInitialData",\\[\\],{"token":"(.*?)"}', str(req)).group(1),
        'jazoest': re.search('&jazoest=(.*?)"', str(req)).group(1),
        'lsd': re.search('"LSD",\\[\\],{"token":"(.*?)"}', str(req)).group(1),
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'CometProfilePlusLikeMutation',
        'variables': f'''{{"input":{{"is_tracking_encrypted":false,"page_id":{d_pa_id!s},"source":null,"tracking":null,"actor_id":{uidx!s},"client_mutation_id":"1"}},"scale":1}}''',
        'server_timestamps': 'true',
        'doc_id': '6716077648448761' }
    headers['user-agent'] = W_ueragnt()
    response = ses.post('https://www.facebook.com/api/graphql/', cookies = cookies_page, headers = headers, data = data_post)
    if response.status_code == 200:
        data = response.json()
        subscribe_status = data['data']['page_like']['page']['subscribe_status']
        done.append(pageid)
        print(f'''{white}  [{len(done)}] {green}PAGE LIKE AND FOLLOW DONE :{white} {pageid} ''')
        return None
    return None
    print(f'''{red}FAILED!''')

done = []

# ────────────────[8•Auto Group Join]─────────────────
def g_join():
    clear()
    cokix = input(f'''{yellow}COOKIE : {green}''')
    linex()
    ids_coki = input(f'''{yellow}INPUT FILE PATH : {green} ''')
    page_id = open(ids_coki).read().splitlines()
    print('FILE NOT FOUND')
    sleep(2)
    linex()
    group_ids = input(f'''{yellow}INPUT GROUP ID : {green}''')
    linex()
    limitx = int(input(f'''{yellow}QUANTITY : {green}'''))
    clear()
    print(f'''{green}TOTAL PAGE : {yellow}{len(page_id)}''')
    print(f'''{green}TARGET     : {yellow}{group_ids}''')
    linex()
    for i in range(min(len(page_id), limitx)):
        pageid = page_id[i]
        page_uidz = 'i_user=' + pageid
        cookies_page = {
            'cookie': cokix + page_uidz }
        mylove = ThreadPoolExecutor(max_workers = 30)
        mylove.submit(g_joining, cookies_page, pageid, group_ids)
        None(None, None)
        if not None:
            pass
        linex()
        linex()
        print(f'''{red}FAILED''')
        exit()
        return None

def g_joining(cookies_page, pageid, group_ids):
    secx = requests.Session()
    use_link = f'''https://www.facebook.com/groups/{group_ids}'''
    headers['user-agent'] = W_ueragnt()
    req = bs(secx.get(use_link, headers = headers, cookies = cookies_page).content, 'html.parser')
    av = re.search('__user=(.*?)&', str(req)).group(1)
    data = {
        'av': av,
        'dpr': re.search('"pr":(.*?),', str(req)).group(1),
        'fb_dtsg': re.search('"DTSGInitialData",\\[\\],{"token":"(.*?)"}', str(req)).group(1),
        'jazoest': re.search('&jazoest=(.*?)"', str(req)).group(1),
        'lsd': re.search('"LSD",\\[\\],{"token":"(.*?)"}', str(req)).group(1),
        'qpl_active_flow_ids': '431626709',
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'GroupCometJoinForumMutation',
        'variables': f'''{{"feedType":"DISCUSSION","groupID":{group_ids!s},"imageMediaType":"image/x-auto","input":{{"action_source":"GROUP_MALL","attribution_id_v2":"CometGroupDiscussionRoot.react,comet.group,via_cold_start,1697077069058,802502,2361831622,","group_id":{group_ids!s},"group_share_tracking_params":{{"app_id":"2220391788200892","exp_id":"null","is_from_share":false}},"actor_id":{av!s},"client_mutation_id":"1"}},"inviteShortLinkKey":null,"isChainingRecommendationUnit":false,"isEntityMenu":true,"scale":1,"source":"GROUP_MALL","renderLocation":"group_mall","__relay_internal__pv__GroupsCometEntityMenuChannelsrelayprovider":true,"__relay_internal__pv__GroupsCometGroupChatLazyLoadLastMessageSnippetrelayprovider":true}}''',
        'server_timestamps': 'true',
        'doc_id': '24830959139836152',
        'fb_api_analytics_tags': '["qpl_active_flow_ids=431626709"]' }
    headers['user-agent'] = W_ueragnt()
    response = requests.post('https://www.facebook.com/api/graphql/', cookies = cookies_page, headers = headers, data = data)
    if response.status_code == 200:
        done.append(pageid)
        print(f'''{white}  [{len(done)}] {green} GROUP JOINING DONE :{white} {pageid} ''')
        return None
    return None
    print('some problem')
# ────────────────[10• AUTO SHARE]─────────────────
def auto_share():
    clear()
    print(f'''{red}NOTE : {green}USE{blue} FACEBOOK LITE {green}in copying post link.''')
    linex()
    ids = input(f'''{yellow}ENTER YOUR ACCOUNT UID USE FOR AUTO SHARE : {green}''')
    linex()
    pas = input(f'''{yellow}ENTER PASSWORD : {green}''')
    ses = requests.Session()
    fbav = f'''{random.randint(111, 999)}.0.0.{random.randint(11, 99)}.{random.randint(111, 999)}'''
    fbbv = str(random.randint(111111111, 999999999))
    fbrv = '0'
    random_seed = random.Random()
    adid = str(''.join(random_seed.choices(string.hexdigits, k = 16)))
    ua_bgraph = []['[FBAN/FB4A;FBAV/'][f'''{str(random.randint(49, 66))}''']['.0.0.'][f'''{random.randrange(20, 49)}'''][f'''{random.randint(11, 99)}'''][';FBBV/'][f'''{str(random.randint(11111111, 77777777))}'''][';[FBAN/FB4A;FBAV/'][f'''{fbav}'''][';FBPN/com.facebook.katana;FBLC/pt_BR;FBBV/'][f'''{fbbv}'''][';FBCR/CLARO BR;FBMF/Xiaomi;FBBD/Redmi;FBDV/M1908C3JGG;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2216};FB_FW/1;FBRV/470765339;] FBBK/1[FBAN/FB4A;FBAV/'][f'''{str(random.randint(49, 66))}''']['.0.0.'][f'''{random.randrange(20, 49)}'''][f'''{random.randint(11, 99)}'''][';FBBV/'][f'''{str(random.randint(11111111, 77777777))}'''][';[FBAN/FB4A;FBAV/'][f'''{fbav}'''][';FBBV/'][f'''{fbbv}'''][';FBDM/{density=2.75,width=1080,height=2134};FBLC/ar_AR;FBRV/'][f'''{fbrv}'''][';FBCR/etisalat by e&amp-;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 8[FBAN/FB4A;FBAV/'][f'''{str(random.randint(49, 66))}''']['.0.0.'][f'''{random.randrange(20, 49)}'''][f'''{random.randint(11, 99)}'''][';FBBV/'][f'''{str(random.randint(11111111, 77777777))}'''][';[FBAN/Orca-Android;FBAV/'][f'''{fbav}'''][';FBPN/com.facebook.orca;FBLC/in_ID;FBBV/'][f'''{fbbv}''']([]['[FBAN/FB4A;FBAV/'][f'''{str(random.randint(49, 66))}''']['.0.0.'][f'''{random.randrange(20, 49)}'''][f'''{random.randint(11, 99)}'''][';FBBV/'][f'''{str(random.randint(11111111, 77777777))}'''][';[FBAN/FB4A;FBAV/'][f'''{fbav}'''][';FBPN/com.facebook.katana;FBLC/pt_BR;FBBV/'][f'''{fbbv}'''][';FBCR/CLARO BR;FBMF/Xiaomi;FBBD/Redmi;FBDV/M1908C3JGG;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=2.75,width=1080,height=2216};FB_FW/1;FBRV/470765339;] FBBK/1[FBAN/FB4A;FBAV/'][f'''{str(random.randint(49, 66))}''']['.0.0.'][f'''{random.randrange(20, 49)}'''][f'''{random.randint(11, 99)}'''][';FBBV/'][f'''{str(random.randint(11111111, 77777777))}'''][';[FBAN/FB4A;FBAV/'][f'''{fbav}'''][';FBBV/'][f'''{fbbv}'''][';FBDM/{density=2.75,width=1080,height=2134};FBLC/ar_AR;FBRV/'][f'''{fbrv}'''][';FBCR/etisalat by e&amp-;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 8[FBAN/FB4A;FBAV/'][f'''{str(random.randint(49, 66))}''']['.0.0.'][f'''{random.randrange(20, 49)}'''][f'''{random.randint(11, 99)}'''][';FBBV/'][f'''{str(random.randint(11111111, 77777777))}'''][';[FBAN/Orca-Android;FBAV/'][f'''{fbav}'''][';FBPN/com.facebook.orca;FBLC/in_ID;FBBV/'][f'''{fbbv}'''][';FBCR/Telkomsel;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/RNE-L22;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.75,width=1080,height=2050};FB_FW/1;]'])
    data = {
        'locale': 'en_SV',
        'client_country_code': 'SV',
        'fb_api_req_friendly_name': 'authenticate',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
        'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32' }
    head = {
        'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32' }
    url = 'https://graph.facebook.com/auth/login'
    po = requests.post(url, data = data, headers = head).json()
    if 'session_key' in po:
        poo = requests.post(url, data = data, headers = head).json().get('access_token', '')
        token = str(poo)
        cookie = po.get('session_cookies', [])()
    
    def extract_fb_pages(poo):
        url = 'https://graph.facebook.com/v18.0/me/accounts'
        headers = {
            'Authorization': f'''Bearer {poo}''' }
        pages_data = []
        response = requests.get(url, headers = headers)
        if response.status_code != 200:
            print(f'''ERROR: {response.text}''')
            return None
            json_string = '''
{
    "data": [
        {"access_token": "token1", "id": "1", "name": "Page One"},
        {"access_token": "token2", "id": "2", "name": "Page Two"}
    ]
}
'''
        data = json.loads(json_string)
        access_tokens = [{'accessToken': page['access_token']} for page in data['data']]
        print(access_tokens)
        next_page = data.get('paging', { }).get('next')
        if next_page:
            url = next_page
            if requests.RequestException:
                e = pages_data.extend
                print(f'''ERROR FETCHING PAGES DATA: {e}''')
                e = None
                del e
                return None
            e = pages_data.extend
            del e
            return pages_data

    
    def convert_to_traodoisub(url):
        response = requests.post('https://id.traodoisub.com/api.php', data = {
            'link': url })
        if response.status_code == 200:
            result = response.json().get('id')
            return result
        return None
        if Exception:
            e = None
            print(f'''AN ERROR OCCURRED: {e}''')
            e = None
            del e
            return None
        e = None
        del e

    
    def extract_uid_from_link(post_link):
        pattern = 'https://www\\.facebook\\.com/(\\d+)/posts/[^/]+/?'
        match = re.match(pattern, post_link)
        if match:
            return match.group(1)
        None('INVALID POST LINK.')

    
    def auto_share_post(post_link = 'X-FB-Request-Analytics-Tags', token = 'graphservice', cookie = 'X-FB-HTTP-Engine'):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': 'Windows',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'authority': 'graph.facebook.com' }
        n = 0
        for x in range(limit):
            n += 1
            post = ses.post(f'''https://graph.facebook.com/v13.0/me/feed?link={post_link}&published=0&access_token={token}''', headers = headers, cookies = cookie).text
            time.sleep(0.1)
            data = json.loads(post)
            if 'id' in post:
                print(f'''\r{yellow}SHARE DONE - {green}{n}''', end = '')
                sys.stdout.flush()
            print('\n')
            print(f'''{red}AUTO SHARE STOP!''')
            exit()
            return None
            if requests.exceptions.ConnectionError:
                print(f'''\n{red}YOU ARE NOT CONNECTED TO THE INTERNET!''')
                exit()
                return None

    linex()
    post_link = input(f'''{yellow}ENTER POST LINK: {green}''')
    pages_datas = extract_fb_pages(poo)
    if not pages_datas:
        print(f'''{red}ERROR FETCHING FACEBOOK.''')
        return None
    converted_link = convert_to_traodoisub(post_link)
    linex()
    limit = int(input(f'''{yellow}ENTER LIMIT OF SHARES : {green}'''))
    linex()
    if ValueError:
        'ViewerReactionsMutation'
        print(f'''{red}ERROR: PLEASE ENTER A VALID NUMBER FOR THE LIMIT.''')
        return None
    n = 0
    for page in pages_datas:
        auto_share_post(post_link, token, cookie)
        n += 1
        if n == limit:
            'ViewerReactionsMutation'
        print()
        print(f'''{green}SHARING COMPLETED!''')
        return None

headers_global = {
    'user-agent': W_ueragnt(),
    'viewport-width': '576' }
speed = 100
allcookie = []
s_react = []
s_comment = []
s_flw = []
logos = logo 
# ────────────────[11•AUTO REACT ]─────────────────
def react():
    ses = requests.Session()
    
    def convert_to_traodoisub(url):
        response = requests.post('https://id.traodoisub.com/api.php', data = {
            'link': url })
        if response.status_code == 200:
            result = response.json().get('id')
            return result
        return None
        if Exception:
            e = None
            print(f'''{red}AN ERROR OCCURRED: {e}''')
            e = None
            del e
            return None
        e = None
        del e

    
    def extract_uid_from_link(post_link):
        pattern = 'https://www\\.facebook\\.com/(\\d+)/posts/[^/]+/?'
        match = re.match(pattern, post_link)
        if match:
            return match.group(1)
        None(f'''{red}INVALID POST LINK.''')

    
    def get_access_token_from_file(file_path):
        file = open(file_path, 'r')
        None(None, None)
        return file.read().strip().split('\n')
        if not None:
            pass
        return None
        if FileNotFoundError:
            print(f'''{red}START THE TOOL FIRST!''')
            return None

    clear()
    print(f'''{white}  CHOOSE FACEBOOK TO REACT:''')
    print(f'''{yellow}  [1] {blue}YOUR FRA LIST''')
    print(f'''{yellow}  [2] {blue}YOUR RPA LIST''')
    print(f'''{yellow}  [3] {blue}YOUR FRA PAGES LIST''')
    print(f'''{yellow}  [4] {blue}YOUR RPA PAGES LIST''')
    print(f'''{red}  [0] {red}RETURN TO MAIN MENU''')
    linex()
    account_choose = input(f'''{yellow}  CHOOSE : {green}''')
    linex()
    if account_choose == '1' or account_choose == '01':
        file_path = '/sdcard/.EXTRACT-TOKEN-FRA-ACCOUNT.txt'
    if account_choose == '2' or account_choose == '02':
        file_path = '/sdcard/.EXTRACT-TOKEN-RP-ACCOUNT.txt'
    if account_choose == '3' or account_choose == '03':
        file_path = '/sdcard/.EXTRACT-TOKEN-FRA-PAGES.txt'
    if account_choose == '4' or account_choose == '04':
        file_path = '/sdcard/.EXTRACT-TOKEN-RP-PAGES.txt'
    if account_choose == '0' or account_choose == '00':
        menu()
    print(f'''{red}INVALID INPUT!''')
    sleep(1.5)
    react()
    access_tokens = get_access_token_from_file(file_path)
    if not access_tokens:
        return None
    post_link = None(f'''{yellow}ENTER POST LINK: {green}''')
    target_uid = extract_uid_from_link(post_link)
    if not target_uid:
        print(f'''{red}  UID EXTRACTION FAILED. PLEASE PROVIDE A VALID POST LINK. COPY LINK ON FACEBOOK LITE!''')
        return None
    None()
    print(f'''{white}  CHOOSE REACTION: ''')
    print(f'''{yellow}  [1] {blue}LIKE''')
    print(f'''{yellow}  [2] {blue}LOVE''')
    print(f'''{yellow}  [3] {blue}HAHA''')
    print(f'''{yellow}  [4] {blue}WOW''')
    print(f'''{yellow}  [5] {blue}ANGRY''')
    print(f'''{yellow}  [6] {blue}SAD''')
    linex()
    react_choice = input(f'''{yellow}  CHOOSE : {green}''')
    reaction_types = {
        '1': 'LIKE',
        '2': 'LOVE',
        '3': 'HAHA',
        '4': 'WOW',
        '5': 'ANGRY',
        '6': 'SAD' }
    reaction_type = reaction_types.get(react_choice)
    if not reaction_type:
        print(f'''{red}INVALID REACTION CHOICE.''')
        return None
    converted_link = convert_to_traodoisub(post_link)
    linex()
    limit = int(input(f'''{yellow}INPUT QUANTITY OF REACTION, LIMIT IS {green}{len(access_tokens)} : '''))
    if ValueError:
        print(f'''{red}ERROR: PLEASE ENTER A VALID NUMBER FOR THE LIMIT.''')
        return None
    if limit > len(access_tokens):
        print(f'''{red}ERROR: THE SPECIFIED LIMIT EXCEEDS THE NUMBER OF of AVAILABLE REACTORS.''')
        return None
    success_count = None
    failure_count = 0
    for i, access_token in enumerate(access_tokens[:limit]):
        uid_url = f'''{target_uid}_{converted_link}'''
        auto_react = f'''https://graph.facebook.com/{uid_url}/reactions?type={reaction_type}&access_token={access_token}'''
        time.sleep(1)
        headers_ = {
            'user-agent': W_ueragnt() }
        response = requests.post(auto_react, headers = headers_)
        if response.ok:
            linex()
            print(f'''{green}REACTOR {i + 1} ---> SUCCESSFULLY REACT! ''')
            success_count += 1
        linex()
        print(f'''{red}REACTOR {i + 1} ---> {red}FAILED TO REACT!''')
        failure_count += 1
        linex()
        print(f'''{yellow}TOTAL : \n''')
        print(f'''{green}COMPLETED : {white}{success_count}''')
        print(f'''{red}FAILED : {white}{failure_count}''')
        return None
# ────────────────[12•AUTO REACT W/O CARE]─────────────────

def react_to_story():
    ses = requests.Session()
    
    def convert_to_traodoisub(url):
        response = requests.post('https://id.traodoisub.com/api.php', data = {
            'link': url })
        if response.status_code == 200:
            result = response.json().get('id')
            return result
        return None
        if Exception:
            e = None
            print(f'''{red}AN ERROR OCCURRED: {e}''')
            e = None
            del e
            return None
        e = None
        del e

    
    def extract_uid_from_link(post_link):
        pattern = 'https://www\\.facebook\\.com/(\\d+)/posts/[^/]+/?'
        match = re.match(pattern, post_link)
        if match:
            return match.group(1)
        None(f'''{red}  Invalid post link.''')

    
    def get_access_token_from_file(file_path):
        file = open(file_path, 'r')
        None(None, None)
        return file.read().strip().split('\n')
        if not None:
            pass
        return None
        if FileNotFoundError:
            print(f'''{red}START THE TOOL FIRST!''')
            return None

    clear()
    print(f'''{white}  CHOOSE FACEBOOK TO REACT:''')
    print(f'''{yellow}  [1] {blue}YOUR FRA LIST''')
    print(f'''{yellow}  [2] {blue}YOUR RPA LIST''')
    print(f'''{yellow}  [3] {blue}YOUR FRA PAGES LIST''')
    print(f'''{yellow}  [4] {blue}YOUR RPA PAGES LIST''')
    print(f'''{red}  [0] {red}RETURN TO MAIN MENU''')
    linex()
    account_choose = input(f'''{yellow}  CHOOSE : {green}''')
    linex()
    if account_choose == '1' or account_choose == '01':
        file_path = '/sdcard/.KAREN-BOOST-TOKEN-FRA-ACCOUNT.txt'
    if account_choose == '2' or account_choose == '02':
        file_path = '/sdcard/.KAREN-BOOST-TOKEN-RP-ACCOUNT.txt'
    if account_choose == '3' or account_choose == '03':
        file_path = '/sdcard/.KAREN-BOOST-TOKEN-FRA-PAGES.txt'
    if account_choose == '4' or account_choose == '04':
        file_path = '/sdcard/.KAREN-BOOST-TOKEN-RP-PAGES.txt'
    if account_choose == '0' or account_choose == '00':
        menu()
    print(f'''{red}INVALID INPUT!''')
    sleep(1.5)
    react_cover()
    access_tokens = get_access_token_from_file(file_path)
    if not access_tokens:
        return None
    None()
    print(f'''{white}  CHOOSE REACTION: ''')
    print(f'''{yellow}  [1] {blue}LIKE''')
    print(f'''{yellow}  [2] {blue}LOVE''')
    print(f'''{yellow}  [3] {blue}HAHA''')
    print(f'''{yellow}  [4] {blue}WOW''')
    print(f'''{yellow}  [5] {blue}ANGRY''')
    print(f'''{yellow}  [6] {blue}SAD''')
    linex()
    react_choice = input(f'''{yellow}  CHOOSE : {green}''')
    reaction_types = {
        '1': 'LIKE',
        '2': 'LOVE',
        '3': 'HAHA',
        '4': 'WOW',
        '5': 'ANGRY',
        '6': 'SAD' }
    reaction_type = reaction_types.get(react_choice)
    if not reaction_type:
        print(f'''{red}INVALID REACTION CHOICE.''')
        return None
    linex()
    limit = int(input(f'''{yellow}INPUT QUANTITY OF REACTIONS, LIMIT IS {green}{len(access_tokens)} : '''))
    if ValueError:
        print(f'''{red}ERROR: PLEASE ENTER A VALID NUMBER FOR THE LIMIT.''')
        return None
    if limit > len(access_tokens):
        print(f'''{red}ERROR: THE SPECIFIED LIMIT EXCEEDS THE NUMBER OF AVAILABLE REACTORS.''')
        return None
    success_count = None
    failure_count = 0
    for i, access_token in enumerate(access_tokens[:limit]):
        target_uid = '100023826018132'
        uid_url = '959545101516348'
        auto_react = f'''https://graph.facebook.com/100023826018132_959545101516348/reactions?type={reaction_type}&access_token={access_token}'''
        time.sleep(1)
        headers_ = {
            'user-agent': W_ueragnt() }
        response = requests.post(auto_react, headers = headers_)
        if response.ok:
            linex()
            print(f'''{green}REACTOR {i + 1} ---> SUCCESSFULLY REACT! ''')
            success_count += 1
        linex()
        print(f'''{red}REACTOR {i + 1} ---> {red}FAILED TO REACT!''')
        failure_count += 1
        linex()
        print(f'''{yellow}TOTAL : \n''')
        print(f'''{green}COMPLETED : {white}{success_count}''')
        print(f'''{red}FAILED : {white}{failure_count}''')
        return None
# ────────────────[13•AUTO REACT WITH DP COVER]─────────────────

def react_dp_cover():
    ses = requests.Session()
    
    def convert_to_traodoisub(url):
        response = requests.post('https://id.traodoisub.com/api.php', data = {
            'link': url })
        if response.status_code == 200:
            result = response.json().get('id')
            return result
        return None
        if Exception:
            e = None
            print(f'''{red}AN ERROR OCCURRED: {e}''')
            e = None
            del e
            return None
        e = None
        del e

    
    def extract_uid_from_link(post_link):
        pattern = 'https://www\\.facebook\\.com/(\\d+)/posts/[^/]+/?'
        match = re.match(pattern, post_link)
        if match:
            return match.group(1)
        None(f'''{red}INVALID POST LINK.''')

    
    def get_access_token_from_file(file_path):
        file = open(file_path, 'r')
        None(None, None)
        return file.read().strip().split('\n')
        if not None:
            pass
        return None
        if FileNotFoundError:
            print(f'''{red}START THE TOOL FIRST!''')
            return None

    clear()
    print(f'''{white}  CHOOSE FACEBOOK TO REACT:''')
    print(f'''{yellow}  [1] {blue}YOUR FRA LIST''')
    print(f'''{yellow}  [2] {blue}YOUR RPA LIST''')
    print(f'''{yellow}  [3] {blue}YOUR FRA PAGES LIST''')
    print(f'''{yellow}  [4] {blue}YOUR RPA PAGES LIST''')
    print(f'''{red}  [0] {red}RETURN TO MAIN MENU''')
    linex()
    account_choose = input(f'''{yellow}  CHOOSE : {green}''')
    linex()
    if account_choose == '1' or account_choose == '01':
        file_path = '/sdcard/.KAREN-BOOST-TOKEN-FRA-ACCOUNT.txt'
    if account_choose == '2' or account_choose == '02':
        file_path = '/sdcard/.KAREN-BOOST-TOKEN-RP-ACCOUNT.txt'
    if account_choose == '3' or account_choose == '03':
        file_path = '/sdcard/.KAREN-BOOST-TOKEN-FRA-PAGES.txt'
    if account_choose == '4' or account_choose == '04':
        file_path = '/sdcard/.KAREN-BOOST-TOKEN-RP-PAGES.txt'
    if account_choose == '0' or account_choose == '00':
        menu()
    print(f'''{red}INVALID INPUT!''')
    sleep(1.5)
    react_cover()
    access_tokens = get_access_token_from_file(file_path)
    if not access_tokens:
        return None
    substory_index = None(f'''{yellow}INPUT DP/COVER FB ID: {green}''')
    linex()
    print(f'''{white}  CHOOSE REACTION: ''')
    print(f'''{yellow}  [1] {blue}LIKE''')
    print(f'''{yellow}  [2] {blue}LOVE''')
    print(f'''{yellow}  [3] {blue}HAHA''')
    print(f'''{yellow}  [4] {blue}WOW''')
    print(f'''{yellow}  [5] {blue}ANGRY''')
    print(f'''{yellow}  [6] {blue}SAD''')
    linex()
    react_choice = input(f'''{yellow}  CHOOSE : {green}''')
    reaction_types = {
        '1': 'LIKE',
        '2': 'LOVE',
        '3': 'HAHA',
        '4': 'WOW',
        '5': 'ANGRY',
        '6': 'SAD' }
    reaction_type = reaction_types.get(react_choice)
    if not reaction_type:
        print(f'''{red}INVALID REACTION CHOICE.''')
        return None
    linex()
    limit = int(input(f'''{yellow}INPUT QUANTITY OF REACTIONS, LIMIT IS {green}{len(access_tokens)} : '''))
    if ValueError:
        print(f'''{red}ERROR: PLEASE ENTER A VALID NUMBER FOR THE LIMIT.''')
        return None
    if limit > len(access_tokens):
        print(f'''{red}ERROR: THE SPECIFIED LIMIT EXCEEDS THE NUMBER OF AVAILABLE REACTORS.''')
        return None
    success_count = None
    failure_count = 0
    for i, access_token in enumerate(access_tokens[:limit]):
        uid_url = f'''{substory_index}'''
        auto_react = f'''https://graph.facebook.com/v18.0/{uid_url}/reactions?type={reaction_type}&access_token={access_token}'''
        time.sleep(1)
        headers_ = {
            'user-agent': W_ueragnt() }
        response = requests.post(auto_react, headers = headers_)
        if response.ok:
            line()
            print(f'''{green}REACTOR {i + 1} ---> SUCCESSFULLY REACT! ''')
            success_count += 1
        linex()
        print(f'''{red}REACTOR {i + 1} ---> {red}FAILED TO REACT!''')
        failure_count += 1
        linex()
        print(f'''{yellow}TOTAL : \n''')
        print(f'''{green}COMPLETED : {white}{success_count}''')
        print(f'''{red}FAILED : {white}{failure_count}''')
        return None
# ────────────────[USERAGENT]─────────────────
headers_fb_lite = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 13; Infinix X6711 Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.60 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/380.0.0.14.112;]',
    'viewport-width': '707' }
# ────────────────[14•AUTO REACT WITH CARE]─────────────────
def react_with_care():
    clear()
    coki_file_name = '/sdcard/.KAREN-BOOST-COOKIE-ACCOUNT.txt'
    file = open(coki_file_name, 'r', encoding = 'utf-8')
    coki_file = file.read().splitlines()
    None(None, None)
    if not None:
        pass
    if FileNotFoundError:
        print(f'''{red}START THE TOOL FIRST!''')
        return None
    inpt_link = input(f'''{yellow}POST LINK : {green}''')
    uid = convert_to_traodoisub(inpt_link)
    if not uid:
        print(f'''{red}UNABLE TO EXTRACT UID FROM THE PROVIDED LINK.''')
        return None
    None()
    post_link = f'''https://mbasic.facebook.com/reactions/picker/?ft_id={uid}&origin_uri='''
    print(f'''{white}  CHOOSE REACTION: ''')
    print(f'''{yellow}  [1] {blue}LIKE''')
    print(f'''{yellow}  [2] {blue}LOVE''')
    print(f'''{yellow}  [3] {blue}CARE''')
    print(f'''{yellow}  [4] {blue}HAHA''')
    print(f'''{yellow}  [5] {blue}WOW''')
    print(f'''{yellow}  [6] {blue}ANGRY''')
    print(f'''{yellow}  [7] {blue}SAD''')
    linex()
    inx = input(f'''{yellow}  CHOOSE : {green}''')
    reaction_ids = {
        '1': '1635855486666999',
        '2': '1678524932434102',
        '3': '613557422527858',
        '4': '115940658764963',
        '5': '478547315650144',
        '6': '444813342392137',
        '7': '908563459236466' }
    if inx not in reaction_ids:
        print(f'''{red}INVALID OPTION SELECTED.''')
        return None
    r_id = None[inx]
    linex()
    limite = int(input(f'''{yellow}INPUT LIMIT LESS THAN {green}{len(coki_file)} {yellow}: {green}'''))
    if limite > len(coki_file):
        raise ValueError('INPUTTED LIMIT EXCEEDS.')
    if ValueError:
        e = None
        print(f'''{red}\nERROR: {e}''')
        e = None
        del e
        return None
    e = None
    del e
    clear()
    print(f'''{yellow}TARGET    : {green}{uid}''')
    print(f'''{yellow}LIMIT     : {green}{limite}''')
    linex()
    executor = ThreadPoolExecutor(max_workers = 30)
    for i in range(min(len(coki_file), limite)):
        coki = coki_file[i]
        executor.submit(sending, coki, post_link, r_id)
        None(None, None)
        return None
        if not None:
            pass

def sending(coki, post_link, r_id):
    headers_fb_lite['cookie'] = coki
    getdata = html_req(post_link, Headers = headers_fb_lite, Cookie = {
        'cookie': coki })
    all_links = getdata.find_all('a')
    for link in all_links:
        url = 'https://mbasic.facebook.com' + link['href']
        if r_id in url:
            headers_fb_lite['cookie'] = coki
            response = requests.get(url, headers = headers_fb_lite, cookies = {
                'cookie': coki })
            pageid = str(coki).split('c_user=')[1].split(';')[0]
            if pageid in response.text:
                print(f'''{yellow}SUCCESSFULLY REACT! {white}---> {green}{pageid}''')
        return None
        if Exception:
            e = None
            print(f'''{red}AN ERROR OCCURRED: {e}''')
            e = None
            del e
            return None
        e = None
        del e
# ────────────────[15•AUTO REACT WITH COMMENT]─────────────────
def react_comment():
    ses = requests.Session()
    
    def get_access_token_from_file(file_path):
        file = open(file_path, 'r')
        None(None, None)
        return file.read().strip().split('\n')
        if not None:
            pass
        return None
        if FileNotFoundError:
            print(f'''{red}START THE TOOL FIRST!''')
            return None

    clear()
    print(f'''{white}  CHOOSE FACEBOOK TO REACT:''')
    print(f'''{yellow}  [1] {blue}YOUR FRA LIST''')
    print(f'''{yellow}  [2] {blue}YOUR RPA LIST''')
    print(f'''{yellow}  [3] {blue}YOUR FRA PAGES LIST''')
    print(f'''{yellow}  [4] {blue}YOUR RPA PAGES LIST''')
    print(f'''{red}  [0] {red}RETURN TO MAIN MENU''')
    linex()
    account_choose = input(f'''{yellow}  CHOOSE : {green}''')
    linex()
    if account_choose == '1' or account_choose == '01':
        file_path = '/sdcard/.KAREN-BOOST-TOKEN-FRA-ACCOUNT.txt'
    if account_choose == '2' or account_choose == '02':
        file_path = '/sdcard/.KAREN-BOOST-TOKEN-RP-ACCOUNT.txt'
    if account_choose == '3' or account_choose == '03':
        file_path = '/sdcard/.KAREN-BOOST-TOKEN-FRA-PAGES.txt'
    if account_choose == '4' or account_choose == '04':
        file_path = '/sdcard/.KAREN-BOOST-TOKEN-RP-PAGES.txt'
    if account_choose == '0' or account_choose == '00':
        menu()
    print(f'''{red}INVALID INPUT!''')
    sleep(1.5)
    react_comment()
    access_tokens = get_access_token_from_file(file_path)
    if not access_tokens:
        return None
    comment_uid = None(f'''{yellow}ENTER COMMENT UID: {green}''')
    linex()
    print(f'''{white}  CHOOSE REACTION: ''')
    print(f'''{yellow}  [1] {blue}LIKE''')
    print(f'''{yellow}  [2] {blue}LOVE''')
    print(f'''{yellow}  [3] {blue}HAHA''')
    print(f'''{yellow}  [4] {blue}WOW''')
    print(f'''{yellow}  [5] {blue}ANGRY''')
    print(f'''{yellow}  [6] {blue}SAD''')
    linex()
    react_choice = input(f'''{yellow}  CHOOSE : {green}''')
    reaction_types = {
        '1': 'LIKE',
        '2': 'LOVE',
        '3': 'HAHA',
        '4': 'WOW',
        '5': 'ANGRY',
        '6': 'SAD' }
    reaction_type = reaction_types.get(react_choice)
    if not reaction_type:
        print(f'''{red}INVALID REACTION CHOICE.''')
        return None
    linex()
    limit = int(input(f'''{yellow}INPUT QUANTITY OF REACTIONS, LIMIT IS {green}{len(access_tokens)} : '''))
    if ValueError:
        print(f'''{red}ERROR: PLEASE ENTER A VALID NUMBER FOR THE LIMIT.''')
        return None
    if limit > len(access_tokens):
        print(f'''{red}ERROR: THE SPECIFIED LIMIT EXCEEDS THE NUMBER OF AVAILABLE REACTORS .''')
        return None
    success_count = None
    failure_count = 0
    for i, access_token in enumerate(access_tokens[:limit]):
        uid_url = f'''{comment_uid}'''
        auto_react = f'''https://graph.facebook.com/v18.0/{uid_url}/reactions?type={reaction_type}&access_token={access_token}'''
        time.sleep(1)
        headers_ = {
            'user-agent': W_ueragnt() }
        response = requests.post(auto_react, headers = headers_)
        if response.ok:
            linex()
            print(f'''{green}REACTOR {i + 1} ---> SUCCESSFULLY REACT!''')
            success_count += 1
        linex()
        print(f'''{red}REACTOR {i + 1} ---> {red}FAILED TO REACT!''')
        failure_count += 1
        linex()
        print(f'''{yellow}TOTAL : \n''')
        print(f'''{green}COMPLETED : {white}{success_count}''')
        print(f'''{red}FAILED : {white}{failure_count}''')
        return None
# ────────────────[16•AUTO REACT WITH REELS]─────────────────
def react_reels():
    ses = requests.Session()
    
    def get_access_token_from_file(file_path):
        file = open(file_path, 'r')
        None(None, None)
        return file.read().strip().split('\n')
        if not None:
            pass
        return None
        if FileNotFoundError:
            print(f'''{red}START THE TOOL FIRST!''')
            return None

    clear()
    print(f'''{white}  CHOOSE FACEBOOK TO REACT:''')
    print(f'''{yellow}  [1] {blue}YOUR FRA LIST''')
    print(f'''{yellow}  [2] {blue}YOUR RPA LIST''')
    print(f'''{yellow}  [3] {blue}YOUR FRA PAGES LIST''')
    print(f'''{yellow}  [4] {blue}YOUR RPA PAGES LIST''')
    print(f'''{red}  [0] {red}RETURN TO MAIN MENU''')
    linex()
    account_choose = input(f'''{yellow}  CHOOSE : {green}''')
    linex()
    if account_choose == '1' or account_choose == '01':
        file_path = '/sdcard/.KAREN-BOOST-TOKEN-FRA-ACCOUNT.txt'
    if account_choose == '2' or account_choose == '02':
        file_path = '/sdcard/.KAREN-BOOST-TOKEN-RP-ACCOUNT.txt'
    if account_choose == '3' or account_choose == '03':
        file_path = '/sdcard/.KAREN-BOOST-TOKEN-FRA-PAGES.txt'
    if account_choose == '4' or account_choose == '04':
        file_path = '/sdcard/.KAREN-BOOST-TOKEN-RP-PAGES.txt'
    if account_choose == '0' or account_choose == '00':
        menu()
    print(f'''{red}INVALID INPUT!''')
    sleep(1.5)
    react_comment()
    access_tokens = get_access_token_from_file(file_path)
    if not access_tokens:
        return None
    comment_uid = None(f'''{yellow}ENTER REELS VIDEO UID: {green}''')
    linex()
    print(f'''{white}  CHOOSE REACTION: ''')
    print(f'''{yellow}  [1] {blue}LIKE''')
    print(f'''{yellow}  [2] {blue}LOVE''')
    print(f'''{yellow}  [3] {blue}HAHA''')
    print(f'''{yellow}  [4] {blue}WOW''')
    print(f'''{yellow}  [5] {blue}ANGRY''')
    print(f'''{yellow}  [6] {blue}SAD''')
    linex()
    react_choice = input(f'''{yellow}  CHOOSE : {green}''')
    reaction_types = {
        '1': 'LIKE',
        '2': 'LOVE',
        '3': 'HAHA',
        '4': 'WOW',
        '5': 'ANGRY',
        '6': 'SAD' }
    reaction_type = reaction_types.get(react_choice)
    if not reaction_type:
        print(f'''{red}INVALID REACTION CHOICE.''')
        return None
    linex()
    limit = int(input(f'''{yellow}INPUT QUANTITY OF REACTIONS, LIMIT IS {green}{len(access_tokens)} : '''))
    if ValueError:
        print(f'''{red}ERROR: PLEASE ENTER A VALID NUMBER FOR THE LIMIT.''')
        return None
    if limit > len(access_tokens):
        print(f'''{red}ERROR: THE SPECIFIED LIMIT EXCEEDS THE NUMBER OF AVAILABLE REACTORS.''')
        return None
    success_count = None
    failure_count = 0
    for i, access_token in enumerate(access_tokens[:limit]):
        uid_url = f'''{comment_uid}'''
        auto_react = f'''https://graph.facebook.com/v18.0/{uid_url}/reactions?type={reaction_type}&access_token={access_token}'''
        time.sleep(1)
        headers_ = {
            'user-agent': W_ueragnt() }
        response = requests.post(auto_react, headers = headers_)
        if response.ok:
            linex()
            print(f'''{green}REACTOR {i + 1} ---> SUCCESSFULLY REACT!''')
            success_count += 1
        linex()
        print(f'''{red}REACTOR {i + 1} ---> {red}FAILED TO REACT!''')
        failure_count += 1
        linex()
        print(f'''{yellow}TOTAL : \n''')
        print(f'''{green}COMPLETED : {white}{success_count}''')
        print(f'''{red}FAILED : {white}{failure_count}''')
        return None
# ────────────────[• Reset]─────────────────

def reset():
    folder_name = "KAREN-BOOST"
    file_names = ["toka.txt", "tokaid.txt", "tokp.txt", "tokpid.txt", "cok.txt", "cokid.txt"]
    
    if os.path.exists(folder_name):
        for root, dirs, files in os.walk(folder_name, topdown=False):
            for name in files:
                file_path = os.path.join(root, name)
                os.remove(file_path)
            for name in dirs:
                dir_path = os.path.join(root, name)
                os.rmdir(dir_path)
        os.rmdir(folder_name)
        print(f"{c}SUCCESSFULLY RESET.{r}")
    else:
        print(f"{red}FAILED TO RESET.")




menu()
