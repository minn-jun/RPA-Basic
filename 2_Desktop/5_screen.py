import pyautogui

# 스크린샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png")    # 파일로 저장

# pyautogui.mouseInfo()
# 31,18 69,173,243 #45ADF3

pixel = pyautogui.pixel(31, 18)    # 해당 위치 픽셀의 RGB값 반환
print(pixel)

# 해당 위치 픽셀의 RGB값과 지정한 RGB값이 맞는지 확인
print(pyautogui.pixelMatchesColor(28, 18, pixel))    # True
print(pyautogui.pixelMatchesColor(28, 18, (69, 173, 25)))    # False