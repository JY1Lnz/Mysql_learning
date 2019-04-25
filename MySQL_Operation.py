import pymysql

class MySql(object):
    """mysql 操作整合"""
    def __init__(self, username, userpd, database):
        """初始化 username为登录用户名
            userpd为登录密码
            database为操作的数据库
        """
        self.database = pymysql.connect("localhost", username, userpd, database)
        self.cursor = self.database.cursor()
    def Close(self):
        self.database.close()

    def CreateTable(self, tablename):
        """创建新表"""
        self.cursor.execute("SHOW TABLES")  # 显示所有表
        result = self.cursor.fetchall()
        for table in result:
            if tablename in table:
                print("表:"+tablename+"已经被创建")
                return False  # 如果表已经被创建则直接返回
        sql = "CREATE TABLE %s ( \
                NAME CHAR(20), \
                NUMBER CHAR(20), \
                SEX CHAR(1) \
                )" % tablename
        self.cursor.execute(sql)
        return True

    def InsertInformation(self, tablename, name, number, sex):
        """给表中插入数据"""
        try:
            sql = "INSERT INTO %s \
                    (NAME, NUMBER, SEX) \
                    VALUES \
                    ('%s', '%s', '%s')" % \
                    (tablename, name, number, sex)
            try:
                self.cursor.execute(sql)
                self.database.commit()
            except:
                self.database.rollback()
        except:
            print("ValueError:this table is not founded")
            return False
        return True

    def QueryInformation(self, tablename):
        try:
            sql = "SELECT * FROM %s" % tablename
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            print("姓名 年龄 性别")
            for row in results:
                for col in row:
                    print(col, end=' ')
                print()
        except:
            print("ValueError:this table is not founded")
            return False
        return True

    def DeleteInformation(self, tablename, isempty=False):
        if isempty:
            try:
                self.cursor.execute("DELETE FROM %s" % tablename)
                self.database.commit()
            except:
                self.database.rollback()

