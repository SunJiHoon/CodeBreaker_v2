import pandas as pd
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
    
#from PIL import Image

def doLearning():
    print("abc")
    #####################################################################
    #file_path_letter_train = 'E:/deepLearning_3/archive/emnist-letters-train.csv'
    file_path_letter_train = 'modelGenerator/archive/emnist-letters-train.csv'
    df = pd.read_csv(file_path_letter_train, header=None)
    
    print("def")
    y_train_letter = df.iloc[:, 0].values
    x_train_letter = df.iloc[:, 1:].values
    x_train_letter = x_train_letter.reshape(-1, 28, 28)
    
    # CSV 파일 로드
    #file_path_letter_test = 'E:/deepLearning_3/archive/emnist-letters-test.csv'
    file_path_letter_test = 'modelGenerator/archive/emnist-letters-test.csv'
    df = pd.read_csv(file_path_letter_test, header=None)
    # 데이터 전처리
    y_test_letter = df.iloc[:, 0].values  # 첫 번째 열은 레이블입니다.
    x_test_letter = df.iloc[:, 1:].values  #나머지 열은 이미지 데이터입니다.
    # 이미지 데이터를 28x28 크기로 재조정 (MNIST 이미지 크기와 동일)
    x_test_letter = x_test_letter.reshape(-1, 28, 28)
    
    y_train_letter = y_train_letter
    y_test_letter = y_test_letter
    
    
    x_train = x_train_letter
    y_train = y_train_letter
    x_test = x_test_letter
    y_test = y_test_letter
    
    """
    for i in range(3):
        print(y_train[i])
        image = x_train[i]
        plt.imshow(image, cmap='gray')
        plt.show()
"""    
    ###########################################################################
    x_train, x_test = x_train / 255.0, x_test / 255.0
    
    #print(y_train[15])
    #image = x_train[15]
    #plt.imshow(image*255.0, cmap='gray')
    #plt.show()
    
    #0.98asfd
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(32, (3, 3), input_shape=(28, 28, 1), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(26+1, activation='softmax')
    ])
    
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    print(x_train)
    print(y_train)
    
    model.fit(x_train, y_train, epochs=5)#5
    
    model.save("mnist_model.h5")
    
    
    test_loss, test_accuracy = model.evaluate(x_test, y_test)
    print("test data loss:", test_loss)
    print("test data accuacy:", test_accuracy)
    
    
    image_data = np.array(x_test[10])
    expectedVal = model.predict(image_data.reshape(1, 28, 28))
    print("y_test[10] correct?")
    print(expectedVal)
    max_index = np.argmax(expectedVal)
    print(max_index)
    print(y_test[10])
    
    image = x_test[10]
    plt.imshow(image*255.0, cmap='gray')
    plt.show()
    
    if(max_index == y_test[10]):
        print("yes!")
    else:
        print("no..")
    
    