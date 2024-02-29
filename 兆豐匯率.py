# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 13:27:45 2022

@author: sian
"""

import pandas as pd
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver

url='https://www.megabank.com.tw/personal/foreign-service/forex'
webdriver_path='C:\webdriver\chromedriver'
path="C:\\Users\\sian\\Desktop\\python\\123\\匯率.xlsx"


df=pd.read_excel(path)
if df['日期'][2]!=datetime.date.today().strftime('%Y-%m-%d'):
    chrome=webdriver.Chrome(webdriver_path)
    chrome.implicitly_wait(10)
    chrome.get(url)
    soup=BeautifulSoup(chrome.page_source,'lxml')   
    tds=soup.find_all('tbody')[1].find_all('td',class_="dollar")[0:4]
    eus=soup.find_all('tbody')[1].find_all('td',class_="dollar")[48:52]
    chrome.quit()
    datas=[]
    year=datetime.datetime.now().date()
    year=year.strftime("%Y")
    td=datetime.date.today().strftime('%Y-%m-%d')
    datas.append(td)
    for td in tds:
        datas.append(td.text)
    for eu in eus:
        datas.append(eu.text)
    datas2=[]
    datas2.append(datas)    
    df.loc[-1]=datas
    df=df.set_index('日期')
    writer=pd.ExcelWriter(path,engine='xlsxwriter')
    df.to_excel(writer,sheet_name=f"{year}",encoding=('tuf-8-sig'))
    writer.save()
else:
    print('今天寫過了')