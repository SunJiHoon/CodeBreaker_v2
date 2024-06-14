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
    # TF-Hub���� ���� �Ʒõ� ��Ÿ�� Ʈ������ �� �ε�
    hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
    #################
    # �̹��� ��� ����
    content_image_path = 'temp_userPicture.jpg'  # ��� �̹���
    style_image_path = 'styleTransfer/style_image.jpg'      # ��Ÿ�� �̹���
    # �̹����� �ε��ϰ� ��ó��
    content_image = load_image(content_image_path)
    style_image = load_image(style_image_path)
    # ��Ÿ�� Ʈ������ ����
    stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]
    stylized_image = tf.squeeze(stylized_image)  # ���� ���
    # ��� �̹��� ����
    tf.keras.utils.save_img('styleTransfer/styled_result_image1.jpg', stylized_image.numpy())
    ############################################
    # �̹��� ��� ����
    content_image_path = 'temp_userPicture.jpg'  # ��� �̹���
    style_image_path = 'styleTransfer/style_image2.jpg'      # ��Ÿ�� �̹���
    # �̹����� �ε��ϰ� ��ó��
    content_image = load_image(content_image_path)
    style_image = load_image(style_image_path)
    # ��Ÿ�� Ʈ������ ����
    stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]
    stylized_image = tf.squeeze(stylized_image)  # ���� ���
    # ��� �̹��� ���
    # ��� �̹��� ����
    tf.keras.utils.save_img('styleTransfer/styled_result_image2.jpg', stylized_image.numpy())
    ############################################
    # �̹��� ��� ����
    content_image_path = 'temp_userPicture.jpg'  # ��� �̹���
    style_image_path = 'styleTransfer/style_image3.jpg'      # ��Ÿ�� �̹���
    # �̹����� �ε��ϰ� ��ó��
    content_image = load_image(content_image_path)
    style_image = load_image(style_image_path)
    # ��Ÿ�� Ʈ������ ����
    stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]
    stylized_image = tf.squeeze(stylized_image)  # ���� ���
    # ��� �̹��� ���
    # ��� �̹��� ����
    tf.keras.utils.save_img('styleTransfer/styled_result_image3.jpg', stylized_image.numpy())
    ############################################
    # �̹��� ��� ����
    content_image_path = 'temp_userPicture.jpg'  # ��� �̹���
    style_image_path = 'styleTransfer/style_image4.jpg'      # ��Ÿ�� �̹���
    # �̹����� �ε��ϰ� ��ó��
    content_image = load_image(content_image_path)
    style_image = load_image(style_image_path)
    # ��Ÿ�� Ʈ������ ����
    stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]
    stylized_image = tf.squeeze(stylized_image)  # ���� ���
    # ��� �̹��� ���
    # ��� �̹��� ����
    tf.keras.utils.save_img('styleTransfer/styled_result_image4.jpg', stylized_image.numpy())
    
