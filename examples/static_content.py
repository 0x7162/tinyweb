#!/usr/bin/env micropython
"""
MIT license
(C) Konstantin Belyalov 2017-2018
"""
import tinyweb


# Create web server application
app = tinyweb.webserver()


# Index page
@app.route('/')
@app.route('/index.html')
def index(req, resp):
    # Just send file
    yield from resp.send_file('static/index.simple.html')


# Images
@app.route('/images/<fn>')
def images(req, resp, fn):
    # Send picture. Filename - in parameter
    yield from resp.send_file('static/images/{}'.format(fn))


if __name__ == '__main__':
    app.run()
    # To test your server just open page in browser:
    #   http://localhost:8081
    #   or
    #   http://localhost:8081/index.html
