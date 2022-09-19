from pylab import *
import plotly.graph_objects as px
import plotly.graph_objects as go
#import webbrowser

# GraphCreator
# Create Bar Chart (Top 25 views & likes)
class GraphCreator:
    def __init__(self, view_title_link, like_title_link):
        # views info
        self.view = [ ]
        self.titleV = [ ]
        # likes info
        self.like = [ ]
        self.titleL = [ ]
        
        # Set views & likes info
        for i in range(25):
            self.view.append(view_title_link[i][0])
            self.titleV.append(view_title_link[i][1])
            self.like.append(like_title_link[i][0])
            self.titleL.append(like_title_link[i][1])
            
        #self.view_di = dict(zip(self.num, view_title_link))
        #self.like_di = dict(zip(self.num, like_title_link))


    # createTable
    # create bar graph table
    # includes two version (views & likes)
    # two buttons (views & likes)
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

