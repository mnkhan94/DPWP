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

        lib = FavoriteSongs()

        # 

        s1 = Song()
        s1.title = "This is what you came for"
        s1.artist = "Calvin Harris"
        s1.rating = "5"
        s1.genre = "Pop"
        s1.link = "https://www.youtube.com/watch?v=Ybo4QvKVHoE"
        lib.addSong(s1)


        # 


        p.body = lib.compileList()
        self.response.write(p.print_out())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
