#!/usr/bin/python2.7
# coding=utf-8
from bs4 import BeautifulSoup
import re
import sys
import urllib2

reload(sys)
sys.setdefaultencoding("utf-8")

class DownloadHtml(object):
    def download(self,base_url,num_retries=2):
        #print 'Download:',base_url
        try:
            html=urllib2.urlopen(base_url).read()
        except urllib2.URLError as e:
            #print "Download error:",e.reason
            html=None
            if num_retries > 0 :
                if hasattr(e,'code') and 500 < e.code() <600 :
                    return self.download(base_url,num_retries-1)
        # print html
        return html
