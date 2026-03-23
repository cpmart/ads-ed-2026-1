def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
    
n = int(input("Informe o valor: "))
resultado = fatorial(n)

print(f"Resultado = {resultado}")