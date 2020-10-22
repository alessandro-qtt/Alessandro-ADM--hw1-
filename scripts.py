problem_1: \
1.1 Introduction
#exsercise_1
print "Hello, World!"

#exsercise_2
#!/bin/python
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(raw_input().strip())
if n % 2 == 1:
    print ("Weird")
elif n % 2 ==0 and n in range(2,6):
    print ('Not Weird')
elif n % 2 == 0 and n in range(6,21):
    print ('Weird')
elif n % 2 == 0 and n>20:
    print('Not Weird')

#exsercise_3
if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print(a+b)
    print(a-b)
    print(a*b)

#exercise_4
from __future__ import division
a = int(raw_input())
b = int(raw_input())
print (a//b)
print(a/b)

#exercise_5
if __name__ == '__main__':
    n = int(raw_input())
for i in range(0, n):
    print(i * i)

#exercise_6
def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
year = int(raw_input())

#exercise7
from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())
    for i in range(1,n+1):
        print(i,end="")

1.2 Data Types

#exercise8
if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())

permutations = [[i,j,k] for i in range(x+1) for j in range (y+1) for k in range (z+1)if (i+j+k != n)]
print (permutations)

#exercise9
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr.sort()
    arr.remove(max(arr))
print(arr [-2])

#exercise10
if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    sum_values = sum(student_marks[query_name])
    lenght = len(student_marks[query_name])
    average = sum_values/lenght
    print("{0:.2f}".format(average))

#exersice11 DA FARE

#exercise12 NON CAPITO
if __name__ == '__main__':
    N = int(raw_input())

arr = []
for i in range(N):
    s = raw_input().split()

    for i in range(1, len(s)):
        s[i] = int(s[i])

    if s[0] == "append":
        arr.append(s[1])
    elif s[0] == "extend":
        arr.extend(s[1:])
    elif s[0] == "insert":
        arr.insert(s[1], s[2])
    elif s[0] == "remove":
        arr.remove(s[1])
    elif s[0] == "pop":
        arr.pop()
    elif s[0] == "index":
        print
        arr.index(s[1])
    elif s[0] == "count":
        print
        arr.count(s[1])
    elif s[0] == "sort":
        arr.sort()
    elif s[0] == "reverse":
        arr.reverse()
    elif s[0] == "print":
        print
        arr

#exercise13
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    for i in range(n):
        integer_list[i] = int(integer_list[i])
t = tuple(integer_list)
print hash(t)

1.3 Strings

#exercise14 Swap Case
def swap_case(s):
    return s.swapcase()
if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result

#exercise15 String Split and Join
def split_and_join(line):
    words = line.split(" ")
    words = "-".join(words)
    return words
if __name__ == '__main__':
    line = raw_input()
    result = split_and_join(line)
    print result

#exercise16 What's Your Name?
def print_full_name(a, b):
    print("Hello %s %s! You just delved into python." % (a,b))
if __name__ == '__main__':
    first_name = raw_input()
    last_name = raw_input()
    print_full_name(first_name, last_name)

#exercise17 Mutations
def mutate_string(string, position, character):
    l= list(string)
    l[position] = character
    string = ''.join(l)
    return  string
if __name__ == '__main__':
    s = raw_input()
    i, c = raw_input().split()
    s_new = mutate_string(s, int(i), c)
    print s_new

#exercise18 Find a string
def count_substring(string, sub_string):
    counter=0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i+len(sub_string)] == sub_string:
            counter+=1
    return counter
#exercise19 String Validator
if __name__ == '__main__':
    s = raw_input()
print (any(i.isalnum() for i in s))
print (any(i.isalpha() for i in s))
print (any(i.isdigit() for i in s))
print (any(i.islower() for i in s))
print (any(i.isupper() for i in s))

#exercise20 Text Alignment
#Replace all ______ with rjust, ljust or center.
thickness = int(raw_input()) #This must be an odd number
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

#exercise21 Text Wrap
import textwrap
def wrap(string, max_width):
    l= (textwrap.fill(string,max_width))
    return l
if __name__ == '__main__':
    string, max_width = raw_input(), int(raw_input())
    result = wrap(string, max_width)
    print result
#exercise22
N, M = map(int,raw_input().split())
for i in range(0,N/2):
    print ('.|.'*i).rjust((M-2)/2,'-')+'.|.'+('.|.'*i).ljust((M-2)/2,'-')
print 'WELCOME'.center(M,'-')
for i in reversed(range(0,N/2)):
    print ('.|.'*i).rjust((M-2)/2,'-')+'.|.'+('.|.'*i).ljust((M-2)/2,'-')
#exercise22

#exercise23 String Formatting
def print_formatted(number):
    l = len(bin(n)) - 2
    for i in range(1, n + 1):
        print("{0:{width}d} {0:{width}o} {0:{width}x} {0:{width}b}".format(i, width=l))
if __name__ == '__main__':
    n = int(raw_input())
    print_formatted(n)
#exercise24
#exercise25
#exercise26
#exercise27

4 Sets
#exercise28 Introduction to Set
from __future__ import division
def average(array):
    heights = set(array)
    n = len(heights)
    sum_heights = sum(heights)
    average = sum_heights / n
    return average
if __name__ == '__main__':

#exercise 29 No Idea!
n_m = raw_input().split()
n_m = map(int, n_m)
n = map(int, raw_input().split())
A = set(map(int, raw_input().split()))
B = set(map(int, raw_input().split()))

happy = 0
for i in n:

    if i in A:
        happy += 1
    elif i in B:
        happy -= 1

print
happy

#exercise30 Symmetric Difference RIFAI
int(raw_input())
N= raw_input().split()
N_int = set(list(map(int, N)))
int(raw_input())
M = raw_input().split()
M_int = set(list(map(int, M)))
lis=[]
for x in list(N_int.difference(M_int)):
    lis.append(x)
for y in list(M_int.difference(N_int)):
    lis.append(y)
for z in sorted(lis):
    print z

#exercise31 set .add()

N= int(input())
countries = set()

for i in range (N):
    stamps= raw_input()
    countries.add(stamps)
print (len(countries))

#exercise 32 Discard, removeand pop

#exercise 33 Set Union Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n_engl = input()
english = set(map(int,input().split()))
n_french = input()
french = set(map(int,input().split()))
un = english.union(french)
print (len(un))

#exercise 34 Intersection
# Enter your code here. Read input from STDIN. Print output to STDOUT
n_engl = input()
english = set(map(int,input().split()))
n_french = input()
french = set(map(int,input().split()))
un = english.intersection(french)
print (len(un))

#exercise 35 Difference
n_engl = input()
english = set(map(int,input().split()))
n_french = input()
french = set(map(int,input().split()))
un = english.difference(french)
print (len(un))

#exercise 36 Symmetric Difference

n_engl = input()
english = set(map(int,input().split()))
n_french = input()
french = set(map(int,input().split()))
un = english.symmetric_difference(french)
print (len(un))

#exercise 37 Set Mutations

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

#exercise 38 collections.Counter()
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

from collections import namedtuple

n_elements = int(input())
fields = input().split()
sum_marks = 0

for _ in range(n_elements):
    columns = namedtuple('columns', fields)
    Id, marks, name, classe = input().split()
    x = columns(Id, marks, name, classe)
    y = int(x.MARKS)
    sum_marks += int(y)

print(float(sum_marks / n_elements))

from collections import defaultdict
dictonary  = defaultdict(list)
lista=[]


n, m = map(int,input().split()) # acquire n and m in input

for i in range(0,n):
    dictonary [input()].append(i+1)


for i in range(0,m): #fill the list with a for cicle
    lista=lista+[input()]


for i in lista: # for the len of lista
    if i in dictonary : #if you find i in d print togheter
        print (" ".join(map(str,dictonary [i]) )) #print with space the dictonary as list
    else:
        print -1

#exercise 40 collection.namedtuple()

from collections import namedtuple
n_elements = int(input())
fields = input().split()
sum_marks = 0
for _ in range(n_elements):
    columns = namedtuple('columns', fields)
    Id, marks, name, classe = input().split()
    x = columns(Id, marks, name, classe)
    y = int(x.MARKS)
    sum_marks += int(y)
print(float(sum_marks / n_elements))

#exercise 41 collection.ordered_dict
from collections import OrderedDict
n= int(input())
d= OrderedDict()
for i in range(n):
    products,space,quantity = input().rpartition(' ')
    d[products] = d.get(products,0)+ int(quantity)

for products, quantity in d.items():
    print(products, quantity)

#exercise 42 Word order
import collections
N = int(input())
dictionary = collections.OrderedDict()
for i in range(N):
    words = input()
    if words in dictionary:
        dictionary[words] += 1
    else:
        dictionary[words] = 1
print(len(dictionary))
for key, value in dictionary.items():
    print(value, end=' ')

#exercise 43

import math
import os
import random
import re
import sys
from collections import Counter
if __name__ == '__main__':
    s = input()
    words_count = (word for word in s)
    c = Counter(words_count).most_common(3)
    for i in range(0, len(c)):
        print(' '.join(map(str, c[i])))
























