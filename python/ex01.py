import numpy as np

def doA():
    np1= np.arrange(4) #0~3까지 numpy배열 선언
    np2= np.zeros((4,4),dtype=float)# 0으로 초기화 2차원 배열 4햏4열 flost형 선언
    np3= np.ones((3,3), dtype=str) # 1로 초기화 3행 3열 문자열형 선언

    np4= np.random.randint(0,10,(2,2))# 0~9까지 2행2열
    np5= np.random.normal(0,1,(3,3)) #0~1가지 표준정규를 띄는 배열
    print(np1)
    print(np2)
    print(np3)
    print(np4)
    print(np5)

def doB():
    np1 =np.array([1,2])
    np2 = np.array([3,4])
    np3 = np1+np2
    np4 = np.concatenate(np1,np2)
    print(np3)
    print(np4)
    print(np3.shape)
    print(np4.shape)
    
    np5 = np.random.randint(0,10,(3,3))
    print(np5.shape)