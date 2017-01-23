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
import random

def getRandomFortune():
    fortune_list = [
    "You will marry a frog.",
    "Your kids will love Eric Clapton.",
    "You will have a zillion guinea pigs."
    ]

    index = random.randint(0, len(fortune_list)-1)
    #fortune = fortune_list[index]

    return fortune_list[index]


class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookie</h1>"

        fortune = "<strong>" + getRandomFortune() + "</strong>"

        fortune_paragraph = '<p>Your fortune: ' + fortune + '</p>'

        lucky_no = random.randint(1, 100)
        lucky_no = str(lucky_no)
        number_sentence = '<button>Your lucky number is <strong>' + lucky_no +'</strong></button>'
        number_paragraph = '<p>' + number_sentence + "</p>"

        another_cookie = "<a href='.'><button>Give me another cookie please!</button></a>"

        content = header + fortune_paragraph + number_paragraph + another_cookie
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
