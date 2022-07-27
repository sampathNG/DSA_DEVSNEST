# FIBONACCI SEQUENCE
# def recur_fibo(n):
#    if n <= 1:
#        return n
#    else:
#        return(recur_fibo(n-1) + recur_fibo(n-2))

# FOR PRINTING NTH FIBONACCI NIUMBER
# print(recur_fibo(5))

# nterms = 10

# if nterms <= 0:
#    print("Plese enter a positive integer")
# else:
# FOR PRINTING COMPLETE FIBONACCI SEQUENCE NUMBERS
#    print(recur_fibo(nterms))
#    print("Fibonacci sequence:")
#    for i in range(nterms):
    #    print(recur_fibo(i))

# *********************************

# FACTORIAL
def fac(n):
    if n <= 1:
        return n
    else:
        return n * fac(n-1)
# print(fac(5))

def iterative_factorial(n):
    f = 1
    for i in range(2, n+1):
        f *= i
    return f
# print(iterative_factorial(5))

# SUM USING RECURSSION
def sum(n):
    if(n<=0):
        return n
    else:
        return n + sum(n-1)
print(sum(5))

# Python program to check if given
# number is power of 2 or not

# Function to check if x is power of 2
def isPowerOfTwo(n):
	if (n == 0):
		return False
	while (n != 1):
			if (n % 2 != 0):
				return False
			n = n // 2

	return True
print(isPowerOfTwo(5))
