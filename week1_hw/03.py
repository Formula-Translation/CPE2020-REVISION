'''
    ตัวตั้ง = ตัวหาร * ผลหาร + เศษ

Example1

Input Dividend: 73
Input Divider: 9
73 = 9 * 8 + 1

'''

#-----------input---------------
dvd = int(input('Input Dividend: '))
dvr = int(input('Input Divider: '))

#----------output----------------
print(f'{dvd} = {dvr} * {dvd//dvr} + {dvd%dvr}')