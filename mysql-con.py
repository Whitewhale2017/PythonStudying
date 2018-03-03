import pymssql

try:
    conn = pymssql.connect(host='192.168.150.245', user='sa', password='Ytx@123456', database="ecology8")
except Exception as e:
    print(e)
else:
    cur = conn.cursor()
    sqlstr = input("Please input select str:\n")
    cur.execute(sqlstr)
    if (sqlstr[:6].find('select') != -1 or sqlstr[:6].find('SELECT') != -1):
        res = cur.fetchall()
        print(res[1])
    # print(cur.fetchall())
    else:
        conn.commit()
    cur.close()
    conn.close()
