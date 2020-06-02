#!/usr/bin/python
# -*- coding: utf-8 -*-
#@Author  :   Hezhing
#@Email   :   Hezhing99@163.com
#@Software:   PyCharm
#@File    :   test.py
#@Time    :   2020/6/2 0:48

import os
import sys
import xlrd
import logging
import requests
import datetime

# 导入定时的包，防止在pyinstaller运行的时候报错
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
os.environ['REQUESTS_CA_BUNDLE'] =  os.path.join(os.path.dirname(sys.argv[0]), 'cacert.pem')

# 读取xlsx
def read_excel(path):
    data = xlrd.open_workbook(path)
    table = data.sheet_by_index(0)
    dataFile = []

    for rowNum in range(table.nrows):
        if rowNum >= 0:
            dataFile.append(table.row_values(rowNum))

    return dataFile

# 获取数据
def get_content():
    contents = []
    dataFile = read_excel('./待办任务.xlsx')
    for msg in dataFile:
        text = msg[0] + ' ' + str(msg[1])
        contents.append(''.join(text))
    content = '    \r\n'.join(contents)
    return content

# 发送消息函数
def send_msg(date,content):
    key = ''
    url = "https://sc.ftqq.com/" + key + ".send"
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}
    title = date + ' 待办任务'

    payload = {'text': title, 'desp': content}
    response = requests.post(url, params=payload, headers=headers)
    if response.json()['errno'] == 0:
        logging.info('发送成功')
    else:
        logging.warning('发送失败 %s' %response.json()['errmsg'])

# 发送消息
def entrance():
    date = datetime.datetime.now().strftime("%Y-%m-%d") # 获取当前时间
    content = get_content()
    send_msg(date, content)

# 主函数
def main():
    Schedulers = BlockingScheduler()
    '''
    day_of_week = 0-6 表示周一到周日每天 
    hour 表示小时
    minute 表示分钟
    second 表示秒
    '''
    trigger = CronTrigger(day_of_week='0-6',hour='10',minute='01',second='0')
    Schedulers.add_job(entrance,trigger)
    print('start') # 测试是否运行
    Schedulers.start()

if __name__ == '__main__':
    main()
