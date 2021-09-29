'''
--โปรแกรมแบ่งอายุคน-- โดยเกณฑ์การแบ่งอายุตามนี้

Child (0-12 years)
Adolescence (13-18 years)
Adult (19-59 years)
Senior Adult (60 years and above)

Example1
Enter your age : 11
You are Child.

'''
#-----------input---------------
age = int(input('Enter your age : '))

#----------condition----------------
if age < 12 and 0 < age:
    res = 'Child'
elif age < 18 and 13 < age:
    res = 'Adolescence'
elif age < 19 and 59 < age:
    res = 'Adult'
else:
    res = 'Senior Adult'

#-----------output------------------
print(f'You are {res}.')