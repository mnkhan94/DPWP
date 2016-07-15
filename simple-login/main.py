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
			
			<label>Name: <input type="text" />
			<label>Email: <input type="text" />

		</form>
	</body>
</html>'''
        self.response.write(page)

#never touch this. This is just magic.
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
