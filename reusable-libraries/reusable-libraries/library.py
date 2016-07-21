class Song(object): #Data Object
	def __init__(self):
		self.title = "" #Validate Title
		self.artist = ""
		self.__rating = "" #Validate Rating
		self.__length = "" #Validate Length
		self.genre = ""
		self.link = ""