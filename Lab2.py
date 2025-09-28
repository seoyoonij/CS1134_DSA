# 1.
class Polynomial:
    def __init__ (self, coeff):
        self.data = coeff

    def __add__ (self, other):
        lst = self.data.copy()
        temp = other.data.copy()

        if len(lst) > len(temp):
            lst, temp = temp, lst # swap: have lst be the shorter one
        while len(lst) < len(temp): # extend lst with 0's
            lst.append(0)
        
        lst = [lst[i] + temp[i] for i in range(len(lst))]
        return Polynomial(lst)

    def __call__ (self, param):
        res = 0
        for i in range(len(self.data)):
            res += (val**i)*self.data[i]
        return res
    
    def __repr__ (self):
        return " + ".join([f"{self.data[i]}x^{i}" for i in range(len(self.data)-1, -1, -1)])
    
    def __mul__ (self, other):
        lst = [0] * (len(self.data) + len(other.data) -1)
        for i in range(len(self.data)):
            for j in range(len(other.data)):
                lst[i+j] += self.data[i] * other.data[j]
        return Polynomial(lst)

    def __derive__ (self):
        self.data = [i * self.data[i] for i in range(1, len(self.data))]


# 2.
class UnsignedBinaryInteger:
    def __init__ (self, bin_num_str):
        self.data = bin_num_str

    def decimal (self):
        value = 0
        for i in range(len(value)):
            value += int(self.data[i] * 2** (len(self.data)-1-i))
        return value
    
    def __lt__ (self, other): # self < other
        if len(self.data) < len(other.data): # longer, more digits, greater value
            return True
        elif len(self.data) > len(other.data):
            return False
        # if same number of digits
        for i in range(len(self.data)):
            if self.data[i] != other.data[i]:
                return self.data[i] == '0' # if self is 0, other is bigger. so True
        return False # in case no difference in digits

    def __gt__ (self, other):
        return other < self

    def __eq__ (self, other):
        return self.data == other.data # same bin_num_str
        # or, return not (self<other or self>other)

    def __is_twos_power__ (self):
        # two's power = first element is 1 and rest are all 0
        for i in range(1, len(self.data)):
            if self.data[i] == '1':
                return False
        return self.data[0] == '1'
    
    def largest_twos_power (self):
        if self.data[0] == '0':
            raise Exception("No twos power for 0")
        largest_sum = 1
        value = self. decimal()

        while largest_sum *2 <= value:
            largest_sum *= 2
        return largest_sum

    def __repr__ (self):
        return f"0b{self.data}"