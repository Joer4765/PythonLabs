class Vector:
    _num_vec = 0

    def __init__(self, size=1, init_value=0.0):
        self.float_array = [init_value] * size
        self._size = size
        self._code_error = 0
        Vector._num_vec += 1

    def __del__(self):
        print("Vector deleted")
        Vector._num_vec -= 1

    def input_elements(self):
        for i in range(self.size):
            self.float_array[i] = float(input(f"Enter element {i}: "))

    def print_elements(self):
        for i in range(self.size):
            print(self.float_array[i], end=' ')
        print()

    def set_value(self, value):
        for i in range(self.size):
            self.float_array[i] = value

    @staticmethod
    def get_num_vectors():
        return Vector._num_vec

    @property
    def size(self):
        return self._size

    @property
    def code_error(self):
        return self._code_error

    @code_error.setter
    def code_error(self, value):
        self._code_error = value

    def __getitem__(self, index):
        if 0 <= index < self.size:
            return self.float_array[index]
        else:
            self.code_error = -1
            return 0

    def __setitem__(self, index, value):
        if 0 <= index < self.size:
            self.float_array[index] = value
        else:
            self.code_error = -1

    def __add__(self, other):
        if isinstance(other, Vector):
            result = Vector(max(self.size, other.size))
            for i in range(result.size):
                if i < self.size and i < other.size:
                    result[i] = self[i] + other[i]
                elif i < self.size:
                    result[i] = self[i]
                else:
                    result[i] = other[i]
            return result
        elif isinstance(other, (int, float)):
            result = Vector(self.size)
            for i in range(result.size):
                result[i] = self[i] + other
            return result
        else:
            raise TypeError("unsupported operand type(s) for +")

    def __sub__(self, other):
        if isinstance(other, Vector):
            result = Vector(max(self.size, other.size))
            for i in range(result.size):
                if i < self.size and i < other.size:
                    result[i] = self[i] - other[i]
                elif i < self.size:
                    result[i] = self[i]
                else:
                    result[i] = -other[i]
            return result
        elif isinstance(other, (int, float)):
            result = Vector(self.size)
            for i in range(result.size):
                result[i] = self[i] - other
            return result
        else:
            raise TypeError("unsupported operand type(s) for -")

    def __mul__(self, other):
        if isinstance(other, Vector):
            result = Vector(max(self.size, other.size))
            for i in range(result.size):
                if i < self.size and i < other.size:
                    result[i] = self[i] * other[i]
                else:
                    result[i] = 0
            return result
        elif isinstance(other, (int, float)):
            result = Vector(self.size)
            for i in range(result.size):
                result[i] = self[i] * other
            return result
        else:
            raise TypeError("unsupported operand type(s) for *")

    def __truediv__(self, other):
        if isinstance(other, Vector):
            result = Vector(max(self.size, other.size))
            for i in range(result.size):
                if i < self.size and i < other.size:
                    if other[i] != 0:
                        result[i] = self[i] / other[i]
                    else:
                        raise ZeroDivisionError("division by zero")
                else:
                    result[i] = 0
            return result
        elif isinstance(other, (int, float)):
            if other != 0:
                result = Vector(self.size)
                for i in range(result.size):
                    result[i] = self[i] / other
                return result
            else:
                raise ZeroDivisionError("division by zero")
        else:
            raise TypeError("unsupported operand type(s) for /")

    def __mod__(self, other):
        if isinstance(other, Vector):
            result = Vector(max(self.size, other.size))
            for i in range(result.size):
                if i < self.size and i < other.size:
                    if other[i] != 0:
                        result[i] = self[i] % other[i]
                    else:
                        raise ZeroDivisionError("division by zero")
                else:
                    result[i] = 0
            return result
        elif isinstance(other, (int, float)):
            if other != 0:
                result = Vector(self.size)
                for i in range(result.size):
                    result[i] = self[i] % other
                return result
            else:
                raise ZeroDivisionError("division by zero")
        else:
            raise TypeError("unsupported operand type(s) for %")

    def __eq__(self, other):
        if isinstance(other, Vector):
            for i in range(min(self.size, other.size)):
                if self[i] != other[i]:
                    return False
            return True
        else:
            return False

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        if isinstance(other, Vector):
            for i in range(min(self.size, other.size)):
                if self[i] <= other[i]:
                    return False
            return True
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, Vector):
            for i in range(min(self.size, other.size)):
                if self[i] < other[i]:
                    return False
            return True
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Vector):
            for i in range(min(self.size, other.size)):
                if self[i] >= other[i]:
                    return False
            return True
        else:
            return False

    def __le__(self, other):
        if isinstance(other, Vector):
            for i in range(min(self.size, other.size)):
                if self[i] > other[i]:
                    return False
            return True
        else:
            return False

    def __bool__(self):
        for i in range(self.size):
            if self[i] != 0:
                return True
        return False

    def __invert__(self):
        result = Vector(self.size)
        for i in range(result.size):
            result[i] = ~int(self[i])
        return result

    def __and__(self, other):
        if isinstance(other, Vector):
            result = Vector(max(self.size, other.size))
            for i in range(result.size):
                if i < self.size and i < other.size:
                    result[i] = int(self[i]) & int(other[i])
                else:
                    result[i] = 0
            return result
        elif isinstance(other, int):
            result = Vector(self.size)
            for i in range(result.size):
                result[i] = int(self[i]) & other
            return result
        else:
            raise TypeError("unsupported operand type(s) for &")

    def __or__(self, other):
        if isinstance(other, Vector):
            result = Vector(max(self.size, other.size))
            for i in range(result.size):
                if i < self.size and i < other.size:
                    result[i] = int(self[i]) | int(other[i])
                elif i < self.size:
                    result[i] = int(self[i])
                else:
                    result[i] = int(other[i])
            return result
        elif isinstance(other, int):
            result = Vector(self.size)
            for i in range(result.size):
                result[i] = int(self[i]) | other
            return result
        else:
            raise TypeError("unsupported operand type(s) for |")

    def __xor__(self, other):
        if isinstance(other, Vector):
            result = Vector(max(self.size, other.size))
            for i in range(result.size):
                if i < self.size and i < other.size:
                    result[i] = int(self[i]) ^ int(other[i])
                else:
                    result[i] = 0
            return result
        elif isinstance(other, int):
            result = Vector(self.size)
            for i in range(result.size):
                result[i] = int(self[i]) ^ other
            return result
        else:
            raise TypeError("unsupported operand type(s) for ^")

    def __lshift__(self, other):
        if isinstance(other, Vector):
            result = Vector(max(self.size, other.size))
            for i in range(result.size):
                if i < self.size and i < other.size:
                    result[i] = int(self[i]) << int(other[i])
                else:
                    result[i] = 0
            return result
        elif isinstance(other, int):
            result = Vector(self.size)
            for i in range(result.size):
                result[i] = int(self[i]) << other
            return result
        else:
            raise TypeError("unsupported operand type(s) for <<")

    def __rshift__(self, other):
        if isinstance(other, Vector):
            result = Vector(max(self.size, other.size))
            for i in range(result.size):
                if i < self.size and i < other.size:
                    result[i] = int(self[i]) >> int(other[i])
                else:
                    result[i] = 0
            return result
        elif isinstance(other, int):
            result = Vector(self.size)
            for i in range(result.size):
                result[i] = int(self[i]) >> other
            return result
        else:
            raise TypeError("unsupported operand type(s) for >>")
