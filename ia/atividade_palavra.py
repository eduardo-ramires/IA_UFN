import random
import string

# ALFABETO GLOBAL (Letras maiúsculas + espaço em branco)
ALFABETO = string.ascii_uppercase + ' '


# Função simples para ler os dados do teclado
def ler_configuracoes():
    print("\n" + "=" * 45)
    print("      AG - DESCOBRIDOR DE FRASES / PALAVRAS   ")
    print("=" * 45)
    
    palavra = input("\nQual frase/palavra o AG deve achar? ").strip().upper()
    
    # Pega os números tratando erros caso digitem letras
    try:
        pop_tam = int(input("Tamanho da população (ex: 30): "))
        tx_mutacao = float(input("Taxa de mutação em % (ex: 2): ")) / 100
        max_gen = int(input("Máximo de gerações (ex: 2000): "))
    except ValueError:
        print("\n[!] Erro nos dados digitados. Usando valores padrão.")
        pop_tam = 50
        tx_mutacao = 0.02
        max_gen = 5000

    # Taxa de crossover automática para simplificar o código
    tx_crossover = 0.85 
    
    return palavra, pop_tam, tx_mutacao, max_gen, tx_crossover


# Cria uma palavra aleatória do mesmo tamanho do objetivo
def gerar_palavra_aleatoria(tamanho):
    return ''.join(random.choice(ALFABETO) for _ in range(tamanho))


# Mede quantos caracteres estão no lugar certo
def testar_nota(individuo, objetivo):
    nota = 0
    for i in range(len(individuo)):
        if individuo[i] == objetivo[i]:
            nota += 1
    return nota


# Escolha por roleta
def roleta(populacao, notas):
    soma_notas = sum(notas)
    if soma_notas == 0:
        return random.choice(populacao)

    sorteio = random.uniform(0, soma_notas)
    acumulado = 0
    for i in range(len(populacao)):
        acumulado += notas[i]
        if acumulado >= sorteio:
            return populacao[i]
    return populacao[-1]


# Cruza os caracteres de dois pais dividindo em um ponto de corte
def misturar_pais(p1, p2, tx_cross):
    if random.random() > tx_cross:
        return p1, p2

    ponto = random.randint(1, len(p1) - 1)
    f1 = p1[:ponto] + p2[ponto:]
    f2 = p2[:ponto] + p1[ponto:]
    return f1, f2


# Sorteia se cada letra vai mudar para uma aleatória do alfabeto
def aplicar_mutacao(individuo, tx_mut):
    letras = list(individuo)
    for i in range(len(letras)):
        if random.random() < tx_mut:
            letras[i] = random.choice(ALFABETO)
    return ''.join(letras)


# Começa o algoritmo genético principal
def executar_busca():
    # Carrega as configurações do input
    alvo, tam_pop, tx_mut, max_geracoes, tx_cross = ler_configuracoes()
    tam_cromossomo = len(alvo)

    # Cria a primeira lista de palavras aleatórias
    populacao = [gerar_palavra_aleatoria(tam_cromossomo) for _ in range(tam_pop)]
    
    print("\n" + "-" * 45)
    print(" PROCURANDO... POR FAVOR AGUARDE")
    print("-" * 45)

    for g in range(1, max_geracoes + 1):
        # Calcula as notas de todo mundo
        notas = [testar_nota(ind, alvo) for ind in populacao]
        
        melhor_nota = max(notas)
        media_nota = sum(notas) / tam_pop
        melhor_ind = populacao[notas.index(melhor_nota)]

        # Mostra o progresso no terminal a cada 100 gerações ou se achar a palavra
        if g == 1 or g % 100 == 0 or melhor_nota == tam_cromossomo:
            print(f"Ger {g:5d} | Nota: {melhor_nota}/{tam_cromossomo} | Média: {media_nota:.1f} | Texto: [{melhor_ind}]")

        # Verifica se o melhor indivíduo bateu 100% das letras do alvo
        if melhor_nota == tam_cromossomo:
            print(f"\n[✓] Sucesso total na geração {g}!")
            break

        # Elitismo básico: salva o melhor do ciclo direto na nova lista
        nova_pop = [melhor_ind]

        # Completa o restante da população gerando filhos
        while len(nova_pop) < tam_pop:
            pai = roleta(populacao, notas)
            mae = roleta(populacao, notas)

            f1, f2 = misturar_pais(pai, mae, tx_cross)

            f1 = aplicar_mutacao(f1, tx_mut)
            f2 = aplicar_mutacao(f2, tx_mut)

            nova_pop.append(f1)
            if len(nova_pop) < tam_pop:
                nova_pop.append(f2)

        populacao = nova_pop
    else:
        print(f"\n[!] O limite de {max_geracoes} gerações acabou antes de terminar.")


if __name__ == "__main__":
    executar_busca()