'''
Name: Mohammad Khan
Class: DPW
Assignment: Reusable Library
'''

import webapp2

from pages import *
from library import *

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #song title
        #artist
        #length
        #language
        #song rating
        #song link


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
