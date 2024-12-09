from cesar import encrypt_letter,encrypt_word,make_encrypt,creaParCesar

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


cifrar3,desdifrar3 = creaParCesar(3) #Esto se llama desempaquetar
assert cifrar3("ZigZag") == "BLJBDJ"
assert desdifrar3("BLJBDJ") == "ZIGZAG"


