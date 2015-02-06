'''
#Problem 1
def problem1(max, multiple1, multiple2):
    output = 0
    for i in range(1, max):
        if i % multiple1 == 0 or i % multiple2 == 0:
            output += i
    return output
    
print problem1(1000, 3, 5)

#Problem 2
def problem2(max):
    sum = 0
    num = [1, 2]
    i = 2
    while True:
        if (num[i-1] + num[i-2]) > max:
            break
        num.append(num[i-1] + num[i-2])
        if num[i] % 2 == 0:
            sum+=num[i]
        i+=1
    return sum+2
            
print problem2(4000000)

#Problem 3
from datetime import datetime
def is_prime(n):
    for i in range(2, (int(n/2)+1)):
        if n % i == 0:
            return False
    return True
    
def get_factors(num):
    for i in range(2, (int(num/2)+1)):
        if num % i == 0 and is_prime(i):
            return [i, num/i]
    return []

def problem3(number):
    output = []
    result = []
    last_result = []
    while True:
        last_result = result
        result = get_factors(number)
        if result:
            output.append(result[0])
            number = result[1]
        else:
            if last_result:
                output.append(last_result[1])
            else:
                output = [1, number]
            break
    return output[len(output)-1]
    
start = datetime.now()
print problem3(144)
print datetime.now() - start

#Problem 4
from datetime import datetime
def pal_check(input):
    char_list = list(map(str,str(input)))
    n = len(char_list) - 1
    for i in range(0, len(char_list)):
        if i == n:
            break
        if not char_list[i] == char_list[n]:
            return False
        n-=1
    return True

def problem4(num):
    result = 0
    i = num
    while i > (int(num/2)+1):
        n = num
        while n > 0:
            mult = i * n
            if mult > result and pal_check(mult):
                result = mult
            n-=1
        i-=1
    return result
start = datetime.now()
print(problem4(999))
print(datetime.now() - start)
'''
#Problem 5
from datetime import datetime
def problem5(max):
    n=0
    while True:
        n+=1
        i=1
        while i <= max:
            if not n%i == 0:
                break
            elif i == max:
                return n
            else:
                i+=1
start = datetime.now()
print(problem5(20))
print(datetime.now() - start)
#answer: 232792560
#time: 0:04:22.870609