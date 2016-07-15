'''
Mohammad Khan
07/11/16
DPfWP
Simple Form
'''

import webapp2 #use the webapp2 library

class MainHandler(webapp2.RequestHandler): #declaring a class
    def get(self): # function that starts everything. Catalyst.
        page = '''<!DOCTYPE HTML>
<html>
	<head>
		<title>Simple Form</title>
	</head>
	<body>
		<form method="GET">
			
			<label>Name: <input type="text" name="user" />
			<label>Email: <input type="text" name="email" />
			<input type="submit" value="Submit" />

		</form>
	</body>
</html>'''
	if self.request.GET:
		user = self.request.GET['user']
		email = self.request.GET['email']

		print "Hi " + user + "!"

        self.response.write(page) #PRINT 


#never touch this. This is just magic.
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
