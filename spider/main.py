#!/usr/bin/python2.7
# coding=utf-8
import uniout
from bs4 import BeautifulSoup
import re
import download_html
import paraser_html
import save_data
import saveToDB

class videoSpider(object):
    def __init__(self):
        self.download_html = download_html.DownloadHtml()
        self.paraser_html = paraser_html.HtmlParaser()
        self.save_data = save_data.SaveData()
        self.savedb = saveToDB.ConnMysql()


    def getVideoInfo(self, base, pre_url):
        page_i = 1
        i = 1
        while True:
            page_url= base+pre_url+'_s_1_d_1_p_'+str(page_i)+'.html'
            print 'page_url:', page_url
            page_html = self.download_html.download(page_url)
            videos = self.paraser_html.get_video_urls(page_html)
            print videos
            if len(videos) == 0 :
                break
            videos_infos = []

            for video in videos :
                video_html = self.download_html.download(video)
                videos_info_url = self.paraser_html.get_video_info_url(video_html)
                if videos_info_url == None:
                    html=video_html
                else :

                    videos_info_html = self.download_html.download(videos_info_url)
                    videos_info_detail = self.paraser_html.get_beautiful_soup(videos_info_html)
                    #videos_info_detail = self.paraser_html.get_movie_info(videos_info_soup)
                    if videos_info_detail ==None:
                        print 'url地址有问题:', videos_info_url
                        continue
                    print '地址：',i,videos_info_url
                    videos_info_detail['url'] = video
                    videos_infos.append(videos_info_detail)
                print 'craw video:', videos_info_url,i
                i=i+1
            self.save_data.savefile2(videos_infos)
            self.savedb.insertDB(videos_infos)
            page_i += 1


    def craw(self, base_url):
        base_html = self.download_html.download(base_url)
        video_types = self.paraser_html.get_video_types(base_html)
        base = 'http://list.youku.com'
        for key in video_types.keys():
            type_url = video_types[key]
            pre_url=re.findall(r'/category/show/c_\d+',type_url)


