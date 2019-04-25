import pymysql

def query_all_information(table_name):
    db = pymysql.connect("localhost", "root", "jyl1126051x", "TESTDB")
    cursor = db.cursor()
    sql = "SELECT * FROM %s" % \
          table_name
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            for col in row:
                print(col, end=' ')
            print('\n')
    except:
        print("Error: unable to fetch data")
    db.close()

query_all_information('EMPLOYEE')
