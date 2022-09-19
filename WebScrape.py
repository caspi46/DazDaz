
from GraphCreator import GraphCreator
from SaveSQL import *
from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup
import threading
import json

# This class webscrape for DAZADAZ project.
# Process,
# read video list (videos) -> go to the link & check their video title
# -> check if the video is a song (loop)
# if so: -> get other info(views, likes, date) -> put their lists
# not: -> continue
# -> set total, view&title, like&title, and the sum of the view & like

# when main calls gr (graph) function,
# set top 25 view & like list -> call GraphCreator

# 9/14/22
class Webscrape:
    def __init__(self):
        self.url = "https://www.youtube.com/c/Dazbeeee/videos"
        self.session = HTMLSession()
        self.song_title = [ ]
        self.view = [ ]
        self.like = [ ]
        self.date = [ ]
        self.link = [ ]
        self.total = [ ]
        self.totalView = 0
        self.totalLike = 0
        self.info = [ ]
        self.view_title_link = [ ]
        self.like_title_link = [ ]
        self.top25_like = [ ]
        self.top25_view = [ ]

    def readVideoList(self):
        response = self.session.get(self.url)
        response.html.render(sleep=1, keep_page=True, scrolldown=26)
        a = response.html.find('a#video-title')
        for links in a:
            link = next(iter(links.absolute_links))
            thd = threading.Thread(target=self.check, args=(link, ))
            thd.start()
            thd.join()
        self.setTotal()
        self.setViewTitle()
        self.setLikeTitle()
        self.totalView = sum(self.view)
        self.totalLike = sum(self.like)
        

    def videoLikes(self, i):
        r = requests.get(i, headers={'User-Agent': ''})
        likes = r.text[:r.text.find(' likes"')]
        like_num = int(likes[likes.rfind('"') + 1:].replace(',', ""))
        self.like.append(like_num)

    def check(self, i):
        condition.acquire()
        res = requests.get(i)
        soup = BeautifulSoup(res.text, 'lxml')
        video_title = soup.find("meta", itemprop="name")["content"]
        if self.splitTitle(video_title):
            self.link.append(i)
            self.videoLikes(i)
            self.date.append(str(soup.find("meta", itemprop="datePublished")["content"]))
            self.view.append(int(soup.find("meta", itemprop="interactionCount")["content"]))
        condition.release()


    def sql(self):
        print("\n\nSQL to create the table from the web\n")
        sq = sqlite()
        sq.connect()
        sq.table("Database")
        for i in range(len(self.song_title)):
            sql_thd = threading.Thread(target=sq.insert, args=(i + 1, self.song_title[i], self.info[i],
                                                               self.view[i], self.like[i],
                                                               self.date[i], self.link[i]))
            sql_thd.start()
            sql_thd.join()
        print("\nAll of the data inserted successfully as BLOBs into a table\n")

    def gr(self):
        self.set_top25_view()
        self.set_top25_like()
        gc = GraphCreator(self.top25_view, self.top25_like)
        gc.createTable()

    def setTotal(self):
        for i in range(len(self.song_title)):
            self.total.append((self.view[i], self.song_title[i], self.like[i], self.date[i], self.info[i], self.link[i]))

    def setViewTitle(self):
        for i in range(len(self.song_title)):
            self.view_title_link.append((self.view[i], self.song_title[i], self.link[i]))

    def setLikeTitle(self):
        for i in range(len(self.song_title)):
            self.like_title_link.append((self.like[i], self.song_title[i], self.link[i]))

    def set_top25_like(self):
        self.like_title_link.sort()
        for i in range(25):
            info_data = self.like_title_link[len(self.view_title_link) - i - 1]
            self.top25_like.append(info_data)

    def set_top25_view(self):
        self.view_title_link.sort()
        for i in range(25):
            info_data = self.view_title_link[len(self.view_title_link) - i - 1]
            self.top25_view.append(info_data)


    def checkExcludes(self, title):
        excludes = ["Teaser", "#Shorts", "#YouTubeMusic", "RELEASED", "Selection Album"]
        for j in excludes:
            if title.find(j) != -1:
                return True
        return False
    def splitTitle(self, t):
        remain = r'\(([^)]+)'
        remove = "\(.*\)|\s-\s."
        remain_original = r'\|'
        excludes = ["Teaser", "#Shorts", "#YouTubeMusic", "RELEASED", "Selection Album"]
        excludes2 = ['  ／', " / ", " ／",
                     "/", "|"]
        # M/V means the video is her original song
        ta = t
        if self.checkExcludes(ta):
            return False
        if t.find('M/V') != -1: # + 'Official Piano Arrange
            self.info.append("ORIGINAL")
            e = re.sub(remove, '', t.split(" | ")[1]).replace('M/V', "")
            self.song_title.append(e)
            return True

        elif t.find('(') != -1 and t.find(')') != 1:  # check world.execute(me); (...)
            artist = re.findall(remain, t)[0]
            self.info.append(artist)
        else:
            self.info.append("UNKNOWN")

        for j in excludes2:
            if t.find(j) != -1:
                e = re.sub(remove, '', t).split(j)
                self.song_title.append(e[0])
                return True
        self.song_title.append(re.sub(remove, '', t))
        return True


