tabuada = int(input("Qual a tabuada?"))
repetir = 10
contador = 1
while(contador <= repetir):
    resultado = contador * tabuada
    print("%s x %s = %s"%(contador, tabuada, resultado))
    contador = contador + 1
