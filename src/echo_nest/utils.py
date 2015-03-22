'''
Created on Mar 21, 2015

@author: lnunno
'''
from pyechonest import config
from personify import secret

def init():
    config.ECHO_NEST_API_KEY = secret.ECHO_NEST_API_KEY
    
def truncate_text(text,num_char=80):
    text = (text[:num_char] + '...') if len(text) > num_char else text
    return text

def get_artist_display_image(artist):
    return artist.images[0]['url']

def get_brief_bio(artist):
    bio = artist.biographies[0]
    bio_text = bio['text']
    return truncate_text(bio_text,400)
    
init()