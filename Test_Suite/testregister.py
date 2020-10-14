import os
import time
import unittest2
import sys
from lib.HTMLTestRuner import HTMLTestRunner
# print (__file__)
# print (os.path.realpath(__file__))
# print ('using sys.executable:', repr(os.path.dirname(os.path.realpath(sys.executable))))
# print ('using sys.argv[0]:',    repr(os.path.dirname(os.path.realpath(sys.argv[0]   ))))
# print (sys.argv[0])
# print (sys.path[0])


if __name__ == '__main__':
    # suite = unittest2.defaultTestLoader.discover("..\\testCase\\home_page\\", pattern='user_test.py')
    suite = unittest2.defaultTestLoader.discover("..\\testCase\\home_page\\", pattern='*_test.py')

    print(suite)
    path = os.path.dirname(os.getcwd())
    print(path)
    time_sign = time.strftime("%Y-%m-%d_%H-%M-%S")
    target_path = path + "/report/" + "测试报告" + time_sign + ".html"
    file = open(target_path, 'wb')
    HTMLTestRunner(stream=file, verbosity=1, title="核查宝测试报告HTML", description="测试环境：win10、i5、8G、500G", tester="臧一凡").run(suite)
    file.close()
