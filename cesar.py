def encrypt(letter:str,num:int)->str:
    """
    Recibe una letra y un número, devuelve la letra del diccionario que corresponda
    al número de saltos indicados
    """
    dictionary = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                   "K", "L", "M", "N","Ñ", "O", "P", "Q", "R", "S", "T",
                     "U", "V", "W", "X", "Y", "Z"," "]

    
    encrypted = ""
    
    for index,item in enumerate(dictionary):
        if item == letter.upper():
            if index + num >= len(dictionary):
                encrypted = dictionary[(index + num)-len(dictionary)]
                break
            else:
                encrypted = dictionary[index + num]
                break

    return encrypted

def encrypt_word(word:str,num:int)->str:
    """
    Recibe una palabra y un número, devuelve la palabra dcifrada
    """
    new_word = ""
    for leter in word:
        new_word += encrypt(leter,num)
    return new_word

def creaCifrador(d:int)->callable:
    return encrypt(d)

assert encrypt("a",2) == "C"
assert encrypt("C",2) == "E"
assert encrypt("Z",2) == "A"
assert encrypt("z",2) == "A"
assert encrypt(" ",2) == "B"


assert encrypt_word("CABRA", 2) == "ECDTC", "no funciona"
assert encrypt_word("ZIGZAG", 2) == "AKIACI", "no funciona"
assert encrypt_word("ZigZag", 2) == "AKIACI", "no funciona"
#assert creaCifrador