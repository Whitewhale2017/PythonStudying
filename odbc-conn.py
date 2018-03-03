#!/usr/bin/env python3.6
import pyodbc
encoding = 'UTF-8'

constr = 'DRIVER={SQL Server};SERVER=192.168.150.245;DATABASE=ecology8;UID=sa;PWD=Ytx@123456'#公司测试机
#constr = 'DRIVER={SQL Server};SERVER=localhost;DATABASE=ecology8;UID=sa;PWD=123456'
#constr = 'DRIVER={SQL Server};SERVER=192.168.19.203;DATABASE=ecology8;UID=wangyangyang;PWD=Wyy123456'
try:
    conn = pyodbc.connect(constr)
except Exception as e:
    print(e)
# else:
#      print("Connection is builded!")
cur = conn.cursor()
#sqlstr = input("Please input select str:\n")
str_lchj = input("流程合计数量大于:")
sqlstr = "select * from v_glc_lcdb where 待办流程合计> %d" % int(str_lchj)
try:
    cur.execute(sqlstr)
# print(cur.fetchone())
# print(str(cur.rowcount()))
    result = cur.fetchall()
    fmt = "|{:^8}||{:补<4}||{:^8}||{:^8}|"
    #print('人员ID'.center(8,*))
    print(fmt.format('userID', '{:补^4}'.format('姓名'), 'seclevel', 'sum(lc)'))
    for row in result:
        userid = row[0]
        name = row[1]
        seclevel = row[2]
        lchj = row[5]
        print(fmt.format(str(userid), str(name), str(seclevel), str(lchj)))
except Exception as e:
    print(e)
cur.close()
conn.close()
#测试
