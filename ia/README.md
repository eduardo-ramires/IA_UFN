# Inteligência Artificial e Computação Evolutiva


### 
**Otimização Evolutiva para Descoberta de Textos**

Este script traz uma abordagem dinâmica e configurável de um Algoritmo Genético (AG) projetado para adivinhar uma string definida pelo usuário. Ao iniciar, o terminal solicita os seguintes parâmetros de controle:
- Termo ou frase oculta a ser descoberta
- Volume da população inicial
- Probabilidade de recombinação (Crossover entre 0 e 1)
- Probabilidade de alteração genética (Mutação entre 0 e 1)
- Limite de iterações (Gerações)

**Execução:**
```bash

Defina a palavra-alvo para o AG: INTELIGENCIA
Defina a população: 50
Taxa de Crossover [0-1]: 0.85
Taxa de Mutação [0-1]: 0.1
Total de gerações permitidas: 1000
Funcionalidades implementadas:

Menu interativo via console com tratamento de erros de digitação.

Codificação direta por meio de cadeias de caracteres (strings como cromossomos).

Cálculo de fitness (aptidão) baseado na contagem de caracteres idênticos nas posições corretas.

Compatibilidade com caracteres em caixa alta e espaçamentos.

Monitoramento em tempo real do desempenho a cada ciclo.

Critério de parada automático ao atingir a convergência exata.

Relatório final contendo métricas de evolução (desempenho médio e melhor indivíduo).

aula.py
Laboratório Prático de Algoritmo Genético (Baseado nos conceitos de Técnicas de IA - Prof. Alexandre Zamberlan)

Código-fonte estruturado para fins acadêmicos que ilustra o funcionamento de um AG clássico, cujo objetivo é resolver o problema de Maximização de Bits (One-Max).

Pilares Teóricos Abordados:
Codificação de Indivíduos: Cromossomos estruturados em vetores binários.

Métrica de Avaliação (Fitness): Score definido pela somatória de dígitos '1' presentes na cadeia.

Mecanismo de Seleção: Método da Roleta Viciada (proporcional ao desempenho).

Operador de Cruzamento: Recombinação de ponto único (Crossover de 1 ponto).

Operador de Mutação: Mutação por inversão de bits (bit-flip) para evitar convergência prematura.

Preservação de Genes: Estratégia de Elitismo para manter o melhor indivíduo no próximo ciclo.

Configuração Padrão do Experimento:
Comprimento do vetor: 16 bits

População total: 10 espécimes

Chance de crossover: 80%

Chance de mutação: 5%

Ciclo limite: 20 gerações

Meta: Obter a combinação ideal de 16 bits ligados (valor máximo)

Execução:
Bash
python aula.py
Resultados Exibidos:
O programa plota no terminal o histórico de cada iteração, detalhando a evolução da média da população e o melhor arranjo genético encontrado.

🧩 Casos de Estudo e Resolução de Problemas
Otimização de Vetores Binários (One-Max)

Aplicações práticas de AGs frequentemente enfrentam barreiras complexas, tais como:

Espaço de soluções altamente restritivo.

Ausência de pistas claras sobre a configuração do estado final.

Caminhos de otimização não lineares ou pouco evidentes.

Modelagem complexa da função de custo ou aptidão.

Necessidade de indicadores robustos para monitorar a evolução local.

Ajuste fino de operadores biológicos/genéticos conforme o cenário.
