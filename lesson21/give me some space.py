def sum_n(n):
    return n*(n+1)//2
def array_sum(a):
    total = 0 
    for i in a :
        total+= i
    return total
def sum(n):
    if n<= 0:
        return 0 
    return n + sum(n-1)
a=[12,3,4,15]

print("sum of first n numbers (n=5):", sum_n(5))
print("array sum:",array_sum(a))
print("recursive sum (n=5):",sum(5))