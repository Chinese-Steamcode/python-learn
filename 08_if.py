#Filename if.py

age=20
if age>=18:
   print('your age is',age)
   print('adult')

age=3
if age>=18:
   print('your age is',age)
   print('adult')
else:
   print('your age is',age)
   print('teenager')


age=3
if age>=18:
   print('your age is',age)
   print('adult')
elif age>=6:
   print('teenager')
else:
   print('kid')

birth=input('birth_year:')
if int(birth)<2000:
   print('00前')
else:
   print('00后')


height=1.75
weight=80.5
bmi=weight/(height**2)
print(bmi)

if bmi<18.5:
   print('过轻')
elif bmi>18.5 and bmi<25:
   print('正常')
elif bmi>25 and bmi<28:
   print('过重')
elif bmi>28 and bmi<32:
   print('肥胖')
else:
   print('严重肥胖')