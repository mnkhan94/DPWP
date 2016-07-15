'''
Mohammad Khan
07/11/16
DPfWP
Setting Up Launcher
'''

import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler): #declaring a class
    def get(self): # function that starts everything. Catalyst.
        self.response.write('Hello world!')
        #code goes here

    def additional_functions(self):
    	pass
    	#code goes here

#never touch this. This is just magic.
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
