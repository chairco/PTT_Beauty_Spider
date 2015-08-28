# -*- coding:utf-8 -*-

import re
import requests

comment_regex = re.compile(u'class="nrec"><span class="hl (f\d)">(\w+)?')
url_regex = re.compile(r'<a href="([^"]+)">')

def reformalize(level):
    if level == None:
        return 100
    elif level[0] == 'X':
        return -10 * int(level[1])


def getPhoto(url):
    photo_page = requests.get(url)
    print photo_page.text




if __name__ == '__main__':
    source = requests.get('https://www.ptt.cc/bbs/Beauty/index1581.html')


    rent_lst = source.text.split('<div class="r-ent">')
    for each_data in rent_lst:

        comment_rate = comment_regex.search(each_data)

        if comment_rate:
            try:
                rate = int(comment_rate.group(2))
            except Exception as err:
                rate = reformalize(comment_rate.group(2))

            print comment_rate.group(1), comment_rate.group(2), rate

            if rate > -100:
                # parse each url
                # get into new page, parse photo
                try:
                    next_page = url_regex.search(each_data).group(1)
                    # print next_page
                    getPhoto('https://www.ptt.cc/' + next_page)
                except Exception as err:
                    pass
