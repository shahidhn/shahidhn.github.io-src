#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Shahid Hussain Nowshad'
SITENAME = "shahid hussain nowshad"
SITEURL = ''

PATH = '/Users/shahidhn/Documents/Website/shahidhn.github.io-src'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Edits July 27 2017

THEME = '/Users/shahidhn/Documents/Website/pelicanyan/'
TWITTER_ACCOUNT = 'shahidnowshad'
DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'sitemap', 'robots', 'humans')
ROBOTS_SAVE_AS = 'robots.txt'
HUMANS_SAVE_AS = 'humans.txt'
SITEMAP_SAVE_AS = 'sitemap.xml'
STATIC_PATHS = ['images', 'favicon.ico', 'downloads']
DATE_FORMATS = { 'en': '%B %d, %Y', }
# note: this assumes your blog's article images are located in content/images/ and your favicon.ico is located in content/
DISPLAY_PAGES_ON_MENU = True
DEFAULT_DATE = 'fs'
INDEX_SAVE_AS = 'blog_index.html'
SITESUBTITLE = ''
GA_ACCOUNT = 'UA-104461239-1'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
#  	 ('Pelican', 'http://getpelican.com/'),
#        ('Python.org', 'http://python.org/'),
#        ('Jinja2', 'http://jinja.pocoo.org/'),
         ('Blog', 'blog_index.html'),
         ('Projects', 'projects.html'),
#        ('You can modify those links in your config file', '#'),
	)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
