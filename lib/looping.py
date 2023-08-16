#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i= 10
    while i >= 1:
        print (i)
        i-= 1
    print("Happy New Year!")  

def square_integers(int_list):
    new_list=[]
    for n in int_list:
        new_list.append(n * n)
    return new_list


def fizzbuzz():
    for n in range(1,101):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)
            