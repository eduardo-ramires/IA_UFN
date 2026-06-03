import random

# CONFIGURAÇÕES DO AG
BITS_CROMOSSOMO = 16
QTD_POPULACAO   = 10
P_CROSSOVER     = 0.8
P_MUTACAO       = 0.05
MAX_GERACOES    = 20


# Cria um individuo aleatório (vetor de 0 e 1)
def gerar_individuo():
    return [random.randint(0, 1) for _ in range(BITS_CROMOSSOMO)]


# Calcula a nota (fitness) que é a soma de 1s
def avaliar_individuo(ind):
    return sum(ind)


# Seleção por roleta clássica
def roleta(pop, notas):
    total = sum(notas)
    if total == 0:
        return random.choice(pop)

    sorteio = random.uniform(0, total)
    acumulado = 0
    for i in range(len(pop)):
        acumulado += notas[i]
        if acumulado >= sorteio:
            return pop[i]
    return pop[-1]


# Cruza dois pais se passar na chance de crossover
def cruzar(pai, mae):
    if random.random() > P_CROSSOVER:
        return pai.copy(), mae.copy()

    # Ponto de corte aleatório
    corte = random.randint(1, BITS_CROMOSSOMO - 1)
    f1 = pai[:corte] + mae[corte:]
    f2 = mae[:corte] + pai[corte:]
    return f1, f2


# Aplica mutação invertendo o bit de acordo com a taxa
def mutar(ind):
    for i in range(BITS_CROMOSSOMO):
        if random.random() < P_MUTACAO:
            ind[i] = 1 - ind[i]  # Inverte de 0 para 1 ou vice-versa
    return ind


# Função principal que roda o algoritmo
def rodar_algoritmo():
    print("=" * 50)
    print("        TRABALHO DE IA - ALGORITMO GENÉTICO        ")
    print("=" * 50)

    # Cria a população inicial
    populacao = [gerar_individuo() for _ in range(QTD_POPULACAO)]

    for g in range(1, MAX_GERACOES + 1):
        # Avalia todo mundo
        notas = [avaliar_individuo(ind) for ind in populacao]

        melhor_nota = max(notas)
        media_nota = sum(notas) / QTD_POPULACAO
        melhor_ind = populacao[notas.index(melhor_nota)]

        # Transforma a lista em texto para printar bonito
        print(f"Ger {g:02d} | Melhor: {melhor_nota:2d} | Média: {media_nota:.1f} | Genes: {''.join(map(str, melhor_ind))}")

        # Se achou o objetivo máximo para o loop
        if melhor_nota == BITS_CROMOSSOMO:
            print(f"\n[!] Sucesso! Solução perfeita achada na geração {g}!")
            break

        # Separa o melhor (Elitismo) para salvar na próxima geração
        nova_pop = [melhor_ind.copy()]

        # Preenche o resto da nova população
        while len(nova_pop) < QTD_POPULACAO:
            p1 = roleta(populacao, notas)
            p2 = roleta(populacao, notas)

            f1, f2 = cruzar(p1, p2)

            # Aplica mutação e adiciona se ainda tiver espaço na lista
            nova_pop.append(mutar(f1))
            if len(nova_pop) < QTD_POPULACAO:
                nova_pop.append(mutar(f2))

        populacao = nova_pop

    # Mostra o resultado do último ciclo
    notas_finais = [avaliar_individuo(ind) for ind in populacao]
    m_nota = max(notas_finais)
    m_ind = populacao[notas_finais.index(m_nota)]

    print("\n" + "=" * 50)
    print("FIM DO PROCESSO")
    print(f"  Melhor encontrado : {''.join(map(str, m_ind))}")
    print(f"  Nota Final        : {m_nota}/{BITS_CROMOSSOMO}")
    print(f"  Desempenho        : {(m_nota/BITS_CROMOSSOMO)*100:.2f}%")
    print("=" * 50)


if __name__ == "__main__":
    random.seed(42) 
    rodar_algoritmo()