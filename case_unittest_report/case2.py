#coding = utf-8
import unittest
from appium import webdriver
import win32gui,win32api,win32con
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time,os
import binascii
import struct


class MyTest1(unittest.TestCase):
    def setUp(self):
        self.desired_caps = {}
        self.desired_caps['app'] = r"D:\RWD-OFRS\RWD-FPsystem\OFRS.exe"
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities=self.desired_caps)
        print(self.driver)

        self.mainWindow = self.driver.current_window_handle
        # print('当前窗口句柄为：{}'.format(self.mainWindow))
        self.jz10 = str(int(self.mainWindow.upper(), 16))
        print(self.jz10)
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
        """光纤记录系统测试"""
        try:
            DIR = r'D:\RWD-OFRS\Experiment'
            file_num = len(os.listdir(DIR))
            print("文件夹内文件的个数:", file_num)
            i = 1
            while i <= file_num:
                if self.is_element_exist("选择视频"):
                    # print("元素存在")

                    self.mainWindow1 = self.driver.current_window_handle
                    print('当前执行的窗口句柄为：{}'.format(self.mainWindow1))
                    self.driver.implicitly_wait(5)
                    self.driver.find_element_by_name("选择视频").click()
                    self.driver.implicitly_wait(5)
                    # self.driver.find_element_by_name('文件名(N):').click()
                    self.driver.find_element_by_class_name('Edit').send_keys(DIR)
                    self.driver.find_element_by_class_name('Edit').send_keys(Keys.ENTER)
                    self.driver.implicitly_wait(5)
                    s = 1
                    # if i % 13 == 0:
                    while i > 1:
                        self.driver.implicitly_wait(5)
                        self.driver.find_element_by_xpath('//Pane[2]/List/ScrollBar/Thumb').click()
                        self.driver.implicitly_wait(5)
                        for j in range(9):
                            win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -90)
                            time.sleep(0.01)
                        self.driver.implicitly_wait(5)
                        self.driver.find_element_by_xpath('//ListItem[{}]/Edit[1]'.format(i)).click()
                        self.driver.implicitly_wait(5)
                        self.calc2()
                        print('脚本执行第{}次成功'.format(i))
                        return self.test_calc1()

                    else:
                        self.driver.find_element_by_xpath('//ListItem[{}]/Edit[1]'.format(i)).click()
                        self.driver.implicitly_wait(5)
                        self.calc2()
                        # self.driver.find_element_by_xpath('//Window/Button[1]').click()
                        # self.driver.find_element_by_name("打开(O)").click()
                        # time.sleep(1)
                        # self.driver.find_element_by_name("取消").click()

                else:
                    print("元素不存在。")
                    print('脚本执行第{}次失败!'.format(i))
                    self.driver.switch_to.window(self.driver.window_handles[-1])
                    # self.driver.find_element_by_name("确定").click()
                    self.driver.find_element_by_class_name('Button').click()
                    # win32api.SetCursorPos([800, 350])
                    # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                    # time.sleep(1)
                    # # self.driver.find_element_by_class_name('Button').send_keys(Keys.ALT+'t')
                    # # win32api.MessageBox(0, "检测程序已运行，已自动关闭提示框", "提醒", win32con.MB_ICONWARNING)
                    # print('关闭提示框')
                    # print(self.driver.window_handles[-1])
                    # hwnd = win32gui.GetForegroundWindow()
                    # print(hwnd)
                    # if hwnd != 0:
                    #     # 若最小化，则将其显示，反之则最小化
                    #     if win32gui.IsIconic(hwnd):
                    #         win32gui.ShowWindow(hwnd, win32con.SW_SHOWNOACTIVATE)
                    #     else:
                    #         win32gui.ShowWindow(hwnd, win32con.SW_SHOWMINIMIZED)
                    #     win32gui.SetForegroundWindow(hwnd)  # 设置前置窗口

                i += 1
        except Exception as f:
            print(f)
            if self.is_element_exist("取消"):
                self.driver.find_element_by_name("取消").click()


    def calc2(self):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(0.5)
        self.driver.find_element_by_class_name("UIImage").click()
        self.driver.implicitly_wait(5)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)

    def switch_roles(self):
        handle = win32gui.FindWindow("HwndWrapper[OFRS.exe;;39f4cc02-db61-4c83-ae86-32de1528afa4]", None)
        a = win32gui.ShowWindow(handle, win32con.SW_SHOWNORMAL)
        s =win32gui.SetForegroundWindow(handle)
        print(a)
        print(s)


if __name__ == '__main__':
    # 启动单元测试
    unittest.main()

