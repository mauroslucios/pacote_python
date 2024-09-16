class Calculadora:
    def adicionar(self, x, y):
        return x + y

    def subtrair(self, x, y):
        return x - y

    def multiplicar(self, x, y):
        return x * y

    def dividir(self, x, y):
        if y == 0:
            return "Erro: Divisão por zero!"
        return x / y


def main():
    calc = Calculadora()
    
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite o número da operação (1/2/3/4): ")

    if escolha in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(f"{num1} + {num2} = {calc.adicionar(num1, num2)}")
        elif escolha == '2':
            print(f"{num1} - {num2} = {calc.subtrair(num1, num2)}")
        elif escolha == '3':
            print(f"{num1} * {num2} = {calc.multiplicar(num1, num2)}")
        elif escolha == '4':
            print(f"{num1} / {num2} = {calc.dividir(num1, num2)}")
    else:
        print("Escolha inválida!")


if __name__ == "__main__":
    main()

# 1. Adição
# 2. Subtração
# 3. Multiplicação  
# 4. Divisão