word_without_vowels = "" # atribui uma string vazia ("")

palavra = input("Escreva uma palavra: ")
palavra = palavra.upper()

for letra in palavra:
    if letra == "A":
        continue
    elif letra == "E":
        continue
    elif letra == "I":
        continue
    elif letra == "O":
        continue
    elif letra == "U":
        continue
    else:
        print (letra, end="") #o end="" serva para colocar o resultado em um linha só 
                                # ex: GRGRY em vez de:
                                # EX:
                                # G
                                # R
                                # G
                                # R
                                # Y
 
