'''
เสี่ยใหญ่จะขับรถเร็วกว่าเสี่ยเล็กเสมอ (B>A)

Example1
A : 40
B : 60
X : 120
Wait : 3600 sec

--------------------

Example2
A : 15
B : 160
X : 480
Wait : 104400 sec
'''

#-----------input---------------
a = int(input('A : '))
b = int(input('B : '))
x = int(input('X : '))

#----------calculation-------
# a and b are velocity and x is distance
#v = s/t
timeA = x/a
timeB = x/b
res = (timeA - timeB)* 3600

#------------output----------
print(f'Wait : {int(res)} sec')

