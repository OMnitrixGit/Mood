import pymysql
from typing import *
from parsel import Selector
import httpx
import asyncio
import random
import pickle

class Spider():
    def __init__(self,page) -> None:
        self.headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19"}
        self.path = 'spider_downloads'
        self.url = 'https://www.wallpapermaiden.com/category/anime?page=' + str(page)
        self.download_urls = list(tuple())
        self.page = page

    def connect_db(self):
        conn = pymysql.connect(
        host='bj-cynosdbmysql-grp-rjihok1e.sql.tencentcdb.com',
        port=21280,
        user='root',
        password='X46071496xl',
        db='mood',
        charset='utf8',
       # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
        )
        return conn

    async def __get_download_url__(self,url):
        async with httpx.AsyncClient() as client:
            response = await client.get(url,headers=self.headers)
            download_url = Selector(response.text).css('.wpBig > a::attr(href)').get()
            self.download_urls.append(download_url)


    def get_urls(self):
        response = httpx.get(self.url)
        selector = Selector(response.text)
        wallpaper_list = selector.css('.wallpaperList')
        urls = wallpaper_list.css('.wallpaperBgImage > img::attr(src)').getall()
        labels = wallpaper_list.css('.wallpaperBgImage > img::attr(alt)').getall()
        info = list(zip(labels,map(lambda url:'https://www.wallpapermaiden.com'+url,urls)))
        self.download_urls = info
        # loop = asyncio.get_event_loop()
        # tasks = [
        #     self.__get_download_url__(url)\
        #     for url in urls
        # ]
        # loop.run_until_complete(asyncio.wait(tasks))
        # loop.close()
        
    

    async def parse_single_page(self,url):
        async with httpx.AsyncClient() as client:
            conn = self.connect_db()
            cur = conn.cursor()
            insert_sqli = f"insert into images(liked,labels,url) values(0,'{url[0]}','{url[1]}');"
            cur.execute(insert_sqli)
            conn.commit()
            cur.close()
            conn.close()
            

    def crawl(self)->None:
        try:
            print(f"爬取第{self.page}页的图片")
            self.get_urls()
            loop = asyncio.get_event_loop()
            tasks = [
                self.parse_single_page(url)\
                for url in self.download_urls
            ]
            loop.run_until_complete(asyncio.wait(tasks))
            loop.close()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    page = random.randint(2,955)
    ls = []
    with open("paged.txt","rb") as f:
        ls = pickle.load(f)
    while(page in ls):
        page = random.randint(2,955)
    spider = Spider(page)
    spider.crawl()
    print(f"爬取第{page}页成功!")
    ls.append(page)
    with open("paged.txt","wb") as f:
        pickle.dump(ls,f)

    