'''tup = (1,3,4,5,6,7,9)
for num in tup:
    print(num)'''
'''n = 'nishanshrestha'
for i in n:
    if(i == "f"):
        print("f is found")
    break
    print(i)
else:
 print('not found')
'''

'''num = "nepalcollegeofenginnering"
for var in num:
    if (var =='z'):
        print('found')
        break
    print(var)
else:
       print("not found")'''

'''num = [1,4,9,16,25,36,49,64,81,100]
for n in num:
    print(n)'''
'''num =  [1,4,9,16,25,36,49,64,81,100]
for n in num:
    if (n == 36):
       print("n is found")
       break
    print(n)
else:
    print("not found")'''
# range 
# range function return sequence of number ,starting from 0 by default ,and increments by 1 stop before specifed number.
'''seq = range(5)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])
print(seq[4])'''
'''for i in range(2,10,2):# range(start,stop,step)
    print(i)
for i in range(4,20,2):
    print(i)'''

'''n = int(input("enter the number:"))
if (n % 2 == 0):
    print("the n is odd number:")
else:
    print("the n is even number:")]'''
'''n = eval(input("enter the any number multiplication :"))
for i in  range(1,100):
  print(n*i)'''
# pass statement 
# pass statement that does nothing .it is used  as placeholder  for future code
'''for  i in range(5):

  pass
print("some work is done")'''

n = 5
sum = 0
for i in range(1,n+1):
    sum +=i
print("the total number of sum is",sum)