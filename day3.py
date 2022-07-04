# 2ND LARGEST ELEMENT IN ARRAYS after removing duplicates

def solve(n, arr):
    z = []
    for i in arr:
        if i not in z:
            z.append(i)
    z.sort()
    print(z[len(z)-2])