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
         <br><br>
                    <label>Element Type: </label><select name="pizzaType">
                    <option value="Water Bender">Water Bender</option>
                    <option value="Air Bender">Air Bender</option>
                    <option value="Fire Bender">Fire Bender</option>
                    <option value="Earth Bender">Earth Bender</option>
                    </select>
                    <br><br>
                    <label>Select Gender: </label> <br>
                    <form>
  <input type="radio" name="gender" value="male" checked> Male<br>
  <input type="radio" name="gender" value="female"> Female<br>
  <input type="radio" name="gender" value="other"> Other
  </form>
                    <br><br>
                    <textarea name="request" rows="10" cols="30">Tell us all about your special skills</textarea>
                    <br><br>
        <input type="submit" value="Submit" />
        <footer class="clearfix">

                    <p><span class="info"><-</span><a href="#">Go back</a></p>

                </footer>'''


        footer = '''</form>
                </fieldset>

    </div>

    <footer style="text-align:center; color: #ffffff">
        Made By Mohammad Khan using Python 2.7
    </footer>
    <br>

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
