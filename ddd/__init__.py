import pyautogui
import time

# 获取屏幕中心坐标
screen_width, screen_height = pyautogui.size()
center_x, center_y = screen_width // 2, screen_height // 2

while True:
    for _ in range(10000):
        pyautogui.click(center_x, center_y)
    time.sleep(1)
