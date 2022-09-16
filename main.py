# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# THIS PROGRAM IS ONLY FOR DAZBEE YOUTUBE. (FAN MADE LOL)

# this will check the number of views, likes, and comments.
# display them as a graph (prob top 20 or something)
# as y: view, likes, and comments
# as x: title of the video and if click them, open the link
# at start: ask the user what graph they want to see.
# three buttons : views, likes, and comments

# IF POSSIBLE!
# Or, how many video the creator made by genre
# (COVERS, collabs, original songs, or special songs)
# (Also, DAZVillege, too)
# and display the Namuwiki link

# The main purpose of the program is creating graphs with pandas, matplotlib, and other libraries.
# THUS, I might not make other setting that not related in it
# until the program display the graphes(views, likes, comments)
# * for view, the program will also mention the total view *

# What I need for the graph:
# Title: Top # (View, Likes) for (Youtube Creators)
# Y-axis: (# of Views, Likes) - prob bar graph
#         - Start point: lowest number of views, likes, or comments - 1000, 100, or 50
# X-axis: (Title of the videos)
#         If possible, if click the title, go to the link

# Before the graph:
# ask the user what kind of graph they want to see
# show three options: Views, Likes, and Comments
# And one more button (ENTER)


import sqlite3
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import threading
from sklearn.linear_model import LinearRegression
import pandas as pd
from pylab import *
from collections import namedtuple

import SaveSQL
import GraphCreator
import WebScrape

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = WebScrape.Webscrape()
    a.readVideoList()
    a.sql()
    a.gr()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
