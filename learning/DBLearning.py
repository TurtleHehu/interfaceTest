import pymysql

#打开数据库连接
db = pymysql.connect(host="127.0.0.1",user="admin",password="123456",db="mysql",port=3306)

# 使用cursor()获取操作游标
cur = db.cursor()

# 查询操作，编写查询语句进行操作
sql = "select Host,User,password_expired from user"

try:
    # 执行数据库操作
    cur.execute(sql)
    # 获取所有查询结果
    results = cur.fetchone()
    print("Host","User","password_expired")
    print(results)
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