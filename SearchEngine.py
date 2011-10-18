import urllib2
from BeautifulSoup import *
from urlparse import urljoin

ignoreWords = set(['a', 'an', 'the', 'of', 'to', 'from', 'for', 'in', 
                   'is', 'it'])

class Crawler
  def __init__(self, dbName):
    pass
  def addToIndex(self, url, soup)
    print "Indexing page: %s" % url

  def crawl(self, pages, depth=2):
    for i in range(depth):
      newpages = set()
      for page in pages:
        try:
          conn = urllib2.urlopen(page)
        except: 
          print "Cannot open page: %s" % page
          continue 
        soup = BeautifulSoup(conn.read())
        self.addToIndex(page, soup)

        links = soup('a')
        for link in links:
          if ('href' in dict(link.attrs)):
            url = urljoin(page, link['href'])
