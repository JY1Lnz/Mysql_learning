import pymysql

# 打开数据库链接
db = pymysql.connect("localhost", "root", "jyl1126051x", "TESTDB")
# 使用cursor()方式创建一个游标对象
cursor = db.cursor()
# 使用execute()执行操作语句
# 检测EMPLOYEE表是否存在，存在则将其删除
cursor.execute("DROP TABLE IF EXISTS OTHER")
# 创建EMPLOYEE表语句
employee = """CREATE TABLE OTHER(
         FIRST_NAME CHAR(20) NOT NULL,
         LAST_NAME CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT)
         """
cursor.execute(employee)
# 关闭数据库链接
db.close()
