import cv2
from PIL import Image
from PIL import ImageChops 

work_path = 'D:\\qyt\\PycharmProjects\\test\\competitors\\timedelay\\'#设置工作目录
cap = cv2.VideoCapture(work_path + 'video\\20190419_175121.mp4') #创建一个视频获取对象
print(cap.isOpened())
cap.set(cv2.CAP_PROP_POS_AVI_RATIO,1)
length = cap.get(cv2.CAP_PROP_POS_MSEC)
print(length)
#flag = 10000
flag = 17000#人眼看到的预期图片的时间
#flag = 1500
#flag = 1550
cap.set(cv2.CAP_PROP_POS_MSEC, flag)#设置时间标记
ret,im = cap.read()#获取图像
file_name = work_path + str(flag) + '.jpg'
file_name_cropped = work_path + str(flag) + '_cropped.jpg'
cv2.imwrite(file_name, im)#保存图片

height_top = 200#截取图片的高度的上坐标
height_bottom = 1504#截取图片的高度的下坐标
width_left = 0#截取图片的宽度的左坐标
width_right = 720#截取图片的宽度的右坐标
img = cv2.imread(file_name)
print(img.shape)
cropped = img[height_top:height_bottom, width_left:width_right]  # 裁剪坐标为[y0:y1, x0:x1]
cv2.imwrite(file_name_cropped, cropped)

'''
image_expected = Image.open('D:\\qyt\\PycharmProjects\\test\\competitors\\timedelay\\expected.jpg')
image_actual = Image.open(file_name)
diff = ImageChops.difference(image_expected, image_actual)
if diff.getbbox() is None:
    print('same')
else:
    print('diff')
'''