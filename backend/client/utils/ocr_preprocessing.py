# coding=utf-8
import cv2
import numpy as np


# 处理文本类图片，并返回二值化中间结果
def binary(gray):
    sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, ksize=3)
    ret, thre = cv2.threshold(sobel, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)  # 二值化
    element1 = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 9))
    element2 = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 5))
    dilation = cv2.dilate(thre, element2, iterations=1)  # 膨胀
    erosion = cv2.erode(dilation, element1, iterations=1)  # 腐蚀
    dilation2 = cv2.dilate(erosion, element2, iterations=2)

    return dilation2


# 处理其他类图片，做前景背景分离，并返回二值化中间结果
def grab_cut(src):
    resize_height = 150
    resize_width = 200
    temporary_img = cv2.resize(src, (resize_width, resize_height), interpolation=cv2.INTER_AREA)  # 缩小图片，减少前景背景分割时间
    rect = (20, 10, 160, 130)
    mask = np.zeros(temporary_img.shape[:2], np.uint8)
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)
    cv2.grabCut(temporary_img, mask, rect, bgdModel, fgdModel, iterCount=1, mode=cv2.GC_INIT_WITH_RECT)  # 前景背景分离
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    foreground = temporary_img * mask2[:, :, np.newaxis]
    foreground = cv2.resize(foreground, (src.shape[1], src.shape[0]), interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(foreground, cv2.COLOR_RGB2GRAY)
    scale = src.shape[1] / 800
    gray = cv2.resize(gray, (800, round(gray.shape[0] / scale)), interpolation=cv2.INTER_AREA)
    ret, thre = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)
    element2 = cv2.getStructuringElement(cv2.MORPH_RECT, (24, 6))
    dilation = cv2.dilate(thre, element2, iterations=1)

    return dilation


def ocr_preprocessing(path, threshold=5):
    src = cv2.imdecode(np.fromfile(path, dtype=np.uint8), cv2.IMREAD_COLOR)
    if src is None:
        return -1
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    scale = gray.shape[1] / 800
    gray = cv2.resize(gray, (800, round(gray.shape[0] / scale)), interpolation=cv2.INTER_LINEAR)  # 归一化，便于后续统一标准处理
    mean = cv2.mean(gray)  # 求均值
    binary1 = np.where(gray < 20 + mean[0], 1, 0)
    if mean[0] > 190:  # 背景为白色的扫描件
        dilation2 = binary(gray)
    elif mean[0] < 40:  # 背景可能为黑色扫描件
        if sum(sum(binary1)) > gray.shape[0] * gray.shape[1] * 0.8:  # 背景为黑色扫描件
            dilation2 = binary(gray)
        else:  # 其他图片
            dilation2 = grab_cut(src)
    elif sum(sum(binary1)) > gray.shape[0] * gray.shape[1] * 0.8:  # 背景可能为其他颜色扫描件或图片中参杂其他内容的文字图片
        dilation2 = binary(gray)
    else:  # 其他类别图片
        dilation2 = grab_cut(src)

    dilation2, contours, hierarchy = cv2.findContours(dilation2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # 找轮廓
    box_heights = []
    area_heights = []
    region = []
    max_area_gray = gray.shape[1] * 0.8 * 50  # 设置的文本行可能的最大面积
    sum_area_cons = 0  # 所有轮廓的面积和
    sum_area_rect = 0  # 可能的非文本行的轮廓区域面积和
    sum_big_area = 0  # 非文本行区域面积
    num_area = 0  # 可能的文本行数量
    for i in range(len(contours)):
        cnt = contours[i]
        area = cv2.contourArea(cnt)
        sum_area_cons += area
        if area < 1500:
            continue
        elif area <= int(max_area_gray):
            rect = cv2.minAreaRect(cnt)  # 求轮廓的最小矩形
            box = cv2.boxPoints(rect)
            region.append(rect)
            num_area += 1
            temp = sorted(box[:, 1])
            if (abs(temp[2] - temp[1]) >= 10) & (abs(temp[2] - temp[1]) <= 40):
                box_heights.append(abs(temp[2] - temp[1]))  # 保存可能的文本行矩形高度
            else:
                area_heights.append(abs(temp[2] - temp[1]))  # 非文本行矩形高度
                sum_area_rect += area
        else:
            sum_big_area += area
    if len(box_heights) >= threshold:
        if num_area < 10:
            if sum_big_area <= 0.2 * gray.shape[0] * gray.shape[1]:
                return 1
            else:
                return 0
        else:
            return 1
    elif len(box_heights) > 0 and sum_big_area <= 0.1 * gray.shape[0] * gray.shape[1]:
        if len(box_heights) > len(area_heights):
            return 1
        else:
            return 0
    else:
        return 0



