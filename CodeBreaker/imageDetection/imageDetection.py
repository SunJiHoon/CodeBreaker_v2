from tensorflow import keras
import matplotlib.pyplot as plt

from PIL import Image
from PIL import ImageOps

import numpy as np

import cv2


def imageSplitAndRecognize():#tino
    characterList = []
    
    #Load Image
    image_path = 'imageDetection/TestImage/testImage.jpg' #plz make image and test

    
    #이미지 리스트만들기
    #make image list
    imageList = []
    
    
    #for문으로 이미지 배열을 model에 통과시키면서 값 얻기
    loaded_model = keras.models.load_model('imageDetection/mnist_model.h5')


    #무슨 글자들인지 출력하기
    print(characterList)
    

# 1 이미지 크기 조정 함수, 2 좌우대칭, 3 이미지 왼쪽으로 90도 회전, 4 이미지 회색으로 전환,  5 이미지 numpy로 만들기
#    expectVal = loaded_model.predict(image_data.reshape(1, 28, 28))가 실행되는지 구현 #기훈&녕준

def doTheImageTest():
    # 현재 스크립트 파일의 디렉토리를 기준으로 상대 경로 생성

    loaded_model = keras.models.load_model('imageDetection/mnist_model.h5')
    
    # JPG 이미지 로드
    image_path = 'imageDetection/TestImage/whiteA.jpg'
    image = Image.open(image_path)

    # 이미지 크기 조정
    image = image.resize((28, 28))
    
    #좌우대칭시키기
    flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    # 이미지를 왼쪽으로 90도 회전
    rotated_image = flipped_image.rotate(90)
    image = rotated_image
    
    # 이미지를 흑백으로 변환
    image = image.convert('L')  # 'L'은 흑백 모드입니다.

    # 이미지를 NumPy 배열로 변환 (부동 소수점으로 변환)
    image_data = np.array(image, dtype=np.float32) / 255.0
    for i in range(28):
        for j in range(28):
            image_data[i][j] = 1.0 - image_data[i][j]
    plt.imshow(image_data, cmap='gray')
    plt.show()
    
    expectVal = loaded_model.predict(image_data.reshape(1, 28, 28))
    print(expectVal)
    max_index = np.argmax(expectVal)
    print(max_index)
    print("num6")
    

def doTheImageClassficationByList(chracterImageLi):
    charList = []
    # 현재 스크립트 파일의 디렉토리를 기준으로 상대 경로 생성

    loaded_model = keras.models.load_model('imageDetection/mnist_model.h5')
    for image in chracterImageLi:
        cv2.imwrite('temp.jpg', image)
        
        # JPG 이미지 로드
        image_path = 'temp.jpg'
        image = Image.open(image_path)
        # 이미지 크기 조정
        image = image.resize((28, 28))
        # crop한 부분을 resize
        #image = cv2.resize(image, (28, 28))

        #좌우대칭시키기
        flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
        # 이미지를 왼쪽으로 90도 회전
        rotated_image = flipped_image.rotate(90)
        image = rotated_image
        # 이미지를 흑백으로 변환
        image = image.convert('L')  # 'L'은 흑백 모드입니다.
        # 이미지를 NumPy 배열로 변환 (부동 소수점으로 변환)
        image_data = np.array(image, dtype=np.float32) / 255.0
        for i in range(28):
            for j in range(28):
                image_data[i][j] = 1.0 - image_data[i][j]
        #plt.imshow(image_data, cmap='gray')
        #plt.show()
        
        expectVal = loaded_model.predict(image_data.reshape(1, 28, 28))
        print(expectVal)
        max_index = np.argmax(expectVal)
        print("expected char : " + chr(96 + max_index))
        print("index info : ", end = '')
        print(max_index)
        print()
        
        if len(charList) > 0 and charList[-1] == 'z' and chr(96 + max_index) == 'z':
            charList.pop()
            break
        charList.append(chr(96 + max_index))
    return charList        