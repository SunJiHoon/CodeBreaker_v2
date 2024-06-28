import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import tensorflow_hub as hub

# �̹����� �ε��ϰ� ��ó���ϴ� �Լ�
def load_image(image_path):
    image = tf.io.read_file(image_path)
    image = tf.image.decode_image(image, channels=3)
    image = tf.image.convert_image_dtype(image, tf.float32)
    image = tf.image.resize(image, [224, 224])  # �̹��� ũ�� ����
    image = image[tf.newaxis, :]
    return image


def doTransfer():
    # �̹��� ��� ����
    content_image_path = 'styleTransfer/content_image_5.jpg'  # ��� �̹���
    style_image_path = 'styleTransfer/style_image_5.jpg'      # ��Ÿ�� �̹���
    
    # �̹����� �ε��ϰ� ��ó��
    content_image = load_image(content_image_path)
    style_image = load_image(style_image_path)
    
    # TF-Hub���� ���� �Ʒõ� ��Ÿ�� Ʈ������ �� �ε�
    hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
    
    # ��Ÿ�� Ʈ������ ����
    stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]
    stylized_image = tf.squeeze(stylized_image)  # ���� ���
    
    # ��� �̹��� ���
    plt.imshow(stylized_image)
    plt.axis('off')
    plt.show()
    
    # ��� �̹��� ����
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
    
