# coding=utf-8
from spiders import spiders

s=spiders()
s.getContent('https://v.qq.com/x/list/tv','http(s)?://v.qq.com/x/(.*)')