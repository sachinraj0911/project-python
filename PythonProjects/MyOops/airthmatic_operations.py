class AirthmaticOp():

    def operations(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.res = 0
        print(self.b.__class__)
        print(type(self.b))
        if self.b.__class__ == int:
            if self.c == '+':
                self.res = self.a + self.b
            if self.c == '-':
                self.res = self.a - self.b
            if self.c == '*':
                self.res = self.a * self.b
            if self.c == '/':
                self.res = self.a // self.b
        else:
            return "operation not allowed"
        return self.res

a = AirthmaticOp()

val = a.operations(10, 8, '*')
print(val)

