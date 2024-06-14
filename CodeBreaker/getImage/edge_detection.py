import sys
import io
# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import cv2

global img
global dst

global visited
global center
global lu, ld, ru, rd
global result


def detect_vertex(img_path):
    print('detect vertex')
    global img

    test_img = cv2.imread(img_path)
    height, width, channels = test_img.shape
    global dst
    dst = test_img.copy()

    global visited
    visited = [[False for i in range(width)] for j in range(height)]

    global result
    result = [[0, 0], [0, 0], [0, 0], [0, 0]]

    for col in range(1, height - 1):
        for row in range(1, width - 1):
            gray_color = (int(test_img[col][row][0]) + int(test_img[col][row][1]) + int(test_img[col][row][2])) / 3
            dst[col][row] = [gray_color, gray_color, gray_color]
            if dst[col][row][0] > 200:
                dst[col][row] = [255, 255, 255]
            else:
                dst[col][row] = [0, 0, 0]

    global center
    center = [int(height / 2), int(width / 2)]

    global lu, ld, ru, rd
    lu, ld, ru, rd = center[0] + center[1], 0, center[0] + center[1], 0

    for i in range(1, height - 1):
        for j in range(1, width - 1):
            if dst[i][j][0] == 255 and not visited[i][j]:
                dfs([i, j])

    print(result)

    return result, test_img


def dfs(pos):
    global lu, ld, ru, rd
    global result
    global visited

    tlu, tld, tru, trd = lu, ld, ru, rd
    temp_result = result

    stack = [pos]
    count = 0

    while len(stack) != 0:
        cur = stack.pop()

        if visited[cur[0]][cur[1]]:
            continue

        visited[cur[0]][cur[1]] = True
        count += 1

        if cur[0] < center[0]:
            if cur[1] > center[1]:  # 1��и� d = y - x�� �ּ�
                if tru > cur[0] - cur[1]:
                    tru = cur[0] - cur[1]
                    temp_result[1] = [cur[0], cur[1]]
            else:  # 2��и� d = y + x�� �ּ�
                if tlu > cur[0] + cur[1]:
                    tlu = cur[0] + cur[1]
                    temp_result[0] = [cur[0], cur[1]]
        else:
            if cur[1] > center[1]:  # 4��и� d = y + x�� �ִ�
                if trd < cur[0] + cur[1]:
                    trd = cur[0] + cur[1]
                    temp_result[3] = [cur[0], cur[1]]
            else:  # 3��и� d = y - x�� �ִ�
                if tld < cur[0] - cur[1]:
                    tld = cur[0] - cur[1]
                    temp_result[2] = [cur[0], cur[1]]

        if dst[cur[0] + 1][cur[1]][0] == 255 and not visited[cur[0] + 1][cur[1]]:
            stack.append([cur[0] + 1, cur[1]])
        if dst[cur[0]][cur[1] + 1][0] == 255 and not visited[cur[0]][cur[1] + 1]:
            stack.append([cur[0], cur[1] + 1])
        if dst[cur[0] - 1][cur[1]][0] == 255 and not visited[cur[0] - 1][cur[1]]:
            stack.append([cur[0] - 1, cur[1]])
        if dst[cur[0]][cur[1] - 1][0] == 255 and not visited[cur[0]][cur[1] - 1]:
            stack.append([cur[0], cur[1] - 1])

    if count > 1000:
        if tlu < lu:
            lu = tlu
            result[1] = temp_result[1]
        if tld > ld:
            ld = tld
            result[2] = temp_result[2]
        if tru < ru:
            ru = tru
            result[0] = temp_result[0]
        if trd > rd:
            rd = trd
            result[3] = temp_result[3]


## Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    detect_vertex("test1.jpg")