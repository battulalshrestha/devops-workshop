# function 
# block of statements that perform a specific task
'''
 def function_name(para1,para2,...):
   return val 
func_name(arg1,arg2,....)# function call

'''
'''def calculate_sum(a,b):
    return a*b
   # return sum'''
'''sum =calculate_sum(2,4)
sum =calculate_sum(4,66)
sum =calculate_sum(2,44)
sum =calculate_sum(22,4)
sum =calculate_sum(26,4)
print(sum)

def cal_mul(a,b,c):
    mul = a*b*c
    print(mul)
cal_mul(2,3,4)
cal_mul(5,5,5)'''


'''def hello_nishan():
    print("helllo nishan")
output = hello_nishan()
print(output)'''

'''cities = ['n','b','c','d','e','f','y']
hero = ['wdsd','sdds','ddf','dfd','dfd']
def print_len(list):
    print(len(list))
print_len(cities)
print_len(hero)
def print_len(list):
    for item in list:
        print(item,end ='')'''

'''def converter(usd_val):
    inr_value = usd_val*131
    print(usd_val,"USD =",inr_value,"INR ")
converter(2)'''
# wap to convert  celcius to ferehite

'''def converter(f):
    c = ((f-32)/180)*100
    print(f,"ferenhite=",c ,"celcius")
converter(1)'''
    

'''def func(num):
    if num % 2 ==0:
       print("EVEN")
    else:
       print("ODD")
func(7)'''
'''username = input("enter the user name:")
password = input("enter the password:")
def has_permitted(user,psw):
    if user =="nishan" and psw =='12345':
        return True
    else:
        return False
verified = has_permitted(username,password)
if verified == True:
    print("access allowed")
else:
    print("access denied")'''


def print_me(str):
    print(str)
print_me("hello nishan")