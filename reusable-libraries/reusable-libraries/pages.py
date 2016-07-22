class FormPage(object):
    def __init__(self):
        self.__title = "Welcome!"
        self.css = "css/styles.css"
        self.__head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>Create Your Playlist</title>
        <link href="css/styles.css" rel="stylesheet" type="text/css" />
    </head>
    <body>
        """

        self.body = """
        <div class="content">
        <h1>Add a Song</h1>
        <form method"GET" action="" name="form" onsubmit="return validateForm();">
            <input id="title" type="text" placeholder="Song Title:" name="title"/><br>
            <input id="artist" type="text" placeholder="Artist:" name="artist"/><br>
            <input id ="genre" type="text" placeholder="Genre:" name="genre"/><br>
            <input id ="year" type="number" placeholder="Year Released:" name="year"/><br>
            <input id ="rating" type="number" placeholder="Rating:" name="rating"/><br>
            <input id ="link" type="text" placeholder="Youtube Link:" name="link"/><br>

            <input id="submit" class="btn btn-blue" type="submit" value="Add Song" onclick="validateForm()" />
        </form>    """

        # errors go here
        self.__error = ''
        self.__close = """
        </div>
        <script src="js/main.js"></script>
    </body>
</html>
                     """
    # this is a printout function used to write html to the page.

    def print_out(self):
        all = self.__head + self.body + self.__error + self.__close
        return all


class ResultsPage(object):
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
    <div class="content-results">
        """

        self.body = """
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