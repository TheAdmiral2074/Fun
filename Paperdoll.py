def paperdoll(text):
    result= ''
    for char in text:
        result+=char*3+'.'
    return result

print(paperdoll('hello world'))

