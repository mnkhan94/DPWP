#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import webapp2
from data import *
from pages import *
from lib import *

class MainHandler(webapp2.RequestHandler):
    def get(self):

        secure = WondersData()
        compiler = DataCompiler()
        compiler.config(secure.database)

        if 'wonder' in self.request.GET:
            compiler.collate(secure.auth(self.request.GET['wonder']))
            display = WonderPage(compiler.store)

        else:
            display = LandingPage(compiler.store)

        self.response.write(display.load())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
