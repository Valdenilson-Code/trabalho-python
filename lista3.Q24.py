#Lista 3 — Questão 24

#Um professor precisa desenvolver um pequeno sistema para acompanhar o desempenho de dez estudantes. Cada estudante realizou três avaliações, com os seguintes pesos:

# Avaliação 1: peso 3;
# Avaliação 2: peso 4;
# Avaliação 3: peso 3.

#Desenvolva um programa em Python que solicite, para cada estudante, seu nome e as notas obtidas nas três avaliações. O programa deverá calcular a média ponderada de cada estudante.

#Ao final, o programa deverá:

# exibir na tela o nome, as três notas e a média ponderada de cada estudante;
# identificar e exibir o estudante que obteve a maior média;
# salvar os dados de todos os estudantes em um arquivo chamado notas.cs comentários no código para deixar mais clara a função de cada parte, conforme foi solicitado na atividade.
import csv

# Lista para armazenar os dados dos estudantes
estudantes = []

# cadatro dos 10 estudantes
for i in range(10):
    nome = input("Digite o nome do estudante: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
 
    # Calcula a média poderada
    media = (nota1 * 3 + nota2 * 4 + nota3 * 3) / 10

    # Armazena os dados do estudante
    estudantes.append([nome, nota1, nota2, nota3, media])

# Identifica o estudante cpm maior média
maior_media = -1 
melhor_estudante = ""

for estudante in estudantes:
    if estudante[4] > maior_media:
        maior_media = estudante[4]
        melhor_estudante = estudante[0]

# Exibe os dados dos estudantes
for estudante in estudantes:
      print(f"nome: {estudante[0]} | nota 1: {estudante[1]} | nota 2: {estudante[2]} | nota 3: {estudante[3]} | média: {estudante[4]:.2f}")

# Exib o estudante com a maior média
print (f"\n Estudante com a maior média: {melhor_estudante}")
print (f"Maior média: {maior_media}:.2f")

#  Salva os dados  no arquivo notas.csv
with open("notas.csv", "w", newline ="") as arquivo:
    escritor = csv.writer(arquivo)

    # Cria o cabeçalho do arquivo
    escritor.writerow(["Nome","Nota 1","Nota 2", "Nota 3","Média"])

    # Salva os dados de cada estudantes
    for estudante in estudantes:
        escritor.writerow(estudante)