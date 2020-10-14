import uiautomator2 as u2
import time
d = u2.connect('PNXGAM6890801418')
estimated_delay_time = 20#预计时延时间，单位：秒
record_count = 3#录屏次数
package_name = 'cmb.pb'
print(d.info)
for i in range(record_count):
    print('record: ' + str(i + 1))
    d.press('home')
    d(text=u'小熊录屏').click()#启动录频app
    time.sleep(2)
    start = time.time()
    #print(start)
    d.click(961, 875)#点开始录频按钮
    time.sleep(5)
    end = time.time()
    #print(end)
    d.click(970, 1345)#启动被测app
    time.sleep(estimated_delay_time)
    d(resourceId='com.duapps.recorder:id/durec_float_little_view_dot_red').click()#点开录制app浮窗
    time.sleep(2)
    d.click(878, 1062)#点结束录频按钮
    time.sleep(2)
    d.swipe(907, 58, 907, 1551)#下拉快捷工具栏
    time.sleep(2)
    #d.click(983, 941)
    d(resourceId="com.duapps.recorder:id/action_view", className="android.widget.ImageView", instance=4).click()#关闭录频app
    time.sleep(2)
    d.press('back')
    #d.press('home')
    time.sleep(5)
    d.app_stop(package_name)#停止被测app
    time.sleep(2)
    #d.app_clear(package_name)#清除被测app数据和缓存
    print(round((end - start) * 1000))
    print('end\n')