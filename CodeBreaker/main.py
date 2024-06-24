def makingModelH5():
    from modelGenerator import modelGenerator
    modelGenerator.doLearning()

def makingCover():
    # codebreaker.py
    # from getImage import edge_detection
    from getImage import projection
    import cv2

    img_path = 'userImage/userInputImage_4.jpg'
    img = cv2.imread(img_path)

    # picture style transfer
    from styleTransfer import getUserPicture
    # userImage = getUserPicture.getUserImage(img_result)  # temp_userPicture made
    userImage = getUserPicture.getUserImage(img)  # temp_userPicture made
    from styleTransfer import styleTransfer
    styleTransfer.doTransferwithUserImage()  # temp_userPicture util, styleTransfer/styled_result_image1,2,3,4 made
    # get character image list 7*4
    from dividor import chracterDividor
    # chracterImageLi = chracterDividor.chracterDividor(img_result)  # it will generator imagle List
    chracterImageLi = chracterDividor.chracterDividor(img)  # it will generator imagle List
    # charater classfication and get character list
    from imageDetection import imageDetection
    charLi = imageDetection.doTheImageClassficationByList(chracterImageLi)
    print(charLi)
    # finally combining
    from imageCombiner import combine
    combine.drawImagewithText(charLi)


def doAddingTest():
    import cv2
    #cv2 설치 안 될 경우 -> pip install opencv-python 로 설치하는 것을 추천함

    print("abc")
    from getImage import edge_detection
    from getImage import projection
    vertices, img = edge_detection.detect_vertex('origin_imapge_3.png')
    result = [[10, 10], [200, 1100], [1300, 10], [1100, 1100]]
    #
    img_result = projection.perspective_projection(result, img)
    cv2.imshow("cat", img_result)
    cv2.waitKey()
    cv2.destroyAllWindows()
    cv2.imwrite('cat.jpg', img_result)


if __name__ == '__main__':
    print("Choose a function to execute:")
    print("1: makingModelH5")
    print("2: makingCover")

    choice = input("Enter the number of the function to execute: ")

    if choice == '1':
        makingModelH5()
    elif choice == '2':
        makingCover()
    else:
        print("Invalid choice. Please enter a number 1 or 2.")
