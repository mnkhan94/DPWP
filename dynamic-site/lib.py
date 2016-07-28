class DataCompiler(object):

    def __init__(self):
        self.__auth_key = False
        self.__pages = False
        self.__operation = False


    def config(self, database):
        self.__pages = database


    def collate(self, data):
        self.__operation = data
        local = data['local'].lower()
        image = "image/" + local + ".png"
        self.__operation['image'] = image
        self.__auth_key = True


    @property
    def store(self):
        if self.__auth_key:
            result = self.__operation
        else:
            result = self.__pages
        return result
