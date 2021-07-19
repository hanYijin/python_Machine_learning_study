import pandas as pd
import glob
import os
input_file= r'D:\python_study\smartFarm\data_csv' # csv파일들이 있는 디렉토리 위치
output_file=r'D:\python_study\smartFarm\data_csv\result.csv' #병합하고 저장하려는 파일명

allFile=glob.glob(os.path.join(input_file,'tomatoFarm*'))# glob함수로 tomatoFarm_로 시작하는 파일들을 모으기
print(allFile)
allData=[]# 읽어 들인 csv파일 내용을 저장할 빈 리스트를 하나 만든다
for file in allFile:
    df=pd.read_csv(file)# for구문으로 csv파일들을 읽어 들인다
    allData.append(df)# 빈 리스트에 읽어 들인 내용을 추가

dataCombine=pd.concat(allData,axis=0,ignore_index=True) # concat함수를 이용해서 리스트의 내용을 병합
dataCombine.to_csv(output_file,index=False,encoding='UTF-8')# to_csv함수로 저장

print(dataCombine)