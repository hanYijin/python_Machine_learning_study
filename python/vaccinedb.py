import csv
import pymysql

def dateSave():
    file= open('info/vaccine.csv','r', encoding='cp949')
    conn = pymysql.connect(host='jsp.cfy5mbppsewi.us-east-2.rds.amazonaws.com', user='admin', password='12345678', db='JSP',  charset='utf8')

    rd= csv.reader(file)

    for index, line in enumerate(rd):
        print(index)
        print(line)
        row= tuple(line)
        if index != 0:
            print(row[0], row[1],row[2],row[3],row[4],row[5],row[6])

        try:
            sql = "INSERT INTO vaccine (centertype,centerName, operation, facility, postNum, addr, tel) VALUES (%s,%s,%s,%s, %s, %s,%s)"
            cursor=conn.cursor()
            if index != 0:
                row=tuple(line)
                cursor.execute(sql, (row[0], row[1],row[2],row[3],row[4],row[5],row[6]))
            conn.commit()
        except Exception as e:
            print(e)
            continue

    #file.close()
