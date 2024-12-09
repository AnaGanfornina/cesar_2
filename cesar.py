def encrypt_letter(letter:str,num:int)->str:
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
        new_word += encrypt_letter(leter,num)
    return new_word

def make_encrypt(d:int)->callable:
   
   def encrypt(word:str)-> str:
        return encrypt_word(word,d)
   
   return encrypt


def creaParCesar(d:int):
    def encrypt(word:str)-> str:
        return encrypt_word(word,d)
    
    def decrypt(word:str)-> str:
        return encrypt_word(word,-d)
    
    return encrypt,decrypt
   

assert encrypt_letter("a",2) == "C"
assert encrypt_letter("C",2) == "E"
assert encrypt_letter("Z",2) == "A"
assert encrypt_letter("z",2) == "A"
assert encrypt_letter(" ",2) == "B"


assert encrypt_word("CABRA", 2) == "ECDTC", "no funciona"
assert encrypt_word("ZIGZAG", 2) == "AKIACI", "no funciona"
assert encrypt_word("ZigZag", 2) == "AKIACI", "no funciona"


cesar2 = make_encrypt(2)
assert cesar2("ZigZag") == "AKIACI" 


cifrar3,desdifrar3 = creaParCesar(3)
assert cifrar3("ZigZag") == "BLJBDJ"
assert desdifrar3("BLJBDJ") == "ZIGZAG"


