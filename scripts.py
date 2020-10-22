problem_1: \
1.1 Introduction
#exsercise Hello, World!
print ("Hello, World!")

#exsercise Python if-else
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 1:
        print ("Weird")
    elif n % 2 ==0 and n in range(2,6):
        print ('Not Weird')
    elif n % 2 == 0 and n in range(6,21):
        print ('Weird')
    elif n % 2 == 0 and n>20:
        print('Not Weird')

#exsercise Arithmetic Operator
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

#exercise Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

#exercise loops
if __name__ == '__main__':
    n = int(input())
for i in range(0, n):
    print(i * i)

#exercise Write a function
def is_leap(year):
    leap = False

    # Write your logic here
    year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
    return leap
year = int(input())
print(is_leap(year))

#exercise Print function
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i,end="")

1.2 Data Types

#exercise List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
permutations = [[i,j,k] for i in range(x+1) for j in range (y+1) for k in range (z+1)if (i+j+k != n)]
print (permutations)

#exercise Find the Runner-Up Score
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    arr.remove(max(arr))
print(arr [-2])

#exercise Finding the Percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    sum_values = sum(student_marks[query_name])
    lenght = len(student_marks[query_name])
    average = sum_values/lenght
    print("{0:.2f}".format(average))

#exersice Lists
if __name__ == '__main__':
    N = int(input())
    results = []

    for _ in range(N):
        x = input().split(" ")
        command = x[0]
        if command == 'pop':
            results.pop()
        if command == 'print':
            print(results)
        if command == 'append':
            results.append(int(x[1]))
        if command == 'insert':
            results.insert(int(x[1]), int(x[2]))
        if command == 'remove':
            results.remove(int(x[1]))
        if command == 'reverse':
            results = results[::-1]
        if command == 'sort':
            results = sorted(results)

#exercise Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    print(hash(integer_list))

#exercise Nested List

1.3 Strings

#exercise14 Swap Case
def swap_case(s):
    return s.swapcase()
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print result

#exercise String Split and Join
def split_and_join(line):
    words = line.split(" ")
    words = "-".join(words)
    return words
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print result

#exercise What's Your Name?
def print_full_name(a, b):
    print("Hello %s %s! You just delved into python." % (a,b))
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

#exercise Mutations
def mutate_string(string, position, character):
    l= list(string)
    l[position] = character
    string = ''.join(l)
    return  string
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print s_new

#exercise Find a string

def count_substring(string, sub_string):
    counter = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            counter += 1
    return counter
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

#exercise String Validator
if __name__ == '__main__':
    s =input()
print (any(i.isalnum() for i in s))
print (any(i.isalpha() for i in s))
print (any(i.isdigit() for i in s))
print (any(i.islower() for i in s))
print (any(i.isupper() for i in s))

#exercise Text Alignment
thickness = int(input()) #This must be an odd number
c = 'H'
#Top Cone
for i in range(thickness):
    print (c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1)
#Top Pillars
for i in range(thickness+1):
    print (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)
#Middle Belt
for i in range((thickness+1)/2):
    print (c*thickness*5).center(thickness*6)
#Bottom Pillars
for i in range(thickness+1):
    print (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)
#Bottom Cone
for i in range(thickness):
    print ((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6)

#exercise Text Wrap
import textwrap

def wrap(string, max_width):
    l= (textwrap.fill(string,max_width))
    return l

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


#exercise Designer Door Mat
N, M = map(int, input().split())
for i in range(1,N,2):
    print ((i*'.|.').center(M, '-'))
print ('WELCOME'.center(M,'-'))
for i in range(N-2,-1,-2):
    print ((i*'.|.').center(M, '-'))

#exercise String Formatting
def print_formatted(number):
    l = len(bin(n)) - 2
    for i in range(1, n + 1):
        print("{0:{width}d} {0:{width}o} {0:{width}x} {0:{width}b}".format(i, width=l))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

#exercise Capitalize
 a= s.split(" ")
    b= [i.capitalize() for i in a]
    return " ".join

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

#exercise The Minion Game
def minion_game(string):
    vocali = ['A', 'I', 'O', 'E', 'U']
    c_t = dict()
    v_t = dict()
    kevin = 0
    stuart = 0
    count = 0
    for i in range(len(string)):
        if string[i] in vocali:
            kevin = kevin + len(string) - i
        else:
            stuart = stuart + len(string) - i

    if stuart > kevin:
        print("Stuart", stuart)
    elif stuart < kevin:
        print("Kevin", kevin)
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)

#exercise Merge The Tools!
def no_rep(t):
    string= set()
    a= []
    for i in t:
        if i not in string:
            string.add(i)
            a.append(i)
    return "".join(a)


def merge_the_tools(string, k):
     n= len(string)
     for j in [string[i:i+k] for i in range (0,n,k)]:
         print(no_rep(j))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)




4 Sets
def average(array):
    heights = set(array)
    n = len(heights)
    sum_heights = sum(heights)
    average = sum_heights / n
    return average

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

#exercise No Idea!
n_m = input().split()
n_m = map(int, n_m)
n = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int,input().split()))
happy = 0
for i in n:
    if i in A:
        happy += 1
    elif i in B:
        happy -= 1
print (happy)


#exercise Symmetric Difference
int(input())
N= input().split()
N_int = set(list(map(int, N)))
int(input())
M = input().split()
M_int = set(list(map(int, M)))
lis=[]
for x in list(N_int.difference(M_int)):
    lis.append(x)
for y in list(M_int.difference(N_int)):
    lis.append(y)
for z in sorted(lis):
    print (z)

#exercise Set .add()
N= int(input())
countries = set()
for i in range (N):
    stamps= input()
    countries.add(stamps)
print (len(countries))

#exercise 32 Discard,Remove and Pop
n = input()
s = set(map(int,input().split()))
a = int(input())

for _ in range(a):
    k = []
    k = input().split(" ")
    if k[0] == 'pop':
        s.pop()
    elif k[0] == 'remove':
        s.remove(int(k[1]))
    elif k[0] == 'discard':
        s.discard(int(k[1]))
print(sum(set(s)))

#exercise Set Union Operation
n_engl = input()
english = set(map(int,input().split()))
n_french = input()
french = set(map(int,input().split()))
un = english.union(french)
print (len(un))

#exercise Set Intersection Operation
n_engl = input()
english = set(map(int,input().split()))
n_french = input()
french = set(map(int,input().split()))
un = english.intersection(french)
print (len(un))

#exercise 35 Set Difference Operation
n_engl = input()
english = set(map(int,input().split()))
n_french = input()
french = set(map(int,input().split()))
un = english.difference(french)
print (len(un))

#exercise Symmetric Difference
n_engl = input()
english = set(map(int,input().split()))
n_french = input()
french = set(map(int,input().split()))
un = english.symmetric_difference(french)
print (len(un))

#exercise Set Mutations
n = int(input())
A = set(input().split())
for _ in range (int(input())):
    op = input().split()
    B= input().split()
    if op[0]== 'intersection_update':
        A.intersection_update(B)
    elif op[0]== 'difference_update':
        A.difference_update(B)
    elif op[0]== 'symmetric_difference_update':
        A.symmetric_difference_update(B)
    elif op[0] == 'update':
        A.update(B)
print(sum(map(int, A)))

#exercise The Captain's Room
from collections import Counter

n=int(input())
A= list(map(int,input().split()))
AA= Counter(A)

for i in A:
    if AA[i]==1:
        print(i
#exercise Check Subset
T = int(input())
for _ in range(T):
    n = int(input())
    A = set(list(map(int, input().split())))
    m = int(input())
    B = set(list(map(int, input().split())))
    print(True if len(A.difference(B)) == 0 else False)

# exercise Check String Superset
A = set(input().split())
N = int(input())
conta = 0
for _ in range(N):
    B = set(input().split())
if len(B.difference(A)) != 0:
    conta = 1
if conta == 0:
    print("True")

else:
    print("False")

1.5 Collection

#exercise Collections.Counter()-1
from collections import Counter
X = int(input())
collected_shoes = [int(val) for val in input().split()]
N = int(input())

shoes_stored = Counter(collected_shoes)
daily_budget = 0

for i in range(N):
    size, money = [int(val) for val in input().split()]

    if shoes_stored.get(size):
        daily_budget += money
        shoes_stored[size] -= 1

print(daily_budget)











