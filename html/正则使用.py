#coding:utf-8
import cgi
import MySQLdb as sql
import time

data = cgi.FieldStorage()





file_name = "web-6.html"
with open(file_name,'r+') as file:
    str1 = file.read()
    str2 = str1.replace("categories:","")
    str2 = str2.replace("seriesreplace", "")
    fl = open('.//getInfo//index.html', 'w')
    fl.write(str2)

    con = sql.connect(user='root', passwd='xuegod123', db='test', host='localhost')
    cur = con.cursor()
    for key in data.keys():
        cur.execute("insert into test (inFo,value,time) VALUE ('%s','%s',%d);" % (
        str(key).decode("GBK"), data[key].value, int(time.time())))

con.commit()
cur.close()
con.close()

# categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#           {
#                 name: 'Tokyo',
#                 data: [7.0, 6.9, 6.5, 14.5, 16.2, 21.5, 24.2, 26.5, 28.3, 18.3, 12.9, 9.6]
#             }