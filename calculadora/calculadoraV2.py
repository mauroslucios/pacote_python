class Calculadora:
    def adicionar(self, numeros):
        return sum(numeros)

    def subtrair(self, numeros):
        resultado = numeros[0]
        for num in numeros[1:]:
            resultado -= num
        return resultado

    def multiplicar(self, numeros):
        resultado = 1
        for num in numeros:
            resultado *= num
        return resultado

    def dividir(self, numeros):
        resultado = numeros[0]
        for num in numeros[1:]:
            if num == 0:
                return "Erro: Divisão por zero!"
            resultado /= num
        return resultado


def main():
    calc = Calculadora()
    
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite o número da operação (1/2/3/4): ")

    if escolha in ['1', '2', '3', '4']:
        numeros = []
        print("Digite os números (digite '=' para calcular):")
        
        while True:
            entrada = input()
            if entrada == '=':
                break
            try:
                numero = float(entrada)
                numeros.append(numero)
            except ValueError:
                print("Entrada inválida! Por favor, digite um número ou '=' para calcular.")

        if escolha == '1':
            print(f"Soma: {calc.adicionar(numeros)}")
        elif escolha == '2':
            print(f"Subtração: {calc.subtrair(numeros)}")
        elif escolha == '3':
            print(f"Multiplicação: {calc.multiplicar(numeros)}")
        elif escolha == '4':
            print(f"Divisão: {calc.dividir(numeros)}")
    else:
        print("Escolha inválida!")


if __name__ == "__main__":
    main()