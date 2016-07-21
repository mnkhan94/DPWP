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

		self.response.write(p.print_out())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
