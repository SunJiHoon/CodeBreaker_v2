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
        
        # JPG �̹��� �ε�
        image_path = 'temp.jpg'
        image = Image.open(image_path)
        # �̹��� ũ�� ����
        image = image.resize((28, 28))
        # crop�� �κ��� resize
        #image = cv2.resize(image, (28, 28))

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