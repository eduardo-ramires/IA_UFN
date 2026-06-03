import random

# Variáveis globais do trabalho
CIDADES = [1, 2, 3, 4, 5, 6, 7, 8, 9]
TAM_POP = 100
MAX_GERACOES = 500
TX_MUTACAO = 0.15
TX_CROSSOVER = 0.85
TORNEIO_K = 3


# Função que calcula os erros da rota (quanto menor a nota, melhor)
def calcular_aptidao(rota):
    penalidade = 0

    # 1. Testa se a rota está na ordem crescente
    for i in range(len(rota) - 1):
        if rota[i] > rota[i + 1]:
            penalidade += 10

    # 2. Testa se tem cidade repetida na rota
    for cidade in CIDADES:
        qtd = rota.count(cidade)
        if qtd > 1:
            penalidade += (qtd - 1) * 20

    return penalidade


# Cria um indivíduo aleatório embaralhando as cidades
def criar_individuo():
    ind = CIDADES.copy()
    random.shuffle(ind)
    return ind


# Faz a seleção por torneio pegando K aleatórios e escolhendo o com menos erros
def torneio(pop):
    competidores = random.sample(pop, TORNEIO_K)
    # Retorna quem tiver o menor valor na função calcular_aptidao
    return min(competidores, key=calcular_aptidao)


# Operador de cruzamento OX (Order Crossover) para não quebrar a ordem
def crossover_ox(pai, mae):
    n = len(pai)
    # Sorteia dois pontos de corte
    a, b = sorted(random.sample(range(n), 2))

    def montar_filho(p1, p2):
        meio = p1[a : b + 1]
        # Pega o resto que não tá no meio
        resto = [x for x in p2 if x not in meio]
        return resto[:a] + meio + resto[a:]

    return montar_filho(pai, mae), montar_filho(mae, pai)


# Troca duas cidades de lugar na rota (mutação por sorteio)
def mutar(ind):
    novo_ind = ind.copy()
    i, j = random.sample(range(len(novo_ind)), 2)
    novo_ind[i], novo_ind[j] = novo_ind[j], novo_ind[i]
    return novo_ind


# Função principal que roda o Algoritmo Genético
def rodar_ag():
    # Cria a primeira população
    pop = [criar_individuo() for _ in range(TAM_POP)]

    for g in range(MAX_GERACOES):
        # Ordena a população deixando os melhores (menor erro) no topo
        pop.sort(key=calcular_aptidao)
        melhor = pop[0]
        nota_melhor = calcular_aptidao(melhor)

        # Mostra o progresso a cada 50 gerações
        if g % 50 == 0:
            print(f"Geração {g:3d} | Erros: {nota_melhor} | Rota: {melhor}")

        # Se achou a rota perfeita (0 erros), para o programa
        if nota_melhor == 0:
            print(f"\n[!] Rota perfeita encontrada na geração {g}!")
            break

        # Elitismo: passa o melhor direto para a próxima geração
        nova_pop = [melhor.copy()]

        # Loop para preencher o resto da população
        while len(nova_pop) < TAM_POP:
            pai = torneio(pop)
            mae = torneio(pop)

            # Vê se vai cruzar os pais
            if random.random() < TX_CROSSOVER:
                f1, f2 = crossover_ox(pai, mae)
            else:
                f1, f2 = pai.copy(), mae.copy()

            # Vê se vai mutar o filho 1
            if random.random() < TX_MUTACAO:
                f1 = mutar(f1)
            # Vê se vai mutar o filho 2
            if random.random() < TX_MUTACAO:
                f2 = mutar(f2)

            nova_pop.append(f1)
            if len(nova_pop) < TAM_POP:
                nova_pop.append(f2)

        pop = nova_pop

    # Print final do resultado
    pop.sort(key=calcular_aptidao)
    campeao = pop[0]
    print("\n" + "=" * 50)
    print("        RESULTADO DO ALGORITMO GENÉTICO        ")
    print("=" * 50)
    print(f"Melhor rota achada : {campeao}")
    print(f"Total de erros     : {calcular_aptidao(campeao)}")
    print("=" * 50)


if __name__ == "__main__":
    random.seed(42)  # Deixei o seed para manter o resultado igual do original
    rodar_ag()