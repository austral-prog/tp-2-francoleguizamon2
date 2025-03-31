def change():
    expense = 23.75
    money = 100
    print('Ingresar gasto:')
    print(expense)
    print('Dinero recibido')
    print(money)
    print('')
    print('Vuelto')
    print('')
    if expense > money:
        print('Saldo insuficiente')
        return False
    elif expense == money:
        print('Pagó justo')
    else:
        change = money - expense
        change_entero = int(money - expense)
        change_centavos = change - (change_entero)
        print('Pesos:')
        print(change_entero)
        print('Centavos:')
        print(int(change_centavos * 100))
        return True
change()
