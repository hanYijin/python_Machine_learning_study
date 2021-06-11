import csv
import pymysql


def read_csv_write_mysql():
    file = open("info/daegu.csv", "r", encoding='utf8')
    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='spro', charset='utf8')
    curs = conn.cursor()
    sql = "INSERT INTO daegu " \
          "(  idx, name, location, code1, code1_name," \
          "  code2, code2_name, code_3, code4, code4_name, " \
          "  code_sido, code_sidoname, code_gu, code_guname, code_dong," \
          "  code_dongname, code_legar, code_legarname, code_jibun, code_jibunname," \
          "  code_gubun, code_gubunname, jibon_bon, jibon_bu, jibon_addr, " \
          "  code_doro, code_doroname, building_bon, building_bu, building_num, " \
          "  building_name, doro_addr, oldzip, newzip, donginfo, " \
          "  floorinfo,hoinfo, longitude, latitude) " \
          "VALUES " \
          "( %s, %s, %s, %s, %s," \
          "  %s, %s, %s, %s, %s, " \
          "  %s, %s, %s, %s, %s, " \
          "  %s, %s, %s, %s, %s, " \
          "  %s, %s, %s, %s, %s, " \
          "  %s, %s, %s, %s, %s, " \
          "  %s, %s, %s, %s, %s, " \
          "  %s, %s, %s, %s)";

    rd = csv.reader(file)

    for index,line in enumerate(rd):
        if index == 0:
            continue
        row = str(line).split('|')
        try:
            curs.execute(sql, ( row[0].replace("['", ""), row[1], row[2], row[3], row[4], \
                         row[5], row[6], row[7], row[8], row[9], \
                         row[10], row[11], row[12], row[13], row[14], \
                         row[15], row[16], row[17], row[18], row[19], \
                         row[20], row[21], row[22], row[23], row[24], \
                         row[25], row[26], row[27], row[28], row[29], \
                         row[30], row[31], row[32], row[33], row[34],
                         row[35], row[36], row[37], row[38].replace("']", "") ))
            conn.commit()
        except :
            continue
    file.close()

