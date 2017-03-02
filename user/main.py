import json
import webapp2
import logging

from google.appengine.api import app_identity


with open('data/users.json') as f:
    users = json.loads(f.read())

app_id = app_identity.get_application_id()


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('User service')


class UserList(webapp2.RequestHandler):
    def get(self):
        incoming_app_id = self.request.headers.get('X-Appengine-Inbound-Appid', None)

        if incoming_app_id != app_id:
            logging.error("Access denied for App ID: {}".format(incoming_app_id))
            self.abort(403)

        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(users))


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/users/', UserList),
], debug=True)