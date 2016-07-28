class DefaultPage(object):
    def __init__(self):
        self.html = {}
        self.build = {}
        self.html['header'] = '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>The 7 Wonders</title>

    <link href="css/styles.css" rel="stylesheet" type="text/css" />
    <script src="https://code.jquery.com/jquery-3.1.0.min.js" integrity="sha256-cCueBR6CsyA4/9szpPfrX3s49M9vUU5BgtiJj06wt/s=" crossorigin="anonymous"></script>

  </head>
  <body>
'''
        self.html['footer'] = '''
    <footer class="footer">
    </footer>

    <script src="js/main.js"></script>

  </body>
</html>
'''

    def load(self):
        self.build_hook()
        output = self.html['header'] + self.html['section'] + self.html['footer']
        return output.format(**self.build)

    def build_hook(self):
        print "build_hook is not available in this module"

class LandingPage(DefaultPage):
    def __init__(self, pages):
        DefaultPage.__init__(self)
        self.pages = pages
        self.html['navbar'] = '''
'''
        self.html['section'] = '''
<section class="intro">
      <div class="left">
        <div>
          <span>Explore</span>
          <h1>The New 7 Wonders</h1>
          <p>The Official New 7 Wonders of the World have been elected by more than 100 million votes to represent global heritage throughout history. The listing is in random order, as announced at the Declaration Ceremony on 07.07.07.

</p>
          <a href="https://unsplash.com/" target="_blank">Images by Unsplash</a>
        </div>
      </div>

      <div class="slider">
        <ul>
{links}
        </ul>

        <ul>
          <nav>
            <a href="#"></a>
            <a href="#"></a>
            <a href="#"></a>
            <a href="#"></a>
            <a href="#"></a>
            <a href="#"></a>
            <a href="#"></a>

          </nav>
        </ul>
      </div>
  </section>
'''

    def build_hook(self):
        self.build['links'] = ""
        for page in self.pages:
            self.build['links'] += ''' 
<li style="background-image:url(%s)">
            <div class="center-y">
            <p>%s</p>
''' % (page[2], page[1]) + '''
<h3>%s</h3>
<a href="/?wonder=%s">View Wonder</a>  
            </div>
          </li>
''' % (page[0],page[0])

class WonderPage(DefaultPage):
    def __init__(self, build):
        DefaultPage.__init__(self)
        self.build = build
        self.html['section'] = '''
    <section>
      <div class="">
        <h1>Hello World!</h1>
      </div>
    </section>
'''
