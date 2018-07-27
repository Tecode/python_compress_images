#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
import requests
import pymysql


def request(db, cursor, url, html_id):
    # 关闭不需要的链接
    close = requests.session()
    close.keep_alive = False
    # 设置连接数
    requests.adapters.DEFAULT_RETRIES = 5
    html = requests.get("http://sc.chinaz.com" + url)
    demo_url = re.findall('<iframe id="iframe" src="(.*?)"', html.content)
    print demo_url[0]
    # sql = "INSERT INTO site_html_info(demo_url) VALUES ('%s')" % (demo_url[0])
    sql = "UPDATE site_html_info SET demo_url = '%s' WHERE id = '%s'" % (demo_url[0], html_id)
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()


def selectDB(db, cursor):
    # SQL 查询语句
    # sql = "SELECT `id`, `password` FROM `users` WHERE `email`='huzhiheng@itest.info'"
    sql = "SELECT `link_url`, `id` FROM `site_html_info`"
    cursor.execute(sql)
    # 获取所有记录列表
    result = cursor.fetchall()
    for data in result:
        request(db, cursor, data[0], data[1])


def main():
    # 打开数据库连接
    db = pymysql.Connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='123456',
        db='site_db',
        charset='utf8'
    )
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    selectDB(db, cursor)


if __name__ == "__main__":
    main()
