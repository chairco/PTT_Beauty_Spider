import requests
import urllib2
import re
import os


img_regex = re.compile(r'<img src="(//i.imgur.com/[^"]+jpg)" alt=')
if __name__ == '__main__':
    url = urllib2.urlopen('https://www.ptt.cc/bbs/Beauty/M.1440686753.A.F57.html')
    img_lst = img_regex.findall(url.read())
    img_lst = [ 'https:' + url for url in img_lst ]

    for url in img_lst:
        os.system('wget ' + url)


#   print len(img_lst)
