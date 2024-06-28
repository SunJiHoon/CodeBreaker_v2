# CodeBreaker_v2

## 목차
1.	파일 다운로드
2.	프로젝트 열기 및 세팅
3.	터미널 명령어 입력하기
4.	main.py 실행하기 makingModelH5
5.	main.py 실행하기 makingCover
6.	결과물 확인하기



## 파일 다운로드
https://github.com/SunJiHoon/CodeBreaker_v2 접속 후 Code -> Download ZIP 클릭
 
![image](https://github.com/SunJiHoon/CodeBreaker_v2/assets/46434398/9cfa9297-76e0-483a-9b6f-c59d93459088)


다운로드 받은 후 압축 풀기
 
 ![image](https://github.com/SunJiHoon/CodeBreaker_v2/assets/46434398/80422067-3fb2-4e05-9bef-7ed579831130)

 ![image](https://github.com/SunJiHoon/CodeBreaker_v2/assets/46434398/fcd8df9a-1842-4ce0-a25a-62a704be2664)


프로젝트 열기 및 세팅
Pycharm으로 프로젝트 열기

 ![image](https://github.com/SunJiHoon/CodeBreaker_v2/assets/46434398/322cb368-dcf6-4817-a9db-401d79c46b88)


파이참에서 다운로드 받은 프로젝트 열기(1)

![image](https://github.com/SunJiHoon/CodeBreaker_v2/assets/46434398/1924988a-9ca7-4cb0-83bc-0cae5fc41518)

 
파이참에서 다운로드 받은 프로젝트 열기(2)

![image](https://github.com/SunJiHoon/CodeBreaker_v2/assets/46434398/52c93e1d-e151-4097-9cfc-747d78a3f994)

 
파이참에서 다운로드 받은 프로젝트 열기(3)

![image](https://github.com/SunJiHoon/CodeBreaker_v2/assets/46434398/cc86e5da-1232-433e-a68a-dc3433b8dadf)

 

파일들 위치 시키기

.env, emnist-letters-test.csv, emnist-letters-train.csv 세 파일을 다운 받아서 해당 디렉터리에 위치 시킵니다.

CodeBreaker_v2/CodeBreaker/.env

CodeBreaker_v2/CodeBreaker/modelGenerator/archive/emnist-letters-test.csv

CodeBreaker_v2/CodeBreaker/modelGenerator/archive/emnist-letters-train.csv


![image](https://github.com/SunJiHoon/CodeBreaker_v2/assets/46434398/6994f075-e031-4294-9a9c-688e4410d15f)
 

 

## 터미널 명령어 입력하기
이어서 터미널을 열고 해당 명령어를 따라 칩니다.
가상환경 만들기

 ![image](https://github.com/SunJiHoon/CodeBreaker_v2/assets/46434398/0cb989fb-78b0-46ce-851a-cc66c748ff77)

가상환경 실행하기

 ![image](https://github.com/SunJiHoon/CodeBreaker_v2/assets/46434398/3051e7a5-b543-4555-afac-5d82cc0622af)

가상환경 실행된 것 확인하기 (초록색으로 venv 글자가 띄어진 것을 확인하면 됩니다.)

![image](https://github.com/SunJiHoon/CodeBreaker_v2/assets/46434398/9355eb3d-feb0-413f-ac50-ebdefd8aea42)
 
Pip로 요구사항 설치하기(1)

 ![image](https://github.com/SunJiHoon/CodeBreaker_v2/assets/46434398/913943cf-dfc7-4e3e-9943-5ff1d99f1d7e)

Pip로 요구사항 설치하기(2) – 설치할 것이 꽤 많아서 오래 걸립니다.

![image](https://github.com/SunJiHoon/CodeBreaker_v2/assets/46434398/9b785b0c-5628-447a-9cda-394f04afddd0)
 
Pip로 요구사항 설치하기(3) – 설치 후
 
![image](https://github.com/SunJiHoon/CodeBreaker_v2/assets/46434398/40e172b4-e4dc-477c-a443-fc6e64c8baf8)

 

## main.py 실행하기 – makingModelH5

main.py 실행시키기

 ![image](https://github.com/SunJiHoon/CodeBreaker_v2/assets/46434398/dd5284a1-1240-45ec-99ce-6ec67c250eec)

1누르고 엔터를 눌러서, model.h5 생성하기

 ![image](https://github.com/SunJiHoon/CodeBreaker_v2/assets/46434398/ad4febcf-383d-499a-a595-013883e08022)

실행 후 화면

 ![image](https://github.com/SunJiHoon/CodeBreaker_v2/assets/46434398/bcd96d85-c9bc-48d3-9b8a-5dfd26e1f2fa)

생성된 mnist_model.h5를 확인하기

 ![image](https://github.com/SunJiHoon/CodeBreaker_v2/assets/46434398/5a041c8c-f2ed-41d9-9c68-bc81bd8ac860)

mnist_model.h5를 CodeBreaker/imageDetection/mnist_model.h5로 옮기기

 ![image](https://github.com/SunJiHoon/CodeBreaker_v2/assets/46434398/a144ac1b-35bd-4868-8ce6-616c15802642)

![image](https://github.com/SunJiHoon/CodeBreaker_v2/assets/46434398/6f84608c-2ac9-4e5b-89da-fef74509c296)

![image](https://github.com/SunJiHoon/CodeBreaker_v2/assets/46434398/8ff68a83-2fde-4f40-87c4-287a9cebf4e2)

 
 

 

## main.py 실행하기 – makingCover
main.py 실행하기

 ![image](https://github.com/SunJiHoon/CodeBreaker_v2/assets/46434398/7a20d74e-4b50-47be-b5a2-89bc42bb2aa3)

2번 누르고 엔터 눌러서 실행하기(1)

 ![image](https://github.com/SunJiHoon/CodeBreaker_v2/assets/46434398/3872cfe9-b08e-42b2-a4cd-8db8749b4001)

2번 누르고 엔터 눌러서 실행하기(2)

 ![image](https://github.com/SunJiHoon/CodeBreaker_v2/assets/46434398/72850689-1758-4bc3-a9c7-92a8cba32448)


 

## 결과물 확인하기
Input이었던 이미지

 ![image](https://github.com/SunJiHoon/CodeBreaker_v2/assets/46434398/43dd50a1-07c8-49dd-91c3-cbe454bcec87)


Output 이미지

 ![image](https://github.com/SunJiHoon/CodeBreaker_v2/assets/46434398/73666d47-71a8-441d-95b0-9c76539f305b)

