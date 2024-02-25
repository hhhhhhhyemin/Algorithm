A, B = input().split()
if A and B != '0':
    A = A[::-1]; B = B[::-1]
    print(max(A, B))