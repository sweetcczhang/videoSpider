#!/usr/bin/python
# coding=utf-8
import download_html
import paraser_html
import save_data
import sys
import json


#url = sys.argv[1]

url = 'http://v.youku.com/v_show/id_XMjUzMjYwODY0MA==.html?spm=a2h1n.8251845.0.0'

downloader = download_html.DownloadHtml()
paraser = paraser_html.HtmlParaser()
save = save_data.SaveData()


html = downloader.download(url)
detail_info_url = paraser.get_video_info_url(html)
video_type = paraser.get_first_info(html)
print '视频的类型：', video_type

detail_html = downloader.download(detail_info_url)
vdieo_info = paraser.get_beautiful_soup(detail_html, video_type)

sss = json.dumps(vdieo_info, ensure_ascii=False)
print sss



