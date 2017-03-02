import json
import webapp2
import logging


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps({'message': 'My dummy service!'}))


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)