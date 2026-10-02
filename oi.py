duziaovos = int(input("Digite quantas duzias de ovos voce tem?:\n"))
litrosdeleite = float(input("Digite a quantidade de litros de leite: "))
kilodequeijo = float(input("Digite a quantidade de quilos de queijo: "))

valorovo= float(input("Digite o valor da duzia de ovos: "))
valorleite=float(input("Digite o valor do litro de leite: "))
valorqueijo=float(input("Digite o valor do kilo de queijo: "))

digovo = float(input("Digite o valor de custo do produto da duzia de ovos: "))
digoleite = float(input("Digite o valor de custo do produto do litro de leite: "))
digoqueijo = float(input("Digite o valor de custo do produto do kilo de queijo: "))

custoovo = duziaovos * digovo
custoleite = litrosdeleite * digoleite
custoqueijo = kilodequeijo * digoqueijo

print("O custo total dos ovos é: R$", custoovo)
print("O custo total do leite é: R$", custoleite)
print("O custo total do queijo é: R$", custoqueijo)