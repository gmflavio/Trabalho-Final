def entrada(mensagem, min, max):
    while True:
        try:
            valor = float(input(mensagem))
            if min <= valor <= max:
                return valor
            else:
                print(f"O valor deve estar entre {min} e {max}.")
        except ValueError:
            print("Insira um valor numérico válido.")

def calcular_emprestimo(renda_mensal, valor_emprestimo, prazo_emprestimo):
    taxa_juros = 0.005  # 0,5% ao mês
    valor_prestacao = (valor_emprestimo * taxa_juros) / (1 - (1 + taxa_juros) ** -prazo_emprestimo)
    custo_total = valor_prestacao * prazo_emprestimo
    return taxa_juros, valor_prestacao, custo_total

renda_mensal = entrada("Por favor, insira sua renda mensal: R$ ", 1000, 5000)
valor_emprestimo = entrada("Qual o valor do empréstimo desejado: R$ ", 1000, 30000)
prazo_emprestimo = entrada("Por favor, insira o prazo do empréstimo desejado (em meses): ", 12, 72)

taxa_juros, valor_prestacao, custo_total = calcular_emprestimo(renda_mensal, valor_emprestimo, prazo_emprestimo)

print(f"Taxa de juros mensal: {taxa_juros * 100:.2f}%")
print(f"Valor da prestação mensal: R${valor_prestacao:.2f}")
print(f"Custo total do empréstimo: R${custo_total:.2f}")