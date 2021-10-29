import win32con
import win32gui
import time

'''
hwnd = win32gui.FindWindow(lpClassName=None, lpWindowName=None)  # 查找窗口，不找子窗口，返回值为0表示未找到窗口
hwnd = win32gui.FindWindowEx(hwndParent=0, hwndChildAfter=0, lpszClass=None, lpszWindow=None)  # 查找子窗口，返回值为0表示未找到子窗口

win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
SW_HIDE：隐藏窗口并激活其他窗口。nCmdShow=0。
SW_SHOWNORMAL：激活并显示一个窗口。如果窗口被最小化或最大化，系统将其恢复到原来的尺寸和大小。应用程序在第一次显示窗口的时候应该指定此标志。nCmdShow=1。
SW_SHOWMINIMIZED：激活窗口并将其最小化。nCmdShow=2。
SW_SHOWMAXIMIZED：激活窗口并将其最大化。nCmdShow=3。
SW_SHOWNOACTIVATE：以窗口最近一次的大小和状态显示窗口。激活窗口仍然维持激活状态。nCmdShow=4。
SW_SHOW：在窗口原来的位置以原来的尺寸激活和显示窗口。nCmdShow=5。
SW_MINIMIZE：最小化指定的窗口并且激活在Z序中的下一个顶层窗口。nCmdShow=6。
SW_SHOWMINNOACTIVE：窗口最小化，激活窗口仍然维持激活状态。nCmdShow=7。
SW_SHOWNA：以窗口原来的状态显示窗口。激活窗口仍然维持激活状态。nCmdShow=8。
SW_RESTORE：激活并显示窗口。如果窗口最小化或最大化，则系统将窗口恢复到原来的尺寸和位置。在恢复最小化窗口时，应用程序应该指定这个标志。nCmdShow=9。
'''

# # 先等待3秒
# time.sleep(3)
#
# # 查找窗口句柄
# hwnd = win32gui.GetForegroundWindow()
# # hwnd = win32gui.FindWindow("HwndWrapper[OFRS.exe;;9e891d11-0cbc-4908-92fe-156610210b6a]", "")
# print(hwnd)
#
# if hwnd != 0:
#     # 若最小化，则将其显示，反之则最小化
#     if win32gui.IsIconic(hwnd):
#         win32gui.ShowWindow(hwnd, win32con.SW_SHOWMAXIMIZED)
#     else:
#         win32gui.ShowWindow(hwnd, win32con.SW_SHOWMINIMIZED)
#
#     win32gui.SetForegroundWindow(hwnd)  # 设置前置窗口
#     # win32gui.SetFocus(hwnd)  # 设置聚焦窗口

    # 关闭窗口
    # win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)


import os,random
DIR = r'D:\RWD-OFRS\Experiment'
print("文件夹内文件的个数:", len(os.listdir(DIR)))
a = random.randint(1,100)
print(a)
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)