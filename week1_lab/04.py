'''
[Energy] การคำนวนพลังงาน
การคำนวนพลังงานในแต่ละวันนั้นนั้นในความเป็นจริงแล้วมีสูตรที่ตายตัวอยู่
นั่นก็คือ E = MC^2 ย่อมาจาก
Energy = Milk * Coffee^2

Example1
Milk: 2
Coffee: 3
18

--------------------

Example2
Milk: 3
Coffee: 7
147

'''

#-------------input-----------------------
milk = int(input('Milk: '))
coff = int(input('Coffee: '))

#--------------output--------------------
print(milk * coff**2)
