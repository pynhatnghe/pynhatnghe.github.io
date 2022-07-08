from xlsxwriter import Workbook

wb = Workbook("MyBeatiful.xlsx")
ws = wb.add_worksheet("MY_DATA")

bold = wb.add_format({'bold': True})
ws.write("A1", "CHÚC MỪNG", bold)
ws.write("A2", 100)
ws.write("A3", 200)
ws.write("A4", 260)
ws.write_formula("A6", "=sum(A2:A4)")

wb.close()