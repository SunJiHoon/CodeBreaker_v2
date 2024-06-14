import cv2

from getImage import projection

def getUserImage(img_result):
    width = 100*5  # to be resized
    height = 141*5  
    #resized_image = cv2.resize(img_result, (width, height))
    resized_image = projection.resize(img_result, height, width)
    
    #0,0 width, height
    #cv2.imshow("resized_Image", resized_image)
    #cv2.waitKey()
    #cv2.destroyAllWindows()
    x = 77  
    y = 274
    width = 248
    height = 330 
    cropped_image = resized_image[y:y+height, x:x+width]
    #cv2.imshow("cropped_image_stylebefore", cropped_image)
    #cv2.imshow("resized_Image", resized_image)
    #cv2.waitKey()

    cv2.imwrite('temp_userPicture.jpg', cropped_image)
    return cropped_image