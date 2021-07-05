import csv
import pymysql
def covidDateSave():
    file= open("info/Book.csv","r", encoding='cp949')
    rd= csv.reader(file)
    conn= pymysql.connect(host='localhost', user='root', password='dlwls2955', db='mydb', charset='utf8')
    for index, line in enumerate(rd):
        print(index)
        print(line)
        row = tuple(line)
        if index !=0:
            print(int(row[0]), 'row[1] = ', row[1],'row[2] = ',row[2], 'row[3] = ',row[3], 'row[4] = ',row[4],'row[5] = ',row[5],'row[6] = ',row[6],'row[7] = ',int(row[7]))

        try:
            sql = 'INSERT INTO Book VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
            cursor=conn.cursor()
            if index!=0:
                row=tuple(line)
                cursor.execute(sql, ( int(row[0]), row[1], row[2], row[3],row[4],row[5],row[6],int(row[7])))
            conn.commit()
        except Exception as e:
            print(e)
