'''def mult(a,b):
    return a * b
v1= int(input("Digite o primeiro valor: "))
v2= int(input("Digite o segundo valor: "))
resultado = mult(v1,v2)
print(" A multiplicação dos numeros é",resultado)'''

def imc(a,b):
    return (a/(b**2))
peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))

resultado = imc (peso,altura)

print("O IMC é", resultado)

if resultado < 18.5 :
    print("Baixo peso")
elif resultado <= 24.9 :
    print("Peso normal")
elif resultado <= 29.9 :
    print("Excesso de peso")
elif resultado < 35 :
    print("Obesidade")
else :
    print("Obesidade extrema")