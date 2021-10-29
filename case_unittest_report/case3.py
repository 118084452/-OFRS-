#coding = utf-8
import unittest
from appium import webdriver
import win32gui,win32api,win32con
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time,os,random
import binascii
import struct


class MyTest2(unittest.TestCase):
    def setUp(self):
        self.desired_caps = {}
        self.desired_caps['app'] = r"D:\RWD-OFRS\RWD-FPsystem\OFRS.exe"
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities=self.desired_caps)
        # print(self.driver)
        self.mainWindow = self.driver.current_window_handle
        # print('当前窗口句柄为：{}'.format(self.mainWindow))
        self.jz10 = str(int(self.mainWindow.upper(), 16))
        # print(self.jz10)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        if self.is_element_exist("分 析"):
            # print("元素存在")
            self.driver.find_element_by_name("分 析").click()
            self.driver.implicitly_wait(2)
            wz = self.driver.get_window_position(self.mainWindow)
            print(wz)
            self.driver.switch_to.window(self.driver.window_handles[0])
        else:
            pass

    def tearDown(self):
        self.driver.quit()
        # pass

    def is_element_exist(self, element):
        source = self.driver.page_source
        # print(source)
        if element in source:
            return True
        else:
            return False

    def test_calc1(self):
        """ 数据预处理 """
        try:
            DIR = r'D:\RWD-OFRS\Experiment'
            file_num = len(os.listdir(DIR))
            print("文件夹内文件的个数:", file_num)
            num = random.randint(5, 50)
            num1 = random.randint(5, 12)
            self.driver.implicitly_wait(10)
            i = 1
            while i <= 12:
                self.driver.find_element_by_name('选择文件').click()
                self.driver.find_element_by_class_name('Edit').send_keys(DIR)
                self.driver.find_element_by_class_name('Edit').send_keys(Keys.ENTER)
                self.driver.find_element_by_xpath('//ListItem[{}]/Edit[1]'.format(i)).click()   # 选择荧光数据
                self.driver.implicitly_wait(10)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                time.sleep(0.01)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                # time.sleep(0.5)
                self.driver.implicitly_wait(5)
                self.driver.find_element_by_class_name("UIImage").click()
                self.driver.implicitly_wait(5)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                time.sleep(0.01)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                self.driver.find_element_by_xpath('//Group/ComboBox[1]').click()
                self.driver.find_element_by_xpath('//Group/ComboBox[1]/ListItem[2]/Text').click()
                self.driver.find_element_by_xpath('//Group/ComboBox[2]').click()
                self.driver.find_element_by_xpath('//Group/ComboBox[2]/ListItem[2]/Text').click()
                # self.driver.find_element_by_xpath('//Group/CheckBox[1]/Text/Text').click()      # 平滑处理勾选
                # self.driver.find_element_by_xpath('//Group/CheckBox[2]/Text/Text').click()      # 基线矫正勾选
                self.driver.find_element_by_name('平滑处理').click()  # 平滑处理勾选
                self.driver.find_element_by_xpath('//Group/Edit[3]').click()
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                time.sleep(0.01)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                self.driver.find_element_by_xpath('//Group/Edit[3]').send_keys(num)
                self.driver.find_element_by_name('基线矫正').click()  # 基线矫正勾选
                self.driver.find_element_by_xpath('//Group/Edit[4]').click()
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                time.sleep(0.01)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                self.driver.find_element_by_xpath('//Group/Edit[4]').send_keys(num1)
                self.driver.find_element_by_name('绘图').click()
                print('脚本执行第{}次成功'.format(i))
                time.sleep(5)
                # break
                i += 1

        except Exception as f:
            print(f)

    def calc2(self):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        # time.sleep(0.5)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_class_name("UIImage").click()
        self.driver.implicitly_wait(5)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)


if __name__ == '__main__':
    # 启动单元测试
    unittest.main()

