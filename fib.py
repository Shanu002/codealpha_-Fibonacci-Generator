n=int(input("Enter the number of terms needed in Fibonacci Series:\n"))
fibonacci=[]
x,y=0,1
for i in range(n):
    fibonacci.append(x)
    x,y=y,x+y
print("The required Fibonacci series is:-\n",fibonacci)
