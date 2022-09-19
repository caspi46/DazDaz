import sqlite3
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import threading
from sklearn.linear_model import LinearRegression
import pandas as pd
from pylab import *
from functools import partial
from collections import namedtuple
import plotly.graph_objects as px
import numpy as np
import plotly.graph_objects as go
import webbrowser

class GraphCreator:
    def __init__(self, view_title_link, like_title_link):
        self.view = [ ]
        self.titleV = [ ]
        self. num = [ ]
        self.like = [ ]
        self.titleL = [ ]

        for i in range(25):
            self.num.append("#" + str(i + 1))
            self.view.append(view_title_link[i][0])
            self.titleV.append(view_title_link[i][1])
            self.like.append(like_title_link[i][0])
            self.titleL.append(like_title_link[i][1])
        self.view_di = dict(zip(self.num, view_title_link))
        self.like_di = dict(zip(self.num, like_title_link))

        if self.view == self.like:
            print(True)
        print(False)


    def createTable(self):
        plot = px.Figure(data=[go.Bar(
            name='VIEW',
            x=self.titleV,
            y=self.view
        ),
            go.Bar(
                name='LIKE',
                x=self.titleL,
                y=self.like
            )
        ])
        plot.update_layout(
            updatemenus=[
                dict(
                    type="buttons",
                    direction="left",
                    buttons=list([

                        dict(label="VIEW TOP25",
                             method="update",
                             args=[{"visible": [True, False]},
                                   {"title": "Data 1",
                                    }]),
                        dict(label="LIKE TOP25",
                             method="update",
                             args=[{"visible": [False, True]},
                                   {"title": "Data 2",
                                    }]),
                    ]),
                )
            ])

        plot.show()
        '''
        t = np.arange(0.0, 1.0, 0.01)
        fig, ax = plt.subplots()
        ax.bar(self.num, self.view, width=0.3)
 #       ax.title('TOP 20 VIEWS')
  #      ax.xlabel('VIDEO')
   #     ax.ylabel('VIEWS')
        plt.subplots_adjust(left=0.3)
        # plt.bar(self.view, self.num)

        # adjust radio buttons
        axcolor = 'lightgoldenrodyellow'
        rax = fig.axes([0.05, 0, 0.8, 1],
                       facecolor=axcolor)

        radio = RadioButtons(rax, self.num,
                             25,
                             activecolor='b')
        radio.on_clicked(self.prints)

        plt.show()
'''
    def prints(self, i):
        print("TITLE - VIEW")
        print(self.dics[i][0], " - ", self.dics[i][1])
        webbrowser.open_new_tab(self.dics[i][2])
