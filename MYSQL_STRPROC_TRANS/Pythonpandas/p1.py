from dataclasses import dataclass
from openpyxl import Workbook
wb=Workbook()
sheet=wb.active
@dataclass
class People():
    name:str
    num:int
    age:int=0
p=[People("mahi",1,20),People('Ajay',2,90),People('Swapna',3,45)]
data=[[p.name,p.num,p.age] for p in p]
data=[['Name','Num','Age']]+data
for d in data:
    sheet.append(d)
wb.save("C://Users/user773/Desktop/workbook1.xlsx")