'''
Quiz) 아래 동작을 자동으로 수행하는 프로그램을 작성하시오

1. 그림판 실행 (단축키 : win + r, 입력값 : mspaint) 및 최대화

2. 상단의 텍스트 기능을 이용하여 흰 영역 아무 곳에다가 글자 입력
    - 입력 글자 : "참 잘했어요"

3. 5초 대기 후 그림판 종료
    - 저장하지 않음을 자동으로 선택하여 프로그램이 완전 종료되도록 함

'''

import sys
import pyautogui
import pyperclip

# 그림판 실행 및 최대화
pyautogui.hotkey("win", "r")
pyautogui.write("mspaint")
pyautogui.press("enter")

pyautogui.sleep(1)

window = pyautogui.getWindowsWithTitle("제목 없음 - 그림판")[0]
if window.isMaximized == False:
    window.maximize()

###################################
    
# 텍스트 기능을 이용하여 글자 입력

btn_txt = pyautogui.locateOnScreen("btn_txt.png")
pyautogui.click(btn_txt)
pyautogui.click(btn_txt.left + 200, btn_txt.top + 200)

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

my_write("참 잘했어요")

###################################

# 5초 대기 후 그림판 종료

pyautogui.sleep(5)

window.close()
pyautogui.sleep(0.5)
pyautogui.press("n")    # 저장하지 않음
