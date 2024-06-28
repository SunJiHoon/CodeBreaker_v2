import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import tensorflow_hub as hub

# 이미지를 로드하고 전처리하는 함수
def load_image(image_path):
    image = tf.io.read_file(image_path)  # 이미지 파일을 읽어옵니다.
    image = tf.image.decode_image(image, channels=3) #binary 이미지를 3차원으로 디코딩
    image = tf.image.convert_image_dtype(image, tf.float32) # 이미지 데이터를 float32 형식으로 변환합니다.
    image = tf.image.resize(image, [224, 224])   # 이미지 크기를 224x224로 조정합니다.
    image = image[tf.newaxis, :] # 배치 차원을 추가합니다.
    return image


def doTransfer():
    # 이미지 경로 설정
    content_image_path = 'styleTransfer/content_image_5.jpg'
    style_image_path = 'styleTransfer/style_image_5.jpg'
    
    # 이미지를 로드하고 전처리합니다.
    content_image = load_image(content_image_path)
    style_image = load_image(style_image_path)
    
    # TF-Hub에서 Magenta 스타일 전송 모델을 로드합니다.
    hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
    
    # 스타일 transfer을 수행합니다.
    stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]
    stylized_image = tf.squeeze(stylized_image)  # ���� ���
    
    plt.imshow(stylized_image)
    plt.axis('off')
    plt.show()
    # 결과 이미지를 저장합니다.
    tf.keras.utils.save_img('styleTransfer/result_image.jpg', stylized_image.numpy())
    
def doTransferwithUserImage():
    # TF-Hub에서 Magenta 스타일 전송 모델을 로드합니다.
    hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
    #################
    # 이미지 경로 설정
    content_image_path = 'temp_userPicture.jpg'
    style_image_path = 'styleTransfer/style_image.jpg'
    # 이미지를 로드하고 전처리합니다.
    content_image = load_image(content_image_path)
    style_image = load_image(style_image_path)
    # 스타일 transfer을 수행합니다.
    stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]
    stylized_image = tf.squeeze(stylized_image)
    # 결과 이미지를 저장합니다.
    tf.keras.utils.save_img('styleTransfer/styled_result_image1.jpg', stylized_image.numpy())
    ############################################
    # 이미지 경로 설정
    content_image_path = 'temp_userPicture.jpg'
    style_image_path = 'styleTransfer/style_image2.jpg'
    # 이미지를 로드하고 전처리합니다.
    content_image = load_image(content_image_path)
    style_image = load_image(style_image_path)
    # 스타일 transfer을 수행합니다.
    stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]
    stylized_image = tf.squeeze(stylized_image)
    # 결과 이미지를 저장합니다.
    tf.keras.utils.save_img('styleTransfer/styled_result_image2.jpg', stylized_image.numpy())
    ############################################
    # 이미지 경로 설정
    content_image_path = 'temp_userPicture.jpg'
    style_image_path = 'styleTransfer/style_image3.jpg'
    # 이미지를 로드하고 전처리합니다.
    content_image = load_image(content_image_path)
    style_image = load_image(style_image_path)
    # 스타일 transfer을 수행합니다.
    stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]
    stylized_image = tf.squeeze(stylized_image)
    # 결과 이미지를 저장합니다.
    tf.keras.utils.save_img('styleTransfer/styled_result_image3.jpg', stylized_image.numpy())
    ############################################
    # 이미지 경로 설정
    content_image_path = 'temp_userPicture.jpg'
    style_image_path = 'styleTransfer/style_image4.jpg'
    # 이미지를 로드하고 전처리합니다.
    content_image = load_image(content_image_path)
    style_image = load_image(style_image_path)
    # 스타일 transfer을 수행합니다.
    stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]
    stylized_image = tf.squeeze(stylized_image)
    # 결과 이미지를 저장합니다.
    tf.keras.utils.save_img('styleTransfer/styled_result_image4.jpg', stylized_image.numpy())
    
