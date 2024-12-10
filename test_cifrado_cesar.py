from cesar import encrypt_letter,encrypt_word,make_encrypt,creaParCesar
def test_encrypt_letter():
    assert encrypt_letter("a",2) == "C"
    assert encrypt_letter("C",2) == "E"
    assert encrypt_letter("Z",2) == "A"
    assert encrypt_letter("z",2) == "A"
    assert encrypt_letter(" ",2) == "B"

    assert encrypt_letter("A",-2) == "Z" 

    assert encrypt_letter(",",1) == "," 
    assert encrypt_letter("?",1) == "?" 


def test_encrypt_word():
    assert encrypt_word("CABRA", 2) == "ECDTC", "no funciona"
    assert encrypt_word("ZIGZAG", 2) == "AKIACI", "no funciona"
    assert encrypt_word("ZigZag", 2) == "AKIACI", "no funciona"

def test_simple_encrypt_whith_stranges_characters(): 
    assert encrypt_word("hola, mundo!",1) == "IPMB,ANVÑEP!"

def test_make_encrypt():
    cesar2 = make_encrypt(2)
    assert cesar2("ZigZag") == "AKIACI" 

def test_creaParCesar():
    cifrar3,desdifrar3 = creaParCesar(3) #Esto se llama desempaquetar
    assert cifrar3("ZigZag") == "BLJBDJ"
    assert desdifrar3("BLJBDJ") == "ZIGZAG"


