# Mood
主要思路：
  1. iOS端App通过网络请求，请求服务器
  2. 服务器查询云数据库，获得图片的相关信息(id,url)等
  3. 服务器以通过HTTP Web应用返回JSON数据，包含以上信息
  4. App通过图片的url获取图片，并进行渲染
  5. 图片的url信息由服务器上的爬虫程序定时爬取(每天凌晨三点)，保证图片的更新
### 路径解释：
  - /Mood 包含App源代码
  - /server：
    - crawer.py 爬虫程序
    - server.py web服务程序
    - nohup.out 程序输出
    - paged.txt 辅助爬虫程序的一个文件
    - run_crawler.sh 爬虫程序启动脚本，由服务器定时任务程序cronb执行
