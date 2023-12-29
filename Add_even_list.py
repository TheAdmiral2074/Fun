def check_even_list(num_list):
    #list for even numbers
    even_numbers=[]
    for num in num_list:
        if num%2==0:
            even_numbers.append(num)
        else:
            pass
    return even_numbers

print(check_even_list([1,2,5,7,8,10,13]))