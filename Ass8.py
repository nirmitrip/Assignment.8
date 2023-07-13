class N:
    def __init__(self, a, b, c):
        self.a = b
        self._b = b
        self.__c = c

    def display(self):
        print("Values in Class N:")
        try:
            print("Private member c:", self.__c)
        except AttributeError:
            print("Error: Private member 'c' cannot be accessed.")

        print("Protected member b:", self._b)
        print("Public member a:", self.a)


class G(N):
    def display(self):
        print("Values in Class G:")
        print("Protected member b (inherited from Class N):", self._b)
        print("Public member a (inherited from Class N):", self.a)

obj = G(10, 11, 14)
obj.display()