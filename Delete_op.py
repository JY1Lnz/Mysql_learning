import pymysql

def delete_information():
    db = pymysql.connect("localhost", "root", "jyl1126051x", "TESTDB")
    cursor = db.cursor()
    sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % 20
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()

delete_information()
