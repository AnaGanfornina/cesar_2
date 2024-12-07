def cifrador(letra:str,num:int)->str:
    """
    Recibe una letra y un número, devuelve la letra del diccionario que corresponda
    al número de saltos indicados
    """
    dictionary = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                   "m", "n","ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    encrypted = ""
    for index,item in enumerate(dictionary):
        if item == letra:
            encrypted = dictionary[index + num]
            break

    return encrypted


assert cifrador("a",2) == "c"

def creaCifrador(d:int)->callable:
    pass