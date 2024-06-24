from PIL import Image, ImageDraw, ImageFont

def drawImagewithText(strList):
    # 원본 이미지 불러오기
    style_image = Image.open('styleTransfer/styled_result_image1.jpg')

    # 흰색 배경 이미지 생성 (300x1500)
    background_width = 1500
    background_height = 300
    background = Image.new('RGB', (background_width, background_height), 'white')

    # 스타일 이미지 크기
    style_image_width, style_image_height = style_image.size

    # 스타일 이미지 위치 (좌측 중앙에 배치)
    # position = (0, (background_height - style_image_height) // 2)
    position = (10, 10)
    background.paste(style_image, position)

    # 텍스트 추가
    draw = ImageDraw.Draw(background)
    text = "".join(strList)
    font = ImageFont.truetype("arial.ttf", 36)  # 폰트 크기 조절

    # 텍스트 크기 계산
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_position = (style_image_width + 50, (background_height - text_height) // 2)
    draw.text(text_position, text, fill='black', font=font)  # 흰색 배경이므로 검은색 텍스트 사용

    # 결과 이미지를 파일로 저장
    background.save('newCoverPage/result1.jpg')
    ################################

    style_image = Image.open('styleTransfer/styled_result_image2.jpg')

    # 흰색 배경 이미지 생성 (300x1500)
    background_width = 1500
    background_height = 300
    background = Image.new('RGB', (background_width, background_height), 'white')

    # 스타일 이미지 크기
    style_image_width, style_image_height = style_image.size

    # 스타일 이미지 위치 (좌측 중앙에 배치)
    # position = (0, (background_height - style_image_height) // 2)
    position = (10, 10)
    background.paste(style_image, position)

    # 텍스트 추가
    draw = ImageDraw.Draw(background)
    text = "".join(strList)
    font = ImageFont.truetype("arial.ttf", 36)  # 폰트 크기 조절
    # 텍스트 크기 계산
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_position = (style_image_width + 50, (background_height - text_height) // 2)
    draw.text(text_position, text, fill='black', font=font)  # 흰색 배경이므로 검은색 텍스트 사용

    # 결과 이미지를 파일로 저장
    background.save('newCoverPage/result2.jpg')
################################
    style_image = Image.open('styleTransfer/styled_result_image3.jpg')

    # 흰색 배경 이미지 생성 (300x1500)
    background_width = 1500
    background_height = 300
    background = Image.new('RGB', (background_width, background_height), 'white')

    # 스타일 이미지 크기
    style_image_width, style_image_height = style_image.size

    # 스타일 이미지 위치 (좌측 중앙에 배치)
    # position = (0, (background_height - style_image_height) // 2)
    position = (10, 10)
    background.paste(style_image, position)

    # 텍스트 추가
    draw = ImageDraw.Draw(background)
    text = "".join(strList)
    font = ImageFont.truetype("arial.ttf", 36)  # 폰트 크기 조절
    # 텍스트 크기 계산
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_position = (style_image_width + 50, (background_height - text_height) // 2)
    draw.text(text_position, text, fill='black', font=font)  # 흰색 배경이므로 검은색 텍스트 사용

    # 결과 이미지를 파일로 저장
    background.save('newCoverPage/result3.jpg')


    ################################
    style_image = Image.open('styleTransfer/styled_result_image4.jpg')

    # 흰색 배경 이미지 생성 (300x1500)
    background_width = 1500
    background_height = 300
    background = Image.new('RGB', (background_width, background_height), 'white')

    # 스타일 이미지 크기
    style_image_width, style_image_height = style_image.size

    # 스타일 이미지 위치 (좌측 중앙에 배치)
    # position = (0, (background_height - style_image_height) // 2)
    position = (10, 10)
    background.paste(style_image, position)

    # 텍스트 추가
    draw = ImageDraw.Draw(background)
    text = "".join(strList)
    font = ImageFont.truetype("arial.ttf", 36)  # 폰트 크기 조절
    # 텍스트 크기 계산
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_position = (style_image_width + 50, (background_height - text_height) // 2)
    draw.text(text_position, text, fill='black', font=font)  # 흰색 배경이므로 검은색 텍스트 사용

    # 결과 이미지를 파일로 저장
    background.save('newCoverPage/result4.jpg')


