import pyautogui

# pyautogui.FAILSAFE = False    # 마우스를 화면 4개의 꼭짓점 중 한 곳으로 이동시켜도 종료X
pyautogui.PAUSE = 1    # 모든 동작에 1초씩 sleep 적용
# pyautogui.mouseInfo()

for i in range(10):
    pyautogui.move(100, 100)
    # 중간에 종료하려면 마우스를 화면 4개의 꼭짓점 중 한 곳으로 이동