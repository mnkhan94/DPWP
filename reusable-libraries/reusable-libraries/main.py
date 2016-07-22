'''
Name: Mohammad Khan
Class: DPW
Assignment: Reusable Library
'''

import webapp2

from pages import FormPage, ResultsPage
from library import *

class MainHandler(webapp2.RequestHandler):
    def get(self):
        
        p = FormPage()
        p = ResultsPage()

        lib = FavoriteSongs()

        # Dummy Content

        s1 = Song()
        s1.title = "This is what you came for"
        s1.artist = "Calvin Harris"
        s1.year = "2016"
        s1.rating = "5"
        s1.genre = "House"
        s1.link = "https://www.youtube.com/watch?v=kOkQ4T5WO9E"
        lib.addSong(s1)

        s2 = Song()
        s2.title = "Love Me Again"
        s2.artist = "John Newman"
        s2.year = "2013"
        s2.rating = "5"
        s2.genre = "Northern Soul"
        s2.link = "https://www.youtube.com/watch?v=CfihYWRWRTQ"
        lib.addSong(s2)

        s3 = Song()
        s3.title = "Genghis Khan"
        s3.artist = "Miike Snow"
        s3.year = "2015"
        s3.rating = "5"
        s3.genre = "Pop"
        s3.link = "https://www.youtube.com/watch?v=P_SlAzsXa7E"
        lib.addSong(s3)


        # Dummy Content

        # if a GET request is sent then get the inputted values and show the songs list page
        if self.request.GET:
            song1 = Song()
            song1.title = self.request.GET['title']
            song1.artist = self.request.GET['artist']
            song1.year = self.request.GET['year']
            song1.rating = self.request.GET['rating']
            song1.genre = self.request.GET['genre']
            song1.link = self.request.GET['link']
            lib.addSong(song1)
            p = ResultsPage()
            p.body = lib.compileList()

        # if not, keep up the form
        else:
            p = FormPage()



        self.response.write(p.print_out())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
