import requests
from dotenv import load_dotenv
import openai
from openai import OpenAI
import os

def load_env_variables():
    # .env 파일로부터 환경변수 로드
    load_dotenv()

def get_api_key():
    # 환경변수에서 API_KEY 가져오기
    return os.getenv('API_KEY')


def makingModelH5():
    from modelGenerator import modelGenerator
    modelGenerator.doLearning()

def makingCover():
    # codebreaker.py
    import cv2
    img_path = 'userImage/userInputImage_4.jpg'
    img = cv2.imread(img_path)

    # picture style transfer
    from styleTransfer import getUserPicture
    userImage = getUserPicture.getUserImage(img)  # temp_userPicture made
    from styleTransfer import styleTransfer
    styleTransfer.doTransferwithUserImage()  # temp_userPicture util, styleTransfer/styled_result_image1,2,3,4 made

    # get character image list 7*4
    from dividor import chracterDividor
    # chracterImageLi = chracterDividor.chracterDividor(img_result)  # it will generator imagle List
    chracterImageLi = chracterDividor.chracterDividor(img)  # it will generator imagle List

    chracterImageLi_1 = chracterImageLi[0:14]
    chracterImageLi_2 = chracterImageLi[14:28]

    # charater classfication and get character list
    from imageDetection import imageDetection
    charLi1 = imageDetection.doTheImageClassficationByList(chracterImageLi_1)
    charLi2 = imageDetection.doTheImageClassficationByList(chracterImageLi_2)
    # print(charLi1)
    # print(charLi2)

    charLi2 = getGPTList(charLi1, charLi2)
    charLi2 = list(charLi2)
    newCharLi = charLi1 + [':'] + charLi2
    # finally combining
    from imageCombiner import combine
    combine.drawImagewithText(newCharLi)


# GPT 모델에 요청 보내는 함수
def get_gpt_response(text):
    # 환경변수 로드
    load_env_variables()

    # API 키 가져오기
    api_key = get_api_key()

    client = OpenAI(
        api_key=api_key,
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text}]
    )
    return response.choices[0].message.content.strip()


# getGPTList 함수
def getGPTList(strList1, strList2):
    region = "".join(strList1)
    text = "".join(strList2)
    text = "Please write a promotional article about an "+ region + " famous for " + text + " in about 20 characters."
    gpt_response = get_gpt_response(text)
    return gpt_response


if __name__ == '__main__':

    print("Choose a function to execute:")
    print("1: makingModelH5")
    print("2: makingCover")

    choice = input("Enter the number of the function to execute: ")

    if choice == '1':
        print("1번을 선택했습니다. model.h5를 생성합니다.")
        # 실행 전 체크할 것
        # 1. modelGenerator/archive 디렉터리에 emnist-letters-test.csv와 emnist-letters-train.csv가 있어야합니다.
        makingModelH5()
        # 실행 후 할 것
        # 1. 생성된 mnist_model.h5를 imageDetection 디렉터리로 옮길 것.
    elif choice == '2':
        print("2번을 선택했습니다. 현수막을 생성합니다.")
        # 실행 전 체크할 것
        #userImage 디렉터리에 변형할 사진이 존재하는지 확인할 것
        makingCover()
        # 실행 후 볼 것
        # 1. 생성된 자료들을 확인 할 것. newCoverPage 디렉터리에 네 개의 사진이 생성된다. 결과물이 잘 생성되었는지 체크할 것.
    else:
        print("Invalid choice. Please enter a number 1 or 2.")
