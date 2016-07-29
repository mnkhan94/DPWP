class WondersData(object):

    # We are initiating the WondersData() object with two arrays.
    def __init__(self):

        # This is the Description array which will hold the results page details.
        description = [
            ['<iframe width="auto" height="auto" src="https://www.youtube.com/v/23oHqNEqRyo" frameborder="0" allowfullscreen></iframe>',
               "The Great Wall of China is a series of fortifications made of stone, brick, tamped earth, wood, and other materials, generally built along an east-to-west line across the historical northern borders of China - Wikipedia"
            ],
            ['<iframe width="auto" height="auto" src="https://www.youtube.com/v/VOaDuwkGWbg" frameborder="0" allowfullscreen></iframe>',
               "Christ the Redeemer is an Art Deco statue of Jesus Christ in Rio de Janeiro, Brazil, created by Polish-French sculptor Paul Landowski and built by the Brazilian engineer Heitor da Silva Costa, in collaboration with the French engineer Albert Caquot. The face was created by the Romanian artist Gheorghe Leonida. The statue is 30 metres (98 ft) tall, not including its 8-metre (26 ft) pedestal, and its arms stretch 28 metres (92 ft) wide. - Wikipedia"
            ],

            ['<iframe width="auto" height="auto" src="https://www.youtube.com/v/Zk9J5xnTVMA" frameborder="0" allowfullscreen></iframe>',
               "Machu Picchu is a 15th-century Inca citadel situated on a mountain ridge 2,430 metres (7,970 ft) above sea level.[1][2] It is located in the Cusco Region, Urubamba Province, Machupicchu District in Peru,[3] above the Sacred Valley, which is 80 kilometres (50 mi) northwest of Cuzco and through which the Urubamba River flows."
            ],
            ['<iframe width="auto" height="auto" src="https://www.youtube.com/v/kyvw6G9Max0" frameborder="0" allowfullscreen></iframe>',
               "Chichen Itza is a world-famous complex of Mayan ruins on Mexico's Yucatan Peninsula. A massive step pyramid known as El Castillo dominates the 6.5-sq.-km. ancient city, which thrived from around 600 A.D. to the 1200s. Graphic stone carvings survive at structures like the ball court, Temple of the Warriors and the Wall of the Skulls. Nightly sound-and-light shows illuminate the buildings' sophisticated geometry."
            ],
            ['<iframe width="100%" height="100%" src="https://www.youtube.com/v/upOPc0Yl12M" frameborder="0" allowfullscreen></iframe>',
               "Petra originally known as Raqmu to the Nabataeans, is a historical and archaeological city in southern Jordan. The city is famous for its rock-cut architecture and water conduit system. Another name for Petra is the Rose City due to the color of the stone out of which it is carved. Established possibly as early as 312 BC as the capital city of the Arab Nabataeans,[3] it is a symbol of Jordan, as well as Jordan's most-visited tourist attraction.[4] The Nabateans were nomadic Arabs who benefited from the proximity of Petra to the regional trade routes, in becoming a major trading hub, thus enabling them to gather wealth. The Nabateans are also known for their great ability in constructing efficient water collecting methods in the barren deserts and their talent in carving structures into solid rocks.[5] It lies on the slope of Jebel al-Madhbah (identified by some as the biblical Mount Hor[6]) in a basin among the mountains which form the eastern flank of Arabah (Wadi Araba), the large valley running from the Dead Sea to the Gulf of Aqaba. Petra has been a UNESCO World Heritage Site since 1985. - Wikipedia"
            ],
            ['<iframe width="auto" height="auto" src="https://www.youtube.com/v/OOylD1KC6kc" frameborder="0" allowfullscreen></iframe>',
               "The Colosseum or Coliseum, also known as the Flavian Amphitheatre, is an oval amphitheatre in the centre of the city of Rome, Italy. Built of concrete and sand, it is the largest amphitheatre ever built. - Wikipedia"
            ],
            ['<iframe width="auto" height="auto" src="https://www.youtube.com/v/D38DGQkE8eU" frameborder="0" allowfullscreen></iframe>',
                "The Taj Mahal is an ivory-white marble mausoleum on the south bank of the Yamuna river in the Indian city of Agra. It was commissioned in 1632 by the Mughal emperor, Shah Jahan, to house the tomb of his favorite wife, Mumtaz Mahal. - Wikipedia"
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
