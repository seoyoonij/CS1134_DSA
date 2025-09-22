lst_a = [10 ** i for i in range(6)] 
lst_b = [i * (i+1) for i in range(10)] 
lst_c = [chr(i) for i in range(ord("a"), ord("z")+1)] # ord() gives ascii. chr() type-casts into char.


# Test
print(lst_a)
print(lst_b)
print(lst_c)
