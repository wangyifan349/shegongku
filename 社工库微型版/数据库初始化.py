#encoding:utf-8
#恢复下载问题
import os,sqlite3
if  os.path.exists("./user.db")==False:
    conn=sqlite3.connect('user.db')
    cursor=conn.cursor()
    sql1="create  table  user(id  varchar(100)  primary key,school  varchar(200),xueli  varchar(200),name varchar(20),age int(3),sex varchar(3),homeaddress  varchar(255),QQ varchar(30),wechat varchar(30),telegram  varchar(20),work  varchar(255),fanzui  varchar(255),relatives  varchar(255),phonenumber  varchar(255),idcard  varchar(255))"
    cursor.execute(sql1)
    print("建立数据库")
else:
    print("检测到数据库")
    conn=sqlite3.connect('user.db')
    cursor=conn.cursor()
#sqlinsert1='insert into  user(id,name,age,homeaddress)values("100","wangyifan2","21","山东省威海市环翠区新都二区14号")'
#cursor.execute(sqlinsert1)
a="select * from user"
cursor.execute(a)
ab=cursor.fetchall()
print(ab)
print("当前数据库中有",len(ab),"条记录")
conn.commit()
cursor.close()
conn.close()
