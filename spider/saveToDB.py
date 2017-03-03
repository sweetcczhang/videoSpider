#!/usr/bin/python2.7
# _*_ coding: utf-8 _*_

import  MySQLdb as mdb
import uniout

# 连接数据库
class ConnMysql:

    def connDB(self):
        conn = mdb.connect(host='111.207.243.70', port=3606, user='root', passwd='cYz#P@ss%w0rd$868', db='video_information_mining', charset='utf8')
        return conn


    def insertDB(self,video_info):
        conn=self.connDB()
        cur = conn.cursor()
        t_name = 'youku_movie_info'
        sql="INSERT INTO youku_movie_info(video_url, leibie, video_name, bieming, shangying, youkushangying, pingfen, " \
                "actor, daoyan, diqu, leixing, bofangshu, pinglunshu, ding, jianjie)" \
                "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            for video in video_info:
                para = [video['url'],
                        video['leibie'],
                        video['电影'],
                        video['别名'],
                        video['上映'],
                        video['优酷上映'],
                        video['评分'],
                        video['主演'],
                        video['导演'],
                        video['地区'],
                        video['类型'],
                        video['总播放数'],
                        video['评论'],
                        video['顶'],
                        video['简介'] ]
                cur.execute(sql, para)
            cout = cur.execute('SELECT * FROM %s' % t_name)
            conn.commit()
            print '数据库条数：',cout
        except Exception as e:
            print '数据库插入失败'
            conn.rollback()
        conn.close()

