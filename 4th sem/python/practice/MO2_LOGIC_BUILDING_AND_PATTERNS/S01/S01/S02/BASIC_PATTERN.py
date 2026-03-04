# # 1.square star pattern 
# n = 4
# output:
# * * * *
# * * * *
# * * * * 
# * * * *
#2. n = int(input())
# for i in range(n):
#     for j in range(n):
#         print("*",end = " ")
#     print()
# # #3. right angle triangle 
# n = int(input())
# for i in range(n):
#     for j in range(i+1):
#         print("*",end= " ")
# #     print()
# # 4.reverse right angle triangle 
# n = int(input())
# for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")
    # print()
# # 5.number based triangle 
# n = int(input())
# for i in range(1,n+1):
#     for j in range(i):
#         print(j+1,end = " ")
#     print()
# 6.number triangle 
# n = int(input())
# for i in range(1,n+1):
#     for j in range(i):
#         print(i+1, end = " ")
#     print()
"""7. with letters
n = int(input())
for i in range(1,n+1):
    ch =  65
    for j in range(i):
        print(chr(ch+j), end = " ")
    print()"""
# given list is multiplied by 2 
# list = [1,2,3,4,5]
# res = []
# for ele in list:
#     res.append(ele*2)
# print(res)
# print([ele*2 for ele in list])
"""to print numbers which are divisible by 2
li = [1,2,3,4,5,6,7]
res = []
for i in li:
    if i%2 == 0:
        res.append(i)
print(res)
[i for i in li if i%2 ==0]"""
# li1 = [1,2,3,4]
# li2 = [6,7,8,9]
# for x in li2:
#     li1.append(x)
# print(li1)
"""to print in single string
li1 = ["a","b","c"]
res = ""
for ch in li1:
    res = res + ch + " "
print(res)"""
# to print a triangle 
# n = int(input())
# for i in range(1,n+1):
#     print(" "*(n-i)+"* "*i)
"""inverted triangle 
n = int(input())
for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i)"""
# diamond shape
# n = int(input())
# for i in range(1,n+1):
#     print(" "*(n-i)+"* "*i)
# for j in range(n-1,0,-1):
#     print(" "*(n-j)+"* "*j)
 