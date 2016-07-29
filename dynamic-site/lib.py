class DataCompiler(object):
    #Initiate the DataCompiler() class with everything set to false.
    # This iway we have a simple way of tracking if anything changes.
    def __init__(self):
        self.__auth_key = False
        self.__pages = False
        self.__wonder = False

    #We will take the data that we get from out controller and set it as an instance.
    def config(self, data):
        self.__pages = data

    #Set everything we get from data argument into a wonder isntance. 
    def collate(self, data):
        self.__wonder = data
        self.__auth_key = True

    @property
    def store(self):
        #If we our GET request is authenticated
        if self.__auth_key:
            #save our Wonder into results variable
            result = self.__wonder
        else:
            # other 
            result = self.__pages
        return result
