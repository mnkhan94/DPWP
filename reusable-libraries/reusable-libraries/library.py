class FavoriteSongs(object):
    def __init__(self):
        self.__song_list = []

    def addSong(self, m):
        self.__song_list.append(m)

    def compileList(self):
        output = ""
        for song in self.__song_list: #for eachs song in song array
            output += "<a href="+song.link+">" + '"' + song.title + '"' + "</a><br /><small>"+song.artist+"</small><br />"+song.year+"<hr />"
        return output

    def calc_time_span(self):
        # calculat the time
        # years
        years = []
        for song in self.__song_list:
            years.append(song.year)

        years.sort()
        print years


class Song(object): #Data Object
    def __init__(self):
        self.__title = "" #Validate Title
        self.__artist = ""
        self.__rating = "" #Validate Rating
        self.__year = "" #Validate Rating
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

    # Song Year getter/setter
    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, y):
        self.__year = y


    # Song Artist getter/setter
    @property
    def genre(self):
        return self.__genre

    @rating.setter
    def genre(self, y):
        self.__genre = y