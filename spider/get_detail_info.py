#!/usr/bin/python2.7
# coding=utf-8
import download_html
import paraser_html
import save_data
import saveToDB
import main


downloader = download_html.DownloadHtml()
paraser = paraser_html.HtmlParaser()
save = save_data.SaveData()
spider = main.videoSpider()
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
pre_url = '/c_96'
spider.getVideoInfo(base_url, pre_url)