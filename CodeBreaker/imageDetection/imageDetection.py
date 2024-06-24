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

    
    #�̹��� ����Ʈ�����
    #make image list
    imageList = []
    
    
    #for������ �̹��� �迭�� model�� �����Ű�鼭 �� ���
    loaded_model = keras.models.load_model('imageDetection/mnist_model.h5')


    #���� ���ڵ����� ����ϱ�
    print(characterList)
    

# 1 �̹��� ũ�� ���� �Լ�, 2 �¿��Ī, 3 �̹��� �������� 90�� ȸ��, 4 �̹��� ȸ������ ��ȯ,  5 �̹��� numpy�� �����
#    expectVal = loaded_model.predict(image_data.reshape(1, 28, 28))�� ����Ǵ��� ���� #����&����

def doTheImageTest():
    # ���� ��ũ��Ʈ ������ ���丮�� �������� ��� ��� ����

    loaded_model = keras.models.load_model('imageDetection/mnist_model.h5')
    
    # JPG �̹��� �ε�
    image_path = 'imageDetection/TestImage/whiteA.jpg'
    image = Image.open(image_path)

    # �̹��� ũ�� ����
    image = image.resize((28, 28))
    
    #�¿��Ī��Ű��
    flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    # �̹����� �������� 90�� ȸ��
    rotated_image = flipped_image.rotate(90)
    image = rotated_image
    
    # �̹����� ������� ��ȯ
    image = image.convert('L')  # 'L'�� ��� ����Դϴ�.

    # �̹����� NumPy �迭�� ��ȯ (�ε� �Ҽ������� ��ȯ)
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
    # ���� ��ũ��Ʈ ������ ���丮�� �������� ��� ��� ����

    loaded_model = keras.models.load_model('imageDetection/mnist_model.h5')
    for image in chracterImageLi:
        cv2.imwrite('temp.jpg', image)
        
        # JPG 이미지 열기
        image_path = 'temp.jpg'
        image = Image.open(image_path)
        # 이미지 크기 조정
        image = image.resize((28, 28))
        # 좌우 반전
        #image = cv2.resize(image, (28, 28))

        # 이미지를 90도 회전
        flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
        # 이미지를 90도 회전
        rotated_image = flipped_image.rotate(90)
        image = rotated_image
        # 이미지를 그레이스케일로 변환
        image = image.convert('L')  # 'L'은 그레이스케일 모드
        # 이미지를 NumPy 배열로 변환 (0~1로 정규화)
        image_data = np.array(image, dtype=np.float32) / 255.0
        for i in range(28):
            for j in range(28):
                image_data[i][j] = 1.0 - image_data[i][j]
        #plt.imshow(image_data, cmap='gray')
        #plt.show()
        # 검정색 픽셀 비율 계산
        white_pixel_ratio = np.mean(image_data > 0.5)

        expectVal = loaded_model.predict(image_data.reshape(1, 28, 28))
        print(expectVal)
        max_index = np.argmax(expectVal)
        print("expected char : " + chr(96 + max_index))
        print("index info : ", end = '')
        print(max_index)
        print()

        # 흰색 픽셀 비율이 높은 경우 ',' 추가
        # if black_pixel_ratio < 0.2:  # 여기서 0.5는 임계값으로 조절 가능
        #     charList.append(',')


        if len(charList) > 0 and white_pixel_ratio > 0.7:
            # charList.pop()
            break
        charList.append(chr(96 + max_index))
    return charList        