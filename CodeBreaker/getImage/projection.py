# import sys
# import io
# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import numpy as np
# import cv2


def perspective_projection_util(img_src, dst, img_dst, src):

    m = np.array(
        [
            [src[0], src[1], 1, 0, 0, 0, -src[0]*dst[0], -dst[0]*src[1]],
            [0, 0, 0, src[0], src[1], 1, -src[0]*dst[1], -src[1]*dst[1]],
            [src[2], src[3], 1, 0, 0, 0, -src[2]*dst[2], -dst[2]*src[3]],
            [0, 0, 0, src[2], src[3], 1, -src[2]*dst[3], -src[3]*dst[3]],
            [src[4], src[5], 1, 0, 0, 0, -src[4]*dst[4], -dst[4]*src[5]],
            [0, 0, 0, src[4], src[5], 1, -src[4]*dst[5], -src[5]*dst[5]],
            [src[6], src[7], 1, 0, 0, 0, -src[6]*dst[6], -dst[6]*src[7]],
            [0, 0, 0, src[6], src[7], 1, -src[6]*dst[7], -src[7]*dst[7]],
        ]
    )

    m_inverse = np.linalg.inv(m)
    a = m_inverse@dst

    # height_src, width_src, channel_src = img_src.shape
    height_dst, width_dst, channel_dst = img_dst.shape

    for y_p in range(height_dst):
        for x_p in range(width_dst):
            x = (a[0]*x_p + a[1]*y_p + a[2]) / (a[6]*x_p + a[7]*y_p + 1)
            y = (a[3]*x_p + a[4]*y_p + a[5]) / (a[6]*x_p + a[7]*y_p + 1)
            x = int(x)
            y = int(y)
            if(x < min(dst[0], dst[2], dst[4], dst[6]) or x > max(dst[0], dst[2], dst[4], dst[6])):
                continue
            if(y < min(dst[1], dst[3], dst[5], dst[7]) or y > max(dst[1], dst[3], dst[5], dst[7])):
                continue
            img_dst[y_p, x_p] = img_src[y, x]


def perspective_projection(vertices, image, new_height=800, new_width=600):
    height, width, channel = image.shape

    print(height, width, channel)
    image_new = np.zeros((new_height, new_width, 3), np.uint8)
    height_dst, width_dst, channel_dst = image_new.shape

    src = np.array(
        [
            vertices[0][1], vertices[0][0],
            vertices[1][1], vertices[1][0],
            vertices[2][1], vertices[2][0],
            vertices[3][1], vertices[3][0]
        ]
    )

    dst = np.array(
        [
            0, 0,
            width_dst-1, 0,
            0, height_dst-1,
            width_dst-1, height_dst-1
        ]
    )

    perspective_projection_util(image, src, image_new, dst)
    
    #cv2.imshow("cat", image)
    #cv2.imshow("cat2", image_new)
    #cv2.waitKey()
    #cv2.destroyAllWindows()

    return image_new

def resize(img, new_height, new_width):
    height, width, channel = img.shape
    vertices = [[0, 0], [0, width-1], [height-1, 0], [height-1, width-1]]
    return perspective_projection(vertices, img, new_height, new_width)