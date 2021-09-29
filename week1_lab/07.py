'''
 ความยาวของประโยค 1 บวก ความยาวประโยค 2 จากนั้นคูณ ความยาวประโยค 3 ชั่วโมง
เว้นวรรคและสัญลักษณ์ต่างๆนับเป็นตัวอักษร 1 ตัว

Example1
First sentence: CPE
Second sentence: 35
Third sentence: Keep fighting!
70

-------------------------------

Example2
First sentence: Sinovac 3 dose
Second sentence: nong nong
Third sentence: Pfizer 
161


'''

#----------input--------------
fSen = input('First sentence: ')
sSen = input('Second sentence: ')
tSen = input('Third sentence: ')

#---------calculation---------
res = (len(fSen) + len(sSen)) * len(tSen)

#--------output----------------
print(res)