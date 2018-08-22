#coding=utf-8
#if weatherstatus = 1, return the today's weather, if weatherstatus = 0, return the current's weather
weatherstatus = 1
#My Zhixin API:https://www.seniverse.com/
KEY = '45fikpfloeqyzenc'  # API key
UID = "U2248FF108"  # 用户ID

LOCATION = 'shanghai'  # 所查询的位置，可以使用城市拼音、v3 ID、经纬度等

if weatherstatus == 0:
    API = 'https://api.seniverse.com/v3/weather/now.json'  # API URL，可替换为其他 URL
elif weatherstatus == 1:
    API = 'https://api.seniverse.com/v3/weather/daily.json' #API URL

UNIT = 'c'  # 单位
LANGUAGE = 'zh-Hans'  # 查询结果的返回语言
