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
        <link rel="stylesheet" href="css/main.css" type="text/css" />
    </head>
    <body>'''


        body = '''    <div id="login-form">

        <h1>Sign Up</h1>

        <fieldset>
        <form method="GET">
        <input type="text" name="user" placeholder="Name" />
        <input type="email" name="email" placeholder="Email"/>
        <input type="submit" value="Submit" />
        <footer class="clearfix">

                    <p><span class="info">?</span><a href="#">Forgot Password</a></p>

                </footer>'''


        footer = '''</form>
                </fieldset>

    </div>
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
