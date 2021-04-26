class Variable:
    def variable_method(self):
        self.a=3
        self.b=4
        return self.a,self.b


class Sum(Variable):
    def sum_method(self):
        print("Sum",(self.a+self.b))

if __name__=='__main__':
    x=Sum()
    x.variable_method()
    x.sum_method()


