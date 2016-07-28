class WondersData(object):
    def __init__(self):

        desciption = [
            "Lorem Ipsum",
            "Lorem Ipsum",
            "Lorem Ipsum",
            "Lorem Ipsum",
            "Lorem Ipsum",
            "Lorem Ipsum",
            "Lorem Ipsum"
        ]

        self.__database = [
            ["title","location","image"],
            ["The Great Wall of China",
                "China",
                "http://foundtheworld.com/wp-content/uploads/2014/10/Great-Wall-of-China-23.jpg",
            desciption[0]],
            ["Christ The Redeemer",
                "Rio de Janeiro, Brazil",
                "https://upload.wikimedia.org/wikipedia/commons/a/ae/Christ_on_Corcovado_mountain.JPG",
            desciption[1]],
            ["Machu Picchu",
                "Peru",
                "http://img0.mxstatic.com/wallpapers/310efc43714ea04445eea08c5f61700b_large.jpeg",
            desciption[2]],
            ["Chichen Itza",
                "Mexico",
                "http://cheapvacationholiday.com/wp-content/uploads/2015/06/Chichen-Itza_date_11.jpg",
            desciption[3]],
            ["Petra",
                "Jordan",
                "https://upload.wikimedia.org/wikipedia/commons/e/ed/Al_khazneh.jpg",
            desciption[4]],
            ["Roman Colosseum",
                "Rome, Italy",
                "https://upload.wikimedia.org/wikipedia/commons/5/53/Colosseum_in_Rome,_Italy_-_April_2007.jpg",
            desciption[5]],
            ["Taj Mahal",
                "Agra, India",
                "http://www.tajmahal.org.uk/gifs/taj-mahal.jpeg",
            desciption[6]]
        ]

    @property
    def database(self):
        wonders = self.__database
        del wonders[0]
        return wonders