#!/usr/bin/env python

'''
Created on Mar 21, 2015

@author: lnunno
'''
import cherrypy
from personify.constants import BASE_DIR
from personify.jinja_init import env
from pyechonest.artist import Artist
from pyechonest import config
from personify import secret

class Personify(object):
    
    def __init__(self):
        config.ECHO_NEST_API_KEY = secret.ECHO_NEST_API_KEY
    
    @cherrypy.expose
    def index(self):
        '''
        Main index page.
        '''
        template = env.get_template('index.html')
        return template.render()
    
    @cherrypy.expose
    def top_artists(self):
        template = env.get_template('top_artists.html')
        return template.render()
    
    @cherrypy.expose
    def artist(self, name):
        '''
        @param name: The name of the artist.
        '''
        template = env.get_template('artist.html')
        artist = Artist(name)
        template.render(artist=artist)
    
    @cherrypy.expose
    def genres(self):
        template = env.get_template('genres.html')
        return template.render()
        
    @cherrypy.expose(alias='404')
    def not_found(self, status, message, traceback, version):
        template = env.get_template('404.html')
        return template.render()
    
if __name__ == '__main__':
    
    instance = Personify()
    
    config = {
              '/':{
                   'tools.sessions.on': True,
                   'tools.staticdir.on': True,
                   'tools.staticdir.root': BASE_DIR,
                   'tools.staticdir.dir': 'static',
                   'error_page.404': instance.not_found
                   }
              }
    cherrypy.server.socket_host = '0.0.0.0'
    cherrypy.server.socket_port = 8080
    cherrypy.quickstart(instance, '/', config=config)