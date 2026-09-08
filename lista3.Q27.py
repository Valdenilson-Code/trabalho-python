#Uma instituição deseja desenvolver uma pequena agenda para armazenar informações de servidores e colaboradores. Para cada pessoa, deverão ser cadastrados os seguintes dados:

#* nome;
#* endereço;
#* DD;
#* telefone.

#Desenvolva um programa em Python que permita cadastrar os contatos da instituição. Após cada cadastro, o programa deverá perguntar ao usuário se deseja cadastrar uma nova pessoa. Quando o cadastro for encerrado, o programa deverá:

#* exibir todos os contatos cadastrados;
#* salvar os dados em um arquivo chamado agenda.txt;
#* solicitar ao usuário o nome de uma pessoa para pesquisa;
#* caso o nome seja encontrado, apresentar o DD e o telefone correspondentes;
#* caso não exista um cadastro com o nome informado, exibir a mensagem “Contato não encontrado”.

#Os dados deverão ser armazenados no arquivo agenda.txt de forma organizada

# Lista que armazena os contatos
contatos = []

#Controla a realização de novos cadastros
continuar ="s"

while continuar == "s":
    # Solicita os dados do contatos
     nome = input ("Digite o nome: ")
     endereço = input ("Digite o endereço: ")
     dd = input ("Digite o DD: ")
     telefone = input ("Digite o telefone: ")
    
    #cria e armazena  o contatos
     contato = [nome, endereço, dd, telefone]
     contatos.append(contato)
    
    #pergunta se deseja cadastrar outra pessoa
     continuar = input ("Deseja cadastrar outra pessoa? (s/n): ").lower()

# exibe todos os contatos  cadastrados
print ("\n Contatos cadastrados:")


for contato in contatos: 
    print (f"nome: {contato[0]}")
    print (f"Endereço: {contato[1]}")
    print (f"DD: {contato[2]}")
    print (f"Telefone: {contato[3]}")

    print("_" * 30)

#salva os contatos no arquivo agenda.txt
with open ("agenda.txt", "w") as arquivo:
    for contato in contatos:
        arquivo.write(f"nome : {contato[0]}\n")
        arquivo.write(f"Endereço: {contato[1]}\n")
        arquivo.write(f"DD: {contato[2]}\n")
        arquivo.write(f"Telefone: {contato[3]}\n")
        arquivo.write("_" * 30 + "\n")

# solicita um nome para pesquisa
nome_pesquisa = input("\nDigite o nome para pesquisar: ")

#controla se o contato foi encontrado
encontrado = False

# procura o contato pelo nome 
for contato in contatos:
    if contato[0].lower() == nome_pesquisa.lower():
        print(f"DD: {contato[2]}")
        print(f"Telefone: {contato[3]}")
        encontrado = True 
        break

# Informa caso o contato não seja encontrado
if not encontrado:
    print ("contato não encontrado")