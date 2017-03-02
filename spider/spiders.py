# coding=utf-8

from bs4 import BeautifulSoup
import uniout
import urllib2
import re
class spiders:
    def download(self,url, num_retries=2):
        print 'Download:',url
        try:
            html = urllib2.urlopen(url).read()
        except urllib2.URLError as e:
            print 'Download error:',e.reason
            html=None
            if num_retries > 0:
                if hasattr(e,'code') and 500 <=e.code <600:
                    # recursively retry 5xx HTTP errors
                    return self.download(url,num_retries-1)
        return html

    def getContent(self,url_list,link_regex):
        url_queue=[url_list]
        seen=set(url_queue)
        while url_queue :
            url= url_queue.pop()
            html=self.download(url)
            for link in self.get_links(html):
                if link!=None:
                    if re.match(link_regex,link):
                        if link not in seen:
                            seen.add(link)
                            url_queue.append(link)
                else:
                    continue


    def get_links(self,html):
        if html ==None:
            return None
        else:
            webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)
            return webpage_regex.findall(html)



