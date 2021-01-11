import requests
import re
from bs4 import BeautifulSoup

class Spider:

    def __init__(self):
        self.books_url = 'http://books.toscrape.com/'
        self.comment_url = 'https://blog.csdn.net/phoenix/web/v1/comment/list/108858689?page=1&size=10&commentId='
        self.songs_url = 'https://y.qq.com/n/yqq/singer/001fNHEf1SFEFN.html'
        self.lyrics_url = 'https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_yqq.fcg?nobase64=1&musicid=200255722&-=jsonp1&g_tk_new_20200303=359979125&g_tk=359979125&loginUin=2593443648&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'

    def spider_books(self):
        response = requests.get(self.books_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find('ul', class_='nav nav-list').find('ul').find_all('li')

        for item in items:
            kind = item.find('a')
            # print(kind)
            print('分类:'+kind.text.strip()+'\n网址:'+self.books_url+kind['href']+'\n')

    def spider_comments(self):
        headers = {
            'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
        }
        res = requests.get(self.comment_url, headers=headers)
        res_json = res.json()
        comment_lists = res_json['data']['list']
        # print(comment_lists)
        for i in comment_lists:
            print('用户名:' + i['info']['userName'] + '\n评论:' + i['info']['content'])


    def spider_song(self):
        res = requests.get(self.songs_url)
        soup = BeautifulSoup(res.text, 'html.parser')
        item = soup.find('div', class_='mod_songlist').find('ul', class_='songlist__list').find('li', mid='200255722').find('div', class_='songlist__songname').find('span', class_='songlist__songname_txt').find('a', class_='js_song')
        print(item['title'])

    def spider_lyrics(self):
        headers = {
            'origin': 'https://y.qq.com',
            'referer': 'https://y.qq.com/',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
        }
        res = requests.get(self.lyrics_url, headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        # 匹配一个或多个中文字符，\u4e00-\u9fa5表示Unicode中汉字的头和尾
        pat = re.compile(r'[\u4e00-\u9fa5]+')
        result = pat.findall(soup.text)
        result = '\n'.join(result[5:])
        print(res.text)


    def restudy(self):
        line = "Cats are smarter than dogs"
        matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
        if matchObj:
            print("matchObj.group() : ", matchObj.group())
            print("matchObj.group(1) : ", matchObj.group(1))
            print("matchObj.group(2) : ", matchObj.group(2))
        else:
            print("No match!!")

test = Spider()
test.spider_lyrics()