import pyautogui

w = pyautogui.getWindowsWithTitle("제목 없음")[0]    # 메모장 1개 띄운 상태에서 가져옴
w.activate()

# pyautogui.write("12345")
# pyautogui.write("Python Coding", interval=0.25)
# pyautogui.write("코딩")    # write -> 한글 작성 불가

# pyautogui.write(["T", "E", "S", "T", "left", "left", "right", "L", "A", "enter"], interval=0.25)
# https://automatetheboringstuff.com/2e/chapter20/  ctrl+F >> keyboard Attributes


# 특수 문자
# shift 4 -> $
# pyautogui.keyDown("shift")    # shift 키를 누른 상태에서
# pyautogui.press("4")    # 숫자 4를 입력하고
# pyautogui.keyUp("shift")    # shift 키를 뗀다


# 조합키 (Hot Key)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")    # press("a")
# pyautogui.keyUp("ctrl")    # ctrl + A


# 간편한 조합키
pyautogui.hotkey("ctrl", "a")
# ctrl 누르고 > A 누르고 > A 떼고 > ctrl 떼고


# 한글 작성
# pip install pyperclip
import pyperclip
pyperclip.copy("프로그래밍")    # "프로그래밍" 글자를 클립보드에 저장
pyautogui.hotkey("ctrl", "v")    # 클립보드에 있는 내용을 붙여넣기

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

my_write("안녕하세요")


# 자동화 프로그램 종료
# win : ctrl + alt + del
# mac : cmd + shift + option + Q