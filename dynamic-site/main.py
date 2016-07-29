import webapp2
from data import *
from page import *
from lib import *

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #Retrieve the 'Wonders' data from the WondersData() object
        secure = WondersData()

        #Bring in the DataCompiler()
        #This gives us the ability to compile the specific data needed at the moment.
        compiler = DataCompiler()
        compiler.config(secure.data)

        #Using GET we will tell the compiler what specific data we need.

        # If there is a GET request i.e. "?wonder=" in the browser, do this:
        if 'wonder' in self.request.GET:
            compiler.collate(secure.auth(self.request.GET['wonder']))

            # compile the specific Wonder page with details
            display = WonderPage(compiler.store)

        #If there is NO GET request, do this:
        else:

            # Just compile the reguler landing page
            display = LandingPage(compiler.store)

        #Print our compiled result
        self.response.write(display.load())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
