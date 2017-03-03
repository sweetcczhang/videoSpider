# coding=utf-8

from bs4 import BeautifulSoup
import re
import uniout

class HtmlParaser(object):

    ''' 获取视频的地址 '''
    def get_video_urls(self,type_htmls):
        video_links=[]
        soup=BeautifulSoup(type_htmls,'lxml')

        try:
            div_tags=soup.find_all('div', class_='box-series')
            li_tags = div_tags[0].find_all('li', class_='yk-col4 mr1')
            i = 1
            for li_tag in li_tags :

                li_div_tag = li_tag.find(name='div', attrs={'class': 'p-thumb'})

                video_link = li_div_tag.find_all('a')[0]['href']
                if video_link[0:5] != 'http:':
                    video_link = 'http:'+video_link
                #print 'Download:',video_link, i
                i=i+1
                video_links.append(video_link)
        except Exception as e:
            return None
        return video_links

    def get_video_info_url(self,type_htmls):
        soup = BeautifulSoup(type_htmls, 'lxml')
        try:
            div_tags = soup.find_all('div', class_='base_info')
            #print 'div_tags:', div_tags
            a_tags = div_tags[0].find_all('a', class_='desc-link')
            info_url = 'http:' + a_tags[0]['href']
            return  info_url
        except Exception as e:
            return None


    ''' 获取视频的类型 '''
    def get_video_types(self,type_htmls):
        video_types=dict()
        soup=BeautifulSoup(type_htmls,'lxml')
        div_tag=soup.find_all(name='div', class_=re.compile(r'item border'))[0]
        a_tags = div_tag.find_all('a')
        try:
            for a_tag in a_tags :
                video_types[a_tag.getText()]=a_tag['href']
            return video_types
        except Exception as e :
            return None


    def get_movie_info(self,soup):
        i=5
        try:
            movie_msg = soup.find(name='div',attrs={'class': 'p-base'})
            tag_li = movie_msg.find_all(name='li')
            movie_info = dict()
            flags = 0
            movie_names=tag_li[flags].getText().split('：')
            lp=movie_names[1].strip()
            movie_info['电影']=movie_names[1].strip()[0:len(lp)-6]
            flags += 1

            bieming=tag_li[flags].getText().split('：')
            movie_info['别名'] = bieming[1].strip()
            flags += 1

            shangying=tag_li[flags].getText().split('：')
            #print shangying[0].strip()
            if '优酷上映' not in shangying[0].strip():
                movie_info['上映'] = shangying[1].strip()
                flags += 1
            else:
                movie_info['上映'] ='未知\t'
                #print '优酷出品'

            youku_time=tag_li[flags].getText().split('：')
            movie_info['优酷上映'] = youku_time[1].strip()
            flags += 1

            pingfen=tag_li[flags].getText().split('：')
            movie_info['评分'] = pingfen[1].strip()
            flags += 1

            zhuyan = tag_li[flags+i].getText().split('：')
            movie_info['主演'] = zhuyan[1].strip()
            flags += 1

            daoyan=tag_li[flags+i].getText().split('：')
            movie_info['导演'] = daoyan[1].strip()
            flags += 1

            diqu = tag_li[flags+i].getText().split('：')
            movie_info['地区'] = diqu[1].strip()
            flags += 1

            leixing = tag_li[flags+i].getText().split('：')
            movie_info['类型'] = leixing[1].strip()
            flags += 1

            bofangshu = tag_li[flags+i].getText().split('：')
            movie_info['总播放数'] = bofangshu[1].strip()
            flags += 1

            pinglun = tag_li[flags+i].getText().split('：')
            movie_info['评论'] = pinglun[1].strip()
            flags += 1

            ding = tag_li[flags+i].getText().split('：')
            movie_info['顶'] = ding[1].strip()
            flags += 1

            jianjie = tag_li[flags+i+1].getText().split('：')
            movie_info['简介'] = jianjie[1].strip()

            return movie_info
        except:
            return None

    def get_tv_info(self,soup):

        try:
            movie_msg = soup.find(name='div', attrs={'class': 'p-base'})
            tag_li = movie_msg.find_all(name='li')
            movie_info = dict()
            flags = 0
            movie_names = tag_li[flags].getText().split('：')
            lp = movie_names[1].strip()
            movie_info['电视剧'] = movie_names[1].strip()[0:len(lp) - 6]
            flags += 2

            bieming = tag_li[flags].getText().split('：')
            movie_info['别名'] = bieming[1].strip()
            flags += 1

            shangying = tag_li[flags].getText().split('：')
            #print shangying[0].strip()
            if '优酷开播' not in shangying[0].strip():
                movie_info['上映'] = shangying[1].strip()
                flags += 1
            else:
                movie_info['上映'] = '未知\t'
                #print '优酷出品'

            youku_time = tag_li[flags].getText().split('：')
            movie_info['优酷上映'] = youku_time[1].strip()
            flags += 1

            pingfen = tag_li[flags].getText().split('：')
            movie_info['评分'] = pingfen[1].strip()
            flags += 1

            zhuyan = tag_li[flags].getText().split('：')
            movie_info['主演'] = zhuyan[1].strip()
            flags += 1

            daoyan = tag_li[flags].getText().split('：')
            movie_info['导演'] = daoyan[1].strip()
            flags += 1

            diqu = tag_li[flags].getText().split('：')
            movie_info['地区'] = diqu[1].strip()
            flags += 1

            leixing = tag_li[flags].getText().split('：')
            movie_info['类型'] = leixing[1].strip()
            flags += 1

            bofangshu = tag_li[flags].getText().split('：')
            movie_info['总播放数'] = bofangshu[1].strip()
            flags += 1

            pinglun = tag_li[flags].getText().split('：')
            movie_info['评论'] = pinglun[1].strip()
            flags += 1

            ding = tag_li[flags].getText().split('：')
            movie_info['顶'] = ding[1].strip()
            flags += 1

            jianjie = tag_li[flags+1].getText().split('：')
            movie_info['简介'] = jianjie[1].strip()

            return movie_info
        except:
            return None

    def get_zongyi_info(self,soup):

        try:
            movie_msg = soup.find(name='div', attrs={'class': 'p-base'})
            # print 'hhhh'
            tag_li = movie_msg.find_all(name='li')
            movie_info = dict()
            flags = 0

            movie_names = tag_li[flags].getText().split('：')
            lp = movie_names[1].strip()
            movie_info['综艺'] = movie_names[1].strip()[0:len(lp) - 6]
            flags += 2

            zhuchiren = tag_li[flags].getText().split('：')
            movie_info['主持人'] = zhuchiren[1].strip()
            flags += 1

            diqu = tag_li[flags].getText().split('：')
            movie_info['地区'] = diqu[1].strip()
            flags += 1

            bochu = tag_li[flags].getText().split('：')
            movie_info['播出'] = bochu[1].strip()
            flags += 1

            leixing = tag_li[flags].getText().split('：')
            movie_info['类型'] = leixing[1].strip()
            flags += 1

            pingfen = tag_li[flags].getText().split('：')
            movie_info['评分'] = pingfen[1].strip()
            flags += 1

            bofangshu = tag_li[flags].getText().split('：')
            movie_info['总播放数'] = bofangshu[1].strip()
            flags += 1

            pinglun = tag_li[flags].getText().split('：')
            movie_info['评论'] = pinglun[1].strip()
            flags += 1

            ding = tag_li[flags].getText().split('：')
            movie_info['顶'] = ding[1].strip()
            flags += 1

            jianjie = tag_li[flags + 1].getText().split('：')
            movie_info['简介'] = jianjie[1].strip()

            bieming = tag_li[flags].getText().split('：')
            movie_info['别名'] = bieming[1].strip()
            flags += 1

            movie_info['上映'] = '未知\t'

            movie_info['优酷上映'] = '未知\t'

            movie_info['主演'] = '未知\t'

            movie_info['导演'] = '未知\t'

            # print movie_info
            return movie_info
        except:
            return None




    def get_beautiful_soup(self,html):
        soup = BeautifulSoup(html, 'lxml')
        video_info = self.get_movie_info(soup)
        if video_info == None:
            video_info = self.get_tv_info(soup)
        if video_info ==None:
            video_info = self.get_zongyi_info(soup)
        return video_info