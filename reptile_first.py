import urllib.request
import urllib
import re
headers = {'Accept': '*/*',
           'Accept-Language': 'en-US,en;q=0.8',
           'Cache-Control': 'max-age=0',
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
           'Connection': 'keep-alive',
           'Referer': 'http://www.baidu.com/'
           }
uapools=[
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    ]
def UA():
    import random
    opener = urllib.request.build_opener()
    thisua = random.choice(uapools)
    ua = ("User-Agent", thisua)
    opener.addheaders = [ua]
    urllib.request.install_opener(opener)
    #print("当前使用UA:" + str(thisua))

for i in range(0, 30):
    if i == 3: continue
    UA()
    if i == 0:
        name_dif = ""
    else:
        name_dif = "/"+str(i+1)
    url = "http://www.midiworld.com/search"+name_dif+"/?q=pop"#+name_dif
    a = urllib.request.Request(url,headers=headers)
    data = urllib.request.urlopen(a).read().decode("utf-8", "ignore")
    pat = 'http://www.midiworld.com/download/.*? '
    rst = re.compile(pat, re.S).findall(data)
    for j in range(0, len(rst)):
        print(rst[j]+ "is downloading...")
        urllib.request.urlretrieve(rst[j],"/home/chi6/Music/pop/"+ str(j) )
        print("-------")
