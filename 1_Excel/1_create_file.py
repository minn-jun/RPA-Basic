# pip install openpyxl
from openpyxl import Workbook

wb = Workbook()    # 새 워크북 생성
ws = wb.active    # 현재 활성화된 sheet를 가져옴
ws.title = "MySheet"    # sheet의 이름을 변경
wb.save("sample.xlsx")

wb.close()