import os
import json
import logging

from google.appengine.api import urlfetch, modules
from flask import Flask, render_template


app = Flask(__name__)

is_dev = not os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/')


def get_host_url(service):
    hostname = modules.get_hostname(module=service)
    #protocol = 'http://' if is_dev else 'https://'
    protocol = 'http://'

    return protocol + hostname + '/'


def get_json(url):
    try:
        result = urlfetch.fetch(url, follow_redirects=False)

        if result.status_code == 200:
            data = json.loads(result.content)
            return data
        else:
            logging.error("Could not retrieve data from {} - status code code: {}".format(url, result.status_code))

    except Exception as e:
        logging.error("Could not retrieve data from {}".format(url))
        logging.exception(e)


services = {
    'dummy': get_host_url('dummy'),
    'movie': get_host_url('movie'),
    'user': get_host_url('user')
}


@app.route('/')
def demo():
    service_urls = {
        'dummy': {
            'base': services['dummy']
        },
        'movie': {
            'base': services['movie'],
            'list': services['movie'] + 'movies/'
        },
        'user': {
            'base': services['user'],
            'internal': services['user'] + 'users/'
        }
    }

    dummy_json = get_json(service_urls['dummy']['base'])
    movies_json = get_json(service_urls['movie']['list'])
    users_json = get_json(service_urls['user']['internal'])

    context = {
        'service_urls': service_urls,
        'dummy_data': dummy_json,
        'movies': movies_json,
        'users': users_json
    }

    return render_template('index.html', **context)