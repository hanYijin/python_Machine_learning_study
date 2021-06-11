import csv
import pymysql


def covidDateSave():
    file= open('info/covid.csv','r', encoding='cp949')
    conn = pymysql.connect(host='localhost', user='root', password='1234', db='covibbs',  charset='utf8')

    rd= csv.reader(file)

    for index, line in enumerate(rd):
        print(index)
        print(line)
        row= tuple(line)
        if index != 0:
            print(int(row[0]), row[1],row[2],row[3])

        try:
            sql = "INSERT INTO seoulCovid VALUES (%s,%s, %s, %s)";
            cursor=conn.cursor()
            if index != 0:
                row=tuple(line)
                cursor.execute(sql, (int(row[0]),row[1],row[2],row[3]))
            conn.commit()
        except Exception as e:
            print(e)
            continue

    #file.close()



