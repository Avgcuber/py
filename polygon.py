class polygon:
    def __init__(self,no_of_sides):
        self.n=no_of_sides
        self.sides=[0 for i in range(no_of_sides)]
    def inputsides(self):
        self.sides=[float(input("enter side "+str(i+1)+" : ")) for i in range(self.n)]
    def dispsides(self):
        for i in range(self.n):
            print("side ",i+1,"is",self.sides[i])
            
class triangle(polygon):
    def __init__(self):
        polygon.__init__(self,3)
    def findarea(self):
        a,b,c=self.sides
        s=(a+b+c)/2
        area=(s*(s-a)*(s-b)*(s-c))**0.5
        print("area of traingle is ",area)
t=triangle()
t.inputsides()
t.dispsides()
t.findarea()


#FOR SQUARE :
class square(polygon):
    def __init__(self):
        polygon.__init__(self,2)
    def findarea(self):
        a,b=self.sides
        area=a*b
        print("area of square is ",area)

