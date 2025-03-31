def ada():
    first_name = "AdA"
    last_name = "LoVeLAce"
    lowercase = first_name.lower() + ' ' + last_name.lower()
    uppercase = first_name.upper() + ' ' + last_name.upper()
    title = first_name.title() + ' ' + last_name.title()
    indentado = '    ' + lowercase
    print(lowercase)
    print(title)
    print(uppercase)
    print(indentado)
# Todos estos print producen el output solicitado en el README
ada()
