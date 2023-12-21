import pyautogui

# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)

# problem = pyautogui.locateOnScreen("problem_menu.png")
# pyautogui.moveTo(problem)

# 이미지를 발견하지 못한 경우 Error 발생. 예외처리로 해결

# 같은 이미지가 여러개 있고 전부 클릭하고 싶은 경우 ex) checkbox
# for i in pyautogui.locateAllOnScreen("checkbox.png"):
#     print(i)
#     pyautogui.click(i, duration=0.25)

# locateOnScreen을 사용한 경우 처음 발견한 이미지에 대해서만 작동


# 속도 개선

# 1. GrayScale
# 전체 화면을 흑백으로 전환하여 이미지 비교
# 공식 문서상으로 30% 속도개선, 정확도는 조금 떨어질 수 있음
# powershell = pyautogui.locateOnScreen("power_shell.png", grayscale=True)
# pyautogui.moveTo(powershell)

# 2. 범위 지정
# powershell = pyautogui.locateOnScreen("power_shell.png", region=(800, 800, 200, 200))    # region=(x, y, width, height)
# pyautogui.moveTo(powershell)

# 3. 정확도 조정
# pip install opencv-python
# powershell = pyautogui.locateOnScreen("power_shell.png", confidence=0.9)    # 90%
# pyautogui.moveTo(powershell)


# 자동화 대상이 바로 보여지지 않는 경우
# 일정 시간 기다리기
import time
import sys

timeout = 10

def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target

def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[TimeOut {timeout}s] Target not found ({img_file}). Terminate Program.")
        sys.exit()


# pyautogui; PyScreeze 의 버전이 0.1.18 >> 0.1.19로 올라가면서
# 찾는 이미지를 발견하지 못하면 None을 반환하는 것이 아닌
# ImageNotFoundException 에러를 발생시키고 종료됨.
# 예외처리로 처리 필요.
        
# while True:
#     try:
#         img = pyautogui.locateOnScreen('images/Menu.PNG', confidence=0.8, grayscale = True)
#         print('Found it!')
#         break
#     except:
#         pass