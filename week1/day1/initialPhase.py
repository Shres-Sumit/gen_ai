#question 1
# width = int(input("enter the width"))
# height = int(input("enter the height"))
# print(type(width))
# print(type(height))

# area = width*height
# radius = int(input("enter the radius for the circle"))
# area_of_circle = 22/7 * radius ** 2

# print(f"the area of reactangle is {area}   the area of circle {area_of_circle} ")

# text = "programming"
# print(text[0:3])
# print(text[-4:])
# print(text[2:8])
# print(text[::2])

# numbers = [10, 20, 30, 40, 50]
# numbers.append(60)
# numbers[2] = 35
# number1_3 = numbers[0:3]
# print(numbers)
# print(number1_3)
# print(len(numbers))

# first_name = "John"
# last_name = "Doe"

# print(first_name +" "+  last_name)

# string1 = 5*"Ha"+"!"
# print(string1)
# print(r"C:\new_folder\test.txt")

# a,b = 0,1
# n=0
# while n < 10:
#     print(a, end=", ")
#     a,b = b , a+b
#     n+=1
# print("\n")

# c,d = 0,1
# while c <500:
#     if d >= 500:
#         print(c)
#     else:
#         print(c ,end=", ")
#     c,d = d , c+d

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# letters[2:5]=["X","y","z"]
# letters[0:3]=[]

# print(letters)
# Copy_letter = letters[:]
# Copy_letter.append("t")
# print(Copy_letter)

# # 1. Define the 2D list (the board)
# board = [
#     ['X', 'O', 'X'],
#     ['O', 'X', 'O'],
#     ['O', 'X', 'X']
# ]

# # 2. Iterate through the board to print it
# for i in range(len(board)):
#     # Join the characters in the current row with a pipe separator
#     print(" | ".join(board[i]) + " ")
    
#calculator program

_ = 0
print("calculator \n")
print("Operations: +, -, *, /, //, %, **")


while True:
    try:
        num1 = input("enter first number")
        if num1 == "quit":
            break
        if num1 == '_':
            num1 = _
        else :
            num1 = int(num1)

        operation = input("Operation (+, -, *, /, //, %, **): ")
        num2 = input("enter second number")
        num2 = int(num2)
        if operation == '+' :
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == "*" :
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2
        elif operation == '//':
            result = num1 // num2
        elif operation == '%':
            result = num1 % num2
        elif operation == '**':
            result = num1 ** num2
        else:
            print("invalid operation")
        
        print(f"Result : {result}")
        _=result
    except ValueError:
        print("invalid number")
    except ZeroDivisionError:
        print("cannot be divied by zero")

    
user_input = int(input("enter a number"))
if user_input > 0:
    print("Positive")
elif user_input < 0:
    print("Negative")
else :
    print("equal")

words = ["hello", "world", "python"]
for w in words:
    print(w,len(w))

for i in range(9):
    print(i)

for i in range(5,15):
    print(i)

for i in range(0,20,3):
    print(i)

for i in range(-10,-50,-10):
    print(i)


for n in range(1,20):
    if n % 2 == 0:
        continue
    else:
        if n <= 15:
            print(n)

for n in range (10,20):
    for x in range(2,n):
        if n % x == 0:
            print(n,'equals',x,"*",n//x)
            break
    else:
        print(n,"is a prime number")



def describe_point(point):
    match point:
        case (0,0) :
            return "origin"
        case (0,y):
            return f"On y axis at y = {y}"
        case (x,0):
            return f"On X asix at x = {x}"
        case (x,y): 
            return f"point at ({x},{y})"
        case _:
            return "not valid point"
        
print(describe_point((10,10)))

def greet(name,greeting="hello",punctuation="!"):
    return f"{greeting}, {name}{punctuation}"

user_name = input("enter the name")
print(greet(user_name))
print(greet(user_name,'hi'))
print(greet(user_name,'welcome',".."))
print(greet(punctuation="@",name="sum",greeting="namaste"))

def make_sentence(*words, **details):
    sentence = " ".join(words)
    punctuation = details.get("end_puncutation","!")
    should_capitalize = details.get("capitalize", True)

    if should_capitalize:
        sentence = sentence.capitalize()

    return f"{sentence}{punctuation}"

result = make_sentence("hello", "world", end_punctuation="!", capitalize=True)
print(result)

def is_prime(n):
    if n <2 :
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i== 0:
            return True
    return True

def find_primes(start,end,mode="all",output_format="list"):
    primes = []
    for num in range(start,end+1):
        if is_prime(num):
            primes.append(num)
            if mode == "first":
                break
    else:
        if not primes:
            return "no primes found in this range"
        
    match output_format:
        case "list":
            return primes
        case "string":
            return ", ".join(map(str,primes))
        case "count":
            return len(primes)
        case _:
            return "invalid format specified"
        
print(f"List: {find_primes(10, 50, mode='all', output_format='list')}")
print(f"First only: {find_primes(10, 50, mode='first', output_format='list')}")
print(f"String format: {find_primes(10, 20, output_format='string')}")
print(f"Count only: {find_primes(1, 100, output_format='count')}")

def add(x, y):
    result = x + y
    return(result)

def multiply(a, b):
    return a * b

my_list=[1, 2, 3, 4]

for item in my_list:
    print(item)
