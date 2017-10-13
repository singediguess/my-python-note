str1 = 'I am {}, I love {}'
str2 = str1.format('k1vin', 'coding')
print (str2)
print('---')

#using index
str3 = '{0:10} : {1:3d}'
table = {'c++':16, 'html':15, 'python':17}
for name, nmb in table.items():
   print (str3.format(name, nmb))
print('---')

#using '%'
import math
print ('pi = %6.4f' % math.pi)
print('---')

#dictionary problems
print (table.items())
print (table['c++'])
print (table['html'])
print('---')

#input
name= input('Give me your name: ')
print ('Welcome,', name, '!!')
