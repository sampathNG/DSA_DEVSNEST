# 1: You are given a String str. Return the String by Concatenating it with String "Hello, " and an exclamation mark at the end “!”

def solve(str):
    x = ["Hello, ","!"]
    x.insert(1,str)
    print("".join(x))
solve("World")

# Compute the Sum and Difference of a and b. Return the Product of Sum and Difference.
def solve(a,b):
    print((a+b)*(a-b))
solve(3,5)

# Let x be the integer division and y be the decimal(float) division of a and b.
# Return the product of x and y.

def solve(a,b):
    print((a/b)*(a//b))
solve(7,5)
