from rich import print

lista = []
contador = 0

while True:
    perg = int(input("Escolher um valor (Valor negativo para cancelar): "))
    if perg >= 0:
        lista.append(perg)
    elif perg < 0:
        break

lista_crescente = []

def crescente():
    while lista != []:
        maior_numero = min(lista, key=int)
        lista_crescente.append(maior_numero)
        lista.remove(maior_numero)
    return lista_crescente

lista_decrescente = []

def decrescente():
    while lista != []:
        menor_numero = max(lista, key=int)
        lista_decrescente.append(menor_numero)
        lista.remove(menor_numero)
    return lista_decrescente

escolha = input("Deseja a lista decrescente ou crescente? : [d/c]: ")

lista_true = []

if escolha == "c":
    lista_true = crescente()
    print(crescente())
    contador += 1

elif escolha == "d":
    lista_true = decrescente()
    print(decrescente())
    contador += 1

qtt_element = len(lista_true)

print(f'Existem {qtt_element} elementos na sua lista')



while True:
    print("O que você deseja fazer?")
    print("1 - Eliminar um valor")
    print("2 - Adicionar um valor numa posição")
    print("3 - Desempilhar a pilha")

    resp = int(input())

    if resp == 1:
        pilha = int(input(" Caso queira remover o valor: [valor negativo para cancelar] "))
        if not pilha in lista_true:
            input("Não existe essa posição na lista, Aperte enter para continuar.")
            print(lista_true)
            print(f'Existem {qtt_element} elementos na sua lista')
        elif pilha in lista_true:
            lista_true.remove(pilha)
            print(lista_true)
            qtt_element -= 1
            contador += 1
            print(f'Existem {qtt_element} elementos na sua lista')
        elif pilha < 0:
            break
    
    elif resp == 2:
        
        perg2 = int(input("Qual posição da lista você quer colocar um valor?: "))-1
        perg_value = int(input("Qual o valor?: "))

        comeco = []
        fim = []

        if perg2 > len(lista_true):
            input("Não existe essa posição na pilha")
        for i, value in enumerate(lista_true):
            if i < perg2:
                comeco.append(value)
            else:
                fim.append(value)
        comeco.append(perg_value)
        lista_true = comeco + fim

        print(lista_true)
        qtt_element += 1
        contador += 1
        print(f'Existem {qtt_element} Elementos na sua lista')
    
    elif resp == 3:
        break

while len(lista_true) != 0:
    print(lista_true)
    del(lista_true[-1])

print(f'Foram feitas {contador} Operações na pilha')
