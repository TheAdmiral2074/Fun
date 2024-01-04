def argss(*args):
    even_args= [arg for arg in args if arg%2==0]
    return (even_args)

result1=(argss(1,2,3,47,48,50))

print(result1)



