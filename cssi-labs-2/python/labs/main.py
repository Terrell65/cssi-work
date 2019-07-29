import webapp2
import jinja2
import os

from meme import MemeInfo
from google.appengine.api import urlfetch
import json
# this intializes the jinja2 environment
# same for app i build
#jinja2.Environment is a constructor
jinja_env = jinja2.Environment(
    loader= jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
curl -d 
# meme_templates=['https://i.imgflip.com/23x7zf.jpg', 'https://www.meme-arsenal.com/memes/ef7e4b1d36d712b8e45283ba3267125f.jpg']

class mainpage(webapp2.RequestHandler):
    def get(self):
        api_url = 'https://api.imgflip.com/get_memes'
        imgflip_response = urlfetch.fetch(api_url).content
        imgflip_response_json = json.loads(imgflip_response)
        print(imgflip_response_json['data']['memes'])
        meme_templates = []
        for meme_template in imgflip_response_json['data']['memes']:
            meme_templates.append(meme_template['url'])

        meme_dict = {
            'imgs': meme_templates
        }
        # self.response.headers['content-type'] = 'text/html'
        # self.response.write('<h1>ric is the name</h1>')
        main_template = jinja_env.get_template('main.html')
        self.response.write(main_template.render(meme_dict))
    # def post(self):
    #     top_line = self.request.get('top-line')
    #     print(top_line)
class allmemespage(webapp2.RequestHandler):
    def get(self):
        allusermemes = MemeInfo.query().fetch()
        data1_dict = {
            'allmemes': allusermemes
        }
        allusermemes = jinja_env.get_template('allmemes.html')
        self.response.write(allusermemes.render(data1_dict))

class resultpage(webapp2.RequestHandler):
    def post(self):
        user_top_line = self.request.get('top-line')
        my_line = self.request.get('my-line')
        my_url = self.request.get('template')
        data_dict = {
            "top": user_top_line,
            "my": my_line,
            "url":my_url
        }
        newmeme = MemeInfo(top_line = user_top_line , bottom_line = my_line, meme_url = my_url )
        result_template = jinja_env.get_template('result.html')
        self.response.write(result_template.render(data_dict))
        newmeme.put()




class drippage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['content-type'] = 'text/plain'
        self.response.write('this drippin gone make me a legend')

#the app configuration section
app = webapp2.WSGIApplication(
    [
        ('/', mainpage),
        ('/result',resultpage),
        ('/all',allmemespage)
        # ('/drip',drippage)

    ],
    debug = True
)
