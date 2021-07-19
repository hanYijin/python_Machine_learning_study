import requests, bs4
import pandas as pd
from lxml import html
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
my_servicekey='H7J7uLgD9PdCIm3xPaTGiRqsInYdN2ANv42apuqJVqFywsRVGkqG5Znn0Q6NqulKUbw1%2FXlS%2FwFuRsgj1o4KPg%3D%3D'
decoding='H7J7uLgD9PdCIm3xPaTGiRqsInYdN2ANv42apuqJVqFywsRVGkqG5Znn0Q6NqulKUbw1/XlS/wFuRsgj1o4KPg=='

def api_read_growth(farmNum):
    url='http://apis.data.go.kr/1390000/SmartFarmdata/grwdatarqst'
    queryParams = '?' + urlencode(
        {quote_plus('ServiceKey'): my_servicekey, quote_plus('serviceKey'): decoding, quote_plus('pageSize'): '15',
         quote_plus('pageNo'): '2', quote_plus('searchFrmhsCode'): farmNum})
    response = requests.get(url + queryParams).text.encode('utf-8')
    xmlobj = bs4.BeautifulSoup(response, 'lxml-xml')
    rows = xmlobj.find_all('item')
    rowList = []
    nameList = []
    columnList = []
    rowsLen = len(rows)
    for i in range(0, rowsLen):
        columns = rows[i].find_all()
        columnsLen = len(columns)
        for j in range(0, columnsLen):
            if i == 0:
                nameList.append(columns[j].name)
            eachColumn = columns[j].text
            columnList.append(eachColumn)
        rowList.append(columnList)
        columnList = []  # 다음 row의 값을 넣기 위해 비워준다

    result = pd.DataFrame(rowList, columns=nameList)
    print(result)
    return result

def api_read_output(farmNum):
    url = 'http://apis.data.go.kr/1390000/SmartFarmdata/prddatarqst'
    queryParams = '?' + urlencode(
        {quote_plus('ServiceKey'): my_servicekey, quote_plus('serviceKey'): decoding, quote_plus('pageSize'): '15',
         quote_plus('pageNo'): '2', quote_plus('searchFrmhsCode'): farmNum})
    response = requests.get(url + queryParams).text.encode('utf-8')
    xmlobj = bs4.BeautifulSoup(response, 'lxml-xml')
    rows = xmlobj.find_all('item')
    rowList = []
    nameList = []
    columnList = []
    rowsLen = len(rows)
    for i in range(0, rowsLen):
        columns = rows[i].find_all()
        columnsLen = len(columns)
        for j in range(0, columnsLen):
            if i == 0:
                nameList.append(columns[j].name)
            eachColumn = columns[j].text
            columnList.append(eachColumn)
        rowList.append(columnList)
        columnList = []  # 다음 row의 값을 넣기 위해 비워준다

    result = pd.DataFrame(rowList, columns=nameList)
    print(result)
    return result

def make_dataframe(result,start,finsh):
    input = result[['frmWeek', 'grwtLt', 'fcluHg', 'stemThck', 'lefLt', 'lefCunt', 'frtstGrupp', 'flanGrupp', 'hvstCo',
                    'frtstCo', ]].to_numpy()
    input=input[start:finsh]
    names = ['주차', '생장길이', '화방높이', '줄기굵기', '잎길이(엽장)', '잎수', '착과군', '개화군', '수확수', '열매수']
    df = pd.DataFrame(input, columns=names)
    return df

def save_to_csv(dataFrame,fileName):
    dataFrame.to_csv(fileName,encoding="UTF-8")

res=api_read_output('339')
result=api_read_growth('339')
print(make_dataframe(result,1,15))
df=make_dataframe(result,1,15)
save_to_csv(df,'tomatoFarm339.csv')

