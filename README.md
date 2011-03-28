#Facebook Albumshare

Proof of concept for a straightforward way of bypassing Facebook's album privacy measures

##User Guide

(see [http://fbalbumshare.appspot.com](http://fbalbumshare.appspot.com))

1.	Add javascript bookmark to bookmarks bar
+	Browse to a facebook album
+	Click on the bookmark

You will now be taken to an page containing all the images of the album with a unique but publicly browsable url

##Requirements

###Server

+	Google App Engine
+	Python 2.5

###User 

+	Webkit/Gecko based browser (for javascript bookmark)

##Dependencies

+	http://code.google.com/p/simplejson/
+	http://code.activestate.com/recipes/496882-javascript-code-compression/
+	http://www.bram.us/projects/js_bramus/lazierload/