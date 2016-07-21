class Song(object): #Data Object
	def __init__(self):
		self.__title = "" #Validate Title
		self.__artist = ""
		self.__rating = "" #Validate Rating
		self.__length = "" #Validate Length
		self.__genre = ""
		self.__link = ""

	# Song Title getter/setter
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, y):
        self.__title = y

	# Song Artist getter/setter
    @property
    def artist(self):
        return self.__artist

    @artist.setter
    def artist(self, y):
        self.__artist = y

	# Song Rating getter/setter
    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, y):
        self.__rating = y

	# Song Length getter/setter
    @property
    def length(self):
        return self.__length

    @rating.setter
    def rating(self, y):
        self.__length = y

	# Song Artist getter/setter
    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, y):
        self.__rating = y