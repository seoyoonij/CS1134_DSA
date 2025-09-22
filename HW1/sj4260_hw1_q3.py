# 3a.
def sum_squares_a(n):
    res = 0 
    for i in range(n):
         res += i**2
    return res

# 3b. 
def sum_squares_b(n):
    return sum(i**2 for i in range(n))

# 3c.
def sum_squares_odd_c(n):
    res = 0 
    for i in range(1,n,2):
        res += i**2
    return res

# 3d.
def sum_squares_odd_d(n):
    return sum(i**2 for i in range(1,n,2))


# Test
print(sum_squares_a(4)) # 1+4+9 = 14
print(sum_squares_b(4))
print(sum_squares_odd_c(4)) # 1+9 = 10
print(sum_squares_odd_d(4))