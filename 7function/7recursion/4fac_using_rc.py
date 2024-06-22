
# explain
# if we need fact of 5 = 5x4!
# similarly 4! = 4x3!
# similarly 3! = 3x2!
# similarly 2! = 2x1!
# similarly 1! = 1x0!
# similarly 0! = 1
# this called recursion
n = int(input())
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

result = fact(n)
print(result)