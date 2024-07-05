from PIL import Image, ImageDraw, ImageFont
import textwrap


def drawImagewithTextDescriptiveAboutOpenAndSave(strList, openAt, saveAt):
    # 원본 이미지 불러오기
    style_image = Image.open(openAt)


    # # 흰색 배경 이미지 생성 (300x1500)
    background_width = 1500
    background_height = 300
    # background = Image.new('RGB', (background_width, background_height), 'white')

    # 흰색 배경 이미지 불러오기
    background = Image.open("./userImage/userBackgroundImage.jpg")

    # 배경 이미지 크기를 1500x300으로 조정
    background = background.resize((background_width, background_height))

    # 스타일 이미지 크기
    style_image_width, style_image_height = style_image.size

    # 스타일 이미지 위치 (좌측 중앙에 배치)
    position = (10, 10)
    background.paste(style_image, position)

    # 텍스트 추가
    draw = ImageDraw.Draw(background)
    text = "".join(strList)
    font = ImageFont.truetype("arial.ttf", 36)  # 폰트 크기 조절

    # 텍스트 줄바꿈 처리
    max_text_width = background_width - style_image_width - 60  # 여백 고려
    wrapped_text = ""
    for line in textwrap.wrap(text, width=60):  # 임의로 40자 기준으로 줄바꿈, 필요시 조정
        while draw.textbbox((0, 0), line, font=font)[2] > max_text_width:
            line = line[:-1]
        wrapped_text += line + "\n"
    # 텍스트 크기 계산
    # text_bbox = draw.textbbox((0, 0), text, font=font)
    text_bbox = draw.textbbox((0, 0), wrapped_text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_position = (style_image_width + 50, (background_height - text_height) // 2)
    draw.multiline_text(text_position, wrapped_text, fill='black', font=font)  # 흰색 배경이므로 검은색 텍스트 사용
    # 결과 이미지를 파일로 저장
    background.save(saveAt)

def drawImagewithText(strList):
    drawImagewithTextDescriptiveAboutOpenAndSave(strList, 'styleTransfer/styled_result_image1.jpg', 'newCoverPage/result1.jpg')
    drawImagewithTextDescriptiveAboutOpenAndSave(strList, 'styleTransfer/styled_result_image2.jpg', 'newCoverPage/result2.jpg')
    drawImagewithTextDescriptiveAboutOpenAndSave(strList, 'styleTransfer/styled_result_image3.jpg', 'newCoverPage/result3.jpg')
    drawImagewithTextDescriptiveAboutOpenAndSave(strList, 'styleTransfer/styled_result_image4.jpg', 'newCoverPage/result4.jpg')


