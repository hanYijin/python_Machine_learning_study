import csv

def doRead():
    file=open("a.csv","r")  #파일 열기
    rd= csv.reader(file)    #읽는 버퍼 가져오기
    for line in rd:         #한 줄씩 꺼내면서 line에 넣기
        print(line)         #line 출력
    file.close()            #파일 닫기

def doWrite():
    file= open("a.csv","w",newline='')
    wr= csv.writer(file)
    wr.writerow(['1','test','aaa'])
    wr.writerow(['2','test','bbb'])
    wr.writerow(['3','test','ccc'])

    file.close()


doWrite()