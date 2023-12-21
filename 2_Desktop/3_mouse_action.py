import pyautogui

pyautogui.sleep(3)    # 3초 대기
# print(pyautogui.position())

# pyautogui.click(69, 14, duration=1)    # 1초 동안 (x, y) 좌표로 이동 후 마우스 클릭
# pyautogui.click()
# pyautogui.mouseDown()
# pyautogui.mouseUp()

# pyautogui.doubleClick()
# pyautogui.click(clicks=500)

# pyautogui.moveTo(100, 100)
# pyautogui.mouseDown()    # 마우스 버튼 누른 상태
# pyautogui.moveTo(300, 300)    # 마우스 버튼 누른 상태
# pyautogui.mouseUp()    # 마우스 버튼 뗀 상태

# pyautogui.rightClick()
# pyautogui.middleClick()

# pyautogui.moveTo(911, 235)
# pyautogui.drag(100, 0)    # 현재 위치 기준으로 (100, 0) 만큼 이동
# pyautogui.drag(100, 0, duration=0.25)    # 너무 빠른 동작으로 drag 수행이 안될 때는 duration 추가
# pyautogui.dragTo(1211, 235, duration=0.25)    # 절대 좌표 기준 드래그

pyautogui.scroll(-300)    # 양수이면 위 방향으로, 음수이면 아래 방향으로 300 만큼 스크롤