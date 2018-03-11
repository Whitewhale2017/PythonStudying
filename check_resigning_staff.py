import pyodbc
import Check_str_in_table as jc

#constr = 'DRIVER={SQL Server};SERVER=192.168.150.245;DATABASE=ecology8;UID=sa;PWD=Ytx@123456'
constr='DRIVER={SQL Server};SERVER=localhost;DATABASE=ecology8;UID=sa;PWD=123456'
try:
    conn = pyodbc.connect(constr)
except Exception as e:
    print(e)
# print(jc.check_str_in_table(conn, 'Matrixtable_6', '5867'))
cur = conn.cursor()
sqlstr1 = """select id,name from MatrixInfo"""
sqlstr2 = """select id,lastname from hrmresource where status=5"""
sqlstr3 = """select b.rolesmark,c.lastname from HrmRoleMembers a
left join HrmRoles b
on a.roleid=b.id
left join hrmresource c
on a.resourceid=c.id
where c.status=5"""
fmt="{:^20}{:^10}{:^3}"
print(fmt.format('矩阵名称', '人员名称', '数量'))
cur.execute(sqlstr3)
res3 = cur.fetchall()
for r in res3:
    print(fmt.format(r[0], ' ', r[1]))
try:
    cur.execute(sqlstr1)
    res = cur.fetchall()
    for r in res:
        tablename = "Matrixtable_"+str(r[0])
        tabname = r[1]
        try:
            cur.execute(sqlstr2)
            res1 = cur.fetchall()
            for r1 in res1:
                fstr = r1[0]
                fname = r1[1]
                fin = jc.check_str_in_table(conn, tablename, fstr)
                if fin > 0:
                    print(fmt.format(tabname, fname, fin))
        except Exception as e1:
            print(e1)
except Exception as e2:
    print(e2)
