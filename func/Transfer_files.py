import os




def wenjianlujin():
    zong = []
    xingxi = []
    kaishi = []
    wenjians = []
    wenjian = os.listdir('D:\\用例文件\\')
    # print(wenjian)
    for i in range(len(wenjian)):
        name = wenjian[i].split('-')[0]
        youyige = os.listdir('D:\\用例文件\\'+wenjian[i]+'\\')
        # print(youyige)
        xingxi.append('测试：'+name)
        xingxi.append('一般企业')
        xingxi.append("admin")
        for j in youyige:
            hhh = 'D:\\用例文件\\'+wenjian[i]+'\\'+ j
            wenjians.append(hhh)
            # print('D:\\用例文件\\'+wenjian[i]+'\\'+ j)
        kaishi.append(wenjians)
        wenjians = []
        kaishi.append(xingxi)
        xingxi = []
        zong.append(kaishi)
        kaishi=[]
    # print(zong)
    return zong


# #
# a = wenjianlujin()
# print(a)