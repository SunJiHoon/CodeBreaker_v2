from PIL import Image, ImageDraw, ImageFont

def drawImagewithText(strList):
    # �̹��� ����
    image = Image.open('styleTransfer/styled_result_image1.jpg')
    
    # �̹����� �ؽ�Ʈ �߰�
    draw = ImageDraw.Draw(image)
    text = ""
    for ch in strList:
        text += ch
    font = ImageFont.truetype("arial.ttf", 36)  # ��Ʈ�� ũ�� ����
    draw.text((50, 50), text, fill='white', font=font)  # �ؽ�Ʈ ��ġ�� ��Ÿ�� ����
    
    # ������ �̹��� ����
    image.save('newCoverPage/result1.jpg')
################################
    # �̹��� ����
    image = Image.open('styleTransfer/styled_result_image2.jpg')
    
    # �̹����� �ؽ�Ʈ �߰�
    draw = ImageDraw.Draw(image)
    text = ""
    for ch in strList:
        text += ch
    font = ImageFont.truetype("arial.ttf", 36)  # ��Ʈ�� ũ�� ����
    draw.text((50, 50), text, fill='white', font=font)  # �ؽ�Ʈ ��ġ�� ��Ÿ�� ����
    
    # ������ �̹��� ����
    image.save('newCoverPage/result2.jpg')
################################
    # �̹��� ����
    image = Image.open('styleTransfer/styled_result_image3.jpg')
    
    # �̹����� �ؽ�Ʈ �߰�
    draw = ImageDraw.Draw(image)
    text = ""
    for ch in strList:
        text += ch
    font = ImageFont.truetype("arial.ttf", 36)  # ��Ʈ�� ũ�� ����
    draw.text((50, 50), text, fill='white', font=font)  # �ؽ�Ʈ ��ġ�� ��Ÿ�� ����
    
    # ������ �̹��� ����
    image.save('newCoverPage/result3.jpg')
################################
    # �̹��� ����
    image = Image.open('styleTransfer/styled_result_image4.jpg')
    
    # �̹����� �ؽ�Ʈ �߰�
    draw = ImageDraw.Draw(image)
    text = ""
    for ch in strList:
        text += ch
    font = ImageFont.truetype("arial.ttf", 36)  # ��Ʈ�� ũ�� ����
    draw.text((50, 50), text, fill='white', font=font)  # �ؽ�Ʈ ��ġ�� ��Ÿ�� ����
    
    # ������ �̹��� ����
    image.save('newCoverPage/result4.jpg')
    


