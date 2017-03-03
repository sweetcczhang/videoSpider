#!/usr/bin/python
# coding=utf-8
import uniout
from bs4 import BeautifulSoup
import re
import download_html
import paraser_html
import save_data
import sys
import json


url = sys.argv[1]

downloader = download_html.DownloadHtml()
paraser = paraser_html.HtmlParaser()
save = save_data.SaveData()


html = downloader.download(url)
detail_info_url = paraser.get_video_info_url(html)
detail_html = downloader.download(detail_info_url)
vdieo_info = paraser.get_beautiful_soup(detail_html)
#vdieo_info['url'] = url
sss = json.dumps(vdieo_info, ensure_ascii=False)
print sss



