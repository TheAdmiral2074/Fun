def fibfunc(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibfunc(n-1)+fibfunc(n-2)

result=fibfunc(10)
n=10

##### FORMATING FOR EASY TO READ IS IMPORTANT #####

print(f"The {n}th Fibonacci number is {result}")
