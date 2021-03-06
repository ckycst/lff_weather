#coding=utf-8
import json
import requests
import MySQLdb
import datetime

from confiles.const_value import API, KEY, UNIT, LANGUAGE
from lff_readcitys import CITYS

class WEATHER(object):
    def __init__(self, location):
        self.result = requests.get(API, params={
        'key': KEY,
        'location': location,
        'language': LANGUAGE,
        'unit': UNIT
    }, timeout=10)
        self.result = self.result.json()

    def _insertdata(self):
        self.today = datetime.date.today()

        city  = self.result['results'][0]["location"]['id']
        high  = self.result['results'][0]["daily"][0]['high']
        low   = self.result['results'][0]["daily"][0]['low']
        today = self.result['results'][0]["daily"][0]['date']

        sql = """insert into weather(city, maxtemperature, mintemperature, date) values(%s, %s, %s, %s)"""
        values = (city, high, low, today)
        try:
            cursor.execute(sql, values)
            db.commit()
        except:
            db.rollback()

if __name__ == '__main__':
    city = CITYS()
    citylist1 = city._getcityenname1()
    citylist2 = city._getcityenname2()

    for c in citylist1:
        print c

    db = MySQLdb.connect("localhost", "root", "!Cky2306mysql", "weather", port=3306)
    cursor = db.cursor()
    for c in citylist1:
        weather = WEATHER(c)
        weather._insertdata()

    for c in citylist2:
        weather = WEATHER(c)
        weather._insertdata()

    cursor.close()
    db.close()
