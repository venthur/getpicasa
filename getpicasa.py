#!/usr/bin/env python

# Copyright (c) 2010, Bastian Venthur
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
# Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.

"""Download picasa webalbums given a URL."""

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
    if len(sys.argv) < 2:
        print "Usage: %s rss-url" % sys.argv[0]
    main(sys.argv[1])

