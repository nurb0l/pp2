#task 1
def generate_squares(n):
    for i in range(n+1):
        yield i**2

n=int(input())

squares_generator = generate_squares(n)

for squares in squares_generator:
    print(squares)

#task 2
def generate_even(n):
    for i in range(n+1):
        if(i%2==0):
            yield i

n=int(input())

even_generator = generate_even(n)

for even in even_generator:
    print(even, end=', ')

#task 3
def divisible_3_and_4(n):
    for i in range(n+1):
        if(i%3==0 and i%4==0):
            yield i 

n=int(input())

divisibility_generator=divisible_3_and_4(n)

for number in divisibility_generator:
    print(number, end=' ')

#task 4
def squares(a,b):
    for i in range(a,b+1):
        yield i**2

a=int(input())

b=int(input())

squares_generator=squares(a,b)

for number in squares_generator(a,b):
    print(number, end=' ')

#task 5
def all_numbers(n):
    for i in range(n,0,-1):
        yield i-1
        
n=int(input())

generate_numbers=all_numbers

for numbers in all_numbers(n):
    print(numbers,end=' ')