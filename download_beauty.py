# -*- coding: utf-8 -*-


import urllib
import urllib2
import re
import os

img_regex = re.compile(r'<img src="(//i.imgur.com/[^"]+jpg)" alt=')


def download_pic(pic_url, dir):
    # 尚未處理重複下載的問題
    urllib.urlretrieve(pic_url, dir + '/' + pic_url.split('/')[-1])


def get_pic_list(url_content):

    img_url_list = img_regex.findall(url_content)
    # 將每一個 list 中的 element 都加上 'https' 但是不確定有沒有更適合的做法
    img_url_list = ['https:' + img_url for img_url in img_url_list]
    return img_url_list


def getTitle(content):
    title_start = content.find(r'og:title" content')
    title_end = content[title_start:].find(r'" />')
    title = content[title_start+19:title_start+title_end]
    return title


def store_pic(url):

    # 在 content 方面沒有處理推文，而是全部讀入
    # 如果要處理不包含推文的圖片可以 parse 到該篇文章 url 的地方
    # 因為在推文的前一行有文章網址
    content = urllib2.urlopen(url).read()

    # Get title as dir name
    title = getTitle(content)
    if not os.path.exists(title):
        os.mkdir(title)

    # Download each picture from picture url. In other word, impur address.
    pic_url_list = get_pic_list(content)
    for pic_url in pic_url_list:
        download_pic(pic_url, title)


def main():
    beauty_article_urls = ['https://www.ptt.cc/bbs/Beauty/M.1440778090.A.116.html',
                           'https://www.ptt.cc/bbs/Beauty/M.1440794981.A.112.html',
                           'https://www.ptt.cc/bbs/Beauty/M.1440741576.A.CF3.html',
                           'https://www.ptt.cc/bbs/Beauty/M.1440657889.A.ABB.html',
                           'https://www.ptt.cc/bbs/Beauty/M.1440520890.A.F24.html']

    for article_url in beauty_article_urls:
        # 下載該網頁的圖片
        store_pic(article_url)

if __name__ == '__main__':
    main()
