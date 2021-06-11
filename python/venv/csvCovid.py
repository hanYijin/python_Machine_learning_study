import csv

def read():
    file= open('info/covid.csv','r',encoding='cp949')
    data= open('csvcovid.csv','w',newline='')
    rd= csv.reader(file)
    wr= csv.writer(data)
    for line in rd:
        wr.writerow(line)
    file.close()
    data.close()