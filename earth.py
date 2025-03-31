def earth():
    x = "Bangladesh"
    y = "Barbados"
    diccionario = [x,y] # En realidad es una lista pero conceptualmente es un diccionario
    diccionario.sort() # Ordena alfabeticamente
    print(f"The result of Bangladesh comes first in the dictionary than Barbados is {diccionario[0] == x}.")
    print(f"The result of Barbados comes first in the dictionary than Bangladesh is {diccionario[0] == y}.")
# El output es el solicitado por el README
earth()
