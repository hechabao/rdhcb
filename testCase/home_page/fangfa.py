# import time
# from selenium import webdriver
# import random
# 
# 
# name_url = ["D:\\2.1\\招股书-测试样本\\科创板\\奥基科技-科创板\\傲基科技：招股说明书 0828-0341.docx",
#             "D:\\2.1\\招股书-测试样本\\科创板\\奥基科技-科创板\\2【傲基科技】法律意见书 20190827 clean.docx",
#             "D:\\2.1\\招股书-测试样本\\科创板\\奥基科技-科创板\\深圳分所：大华审字(2019)009872号傲基科技股份有限公司5+1份-数字.xlsx"]
# 
# def createziranrenkehu(s):
#     drive = webdriver.Firefox()
#     drive.maximize_window()
#     drive.get('http://192.168.6.230:212/#/')
#     time.sleep(1)
#     drive.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div/input').send_keys('zjw')
#     drive.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/input').send_keys('a123456')
#     drive.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/button/span').click()
#     time.sleep(3)
#     drive.find_element_by_xpath('/html/body/div/div/section/section/aside/div/div[1]/div/div/ul/li[2]/div').click()
#     drive.find_element_by_xpath('/html/body/div/div/section/section/aside/div/div[1]/div/div/ul/li[2]/ul/li[2]').click()
#     time.sleep(1)
# 
#     if s != 0:
#         drive.find_element_by_xpath(
#             '/html/body/div[1]/div/section/section/main/div/div[1]/div/div/div[1]/div[2]/button/span').click()
#     else:
#         drive.find_element_by_xpath(
#             '/html/body/div/div/section/section/main/div/div[1]/div/div/div[1]/div[2]/button/span').click()
#     drive.find_element_by_xpath(
#         '/html/body/div[1]/div/section/section/main/div/div[1]/div/div/div[1]/div[6]/div/div[2]/div/div/div[1]/div/form/div[1]/div/div/input').send_keys(
#         '测试' + str(random.randint(0, 90000)))
#     drive.find_element_by_xpath(
#         '/html/body/div[1]/div/section/section/main/div/div[1]/div/div/div[1]/div[6]/div/div[2]/div/div/div[1]/div/form/div[2]/div/div/input').send_keys(
#         'OK')
#     drive.find_element_by_xpath(
#         '/html/body/div[1]/div/section/section/main/div/div[1]/div/div/div[1]/div[6]/div/div[2]/div/div/div[1]/div/form/div[3]/div/div/div[1]/input').click()
#     time.sleep(1)
#     if s != 0:
#         UI = drive.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul')
#         li = UI.find_elements_by_xpath('li')
#         s = len(li)
#         li[s - 1].click()
#     else:
#         UI = drive.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul')
#         li = UI.find_elements_by_xpath('li')
#         s = len(li)
#         li[s - 1].click()
# 
#     drive.find_element_by_xpath(
#         '/html/body/div[1]/div/section/section/main/div/div[1]/div/div/div[1]/div[6]/div/div[2]/div/div/div[1]/div/form/div[4]/div/div/div[1]/input').click()
#     time.sleep(1)
#     if s != 0:
#         drive.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[2]').click()
#     else:
#         drive.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li[2]').click()
# 
#     drive.find_element_by_xpath(
#         '/html/body/div[1]/div/section/section/main/div/div[1]/div/div/div[1]/div[6]/div/div[2]/div/div/div[1]/div/form/div[5]/div/div/label[1]/span[1]/span').click()
#     drive.find_element_by_xpath(
#         '/html/body/div[1]/div/section/section/main/div/div[1]/div/div/div[1]/div[6]/div/div[2]/div/div/div[1]/div/form/div[6]/div/div/input').click()
#     drive.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[2]/table[1]/tbody/tr[5]/td[7]/div/span').click()
#     drive.find_element_by_xpath(
#         '/html/body/div[1]/div/section/section/main/div/div[1]/div/div/div[1]/div[6]/div/div[2]/div/div/div[1]/div/form/div[7]/div/div/input').send_keys(
#         120102201801014215)
#     drive.find_element_by_xpath(
#         '/html/body/div[1]/div/section/section/main/div/div[1]/div/div/div[1]/div[6]/div/div[2]/div/div/div[1]/div/form/div[8]/div/div/div[1]/input').click()
#     drive.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/ul/li[1]').click()
#     time.sleep(1)
#     drive.find_element_by_xpath(
#         '/html/body/div[1]/div/section/section/main/div/div[1]/div/div/div[1]/div[6]/div/div[2]/div/div/div[1]/div/form/div[9]/div/div/input').send_keys(
#         17600446278)
#     drive.find_element_by_xpath(
#         '/html/body/div[1]/div/section/section/main/div/div[1]/div/div/div[1]/div[6]/div/div[2]/div/div/div[1]/div/form/div[10]/div/div/input').send_keys(
#         '502900588@qq.com')
#     drive.find_element_by_xpath(
#         '/html/body/div[1]/div/section/section/main/div/div[1]/div/div/div[1]/div[6]/div/div[2]/div/div/div[1]/div/form/div[11]/div/div/input').send_keys(
#         100000)
#     drive.find_element_by_xpath(
#         '/html/body/div[1]/div/section/section/main/div/div[1]/div/div/div[1]/div[6]/div/div[2]/div/div/div[1]/div/form/div[12]/div/div/div[1]/input').click()
#     time.sleep(1)
#     drive.find_element_by_xpath('/html/body/div[7]/div[1]/div[1]/ul/li[1]').click()
#     drive.find_element_by_xpath(
#         '/html/body/div[1]/div/section/section/main/div/div[1]/div/div/div[1]/div[6]/div/div[2]/div/div/div[1]/div/form/div[13]/div/button').click()
#     time.sleep(1)
#     drive.find_element_by_xpath(
#         '/html/body/div[1]/div/section/section/main/div/div[1]/div/div/div[3]/div/div/div/div[2]/div/div[1]/div[2]/div[1]/input').send_keys(
#         '闫成龙')
#     drive.find_element_by_xpath(
#         '/html/body/div[1]/div/section/section/main/div/div[1]/div/div/div[3]/div/div/div/div[2]/div/div[1]/div[2]/div[1]/div/button').click()
#     time.sleep(2)
#     drive.find_element_by_xpath(
#         '/html/body/div[1]/div/section/section/main/div/div[1]/div/div/div[3]/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div/div[1]/div/div/p[2]').click()
#     drive.find_element_by_xpath(
#         '/html/body/div[1]/div/section/section/main/div/div[1]/div/div/div[3]/div/div/div/div[3]/span/button[2]').click()
#     drive.find_element_by_xpath(
#         '/html/body/div[1]/div/section/section/main/div/div[1]/div/div/div[1]/div[6]/div/div[2]/div/div/div[1]/div/form/div[14]/div/div/textarea').send_keys(
#         '北京市，东城区，广安城，南街98号，99层，983329')
#     drive.find_element_by_xpath(
#         '/html/body/div[1]/div/section/section/main/div/div[1]/div/div/div[1]/div[6]/div/div[2]/div/div/div[1]/div/form/div[15]/div/div/textarea').send_keys(
#         '请及时联系，Call me')
#     drive.find_element_by_xpath(
#         '/html/body/div[1]/div/section/section/main/div/div[1]/div/div/div[1]/div[6]/div/div[3]/span/button[2]').click()
#     time.sleep(2)
#     drive.quit()
# 
# 
# def createzongjiejigou(s):
#     drive = webdriver.Chrome()
#     drive.maximize_window()
#     drive.get('http://192.168.6.230:212/#/')
#     time.sleep(1)
#     drive.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div/input').send_keys('zjw')
#     drive.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/input').send_keys('a123456')
#     drive.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/button/span').click()
#     time.sleep(4)
#     drive.find_element_by_xpath('/html/body/div/div/section/section/aside/div/div[1]/div/div/ul/li[2]/div').click()
#     time.sleep(1)
#     drive.find_element_by_xpath('/html/body/div/div/section/section/aside/div/div[1]/div/div/ul/li[2]/ul/li[3]').click()
#     time.sleep(1)
#     drive.find_element_by_xpath(
#         '/html/body/div/div/section/section/main/div/div[1]/div/div/div[1]/div[2]/button/span').click()
#     drive.find_element_by_xpath(
#         '/html/body/div[1]/div/section/section/main/div/div[1]/div/div/div[1]/div[6]/div/div[2]/div/div/div[1]/div/form/div[1]/div/div/input').send_keys(
#         '中介机构' + str(random.randint(0, 90000)))
#     drive.find_element_by_xpath(
#         '/html/body/div[1]/div/section/section/main/div/div[1]/div/div/div[1]/div[6]/div/div[2]/div/div/div[1]/div/form/div[2]/div/div/input').send_keys(
#         '测试数据验证机构')
#     drive.find_element_by_xpath(
#         '/html/body/div[1]/div/section/section/main/div/div[1]/div/div/div[1]/div[6]/div/div[2]/div/div/div[1]/div/form/div[3]/div/div/div[1]/input').click()
#     drive.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[2]').click()
#     drive.find_element_by_xpath(
#         '/html/body/div[1]/div/section/section/main/div/div[1]/div/div/div[1]/div[6]/div/div[2]/div/div/div[1]/div/form/div[4]/div/div/input').send_keys(
#         '闫成龙2号')
#     drive.find_element_by_xpath(
#         '/html/body/div[1]/div/section/section/main/div/div[1]/div/div/div[1]/div[6]/div/div[2]/div/div/div[1]/div/form/div[5]/div/button/span').click()
#     time.sleep(1)
#     drive.find_element_by_xpath(
#         '/html/body/div[1]/div/section/section/main/div/div[1]/div/div/div[3]/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div/div[1]/div/div/div[1]/div[2]/div[4]/div[2]/div[4]/div[1]/span[2]').click()
#     drive.find_element_by_xpath(
#         '/html/body/div[1]/div/section/section/main/div/div[1]/div/div/div[3]/div/div/div/div[3]/span/button[2]/span').click()
#     drive.find_element_by_xpath(
#         '/html/body/div[1]/div/section/section/main/div/div[1]/div/div/div[1]/div[6]/div/div[2]/div/div/div[1]/div/form/div[6]/div/div/input').send_keys(
#         '17600446278')
#     drive.find_element_by_xpath(
#         '/html/body/div[1]/div/section/section/main/div/div[1]/div/div/div[1]/div[6]/div/div[2]/div/div/div[1]/div/form/div[7]/div/div/input').send_keys(
#         '502900588@qq.com')
#     drive.find_element_by_xpath(
#         '/html/body/div[1]/div/section/section/main/div/div[1]/div/div/div[1]/div[6]/div/div[2]/div/div/div[1]/div/form/div[10]/div/div/input').send_keys(
#         '北京市西城区南街一单元50房间')
#     drive.find_element_by_xpath('/html/body/div[1]/div/section/section/main/div/div[1]/div/div/div[1]/div[6]/div/div[2]/div/div/div[1]/div/form/div[11]/div/div/input').send_keys('www.baidu.com')
#     drive.find_element_by_xpath('/html/body/div[1]/div/section/section/main/div/div[1]/div/div/div[1]/div[6]/div/div[2]/div/div/div[1]/div/form/div[12]/div/div/textarea').send_keys('2018年11月5日，上海证券交易所表示将积极研究制订科创板和注册制试点方案，向市场征求意见并履行报批程序后实施。截止2019-09-16科创板已申报156家')
#     drive.find_element_by_xpath(
#         '/html/body/div[1]/div/section/section/main/div/div[1]/div/div/div[1]/div[6]/div/div[2]/div/div/div[1]/div/form/div[13]/div/div/textarea').send_keys(
#         '发行人及全体董事、监事、高级管理人员承诺招股说明书及其摘要不存在虚假记载、误导性陈述或重大遗漏，并对其真实性、准确性、完整性承担个别和连')
#     drive.find_element_by_xpath('/html/body/div[1]/div/section/section/main/div/div[1]/div/div/div[1]/div[6]/div/div[3]/span/button[2]/span').click()
#     drive.quit()
# 
# for m in range(100):
# #     createzongjiejigou(m)

# import unittest
#
a = 1
def panduan():
    global a
    a+=1
    return a
#
# class TestSetupTeardown(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         print('连接数据库成功...')
#
#     @classmethod
#     def tearDownClass(cls):
#         print('关闭数据库。')
#
#     def test_a(self):
#         print('test_a')
#
#     def test_b(self):
#         print('test_b')
#
#
# if __name__ == '__main__':
#     unittest.main()


# import unittest
#
#
# class TestSetupTeardown(unittest.TestCase):
#     def setUp(self):
#         print('连接数据库成功...')
#
#     def tearDown(self):
#         print('关闭数据库。')
#
#     def test_sdasdsa(self):
#         print('test_b')
#
#     def test_0asdasl(self):
#         print('test_a')
#
#     def test_dsad(self):
#         print('test_b')
# if __name__ == '__main__':
#     unittest.main()

# # import
# # import unittest
# 
# 
# class TestSetupTeardown(unittest2.TestCase):
#     @classmethod
#     def setUpClass(self):
#         print('连接数据库成功...')
# 
#     @classmethod
#     def tearDownClass(self):
#         print('关闭数据库。')
# 
# 
# 
# 
# if __name__ == '__main__':
#     unittest2.main()
# import unittest
# import time
#
# def setUpModule():
#     print("集成测试------开始")
#     print("")
#
# def tearDownModule():
#     print("集成测试------结束")
#     print("")
#
# class SimpleTest1(unittest.TestCase):
#     def test_1st(self):
#         print("单元测试1—step1")
#         time.sleep(1)
#
#     def test_2nd(self):
#         print('单元测试1---step1')
#         time.sleep(1)
#
# class SimpleTest2(unittest.TestCase):
#     def test_3st(self):
#         print("单元测试2—step3")
#         time.sleep(1)
#
#     def test_4nd(self):
#         print('单元测试2---step4')
#         time.sleep(1)
# if __name__=='__main__':
#     unittest.main()
# 集成测试------开始
# 单元测试1—step1
# 单元测试1—step1
# 单元测试2—step3
# 单元测试2—step4
# 集成测试------结束