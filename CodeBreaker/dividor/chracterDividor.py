import cv2
# from getImage import projection

def chracterDividor(img_result):
    width = 100*5  # to be resized
    height = 141*5  
    resized_image = cv2.resize(img_result, (width, height))
    # resized_image = projection.resize(img_result, height, width)

    #cv2.imshow("resized_Image", resized_image)
    #cv2.waitKey()
    #cv2.destroyAllWindows()
    
    imageLi = []
    x = 77  
    y = 70
    width = 37  
    height = 39  
    for i in range(4):
        for j in range(7):
            cropX = x + width * j
            cropY = y + height * i
            cropped_image = resized_image[cropY:cropY+height, cropX:cropX+width]
            imageLi.append(cropped_image)
            #cv2.imshow("cropped_image", cropped_image)
            #cv2.waitKey()
            #cv2.destroyAllWindows()
    return imageLi