from openpyxl.utils import FORMULAE
print(FORMULAE)
wb=openpyxl.load_workbook("C://Users/user773/Desktop/Student.csv")
sheet=wb.active
sheet["A7"]='=SUM(A1:A6)'
wb.save("C://user773/desktop/sumdata.xlsx")