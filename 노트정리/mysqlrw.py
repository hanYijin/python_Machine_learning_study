import pymysql

# pip install pymysql pymysql 라이브러리 설치
def selectMember():
    conn = pymysql.connect(host='127.0.0.1',user='root',password='1234',db='spro',charset='utf8')
    try:
        sql='select * from member'
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        # print(result)
        for row in result:
            print(row[1],row[2],row[3])
    except:
        pass
    finally:
        conn.close()


def insertMember():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='spro', charset='utf8')
    try:
        sql = 'insert into member (id,pw,name,phone) values (%s,%s,%s,%s)'
        cursor = conn.cursor()
        cursor.execute(sql,('cc','cc','cc','cc'))
        cursor.execute(sql, ('dd', 'dd', 'dd', 'dd'))
        conn.commit()
    except:
        pass
    finally:
        conn.close()