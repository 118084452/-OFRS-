#coding = utf-8
import win32gui,win32api,win32con,time

win32api.SetCursorPos([1113, 252])
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
for i in range(9):
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,-90)
    time.sleep(0.01)
