import cv2
import os
from PIL import Image
from PIL import ImageChops

def extract_crop(position_time, height_top, height_bottom, width_left, width_right):
    cap.set(cv2.CAP_PROP_POS_MSEC, position_time)#设置时间标记
    ret,im = cap.read()#获取图像
    cv2.imwrite(work_path + 'temp.jpg', im)#保存图片

    img = cv2.imread(work_path + 'temp.jpg')#读取图片
    #print(img.shape)
    try:
        cropped = img[height_top:height_bottom, width_left:width_right]  # 裁剪坐标为[y0:y1, x0:x1]
    except TypeError:
        print('NoneType Error NoneType Error NoneType Error NoneType Error NoneType Error NoneType Error NoneType Error')
        raise Exception()
    cv2.imwrite(work_path + 'temp.jpg', cropped)#保存图片

def compare_image(image_expected, image_actual):
    diff = ImageChops.difference(image_expected, image_actual)#跟预期图片做比较
    if diff.getbbox() is None:
        #print('same')
        return True#相同返回True
    else:
        #print('diff')
        return False#不同返回False

def interval(duration):
    position_time_list = []
    count = duration // (1000 * interval_time)
    for i in range(count + 1):
        position_time_list.append(i * 1000 * interval_time)
    if duration % (1000 * interval_time) != 0:#如果视频时间长度不能被设置的间隔时间整除，在时间点列表的最后加上最后一帧的时间点
        position_time_list.append(duration)
    return position_time_list

work_path = 'D:\\qyt\\PycharmProjects\\test\\competitors\\timedelay\\'#设置工作目录
image_expected = Image.open(work_path + 'expected.jpg')#打开预期图片，在之后的比较时使用
height_top = 200#截取图片的高度的上坐标
height_bottom = 1504#截取图片的高度的下坐标
width_left = 0#截取图片的宽度的左坐标
width_right = 720#截取图片的宽度的右坐标
interval_time = 3#抽帧间隔时间长度，单位：秒，间隔时间长度一定要小于预期结果在手机上保持不变的时间长度

for filename in os.listdir(work_path + 'video'):#拿到video文件夹下的每一个视频文件名
    has_error = False
    print(filename)
    cap = cv2.VideoCapture(work_path + 'video\\' + filename) #创建一个视频获取对象
    #print(cap.isOpened())
    cap.set(cv2.CAP_PROP_POS_AVI_RATIO,1)#下面三步用来获取整个视频的时长并打印
    duration = int(cap.get(cv2.CAP_PROP_POS_MSEC)) 
    print('duration:' + str(duration) + 'ms')

    
    position_time_list = interval(duration)#获得抽帧的时间点列表，每过一次间隔时间是一个时间点
    #print(position_time_list)
    for position_time in position_time_list:#把抽出的每一张图片与预期图片做比较，找到第一张符合结果的图片后，以这张图片的时间点为end，以前一张图片的时间点为start，供后面精确查找使用
        try:
            extract_crop(position_time, height_top, height_bottom, width_left, width_right)
        except Exception:
            has_error = True
            break
        image_actual = Image.open(work_path + 'temp.jpg')#打开图片
        if compare_image(image_expected, image_actual):
            start = position_time - (1000 * interval_time)
            end = position_time
            break
    if has_error:
        print('\n');
        continue
	
    '''
    start = 0
    end = duration
    '''
    length = end - start
	
    while length > 2:#不断取视频片段的中点帧与预期图片做比较，从而缩小查找范围，直到找到第一次出现预期图片的时间点为止
        if length % 2 == 1:
            position_time = start + (length + 1) / 2
        else:
            position_time = start + length / 2
        position_time = int(position_time)

        try:
            extract_crop(position_time, height_top, height_bottom, width_left, width_right)
        except Exception:
            break
			
        image_actual = Image.open(work_path + 'temp.jpg')#打开图片
        if compare_image(image_expected, image_actual):
            end = position_time
        else:
            start = position_time

        length = end - start
    #print('start:' + str(start) + 'ms')
    print('end:' + str(end) + 'ms\n')