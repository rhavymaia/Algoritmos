# Sortear um número.
from random import randint

sorteio = randint(1, 10)

# Adivinhar o número sorteado n vezes.
acertou = False
while(not(acertou)):
    print("Tentou!")
    acertou = True
