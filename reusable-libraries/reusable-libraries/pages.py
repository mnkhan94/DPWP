class FormPage(object):
    def __init__(self):
        self.__css = ""
        self.__title = ""
        self.__head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Create A Playlist</title>
        <link href="css/styles.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        """

        self.body = """
<h1>Hello World!</h1>
        """

        self.__close = """
        </div>
        <script src="js/main.js"></script>
    </body>
</html>
        """

    def print_out(self):
        all = self.__head + self.body + self.__close
        return all


class ResultsPage(object):
    def __init__(self):
        pass