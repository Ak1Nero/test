
def nums(*n):
    b = 0
    for i in range(len(n)):
        b += n[i]
    return b
print(nums(1,2,3,4,5))