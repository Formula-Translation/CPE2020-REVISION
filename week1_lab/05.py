'''
[Mother Father] ถามหารเศษ
พ่อแม่ของนายเขียวขจี ต้องการแบ่งเงินให้ลูกๆทั้งหมดเท่ากัน
อยากรู้ว่า แต่ละคนได้เงินคนละเท่าไหร่ เศษเหลือเป็นเท่าไหร่

Example1
Money: 10
Son: 2
5 0

-------------------------

Example2
Money: 11
Son: 2
5 1


'''

#-------------input----------------
money = int(input('Money: '))
son = int(input('Son: '))

#------------calculation---------
# 1: แต่ละคนได้เงินคนละเท่าไหร่
monEach = money // son
# 2 :เศษเหลือเป็นเท่าไหร่
remainder = money % son

#-------------output----------
print(f'{monEach} {remainder}')