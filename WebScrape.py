import sqlite3
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import threading
from sklearn.linear_model import LinearRegression
import pandas as pd
from pylab import *
from collections import namedtuple
from GraphCreator import GraphCreator
from SaveSQL import *
from requests_html import HTMLSession

# This class webscrape for DAZADAZ project.
# In read,
# contens -> the video link & save the link the self.link
# -> title, views, date, comments, likes & save them in the lists
# save the data into sql

# 9/14/22
class Webscrape:
    def __init__(self):
        self.url = "https://www.youtube.com/c/Dazbeeee/videos"
        self.session = HTMLSession()
        self.title = [ ]
        self.song_title = [ ]
        self.view = [ ]
        self.like = [ ]
        self.date = [ ]
        self.link = [ ]
        self.total = [ ]
        self.view_title = [ ]
        self.totalView = 0
        self.info = [ ]
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

    def check(self, i):
        condition.acquire()
        res = requests.get(i)
        soup = BeautifulSoup(res.text, 'lxml')
        title = str(soup.find("meta", itemprop="name")["content"])
        if self.splitTitle(title):
            self.link.append(i)
            self.title.append(str(soup.find("meta", itemprop="name")["content"]))
            self.date.append(str(soup.find("meta", itemprop="datePublished")["content"]))
            self.view.append(int(soup.find("meta", itemprop="interactionCount")["content"]))

        condition.release()


    def sql(self):
        print("\n\nSQL to create the table from the web\n")
        sq = sqlite()
        sq.connect()
        sq.table("Database")
        for i in range(len(self.title)):
            sql_thd = threading.Thread(target=sq.insert, args=(i + 1, self.title[i], self.view[i],
                                                               self.date[i], self.link[i]))
            sql_thd.start()
            sql_thd.join()
        print("\nAll of the data inserted successfully as BLOBs into a table\n")

    def gr(self):
        self.set_top25_view()
        gc = GraphCreator(self.view_title)
        gc.createTable()

    def setTotal(self):
        for i in range(len(self.title)):
            self.total.append((self.view[i], self.song_title[i], self.title[i], self.date[i], self.info[i], self.link[i]))

    def setViewTitle(self):
        for i in range(len(self.title)):
            self.view_title.append((self.view[i], self.song_title[i]))

    def set_top25_view(self):
        self.view_title.sort()


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
        if t.find('M/V') != -1:  # + 'Official Piano Arrange
            self.info.append("Original")
            e = re.sub(remove, '', t.split(" | ")[1])
            self.song_title.append(e)
            return True

        elif t.find('(') != -1 and t.find(')') != 1:  # check world.execute(me); (...)
            artist = re.findall(remain, t)[0]
            self.info.append(artist)
        else:
            self.info.append("NONE")

        for j in excludes2:
            if t.find(j) != -1:
                e = re.sub(remove, '', t).split(j)
                self.song_title.append(e[0])
                return True

        return False





# '未来古代楽団 feat. DAZBEE 「はじまりのまえ、おしまいのあと」【Official Video】'
# 'プラスチック  PLUS+ ／ダズビー COVER  -2014'


