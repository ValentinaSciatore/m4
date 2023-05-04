if __name__ == '__main__':
    x = int(input("inserire un numero intero positivo "))
    esponente = 0
    # finchè la potenza di due per l'esponente è minore del numero incrementa di 1 l'esponente
    while 2 ** esponente < x:
        esponente += 1
    # stampa la prima potenza di 2 inferiore al numero dato
    print(2**(esponente - 1))
