import pymysql

'''
db = pymysql.connect("localhost", "root", "jyl1126051x", "TESTDB")
cursor = db.cursor()
sql = """INSERT INTO EMPLOYEE
         (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
         VALUES
         ("Mac", "Mohan", 20, 'M', 2000)"""

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

db.close()
'''

def insert_information(first_name, last_name, age, sex, income):
    """insert EMPLOYEE information"""
    db = pymysql.connect("localhost", "root", "jyl1126051x", "TESTDB")
    cursor = db.cursor()
    sql = "INSERT INTO EMPLOYEE \
        (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) \
        VALUES \
        ('%s', '%s', %d, '%s', %d)" % \
        (first_name, last_name, age, sex, income)

    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()

insert_information('jin', 'yulin', 18, 'm', 2019)
