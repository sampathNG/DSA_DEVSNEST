# Given an array arr of size n, and two intervals x and y. Find the average of elements which lies between the given intervals inclusively.

# def solve(n, arr, x, y):
#     if(n>len(arr)):
#         print("cant do")
#     else:
#         z = (y-x)+1
#         sum = arr[x]
#         for i in range(z):
#             if(x<y):
#                 x = x+1
#                 sum = sum + arr[x]
#         print(sum/z)
# solve( 6,[6,2,5,4,3,1],2, 5)

# Given a string str1, Return the array containing the frequency of each character in the order of their occurrence.

# def solve(str):
#     x = {}
#     for i in str:
#         if i in x:
#             x[i] += 1
#         else:
#             x[i] = 1
#     for j in x:
#         print(x[j],end=" ")

# solve("sampathkumar")
1
121
12321
1234321
# PALINDROME NUMBER PATTERN

n = 6
for i in range(1, n + 1):
    for j in range(1, i - 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()