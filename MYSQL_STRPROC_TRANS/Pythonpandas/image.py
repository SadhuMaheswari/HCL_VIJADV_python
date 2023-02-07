from openpyxl import load_workbook
from openpyxl.drawing.image import Image

workbook=load_workbook(filename="C://Users/user773/Documents/openpyxlstyle.xlsx")
sheet=workbook.active
logo=Image('C://Users/user773/image1.png')
logo.height=150
logo.width=150
sheet.add_image(logo, "D10")
workbook.save(filename="C://Users/user773/Documents/image1.xlsx")