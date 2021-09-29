#-----------------direction------------------
"""
เขียนโปรแกรมคำนวนหาพื้นที่และเส้นรอบรูปให้กับพี่ๆหน่อยได้มั้ย

Example 1
width : 10
length : 20
area : 200.0
perimeter : 60.0

-----------------------

Example 2
width : 12.3
length : 21.4
area : 263.21999999999997
perimeter : 67.4
"""

#------------------input--------------------
#since example 2 have decimal we must consider this as float
width = float(input('width : '))
length = float(input('length : '))

#-----------------calculation----------------
area = width*length
perimeter = 2*(width + length)

#------------------output--------------------
print(f'area : {area}')
print(f'perimeter : {perimeter}')