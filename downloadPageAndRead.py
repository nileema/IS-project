''' Downloads a HTML page from a given URL and reads it'''
import urllib2

conn = urllib2.urlopen("http://google.com")
contents = conn.read()
print contents[0:2000]
