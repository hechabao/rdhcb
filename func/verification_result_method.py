


def baogao(text):
    jianyi = []
    name = []
    shibai = 0
    chengong = 0
    shibaiwenjian = []
    if len(text)/3 == 0:
        for i in range(0,len(text),3):
            if text[i + 1] == '未知错误':
                shibai += 1
                shibaiwenjian.append(text[i + 2])
            elif text[i + 1] == '解析成功':
                chengong += 1
                name.append(text[i + 2])
    elif len(text)/3 != 0:
        for i in range(0, len(text), 3):
            try:
                if text[i+1] == '未知错误':
                    shibai+=1
                    shibaiwenjian.append(text[i+2])
                elif text[i+1] == '解析成功':
                    chengong+=1
                    name.append(text[i+2])
            except:
                jianyi.append(text[i])
    if len(jianyi) == 0:
        jianyi.append('没有建议')

    # print(jianyi,name,shibai,chengong,shibaiwenjian)
    jieguo = '成功%d个分别是%s文件，\n失败%d个分别是%s文件,\n建议%s\n'%(chengong,name,shibai,shibaiwenjian,jianyi)
    return jieguo
