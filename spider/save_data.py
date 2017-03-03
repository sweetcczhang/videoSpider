# coding=utf-8
import uniout

class SaveData(object):

    def __init__(self):
        self.savefile=open('youku_movie_info.txt','wb')

    def savefile2(self, movie_infos):

        for movie_info in movie_infos:
            data = movie_info['url'] + '\t' + movie_info['电影'] + '\t' +'\t' + movie_info['别名'] + '\t' +\
                movie_info['上映'] +'\t'+movie_info['优酷上映'] + '\t' + movie_info['评分'] + '\t' + movie_info['主演'] + '\t' +\
                movie_info['导演'] + '\t' + movie_info['地区'] + '\t' + movie_info['类型'] + '\t' + movie_info['总播放数'] + '\t' +\
                movie_info['评论'] + '\t' + movie_info['顶'] + '\t' + movie_info['简介'] +'\n'

            print data
            self.savefile.write(data)
            self.savefile.flush()

    def close(self):
        self.savefile.close()