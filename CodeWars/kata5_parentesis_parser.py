"""Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.
Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
"""

#Solucion 1
def valid_parentheses(string):
    lista= []
    for elemento in string:
        if elemento == '(':
            lista.append(elemento)
        elif elemento == ')' :
            if len(lista) != 0:
                lista[0] = str(lista[0]) + ")"
                if lista[0] == '()':
                    lista.pop(0)
            else:
                lista.append( elemento)
    return len(lista) == 0

print(valid_parentheses("()()"))

#solucion 2
def valid_parentheses(string):
    count = 0
    for i in string:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0