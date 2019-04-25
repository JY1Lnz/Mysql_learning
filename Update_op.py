import pymysql

def update_information():
    db = pymysql.connect("localhost", "root", "jyl1126051x", "TESTDB")
    cursor = db.cursor()
    sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % 'M'
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    db.close()

update_information()
