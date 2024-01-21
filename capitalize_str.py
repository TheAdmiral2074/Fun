def old_macdonald(name):
    first=name[0:3]
    second=name[3:4]
    rest=name[4:]

    return first.capitalize()+second.capitalize()+rest

print(old_macdonald('oldmacdonald'))