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
                    videos_info_detail['url'] = videos_info_url
                    videos_infos.append(videos_info_detail)
                print 'craw video:', videos_info_url,i
                i=i+1
            self.save_data.savefile2(videos_infos)
            self.savedb.insertDB(videos_infos)


    def craw(self, base_url):
        base_html = self.download_html.download(base_url)
        video_types = self.paraser_html.get_video_types(base_html)
        base = 'http://list.youku.com'
        for key in video_types.keys():
            type_url = video_types[key]
            pre_url=re.findall(r'/category/show/c_\d+',type_url)


downloader = download_html.DownloadHtml()
paraser = paraser_html.HtmlParaser()
save = save_data.SaveData()
spider= videoSpider()
db = saveToDB.ConnMysql()
# movie_url1 = 'http://list.youku.com/show/id_z6f9e63deffb911e5a080.html?spm=a2h0j.8191423.sMain.5~5~A!2'
# movie_url = 'http://list.youku.com/show/id_zef0a07f820b211e6a080.html?spm=a2h0j.8191423.sMain.5~5~A!2'
# movie_html = downloader.download(movie_url,2)
# soup = BeautifulSoup(movie_html, 'lxml')
# movie_info = paraser.get_movie_info(soup)
# movie_info['url']=movie_url
# db.insertDB([movie_info])
# save.savefile2([movie_info])
base_url = 'http://list.youku.com/category/show'
pre_url = '/c_97'
spider.getVideoInfo(base_url, pre_url)