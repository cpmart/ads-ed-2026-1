valor = input("Informe o valor: ")
try:
    valor = float(valor)
    print(f"Dobro de {valor} é {valor*2}")
except ValueError as erro:
    print(f"Valor inválido: {erro}")
