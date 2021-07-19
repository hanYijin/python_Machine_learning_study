import numpy as np
import cv2
import utils
import requests
import shutil
import time
filename= 'trained.npz'
with np.load(filename) as data: #file open close 자동으로
    train= data['train']
    train_labes = data['train_labels']

knn=cv2.ml.KNearest_create()

knn.train(train,cv2.ml.ROW_SAMPLE,train_labes)

def check(test):
    ret,result,neibours,dist= knn.findNearest(test,k=1);
    return result
# print(check(train[:]))
# print(check(train[4:5]))

def get_result(file_name):
    img = cv2.imread(file_name)
    chars=utils.extract_chars(img)
    result_string=''
    for char in chars:
        matched = check(utils.resized20(char[1]))
        if matched <10:
            result_string+= str(int(matched))
            continue
        if matched==10:
            matched ='+'
        elif matched == 11:
            matched ='-'
        elif matched == 12:
            matched ='*'
        result_string += matched
    return result_string

# print(get_result("./images/d0.png"))
# print(eval(get_result("./images/d0.png")))

def remove_first_0(string):
    temp=[]
    for i in string:
        if i == '+' or i== '-' or i=='*':
           temp.append(i)
    import re
    arr=re.split('\*|\+|\-',string)
    print('split')
    print(arr)
    return str(int(arr[0]))+temp[0]+str(int(arr[1]))

# my_number=get_result("./images/d9.png")
# print(my_number)
# print(remove_first_0(my_number))
# print(eval(remove_first_0(my_number)))

host = "http://192.168.0.89:10000"
url = '/start'
# target_images 라는 폴더 생성
with requests.Session() as s:
    answer = ''
    for i in range(0, 30):
        start_time = time.time()
        params = {'ans': answer}
        # 정답을 파라미터에 달아서 전송하여, 이미지 경로를 받아옵니다.
        response = s.post(host + url, params)
        print('Server Return: ' + response.text)
        if i == 0:
            returned = response.text
            image_url = host + returned
            url = '/check'
        else:
            returned = response.json()
            image_url = host + returned['url']

        print('Problem ' + str(i) + ': ' + image_url)
        # 특정한 폴더에 이미지 파일을 다운로드 받습니다.
        response = s.get(image_url, stream=True)
        target_image = './target_images/' + str(i) + '.png'
        with open(target_image, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        # 다운로드 받은 이미지 파일을 분석하여 답을 도출합니다.
        answer_string = get_result(target_image)
        print('String: ' + answer_string)
        answer_string = remove_first_0(answer_string)
        answer = str(eval(answer_string))
        print('Answer: ' + answer)
        print("--- %s seconds ---" % (time.time() - start_time))