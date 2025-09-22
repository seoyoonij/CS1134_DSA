class Vector:
    # 6a. Accept int or list parameter
    def __init__(self, d):
        if isinstance (d, int): # if dimension,
            self.coords = [0]*d # create 0 vector of d-dimension
        elif isinstance (d, list): # or if coord list,
            self.coords = list(d) # create vector of coord vals

    def __len__(self):
        return len(self.coords)
    
    def __getitem__(self, j):
        return self.coords[j]
    
    def __setitem__(self, j, val):
        self.coords[j] = val

    def __add__(self, other):
        if (len(self) != len(other)):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    # 6b. sub: Returns new vector of u-v
    def __sub__(self, other):
        if (len(self) != len(other)):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result
    
    # 6c. neg: Returns new vector with negated values
    def __neg__(self):
        return Vector([-i for i in self.coords])
    
    # 6d-f. mul: Returns new vector scalar/dot-multiplied
    def __mul__(self, c):
        if isinstance (c, (int,float)): # scalar mult
            return Vector([c*i for i in self.coords])
        elif isinstance (c, Vector): # vector mult
            # dimension check
            if (len(self) != len(c)):
                raise ValueError("dimensions must agree")
            return sum(self[i] * c[i] for i in range(len(self)))
        else:
            raise TypeError("Invalid operand for multiplication")
    
    # 6e. mul: Returns new vector scalar multiplied
    def __rmul__(self, c):
        return Vector([i*c for i in self.coords])
    
    def __eq__(self, other):
        return self.coords == other.coords

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        return '<'+ str(self.coords)[1:-1] + '>'
                                     
    def __repr__(self):
        return str(self)
    
# Test
v1 = Vector(5)
v1[1] = 10
v1 [-1] = 10
print(v1)

v2 = Vector([2,4,6,8,10])
print(v2)

u1 = v1+v2
print(u1)

u2 = -v2
print(u2)

u3 = 3 * v2
print(u3)

u4 = v2 * 3
print(u4)

u5 = v1 * v2
print(u5)