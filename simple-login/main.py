'''
Mohammad Khan
07/11/16
DPfWP
Simple Form
'''

import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler): #declaring a class
    def get(self):
        header = '''<!DOCTYPE html>
<html>
    <head>
        <title>Simple Form</title>
    </head>
    <body>'''


        body = '''<form method="GET">
        <label>Name:</label><input type="text" name="user" />
        <label>Email:</label><input type="email" name="email" />
        <input type="submit" value="Submit" />'''

        footer = '''</form>
    </body>
</html>
        '''

        if self.request.GET:
            user = self.request.GET["user"]
            email = self.request.GET["email"]
            self.response.write(header + "Thank You, " + user + "! We sent a confirmation email to: " + email + "<hr>" + body + footer)
        else:
            self.response.write(header+body+footer)

#never touch this. This is just magic.
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
