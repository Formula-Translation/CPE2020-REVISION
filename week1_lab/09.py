'''
ความสูงของเสาไฟฟ้า	ราคาของเสาไฟฟ้าต่อต้น
ไม่เกิน 1 เมตร	ไม่เกิน 1000 บาท
มากกว่า 1 เมตร แต่ไม่เกิน 4 เมตร	ไม่เกิน 5000 บาท
มากกว่า 4 เมตร แต่ไม่เกิน 8 เมตร	ไม่เกิน 30000 บาท
มากกว่า 8 เมตร	ไม่เกิน 75000 บาท

บรรทัดที่ 1 : ผลว่าทุจริตหรือไม่ ( YES : มีการทุจริต, NO : ไม่มีการทุจริต )

Example1
Hight : 0.52
Cost : 112
NO

--------------------------

Example2
Hight : 3
Cost : 5600.05
YES

'''
#------------input-------------
hight = float(input('Hight : '))
cost = float(input('Cost : '))

#------------condition--------
if hight <= 1 and cost <= 1000:
    res = 'no'
elif hight > 1 and hight <= 4 and cost <= 5000:
    res = 'no'
elif hight > 4 and hight <= 8 and cost <= 30000:
    res = 'no'
elif hight > 8 and cost <= 75000:
    res = 'no'
else:
    res = 'yes'

#------------output-----------------
print(res.upper())