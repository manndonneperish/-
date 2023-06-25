import cv2
import os

os.chdir('颜色识别/') # 设置当前工作区，根据自己的实际情况更改

'''
该程序用于识别选定矩形区域的平均rgb值
'''

# 储存区域坐标和全局变量
regions = []

# 鼠标回调函数
def select_region(event, x, y, flags, param):
    global regions
    
    # 单机鼠标左键记录坐标
    if event == cv2.EVENT_LBUTTONDOWN:
        regions.append((x, y))
        
        # 在选定点进行标记
        cv2.circle(image, (x, y), 5, (0, 255, 0), -1)
        cv2.imshow('Image', image)
        
        # 如果选择两个点，绘制矩形区域
        if len(regions) == 2:
            x1, y1 = regions[0]
            x2, y2 = regions[1]
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            # 获取选中区域的平均rgb值
            cropped_image = image[min(y1, y2):max(y1, y2), min(x1, x2):max(x1, x2)]
            average_rgb = calculate_average_rgb(cropped_image)
            
            # 将rgb平均值转换为整数
            average_rgb = (int(average_rgb[0]), int(average_rgb[1]), int(average_rgb[2]))

            # 绘制显示平均rgb值的文本
            text = f"Average RGB: {average_rgb}"
            cv2.putText(image, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            
            # 重置区域
            regions = []
        
        cv2.imshow('Image', image)

# 将图像重置为原始状态
def reset_image():
    global image, regions
    regions = []
    image = cv2.imread(image_path)
    cv2.imshow('Image', image)

# 计算区域的平均rgb值
def calculate_average_rgb(image):
    total_rgb = [0, 0, 0]
    num_pixels = 0

    for row in image:
        for pixel in row:
            b, g, r = pixel
            total_rgb[0] += r
            total_rgb[1] += g
            total_rgb[2] += b
            num_pixels += 1

    average_rgb = [int(total / num_pixels) for total in total_rgb]
    return average_rgb

# 设置图片路径
image_path = 'colorpic.jpg'

# 加载图片
image = cv2.imread(image_path)

# 创建一个窗口并将鼠标回调函数绑定到该窗口
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', select_region)

# 显示图像
cv2.imshow('Image', image)

while True:
    # 等待按键
    key = cv2.waitKey(1) & 0xFF

    # 按'r'键重置图像
    if key == ord('r'):
        reset_image()
    
    # 按'esc'停止循环
    if key == 27:  # '27'为'esc'的ASCII值
        break

cv2.destroyAllWindows()
