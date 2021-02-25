3.03

# 3.11
# a = input().split('@')
# if len(a) == 2:
#     if a[1] == "gmail.com":
#         print(a[0])
#     else:
#         print(f"{a[1]} is not supported")
# else:
#     print("Enter valid mail!")

# 4.01
#
# s =[1,2,51,25,5]
# summ = 0
# i = 0
# while i < len(s):
#     if s[i] > 5:
#         summ += s[i]
#     i+=1
# print(summ)

# 4.03
#
# summ = 0
# while True:
#     a = input("Введите число\n")
#     if not a.isdigit():
#         if a == 'стоп':
#             break
#         continue
#     a = int(a)
#     if a % 5 == 0:
#         continue
#     summ += a
# print(summ)






# num = int(input("Введите целое число"))
# lst = range(num)
# summ = 0
# i = 0
# while i < len(lst):
#     summ += lst[i] ** 3
#     i += 1
# print(summ)

# a = 1
# b = 4
# summ = 0
# for i in range(a,b):
#     summ += i ** 3
# print(summ)


# A, B = 5, 10
# for i in range(A,B+1):
#     print(i)
# N = len(range(A,B+1))
# print(f"Count is {N}")

# def say_hello(name):
#     return f"Hello, {name}"
# print(say_hello('Yaraslau'))

def add(x, y):
    return x + y