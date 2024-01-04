def myfunc(input_string):
    result = ""
    for i in range(len(input_string)):
        if i % 2 != 0:
            result += input_string[i].upper()
        else:
            result += input_string[i].lower()
    return result

# Example usage:
input_str = "skyline"
output_str = myfunc(input_str)
print(output_str)

