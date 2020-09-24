# -*- coding:UTF-8 -*-
import requests
import time
import sys
import json
import yaml
import win32api,win32con

# 学术英语 2400061
# 实用英语 2400051
# 心理健康 2200003
# 学术道德 2200002
course_ids = ['2400061', '2200003', '2200002'] # 想选的课程代码
campus = [u'中关村校区', u'良乡校区'] # 可接受的校区

url = ''
cookie = ''
header = {'Cookie': cookie}
data = {
    'pageIndex': 1,
    'pageSize': 200
}

res = requests.post(url = url, headers = header, data = data)
res_data = res.content
items = json.loads(res_data, encoding='utf-8')['datas']
# print(items[0]['KCMC'])

course_num = len(items)
print('totol course ' + str(course_num))
while(True):
    for i in range(course_num):
        if items[i]['KCDM'] not in course_ids:
            continue
        if items[i]['XQMC'] not in campus:
            continue
        res_hc = items[i]['KXRS'] - items[i]['DQRS']
        if res_hc > 0:
            print(items[i]['KCDM']),
            print(items[i]['KCMC']),
            print(items[i]['BJMC']),
            print(items[i]['XQMC']),
            print(res_hc)
            win32api.MessageBox(0, "course_id: " + items[i]['KCDM'], "!!!!!",win32con.MB_OKCANCEL)
            quit()
