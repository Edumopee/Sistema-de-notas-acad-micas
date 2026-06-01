from nota_alunos import calcular_media, verificar_aprovacao

# Teste 1: Validação de cálculo de média comum
print(calcular_media([8.0, 7.0, 9.0]))  # Saída esperada: 8.0

# Teste 2: Validação de lista vazia (proteção contra divisão por zero)
print(calcular_media([]))  # Saída esperada: 0.0

# Teste 3: Validação da regra de aprovação padrão (Corte: 7.0)
print(verificar_aprovacao(7.5))  # Saída esperada: 'Aprovado'
print(verificar_aprovacao(6.9))  # Saída esperada: 'Reprovado'