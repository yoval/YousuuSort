# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 19:50:29 2022

@author: Administrator
"""
import requests,time
import pandas as pd

df = pd.DataFrame()
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Origin': 'https://www.yousuu.com',
    'Referer': 'https://www.yousuu.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
pages = 100
for page in range(pages):  
    params = {'channel': '0','sort': 'scorer','page': str(page+1),'t': str(int(time.time()*1000))}
    print('正在读取第%s页'%str(page+1))
    books = requests.get('https://api.yousuu.com/api/bookStore/books', params=params, headers=headers).json()['data']['books']
    time.sleep(3)
    for book in books:
        book_name = book['title'] #书名
        book_author = book['author'] #作者
        book_score = book['score'] #评分
        book_scorerCount = book['scorerCount'] #人数
        data = {'书名':book_name,'作者':book_author,'评分':book_score,'人数':book_scorerCount}
        df = df.append(data, ignore_index = True)
fileName = time.strftime('%Y-%m-%d', time.localtime(time.time()))
df.to_excel('%s_优书书库.xlsx'%fileName)