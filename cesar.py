from typing import *

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
            encrypted = dictionary[(index + num) % len(dictionary)] 
            break
        else:
            encrypted = letter
            

    return encrypted

def encrypt_word(word:str,num:int)->str:
    """
    Recibe una palabra y un número, devuelve la palabra dcifrada
    """
    new_word = ""
    for leter in word:
        new_word += encrypt_letter(leter,num)
    return new_word

def make_encrypt(d:int)->Callable:
   
   def encrypt(word:str)-> str:
        return encrypt_word(word,d)
   
   return encrypt


def creaParCesar(d:int):
    def encrypt(word:str)-> str:
        return encrypt_word(word,d)
    
    def decrypt(word:str)-> str:
        return encrypt_word(word,-d)
    
    return encrypt,decrypt
   
