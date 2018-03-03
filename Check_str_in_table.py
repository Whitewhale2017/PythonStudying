def check_str_in_table(conn,tablename, findstr): #conn数据库链接
    """验证字符串是否存在与一张表中，通过sql的存储过程实现"""
    cur = conn.cursor()
    sqlstr = """declare @fin int
                exec @fin=isexists_col %s,%s
                select @fin as fin""" % (tablename, findstr)
    try:
        cur.execute(sqlstr)
        res = cur.fetchall()
        return res[0][0]
        # for r in res:
        #     if r[0] > 0:
        #         print(tablename, findstr, r[0])
    except Exception as e1:
        print(e1)
    cur.close()

# print(check_str_in_table.__doc__)




