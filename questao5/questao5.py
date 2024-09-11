def inverter_string(s):
    s_invertida = ''
    for char in s:
        s_invertida = char + s_invertida
    return s_invertida

# String de entrada
string = input("Digite uma string para inverter: ")
print(f"String invertida: {inverter_string(string)}")
