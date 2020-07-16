"""
Michel Manuel Ampofo
Question 2
"""
class point:
    def __init__(self, x1,y1,x2,y2):
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2

    def UpperRight(self):
        UpperRight = (self.x2,self.y2)
        return UpperRight
    def LowerLeft(self):
        LowerLeft = (self.x1,self.y1)
        return LowerLeft
    

class rectangle:
    def __init__(self,UpperRight, LowerLeft):
        self.UpperRight = UpperRight
        self.LowerLeft= LowerLeft
       
        

    def findarea(self):        
        length = UpperRight[1] - LowerLeft[1]
        width = UpperRight[0] - LowerLeft[0]
        
        return length*width
    
    def findPerimeter(self):
        length = UpperRight[1] - LowerLeft[1]
        width = UpperRight[0] - LowerLeft[0]

        return (2*length)+(2*width) 
        

    


print("To find the Area and perimeter of you Rectangle...")
UpperRightX = float(input("Enter the X component of the Upper Right Corner: "))
UpperRightY = float(input("Enter the Y component of the Upper Right Corner: "))
LowerLeftX= float(input("Enter the X component of the Lower Left Corner: "))
LowerLeftY= float(input("Enter the Y component of the Lower Left Corner: "))

answer = input("Do you want another rectangle(Yes/No): ")
if answer =="Yes":
    UpperRightX2= float(input("Enter the X component of the Upper Right Corner: "))
    UpperRightY2 = float(input("Enter the Y component of the Upper Right Corner: "))
    LowerLeftX2= float(input("Enter the X component of the Lower Left Corner: "))
    LowerLeftY2= float(input("Enter the Y component of the Lower Left Corner: "))
    
    points = point(LowerLeftX, LowerLeftY, UpperRightX, UpperRightY)
    UpperRight= points.UpperRight()
    LowerLeft= points.LowerLeft()

    
    points2 = point(LowerLeftX2, LowerLeftY2, UpperRightX2, UpperRightY2)
    UpperRight2= points2.UpperRight()
    LowerLeft2= points2.LowerLeft()

    rect1 = rectangle(UpperRight,LowerLeft)
    rect2 = rectangle(UpperRight2,LowerLeft2)

    

    print("Area for rectangle 1 : ",  rect1.findarea())
    print("Perimeter for rectangle 1 : ",  rect1.findPerimeter())
    print("Area for rectangle 2: ",  rect2.findarea())
    print("Perimeter for rectangle 2 : ",  rect2.findPerimeter())
    def rectangleIntersect():
        leftmost = min(LowerLeftX, LowerLeftX2)
        if leftmost == LowerLeftX:
            
            width = UpperRightX - LowerLeftX
            if LowerLeftX + width <= LowerLeftX2 :
                return False
            else:
                return True
        else:
            
            width = UpperRightX2 - LowerLeftX2
            if LowerLeftX2 + width <= LowerLeftX :
                return False
            else:
                return True
    print(rectangleIntersect())
 
    

    
    
else: 
   
     
    points = point(LowerLeftX, LowerLeftY, UpperRightX, UpperRightY)
    UpperRight= points.UpperRight()
    LowerLeft= points.LowerLeft()


    rect = rectangle(UpperRight, LowerLeft)


    print("Area : ",  rect.findarea())
    print("Perimeter : ",  rect.findPerimeter())




