# coding = utf-8
#!/usr/bin/python2.7
# coding=utf-8
import uniout
from bs4 import BeautifulSoup
import re
import download_html
import paraser_html
import save_data


url ='http://v.youku.com/v_show/id_XMTg2NTU2MDg2NA==.html?spm=a2h1n.8251845.0.0'
downloader = download_html.DownloadHtml()
paraser = paraser_html.HtmlParaser()
html=downloader.download(url)
# video_url = paraser.get_video_urls(html)
# print video_url
vedio_url = paraser.get_video_info_url(html)

