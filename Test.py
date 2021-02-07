# def reversWards(input):
#     inputWards = input.split(" ")
#
#     inputWards=inputWards[-1::-1]
#
#     output = ' '.join(inputWards)
#     return output
#
# if __name__=="__main__":
#     input='I AM YOUR FATHER'
#     rw=reversWards(input)
#     print(rw)
# arr={x:x+5 for x in (5,10)}
# print(arr)
# a=int('ad',16)
# print(a)
# nunbers = [1, 2, 3, 4, 5, 6, 7, 8]
# even = []
# odd = []
# while len(nunbers) > 0:
#     num=nunbers.pop()
#     if(num % 2 == 0):
#         even.append(num)
#     else:
#         odd.append(num)
# print(even[-1::-1])
# print(odd)
# fruits = ['banana', 'apple',  'mango']
# for index in range(3):
#    print ('当前水果 :', fruits[index])

# row = int(input('输入'))
# i = j = k = 1
# #等腰直角三角形1
# for i in range(0,row):
#     for x in range(0,row - i):
#         print('*', end=" ")
#         k += 1
#     i += 1
#
#     print("\n")
#
import math
import sys
# # print('\a')
# # name = 'ht'
# # print(name.count('t'))
#斐波那契数列
# a,b = 0, 1
# while b < 10:
#     print (b)
#     a,b = b ,a+b
#求N个斐波那契数
# def fibonacci(n):
#     a, b, count = 0, 1, 0
#     while True:
#         if(count > n):
#             return
#         yield a
#         a, b = b, a + b
#         count += 1
# f = fibonacci(10)
#
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()
# def printinfo( arg1, *more ):#重点是*
#     print("输出：")
#     print(arg1)
#     print(more)
#
# printinfo('第一个', '第二个', '以及更多以元组显示')
# from collections import deque
# list = deque(['A', 'B', 'C'])
# list.popleft()
# print(list)
# list.append('D')
# print(list)
# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
# # tran = []
# # for i in range(4):
# #     tran.append([row[i] for row in matrix])
# # print(tran)
# wa=[[row[i] for row in matrix] for i in range(4)]
# list = [11, 22, 33, 4, 55, 66, 77]
# del list[2]
# print(list)
# x = True
# country_counter = {}
#
# def addone(country):
#     if country in country_counter:
#         country_counter[country] += 1
#     else:
#         country_counter[country] = 1
#
# addone('China')
# addone('Japan')
# addone('china')
# addone('china')
#
# print(country_counter['china'])
# from fibo import  fib, fib2
# fib(10)
import sys


# class people:
#     name =''
#     age = 0
#     #定义私有属性，类似于static
#     __weight = 0
#     def __init__(people,n,a,w):
#         people.name = n
#         people.age = a
#         people.__weight = w
#     def sayhello(people):
#         #print("{name}说: 我今年{age}岁，体重{weight}公斤".format(name=people.name,age=people.age,weight=people.__weight))
#         print("%s今年%d岁，体重%d公斤"%(people.name,people.age,people.__weight))
# # p =people('小明', 10 ,30)
# # p.sayhello()
#
#
# class student(people):
#     grage = ''
#     def __init__(student,n,a,w,g):
#         people.__init__(student,n,a,w)
#         student.grage = g
#     def sayhello(student):
#         print("%s今年%d岁,在读%d年纪" % (student.name, student.age, student.grage))
#
#
# s = student('小明',10,60,3)
#  s.sayhello()
# class Vector:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __str__(self):
#         return 'Vector (%d, %d)' % (self.a, self.b)
#
#     def __add__(self, other):
#         return Vector(self.a + other.a, self.b + other.b)
#
#
# v1 = Vector(2, 10)
# v2 = Vector(5,-2)
# print (v1 + v2)
# import os
# for i in dir(os):
#      print(i)
# import glob
# print(glob.glob('*.py'))
# from urllib.request import urlopen
# for line in urlopen('https://www.runoob.com/python3/python3-stdlib.html'):
#     line = line.decode('utf-8')  # Decoding the binary data to text.
#     print(line)
import mysql.connector
