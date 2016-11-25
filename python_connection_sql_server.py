#coding=utf-8
# using python connect with sql server
# sql server is a kind of database
# pymssql Description
# 1.import pymssql for using
# conn=pymssql.connect(..) >  cur=conn.cursor() > cur.execute(..) > (conn.commit()) > (result=cur.fetchone(many|all) for read data) > cur.close() > conn.close()

# 2.function description
# 2.1 pymssql.connect(server='.', user='', password='', database='', timeout=0, login_timeout=60, charset='UTF-8', as_dict=False, host='', appname=None, port='1433', conn_properties, autocommit=False, tds_version='7.1')
#         ----Constructor for creating a connection to the database. Returns a Connection object.

# 2.2 Connection object methods
# 2.2.1 Connection.autocommit(status)  ---Where status is a boolean value. This method turns autocommit mode on or off.
#                                         By default, autocommit mode is off, what means every transaction must be explicitly committed if changed data is to be persisted in the database.
#                                         You can turn autocommit mode on, what means every single operation commits itself as soon as it succeeds.
# 2.2.2 Connection.cursor()   ---Return a cursor object, that can be used to make queries and fetch results from the database
# 2.2.3 Connection.commit()   ---Commit current transaction. You must call this method to persist your data if you leave autocommit at its default value, which is false
# 2.2.4 Connection.rollback()  ---Roll back current transaction
# 2.2.5 Connection.close()     ---Close the connection

# 2.3 Cusor object methods
# 2.3.1 Cursor.execute(operation)/Cursor.execute(operation, params) --Sql statement execution,You must call Connection.commit()
#                                                                    after execute() or your data will not be persisted in the database.
#                                                                   You can also set connection.autocommit if you want it to be done automatically
# 2.3.2 Cursor.executemany(operation, params_seq)   --operation is a string and params_seq is a sequence of tuples (e.g. a list).
#                                                     Execute a database operation repeatedly for each element in parameter sequence.
# 2.3.3 Cursor.fetchone()   --Fetch the next row of a query result, returning a tuple, or a dictionary if as_dict was passed to pymssql.connect(), or None if no more data is available
# 2.3.4 Cursor.fetchmany(size=None)  --Fetch the next batch of rows of a query result, returning a list of tuples, or a list of dictionaries if as_dict was passed to pymssql.connect(), or an empty list if no more data is available
# 2.3.5 Cursor.fetchall()    --Fetch all remaining rows of a query result, returning a list of tuples, or a list of dictionaries if as_dict was passed to pymssql.connect(), or an empty list if no more data is available
# 2.3.6 Cursor.nextset()   --This method makes the cursor skip to the next available result set, discarding any remaining rows from the current set. Returns True value if next result is available, None if not
# 2.3.7 Cursor.close()   --Close the cursor. The cursor is unusable from this point.
import sys
import pymssql

class MSSQL:
    def __init__(self,host,user,pwd,db):
        self.host=host
        self.user=user
        self.pwd=pwd
        self.db=db

    def __GetConnect(self):
        if not self.db:
            raise(NameError,"没有设置数据库信息")
        self.conn=pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset='GB2312')
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"连接数据库失败")
        else:
            return cur

    def ExecQuery(self,sql):
        cur=self.__GetConnect()
        cur.execute(sql)
        resList=cur.fetchall()

        self.conn.close()
        return resList

    def ExecNonQuery(self,sql):
        cur=self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

if __name__=="__main__":
    # 将连接语句中的server地址修改成数据库引擎的名称，用本机ip、localhost、127.0.0.1都会产生以上的那个错误(20009)。
    ms=MSSQL(host='LAPTOP-VMLSAG1J\MRXIAOKE',user='sa',pwd='sa',db='Mingri')
    relist=ms.ExecQuery('SELECT * FROM price_one')
    for i in relist:
        print i[0],i[1],i[2]





