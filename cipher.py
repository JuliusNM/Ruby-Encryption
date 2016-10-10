def open_file(file):
    f = open(file)
    words = f.read()
    return words

def cipher(words,key):
    f = open("cipher_text.txt", "w")
    numbers =[]
    for i in words:
        num = ord(i) + key
        f.write(str(num)+",")
    f.close()

def decipher(file,key):
    ciphered = open_file(file)
    f = open("decipher_text.txt", "w")
    c=[]
    c = ciphered.split(",")
    for i in c:
        x = int(i)
        #print chr(x - key)
        f.write(chr(x-key))
    f.close()

text_file = open_file("text.txt")
cipher(text_file,5)
decipher("cipher_text.txt",6)
