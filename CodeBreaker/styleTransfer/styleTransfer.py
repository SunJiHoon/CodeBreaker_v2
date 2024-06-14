import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import tensorflow_hub as hub

# 이미지를 로드하고 전처리하는 함수
def load_image(image_path):
    image = tf.io.read_file(image_path)
    image = tf.image.decode_image(image, channels=3)
    image = tf.image.convert_image_dtype(image, tf.float32)
    image = tf.image.resize(image, [224, 224])  # 이미지 크기 조절
    image = image[tf.newaxis, :]
    return image


def doTransfer():
    # 이미지 경로 설정
    content_image_path = 'styleTransfer/content_image_5.jpg'  # 대상 이미지
    style_image_path = 'styleTransfer/style_image_5.jpg'      # 스타일 이미지
    
    # 이미지를 로드하고 전처리
    content_image = load_image(content_image_path)
    style_image = load_image(style_image_path)
    
    # TF-Hub에서 사전 훈련된 스타일 트랜스퍼 모델 로드
    hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
    
    # 스타일 트랜스퍼 적용
    stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]
    stylized_image = tf.squeeze(stylized_image)  # 차원 축소
    
    # 결과 이미지 출력
    plt.imshow(stylized_image)
    plt.axis('off')
    plt.show()
    
    # 결과 이미지 저장
    tf.keras.utils.save_img('styleTransfer/result_image.jpg', stylized_image.numpy())
    
def doTransferwithUserImage():
    # TF-Hub에서 사전 훈련된 스타일 트랜스퍼 모델 로드
    hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
    #################
    # 이미지 경로 설정
    content_image_path = 'temp_userPicture.jpg'  # 대상 이미지
    style_image_path = 'styleTransfer/style_image.jpg'      # 스타일 이미지
    # 이미지를 로드하고 전처리
    content_image = load_image(content_image_path)
    style_image = load_image(style_image_path)
    # 스타일 트랜스퍼 적용
    stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]
    stylized_image = tf.squeeze(stylized_image)  # 차원 축소
    # 결과 이미지 저장
    tf.keras.utils.save_img('styleTransfer/styled_result_image1.jpg', stylized_image.numpy())
    ############################################
    # 이미지 경로 설정
    content_image_path = 'temp_userPicture.jpg'  # 대상 이미지
    style_image_path = 'styleTransfer/style_image2.jpg'      # 스타일 이미지
    # 이미지를 로드하고 전처리
    content_image = load_image(content_image_path)
    style_image = load_image(style_image_path)
    # 스타일 트랜스퍼 적용
    stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]
    stylized_image = tf.squeeze(stylized_image)  # 차원 축소
    # 결과 이미지 출력
    # 결과 이미지 저장
    tf.keras.utils.save_img('styleTransfer/styled_result_image2.jpg', stylized_image.numpy())
    ############################################
    # 이미지 경로 설정
    content_image_path = 'temp_userPicture.jpg'  # 대상 이미지
    style_image_path = 'styleTransfer/style_image3.jpg'      # 스타일 이미지
    # 이미지를 로드하고 전처리
    content_image = load_image(content_image_path)
    style_image = load_image(style_image_path)
    # 스타일 트랜스퍼 적용
    stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]
    stylized_image = tf.squeeze(stylized_image)  # 차원 축소
    # 결과 이미지 출력
    # 결과 이미지 저장
    tf.keras.utils.save_img('styleTransfer/styled_result_image3.jpg', stylized_image.numpy())
    ############################################
    # 이미지 경로 설정
    content_image_path = 'temp_userPicture.jpg'  # 대상 이미지
    style_image_path = 'styleTransfer/style_image4.jpg'      # 스타일 이미지
    # 이미지를 로드하고 전처리
    content_image = load_image(content_image_path)
    style_image = load_image(style_image_path)
    # 스타일 트랜스퍼 적용
    stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]
    stylized_image = tf.squeeze(stylized_image)  # 차원 축소
    # 결과 이미지 출력
    # 결과 이미지 저장
    tf.keras.utils.save_img('styleTransfer/styled_result_image4.jpg', stylized_image.numpy())
    
