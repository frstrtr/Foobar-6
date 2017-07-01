import math

def answer(n):
    degeneracy = [0]*(n+1)
    degeneracy [0] = 1
    for i in range(1, n):
        for c in range (n, i-1, -1):
            degeneracy[c] += degeneracy[c-i]

    return degeneracy[n]

print(answer(3))
print(answer(4))
print(answer(5))
print(answer(6))
print(answer(7))
print(answer(8))
print(answer(9))
print(answer(10))
print(answer(11))
print(answer(12))
print(answer(13))
print(answer(14))
print(answer(15))
print(answer(16))
print(answer(200))