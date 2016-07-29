class WondersData(object):

    # We are initiating the WondersData() object with two arrays.
    def __init__(self):

        # This is the Description array which will hold the results page details.
        description = [
            ["Lorem Ipsum",
               "Hello Youtuube"
            ],
            ["Lorem Ipsum",
               ""
            ],
            ["Lorem Ipsum",
               ""
            ],
            ["Lorem Ipsum",
               ""
            ],
            ["Lorem Ipsum",
               ""
            ],
            ["Lorem Ipsum",
               ""
            ],
            ["Lorem Ipsum",
               ""
            ]
        ]

        # This is the basic set of wonder details. We will be calling this upon launch.
        self.__database = [
            ["title","name","image", "description"],
            ["The Great Wall of China",
                "China",
                "http://foundtheworld.com/wp-content/uploads/2014/10/Great-Wall-of-China-23.jpg",
            description[0]],
            ["Christ The Redeemer",
                "Rio de Janeiro, Brazil",
                "https://upload.wikimedia.org/wikipedia/commons/a/ae/Christ_on_Corcovado_mountain.JPG",
            description[1]],
            ["Machu Picchu",
                "Peru",
                "http://img0.mxstatic.com/wallpapers/310efc43714ea04445eea08c5f61700b_large.jpeg",
            description[2]],
            ["Chichen Itza",
                "Mexico",
                "http://cheapvacationholiday.com/wp-content/uploads/2015/06/Chichen-Itza_date_11.jpg",
            description[3]],
            ["Petra",
                "Jordan",
                "https://upload.wikimedia.org/wikipedia/commons/e/ed/Al_khazneh.jpg",
            description[4]],
            ["Roman Colosseum",
                "Rome, Italy",
                "https://upload.wikimedia.org/wikipedia/commons/5/53/Colosseum_in_Rome,_Italy_-_April_2007.jpg",
            description[5]],
            ["Taj Mahal",
                "Agra, India",
                "http://www.tajmahal.org.uk/gifs/taj-mahal.jpeg",
            description[6]]
        ]

    #This GETTER will cycle through the list of Wonders and set them to one neat and clean Array that holds eveything for us.
    @property
    def data(self):
        op_names = []
        for ops in self.__database:
            op_names.append(ops)
        del op_names[0]
        return op_names

    #This Method takes tries finding the requested ky in the DB and returns it for our show page.
    def auth(self, op):
        op_data = {}
        search = (ops for ops in self.__database if ops[0] == op).next()
        i = 0
        for key in self.__database[0]:
            op_data[key] = search[i]
            i += 1
        return op_data
