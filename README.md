# DazDaz
# THIS PROGRAM IS ONLY FOR DAZBEE YOUTUBE. (like FAN MADE)

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
# Title: Top # (View, Likes, or comments) for (Youtube Creators)
# Y-axis: (# of Views, Likes, or comments) - prob bar graph
#         - Start point: lowest number of views, likes, or comments - 1000, 100, or 50
# X-axis: (Title of the videos)
#         If possible, if click the title, go to the link

# Before the graph:
# ask the user what kind of graph they want to see
# show three options: Views, Likes, and Comments
# And one more button (ENTER)

# Classes : GraphCreator, WebScrape, and SaveSQL
# GraphCreator: create Graph (bar graph)
# WebScrape: scraping web (use "https://www.youtube.com/c/Dazbeeee/videos")
# SaveSQL: save the data (id, title, view, like, comment, and link + a(may be the name of other artists if it's collab)

# Final
# In General,
# I didn't add the number of the comments. 
# In main,
# call web scrape class
# In Web Scrape Class,
# set the video link list to get info (song title, info(original artist, etc), view, like, the post date, and link)
# check if the video is a song or not, not to include shorts video, teaser video, etc
# set top 25 views and top 25 likes videos list
# In sql class,
# put info (id, song title, info, view, like, the post date, and the link)
# In CreateGraph class,
# used pylab library

# I referred to some site(s) for this project:
# For web scrape:
# https://www.thepythoncode.com/article/get-youtube-data-python

# During Process,
# At first, I decided to use selenium with chromedriver. 
# But, I changed my mind to use HTML session because it doesn't read whole page somehow (even though I referred to someone's solution) and have short line.
# However, somehow there are some speed issue (too slow, it took over 10 min). So, I fixed second HTML session as request - bs4 way.
# Also, added threading. 
# Although the graph can be displayed in correct data, I found out the matplotlib library cannot display Japanese words (assume Korean, too) So, I fixed it by using pylab.
