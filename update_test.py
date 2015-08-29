#!/usr/bin/env python
version = "0.2"

print "Version: %s" % version

rurl = 'https://api.github.com/repos/kalininei/TestingSandBox/releases/latest'

import urllib2
import json

try:
    response = urllib2.urlopen(rurl, timeout=1)
    r = json.loads(response.read())
    print r['tag_name'], r['html_url']
except:
    print (None, None)
