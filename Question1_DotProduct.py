##This function finds the dot product of two point a and b 
## N represent the number of axis
def DotProduct(N, a,b):
    n=0
    mylist =[]
    for i in range(N):
        acc= a[n] * b[n]
        mylist.append(acc)
        n = n+1    
    print(sum(mylist))
