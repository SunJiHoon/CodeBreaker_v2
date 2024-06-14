from PIL import Image, ImageDraw, ImageFont

def drawImagewithText(strList):
    # 이미지 열기
    image = Image.open('styleTransfer/styled_result_image1.jpg')
    
    # 이미지에 텍스트 추가
    draw = ImageDraw.Draw(image)
    text = ""
    for ch in strList:
        text += ch
    font = ImageFont.truetype("arial.ttf", 36)  # 폰트와 크기 설정
    draw.text((50, 50), text, fill='white', font=font)  # 텍스트 위치와 스타일 설정
    
    # 수정된 이미지 저장
    image.save('newCoverPage/result1.jpg')
################################
    # 이미지 열기
    image = Image.open('styleTransfer/styled_result_image2.jpg')
    
    # 이미지에 텍스트 추가
    draw = ImageDraw.Draw(image)
    text = ""
    for ch in strList:
        text += ch
    font = ImageFont.truetype("arial.ttf", 36)  # 폰트와 크기 설정
    draw.text((50, 50), text, fill='white', font=font)  # 텍스트 위치와 스타일 설정
    
    # 수정된 이미지 저장
    image.save('newCoverPage/result2.jpg')
################################
    # 이미지 열기
    image = Image.open('styleTransfer/styled_result_image3.jpg')
    
    # 이미지에 텍스트 추가
    draw = ImageDraw.Draw(image)
    text = ""
    for ch in strList:
        text += ch
    font = ImageFont.truetype("arial.ttf", 36)  # 폰트와 크기 설정
    draw.text((50, 50), text, fill='white', font=font)  # 텍스트 위치와 스타일 설정
    
    # 수정된 이미지 저장
    image.save('newCoverPage/result3.jpg')
################################
    # 이미지 열기
    image = Image.open('styleTransfer/styled_result_image4.jpg')
    
    # 이미지에 텍스트 추가
    draw = ImageDraw.Draw(image)
    text = ""
    for ch in strList:
        text += ch
    font = ImageFont.truetype("arial.ttf", 36)  # 폰트와 크기 설정
    draw.text((50, 50), text, fill='white', font=font)  # 텍스트 위치와 스타일 설정
    
    # 수정된 이미지 저장
    image.save('newCoverPage/result4.jpg')
    


