def change(expense, money):
    print('Ingresar gasto: ', expense)
    print('Dinero recibido: ', money)
    if expense > money:
        print('Saldo insuficiente')
        return False
    elif expense == money:
        print('Pagó justo')
    else:
        change = money - expense
        change_entero = int(money - expense)
        change_centavos = change - (change_entero)
        print('Vuelto: ', 'Pesos: ', change_entero, 'Centavos: ', change_centavos)
        return True
gasto = 23.75
dinero_recibido = 100
change(gasto, dinero_recibido)
