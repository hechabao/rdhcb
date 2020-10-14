import time
import uiautomator2 as u2
d = u2.connect('WJX7N17A28000509')
print(d.info)
d.press("home")
d(description=u"设置").click()
time.sleep(1)
d.swipe(555, 2270, 555, 391)#滑动屏幕
time.sleep(1)
d(resourceId="android:id/title", text=u"应用管理").click()#进入应用管理
time.sleep(1)
d.swipe(565, 1960, 565, 330)
time.sleep(2)
d.swipe(565, 1960, 565, 330)
time.sleep(3)
'''
滑动屏幕至"咪咕圈圈"
'''
d(resourceId="android:id/title", text=u"咪咕圈圈").click()

#d.click(573, 988)
#d(resourceId="android:id/title", text=u"抖音短视频").click()
#d.press("home")

d(resourceId="com.android.settings:id/right_button").click()    #点击“强制停止”，停止应用
time.sleep(1)
d(resourceId="android:id/button1").click()  #点击“确定”
time.sleep(1)
d(resourceId="android:id/title", text=u"存储").click()
d(resourceId="com.android.settings:id/button_3").click()#清空缓存
d.press("home")
time.sleep(1)


#d(resourceId="androidhwext:id/preference_emui_description_container").click()


'''
sess = d.session('com.kuaikan.comic')
time.sleep(5)
sess.click(1330, 184)
time.sleep(3)
el = sess(resourceId="com.kuaikan.comic:id/search_input", className="android.widget.EditText")
el.set_text('珠')
sess.click(1311, 2304)
'''