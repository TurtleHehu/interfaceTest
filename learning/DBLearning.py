import pymysql
import readConfig as readConfig
#打开数据库连接

class DbLearing():
    def __init__(self):
        global host, port, user, password, db, sql
        localReadConfig = readConfig.ReadConfig()
        self.host = localReadConfig.get_db('host')
        self.port = int(localReadConfig.get_db('port'))
        self.user = localReadConfig.get_db('username')
        self.password = localReadConfig.get_db('password')
        self.db_name = localReadConfig.get_db('database')
        self.sql = "select Host,User,password_expired from user"

    def connectDb(self):
        db = pymysql.connect(host=self.host,user=self.user,password=self.password,db=self.db_name,port=self.port)
        return db
# 使用cursor()获取操作游标

    def cursor(self):
        db = self.connectDb()
        cur = db.cursor()
        try:
            # 执行数据库操作
            cur.execute(self.sql)
            # 获取所有查询结果
            results = cur.fetchall()
            print("Host","User","password_expired")
            print(results)
            print(results[0][0])
            print(type(results))
            # 遍历结果
            for row in results:
                Host = row[0]
                User = row[1]
                password_expired = row[2]
                print(Host,User,password_expired)
        except Exception as e:
            raise e
        finally:
            db.close()

if __name__ == '__main__':
    db = DbLearing()
    db.cursor()