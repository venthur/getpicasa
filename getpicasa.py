#!/usr/bin/env python

from xml.dom import minidom
import urllib2
import sys


def main(rssurl):
    print "Fetching the rss file..."
    response = urllib2.urlopen(rssurl)
    rssfile = response.read()
    response.close()

    print "Parsing the rss file..."
    xmldata = minidom.parseString(rssfile)
    tmp = xmldata.getElementsByTagName('media:content')
    for i in tmp:
        url = i.getAttribute('url')
        filename = url.split('/')[-1]
        print "Downloading", filename
        response = urllib2.urlopen(url)
        img = response.read()
        fh = open(filename, 'w')
        fh.write(img)
        fh.close()


if __name__ == "__main__":
    main(sys.argv[1])

