repetir = int(input("Quantidade de repetições: "))
contador = int(input("Início do contador:"))
salto = int(input("Qual o valor do salto?"))
while(contador <= repetir):
    resto = contador % 2
    if(resto == 0):
        print("É par: %s"%contador)
    else:
        print("É ímpar: %s"%contador)
    contador = contador + salto
