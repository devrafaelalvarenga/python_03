# Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir
# que todos os registros tenham valores positivos para `quantidade` e `preço`.
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos
# forem positivos ou "Dados inválidos" caso contrário.

import re
quantidade: float = 100
preco: float = 20

if quantidade > 0 and preco > 0:
    print('Dados válidos')
else:
    print('Dados invalids')


# Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT.
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'

temperatura: float = 34

if temperatura < 18:
    print('Temperatura baixa')
elif temperatura >= 18 and temperatura <= 26:
    print('Temperatura normal')
else:
    print('Temperatura alta')


# Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`,
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

log = {'timestamp': '2021-06-23 10:00:00',
       'level': 'ERROR', 'message': 'Falha na conexão'}

for k, v in log.items():
    if k == 'level' and v == 'ERROR':
        print(f'{log["timestamp"]} | {log["message"]}')

# opcao2
if log['level'] == 'ERROR':
    print(f'{log["timestamp"]} | {log["message"]}')

# Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação,
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha
# fornecido um email válido. Escreva um programa que valide essas condições
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

email_usuario = input('Informe seu email: ')
idade_usuario = int(input('Informe sua idade: '))

if "@" not in email_usuario or "." not in email_usuario:
    print("Email inválido")
    exit()
elif idade_usuario < 18 or idade_usuario > 65:
    print('Idade invalida')
    exit()
else:
    print('Dados validos')


# Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h).
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

transacao = {'valor': 12000, 'hora': 20}

# or (transacao['hora'] < 9 or transacao['hora'] > 18):
if transacao['valor'] > 100:
    print(f'Transação suspeita. Valor transação: R${transacao["valor"]:.2f} ')
if transacao['hora'] < 9 or transacao['hora'] > 18:
    print('Transação suspeita. Fora do horário comercial.')


# Exercícios com FOR

# Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

texto = 'O Senhor tem muitos filhos muitos filhos ele tem'
palavras = texto.split(' ')
contagem_de_palavras = {}

for palavra in palavras:
    if palavra in contagem_de_palavras:
        contagem_de_palavras[palavra] += 1
    else:
        contagem_de_palavras[palavra] = 1

print(contagem_de_palavras)

# opcao2
texto = "Você atingirá o sucesso sucesso quando apresentar com orgulho as cicatrizes que adquiriu ao longo da sua jornada."
lista_palavras = []

for palavra in texto.split():
    # se existe a palavra na lista nao faz nada
    if palavra in lista_palavras:
        pass
    # adiciona se nao existir
    else:
        lista_palavras.append(palavra)

contagem_palavras = len(lista_palavras)
print(f'A frase tem {contagem_palavras} palavras')


# opcao3

texto = "Você atingirá o sucesso,, sucesso quando apresentar com orgulho as cicatrizes que adquiriu ao longo da sua jornada!@."

# formata texto excluindo caracteres (pontuação)
texto_formatado = re.sub(r'[^\w\s]', '', texto).split()
contagem_palavras = {}

for palavra in texto_formatado:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1
print(contagem_palavras)

# Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

numeros = [10, 20, 30, 40, 50]
minimo = min(numeros)
print(minimo)
maximo = max(numeros)
print(maximo)
normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

print(normalizados)

# Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

# {"nome": "Alice", "email": "alice@example.com"},
# {"nome": "Bob", "email": ""},
# {"nome": "Carol", "email": "carol@example.com"}

usuarios = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"}
]

for usuario in usuarios:
    if not usuario['email']:
        print(usuario)

# opcao2
usuarios = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"}
]

usuarios_validos = [usuario for usuario in usuarios if not usuario["email"]]
print(usuarios_validos)

# Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

numeros = [1, 2, 3, 4, 5, 6, 67, 68, 79, 80, 99, 86]

for numero in numeros:
    if numero % 2 == 0:
        print(numero)

# opcao2
numeros = [1, 2, 3, 4, 5, 6, 67, 68, 79, 80, 99, 86]

numeros_pares = [x for x in numeros if x % 2 == 0]
print(numeros_pares)

# Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800},
    {"categoria": "perifericos", "valor": 350}
]

valor_total_venda_por_categoria = {}

for itens in vendas:
    categoria = itens['categoria']
    valor = itens['valor']
    if categoria in valor_total_venda_por_categoria:
        valor_total_venda_por_categoria += valor
    else:
        valor_total_venda_por_categoria = valor

print(valor_total_venda_por_categoria)

# Exercícios com WHILE

# Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

dados_usuario = input(
    'Digite algum dado para ser guardado ou digite "SAIR" para abortar a operação: ')
dados_armazenados = []

while dados_usuario != 'SAIR':
    dados_armazenados.append(dados_usuario)
    dados_usuario = input(
        'Digite algum dado para ser guardado ou digite "SAIR" para abortar a operação: ')
    if dados_usuario == 'SAIR':
        print('Operação abortada')
        print(f'Dados armazenados: {dados_armazenados}')

#
# Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

numero_usuario = int(input('Digite um numero de 1 a 100: '))

while numero_usuario in range(1, 101):
    numero_usuario = int(input('Digite um numero de 1 a 100: '))
    if numero_usuario not in range(1, 101):
        print('Numero digitado fora do intervalo solicitado')

# Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.


# Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

# Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.
