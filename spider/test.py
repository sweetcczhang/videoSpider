#!/usr/bin/python
# coding=utf-8
import uniout
from bs4 import BeautifulSoup
import re
import download_html
import paraser_html
import save_data
import sys
import saveToDB
import sys



url ='http://v.youku.com/v_show/id_XMTg2NTU2MDg2NA==.html?spm=a2h1n.8251845.0.0'
downloader = download_html.DownloadHtml()
paraser = paraser_html.HtmlParaser()
html=downloader.download(url)
# video_url = paraser.get_video_urls(html)
# print video_url
vedio_url = paraser.get_video_info_url(html)


downloader = download_html.DownloadHtml()
paraser = paraser_html.HtmlParaser()
save = save_data.SaveData()
#spider= main.videoSpider()
db = saveToDB.ConnMysql()
movie_url = 'http://list.youku.com/show/id_zc275562c474811e6a080.html?spm=a2h0j.8191423.sMain.5~5~A!2'
print '传入的参数：', movie_url
# movie_url1 = 'http://list.youku.com/show/id_z6f9e63deffb911e5a080.html?spm=a2h0j.8191423.sMain.5~5~A!2'
# movie_url = 'http://list.youku.com/show/id_zef0a07f820b211e6a080.html?spm=a2h0j.8191423.sMain.5~5~A!2'
movie_html = downloader.download(movie_url,2)
soup = BeautifulSoup(movie_html, 'lxml')
#movie_info = paraser.get_movie_info(soup)
movie_info = paraser.get_zongyi_info(soup)
movie_info['url']=movie_url
#db.insertDB([movie_info])
save.savefile2([movie_info])
