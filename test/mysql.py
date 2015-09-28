# -*- coding: utf-8 -*-
import MySQLdb
import django

#打开数据库连接
db=MySQLdb.connect("localhost","root","123456","test")

#使用cursor()方法操作游标
cursor=db.cursor()

#使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

#使用fetchone()方法获取一条数据
data=cursor.fetchone()

print "Database version :%s" % data


#创建数据表
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
sql="""CREATE TABLE EMPLOYEE(
        FIRST_NAME CHAR(20)NOT NULL,
        LAST_NAME CHAR(20) ,
        AGE INT,
        SEX CHAR(1),
        INCOM FLOAT )"""
cursor.execute(sql)

#数据插入操作
sql1="""INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX,INCOM)
        VALUES ('Mac','Mohan',20,'M',2000)"""
try:
    cursor.execute(sql1)
    db.commit()
except:
    db.rollback()

#查询操作
sql2="SELECT * FROM EMPLOYEE WHERE INCOM>'%d'" % (1000)
try:
    cursor.execute(sql2)
    results=cursor.fetchall()
    for row in results:
        fname=row[0]
        lname=row[1]
        age=row[2]
        sex=row[3]
        incom=row[4]
        print "fname=%s,lname=%s,age=%d,sex=%s,incom=%d" % (fname,lname,age,sex,incom)
except:
    print "Error:unable to fetch data"

#更新操作
sql3="UPDATE EMPLOYEE SET AGE=AGE+1 WHERE SEX='%c'" %('M')
try:
    cursor.execute(sql3)
    db.commit()
except:
    db.rollback()
    print 'Error'

#删除操作
sql4="DELETE FROM EMPLOYEE WHERE AGE>'%d'"%(20)
try:
    cursor.execute(sql4)
    db.commit()
except:
    db.rollback()
    print "删除失败"


#关闭数据库
db.close()