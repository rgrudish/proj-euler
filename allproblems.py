from datetime import datetime
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
'''
'''
#Problem 3
from datetime import datetime
def is_prime(n):
    for i in range(2, (int(n/2)+1)):
        if n % i == 0:
            return False
    return True
'''
'''
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

#Problem 6
def problem6(num):
    return sqsum(num) - sumsq(num)

def sqsum(num):
    x=0
    for i in range(1, num+1):
        x+=i
    return x**2

def sumsq(num):
    x=0
    for i in range(1, num+1):
        x+=i**2
    return x

print(problem6(100))
'''
'''
#Problem 7
def problem7(num):
    x = []
    i=2
    while True:
        if len(x)==num:
            break
        elif is_prime(i):
            x.append(i)
        i+=1
    return x[num-1]

start = datetime.now()
print(problem7(10001))
print(datetime.now() - start)
'''
#Problem 8
def problem8(num, spread):
    i = 1
    low_bound = 0
    high_bound = spread
    highest = 0
    while i <= len(str(num)) and len(str(num)[low_bound:high_bound]) == spread:
        mult = 1
        for item in list(map(int, str(num)[low_bound:high_bound])):
            mult *= item
        if mult > highest:
            highest = mult
        low_bound += 1
        high_bound += 1
        i += 1
    return highest

print(problem8(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450, 13))