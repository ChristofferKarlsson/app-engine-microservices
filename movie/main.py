import json
import webapp2


with open('data/movies.json') as f:
    movies = json.loads(f.read())


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Movie service')


class MoviesList(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(movies))


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/movies/', MoviesList),
], debug=True)