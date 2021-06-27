# -*- coding: UTF-8 -*-
from flask import Flask
import pymysql
app = Flask(__name__)

@app.get("/")
def read_item():
    conn = pymysql.connect(
        host='bj-cynosdbmysql-grp-rjihok1e.sql.tencentcdb.com',
        port=21280,
        user='root',
        password='X46071496xl',
        db='mood',
        charset='utf8',
       # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
    )
    cur = conn.cursor()
    sqli = "select id,labels,url from images order by time desc limit 10;"
    result = cur.execute(sqli)  # 默认不返回查询结果集， 返回数据记录数。
    info = cur.fetchall()     # 3). 获取所有的查询结果
    info = list(map(lambda tup: {"id":tup[0],"labels":tup[1],"url":tup[2]},info))
    info = {"results":info}
    cur.close()
    conn.close()
    return info





if __name__ == '__main__':
    app.run( host="0.0.0.0", port=443,debug=False,ssl_context=('/root/workspace/lqw/5581010_www.hascats.cn.pem','/root/workspace/lqw/5581010_www.hascats.cn.key'))

