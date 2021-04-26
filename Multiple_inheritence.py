class variable:
    def __init__(self):
        self.a=4
        self.b=5
    def var(self,a,b):
        self.a=a
        self.b=b


class sum(variable):
    def sum1(self):
        print("Sum: ",self.a+self.b)

class sub(variable):
    def sub1(self):
        print("Difference: ",self.a-self.b)

if __name__=='__main__':
    x=sum()
    y=sub()
    x.sum1()
    y.sub1()
    print("After passing variables by calling var function: ")
    x.var(10,5)
    y.var(10,5)
    x.sum1()
    y.sub1()
