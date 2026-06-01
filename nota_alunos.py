
# =====================================================================
# ARQUIVO 1: nota_alunos.py
# Propósito: Código-fonte principal da aplicação, contendo a estrutura
#            de dados, motor lógico modularizado e interface CLI.
# =====================================================================

# ---------------------------------------------------------------------
# PARTE 1: ESTRUTURA DE DADOS (Inicialização da base de dados)
# ---------------------------------------------------------------------
# Lista global que atuará como banco de dados temporário na memória.
# Armazenará dicionários com a estrutura: {"ra": str, "nome": str, "notas": list of float}
lista_estudantes = []


# ---------------------------------------------------------------------
# PARTE 2: MOTOR DE LÓGICA E VALIDAÇÕES (Funções documentadas - PEP 8)
# ---------------------------------------------------------------------

def calcular_media(notas):
    """
    Calcula a média aritmética a partir de uma lista de notas.

    Busca somar todos os valores contidos na lista e dividir pela quantidade
    total de elementos. Possui uma validação interna para evitar erros de 
    divisão por zero caso a lista esteja vazia.

    Args:
        notas (list of float): Uma lista contendo as notas numéricas do estudante.

    Returns:
        float: O valor da média aritmética calculada. Retorna 0.0 se a lista estiver vazia.
    """
    if not notas:
        return 0.0
    return sum(notas) / len(notas)


def verificar_aprovacao(media, media_minima=7.0):
    """
    Valida se a média do estudante atinge o critério mínimo para aprovação.

    Compara a média obtida com a nota de corte da instituição, retornando
    o status textual do estudante de forma assertiva.

    Args:
        media (float): A média final obtida pelo estudante.
        media_minima (float, optional): A nota mínima exigida para ser aprovado. 
            O valor padrão flexível é 7.0.

    Returns:
        str: 'Aprovado' se a média for maior ou igual à media_minima, 
             ou 'Reprovado' caso contrário.
    """
    if media >= media_minima:
        return 'Aprovado'
    else:
        return 'Reprovado'


def ra_ja_existe(ra_procurado):
    """
    Percorre a base de dados para checar a duplicidade de Registro Acadêmico.

    Args:
        ra_procurado (str): O RA digitado pelo usuário que precisa ser validado.

    Returns:
        bool: True se o RA já estiver cadastrado no sistema, False caso contrário.
    """
    for estudante in lista_estudantes:
        if estudante["ra"] == ra_procurado:
            return True
    return False


# ---------------------------------------------------------------------
# PARTE 3: INTERAÇÃO COM O USUÁRIO (Fluxos de cadastro e relatórios)
# ---------------------------------------------------------------------

def cadastrar_estudante():
    """Coleta e sanitiza os dados do aluno antes de inseri-lo na lista global."""
    print("\n--- NOVO CADASTRO ---")
    
    # Validação do RA (Garantia de Unicidade)
    while True:
        ra = input("Digite o RA do estudante: ").strip()
        if ra == "":
            print("Erro: O RA não pode ser vazio.")
        elif ra_ja_existe(ra):
            print(f"Erro: O RA {ra} já está cadastrado no sistema! Tente outro.")
        else:
            break
            
    nome = input("Digite o nome do estudante: ").strip()
    
    # Coleta de notas dinâmica com tratamento de exceções
    notas = []
    print("Digite as notas do aluno (ou digite 'fim' para encerrar):")
    while True:
        entrada = input("Nota: ")
        if entrada.lower() == 'fim':
            break
        
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Aviso: A nota deve estar estritamente entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Digite um número decimal válido ou 'fim'.")
            
    # Criação do dicionário estruturado (Requisito da Etapa 1)
    novo_estudante = {
        "ra": ra,
        "nome": nome,
        "notas": notas
    }
    
    lista_estudantes.append(novo_estudante)
    print(f"Estudante {nome} (RA: {ra}) cadastrado com sucesso!")


def exibir_relatorio():
    """Gera o relatório consolidador acionando os motores lógicos do sistema."""
    if not lista_estudantes:
        print("\nNenhum estudante cadastrado no sistema até o momento.")
        return

    print("\n================ RELATÓRIO FINAL ================")
    for estudante in lista_estudantes:
        ra = estudante["ra"]
        nome = estudante["nome"]
        notas = estudante["notas"]
        
        # Chamada das funções modulares documentadas
        media = calcular_media(notas)
        situacao = verificar_aprovacao(media)
        
        print(f"RA: {ra}")
        print(f"Aluno: {nome}")
        print(f"Notas: {notas}")
        print(f"Média: {media:.2f}")
        print(f"Situação: {situacao}")
        print("-" * 49)


# ---------------------------------------------------------------------
# PARTE 4: MENU INTERATIVO PRINCIPAL
# ---------------------------------------------------------------------
if __name__ == "__main__":
    while True:
        print("\n=== SISTEMA DE NOTAS ACADÊMICAS ===")
        print("1 - Cadastrar Estudante")
        print("2 - Exibir Relatório de Notas")
        print("3 - Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            cadastrar_estudante()
        elif opcao == "2":
            exibir_relatorio()
        elif opcao == "3":
            print("Sistema encerrado com segurança. Até logo!")
            break
        else:
            print("Opção inválida! Selecione uma opção do menu (1, 2 ou 3).")


