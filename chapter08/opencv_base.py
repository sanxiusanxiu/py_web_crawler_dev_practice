import cv2

GAUSSIAN_BLUR_KERNEL_SIZE = (5, 5)
GAUSSIAN_BLUR_SIGMA_X = 0
CANNY_THRESHOLD1 = 200
CANNY_THRESHOLD2 = 450

# 传入待处理图片的信息，返回高斯滤波处理后的图片信息
def get_gaussian_blur_image(image):
    """
    OpenCV中用于实现高斯模糊的方法，叫作GaussianBlur，其声明如下：
    def GaussianBlur(src, ksize, sigmaX, dst=None, sigmaY=None, borderType=None)
    src：需要处理的图片
    ksize：高斯滤波处理所用的高斯内核大小，需要传人一个元组，包含x和y两个元素
    sigmaX：高斯内核函数在X方向上的标准偏差
    sigmaY：高斯内核函数在Y方向上的标准偏差。若sigmaY为0，就将它设为sigmaX；若sigmaX和sigmaY都是0，就通过ksize计算出sigmaX和sigmaY

    这里ksize和sigmaX是必传参数
    """
    return cv2.GaussianBlur(image, GAUSSIAN_BLUR_KERNEL_SIZE, GAUSSIAN_BLUR_SIGMA_X)


# 传入待处理图片的信息，返回边缘检测处理后的图片信息
def get_canny_image(image):
    """
    OpenCV中用于实现边缘检测的方法，叫作Canny，其声明如下：
    def Canny(image, threshold1, threshold2, edges=None, apertureSize=None, L2gradient=None)
    image：需要处理的图片
    threshold1、threshold2：最小判定临界点和最大判定临界点
    apertureSize：用于查找图片渐变的索贝尔内核的大小
    L2gradient：用于查找梯度幅度的等式

    通常来说，只需要设置threshold1和threshold2的值即可，其数值大小需要视具体图片而定
    """
    return cv2.Canny(image, CANNY_THRESHOLD1, CANNY_THRESHOLD2)


# 传入待处理图片的信息，返回提取得到的轮廓信息
def get_contours(image):
    """
    OpenCV中提取边缘轮廓的方法叫作findContours，其声明如下：
    def findContours(image, mode, method, contours=None, hierarchy=None, offset=None)
    image：需要处理的图片
    mode：用于定义轮廓的检索模式
    method：用于定义轮廓的近似方法

    这里我们将mode设置为RETRCCOMP，将method设置为CHAINAPPROXSIMPLE，具体的选择标准可以参考OpenCV官方文档的介绍
    """
    contours, _ = cv2.findContours(image, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    return contours

"""
得到各个轮廓信息后，便需要根据这些轮廓的外接矩形的面积和周长筛选我们想要的结果

第一步需要确定怎么筛选，例如我们可以给面积设定一个范围，给周长设定一个范围，另外给缺口位置也设定一个范围，
经过实际测量可以得出目标缺口的外接矩形的高度大约是验证码高度的0.25倍，宽度大约是验证码宽度的0.15倍，
所以在允许误差是20%的情况下，可以根据验证码的宽高信息大约计算出外接矩形的面积和周长的取值范围，
同时，缺口位置（缺口左侧）有一个最小偏移量和一个最大偏移量，这里的最小偏移量是验证码宽度的0.2倍，
最大偏移量是验证码宽度的0.85倍，将这些内容综合起来，我们可以定义以下3个阈值方法
"""

# 定义目标轮廓的面积下限和面积上限，分别为contour_area_min和contour_area_max
def get_contour_area_threshold(image_width, image_height):
    contour_area_min = (image_width * 0.15) * (image_height * 0.25) * 0.8
    contour_area_max = (image_width * 0.15) * (image_height * 0.25) * 1.2
    return contour_area_min, contour_area_max

# 定义目标轮廓的周长下限和周长上限，分别为arc_length_min和arc_length_max
def get_arc_length_threshold(image_width, image_height):
    arc_length_min = ((image_width * 0.15) + (image_height * 0.25)) * 2 * 0.8
    arc_length_max = ((image_width * 0.15) + (image_height * 0.25)) * 2 * 1.2
    return arc_length_min, arc_length_max

# 定义缺口位置的偏移量下限和偏移量上限，分别为offset_min和offset_max
def get_offset_threshold(image_width):
    offset_min = 0.2 * image_width
    offset_max = 0.85 * image_width
    return offset_min, offset_max

def main():
    # 设置待识别的图片
    image_raw = cv2.imread('picture04.png')
    image_height, image_width, _ = image_raw.shape
    # 依次调用高斯滤波、边缘检测、轮廓提取
    image_gaussian_blur = get_gaussian_blur_image(image_raw)
    image_canny = get_canny_image(image_gaussian_blur)
    contours = get_contours(image_canny)
    # 保存图片
    cv2.imwrite('image_canny.png', image_canny)
    cv2.imwrite('image_gaussian_blur.png', image_gaussian_blur)

    # 获取3个判断阈值
    contour_area_min, contour_area_max = get_contour_area_threshold(image_width, image_height)
    arc_length_min, arc_length_max = get_arc_length_threshold(image_width, image_height)
    offset_min, offset_max = get_offset_threshold(image_width)
    # 目标缺口位置的偏移量
    offset = None
    # 遍历contours，通过阈值进行筛选
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if contour_area_min < cv2.contourArea(contour) < contour_area_max and \
                arc_length_min < cv2.arcLength(contour, True) < arc_length_max and \
                offset_min < x < offset_max:
            # 标注外接矩形
            cv2.rectangle(image_raw, (x, y), (x + w, y + h), (0, 0, 255), 2)
            offset = x
    cv2.imwrite('image_label.png', image_raw)
    print('offset', offset)

if __name__ == '__main__':
    main()
