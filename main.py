#!/usr/bin/env python

from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.api import memcache
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from JSCompressor import JSCompressor
import os,re,random,logging,string,urllib
import simplejson as json

class Gallery(db.Model):
	title = db.StringProperty()
	rand  = db.StringProperty()
	urls  = db.TextProperty()

class IndexHandler(webapp.RequestHandler):
	def get(self):
		jspath = os.path.join(os.path.dirname(__file__),'albumshare.js')
		scriptString = open(jspath, 'r').read()
		c = JSCompressor(compressionLevel=2, measureCompression=True)
		scriptString = c.compress(scriptString)
		template_values = { 'js': scriptString, }
		path = os.path.join(os.path.dirname(__file__),'index.html')
		self.response.headers['Content-Type'] = 'text/html'
		self.response.out.write(template.render(path, template_values))

class GalleryHandler(webapp.RequestHandler):
	# Retrieve album
	def get(self):
		id  = int(self.request.get('id'))
		uid = self.request.get('uid')
		gallery = Gallery.get_by_id(id)
		
		if (uid != gallery.rand):
			raise Exception('Invalid Gallery URL')
		
		imagesArray = json.loads(gallery.urls)
		
		# Write out to template
		template_values = { 'images': imagesArray, 'title': gallery.title}
		path = os.path.join(os.path.dirname(__file__),'template.html')
		self.response.headers['Content-Type'] = 'text/html'
		self.response.out.write(template.render(path, template_values))
	
	# Post album, if successful, forward to retrieve album page
	def post(self):
		title  = self.request.get('title')
		images = self.request.get('photos')
		
		gallery = Gallery()
		gallery.title = urllib.unquote(title)
		gallery.urls = images
		gallery.rand = "".join([random.choice(string.ascii_letters + string.digits + ".-") for i in xrange(21)])
		gallery.put()
		
		self.redirect("/album?id=%s&uid=%s" % (str(gallery.key().id()),gallery.rand))

def main():
	application = webapp.WSGIApplication([('/album', GalleryHandler),('/', IndexHandler)], debug=False)
	util.run_wsgi_app(application)

if __name__ == '__main__':
	main()