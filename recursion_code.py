
# This File contain some good example of hoow a recursion and a functin work

def cal_sum(n):
    if n ==0:
        return 0
    print('n = ',n)
    print('n - 1 = ', n)
    return cal_sum(n-1) + n


num = int(input("Enter any number: "))
print(cal_sum(num))



def shw_list(list ,  index = 0):
    if(index == len(list)):
        return 
    print(list[index])
    shw_list(list , index+1)
    print("this print run in reverse order mean first it show list ne by ne and phr jo stack bn geya ho ga us reverve order m chly ga or tb ye wela print chly ga")



list = ['Ali' , 'Mahad' , 'Furqan' , 'Apple']
shw_list(list)


def power_functin(a , b):
    if b == 0:
        return 1
    return  a * power_functin(a , b-1) 
    

num = int(input("Enter any Number: "))
expo = int(input("Enter the exponent: "))

power = power_functin(num , expo)
print('answer is = ' , power)



def GCD(a , b):
    if b == 0:
        return a
    return GCD(b , a % b)

num1 = int(input("Enter any number 1: "))
num2 = int(input("Enter the number 2: "))

if num1 > num2:
    answer = GCD(num1 , num2)
    print("answer is = " , answer)
else:
    print('Number 1 cannot be smaller than number 2')



def area_of_circle(radius):
    if radius > 0:
        return 3.14 * radius ** 2
    else:
        return 0


rad = int(input("Enter Radius of Circle: "))
area = int(area_of_circle(rad))

if area == 0:
    print('Radius must be greater than 0')
else:
    print("Area of Circle is: " , area)





def is_prime(num):
    if num <= 1:
        return False
    for i in range(2 , int(num**0.5)+ 1): # here we take square roo of the number then check if it can be divided by any number less then it.
            if num % i == 0:
                return False
    return True


def sum_of_prime(num):
    prime_sum = 0
    for i in range(2, num):
        if is_prime(i):
            prime_sum += i
    return prime_sum      
        


num = int(input("Enter any Number: "))

if is_prime(num):
    print(f'{num} is a prime number')
    prime_sum = sum_of_prime(num)
    print('sum of all previous prime numbers: ' , prime_sum)
else:
    print(f'{num} is not a prime number')






