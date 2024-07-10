import cv2

# from getImage import projection

def getUserImage(img_result):
    width = 100*5 * 5  # to be resized
    height = 141*5 * 5
    resized_image = cv2.resize(img_result, (width, height))
    # resized_image = projection.resize(img_result, height, width)
    
    #0,0 width, height
    #cv2.imshow("resized_Image", resized_image)
    #cv2.waitKey()
    #cv2.destroyAllWindows()
    x = 77   * 5
    y = 274 * 5
    # width = 248
    # height = 330
    x_fin = (77 + 248) * 5
    y_fin = (274 + 330) * 5
    # cropped_image = resized_image[y:y + height, x:x + width]
    cropped_image = resized_image[y:y_fin, x:x_fin]

    #cv2.imshow("cropped_image_stylebefore", cropped_image)
    #cv2.imshow("resized_Image", resized_image)
    #cv2.waitKey()

    cv2.imwrite('temp_userPicture.jpg', cropped_image)
    return cropped_image