string = "str-str-str"

if string!= '':
    string = string.split('-')
    string = "".join(string)
    print(string)
    string = string.split('_'),
    if string[0][0].upper() == string [0][0]:
        string[0] = string[0].capitalize()
    for i,elemento in enumerate(string):
        if elemento is string[0]:
            pass
        else:
            string[i] = elemento.capitalize()
print("".join(string))
