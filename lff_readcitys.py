#coding=utf-8
import os
import xlrd
# Open the workbook and define the worksheet

class CITYS(object):
    def __init__(self):
        self.citylist1=[]
        self.citylist2=[]
    def _getcityenname1(self):
        ret = os.path.exists("city1.xls")

        if ret == True:
            self.book  = xlrd.open_workbook("city1.xls")
            self.sheet = self.book.sheet_by_name("cncity")
            
            for r in range(0, self.sheet.nrows):
                self.encityname = self.sheet.cell(r,2).value.encode("utf-8")
                self.citylist1.append(self.encityname)
        elif ret == False:
            print "The base file 'city1.xls' is not exist, please check this file!"
        else:
            print "Find base file occur error!"
        return self.citylist1

    def _getcityenname2(self):
        ret = os.path.exists("city2.xls")

        if ret == True:
            self.book  = xlrd.open_workbook("city2.xls")
            self.sheet = self.book.sheet_by_name("cncity")

            for r in range(0, self.sheet.nrows):
                self.encityname = self.sheet.cell(r,2).value.encode("utf-8")
                self.citylist2.append(self.encityname)
        elif ret == False:
            print "The base file 'city1.xls' is not exist, please check this file!"
        else:
            print "Find base file occur error!"
        return self.citylist2

if __name__ == '__main__':
    city = CITYS()
    city._getcityenname1()
    citys = city._getcityenname2()
    for c in citys:
        print c
