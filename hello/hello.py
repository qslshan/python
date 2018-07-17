#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# name=input('Please input your name:')
# print('hello,',name)
# a=100
# if a>=0:
#     print(a)
# else:
#     print(-a)
# print('''line1
# line2
# line3''')
# print(r'''hello,\n
# world''')
# a='ABC'
# b=a
# a='XYZ'

# print(b)
# print(10/3)
# print(10//3)
# print(9/3)
# print(9//3)
# print(10%3)
# print(9%3)
#print('\u4e2d\u6587')
# print('ABC'.encode('ascii'))
# print(b'ABC'.decode('ascii'))
# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
# print(L[0][0])
# print(L[1][1])
# print(L[2][2]) 
# age=20
# if age>=18:
#     print('youe age is',age)
# Height=1.75
# Weight=80.5
# BMI=Weight/(Height*Height)
# #BMI=('% .1f' % s)
# if BMI<18.5:
#     print('过轻')
# elif BMI<25:
#     print('正常')
# elif BMI<28:
#     print('过重')
# elif BMI<32:
#     print('肥胖')
# else:
#     print('过度肥胖')

# names=['qslshan','bon','qinshhan','jack']
# for name in names:
#     print(name)
# sum=0
# number=[1,2,3,4,5,6,7,8,9,10]
# for x in range(101):
#     sum=sum + x
# print('sum=',sum)

# sum=0
# n=99
# while n>0:
#     sum=sum+n
#     n=n-2
# print('sum=',sum)
# s1=set([1,2,3])
# s2=set([2,3,4])
# print(s1&s2)
# print(s1 |s2)
# a=['c','b','a']
# a.sort()
# print(a)
# a='abs'
# print(a.replace('a','A'))
# print(a)
# n1=255
# n2=1000
# print(hex(n1))
# print(hex(n2))
# def my_abs(x):
#     if x>=0:
#         return x
#     else:
#         return -x

# print(my_abs(-99))
# 'a test module'
# __auther__='qslshan'
# import sys
# def test():
#     args=sys.argv
#     if len(args)==1:
#         print('Hello World')
#     elif len(args)==2:
#         print('Hello,%s!'% args[1])
#     else:
#         print('too long')
# if __name__=='__main__':
#     test()

# import math

# def move(x,y,step,angle=0):
#     nx=x+step*math.cos(angle)
#     ny=y-step*math.sin(angle)
#     return nx,ny
# def add(x,n=2):
#     s=1
#     while n>0:
#         s=s*x
#         n=n-1
#     return s
#     m=add(3)
#     print(m)
# def enroll(name,gender):
#     print('name:',name) 
#     print('gender',gender)
def fac(n):
    if n==1:
        return 1
    return n*fac(n-1)
