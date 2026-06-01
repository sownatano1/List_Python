import os
import time
import json

#Para saber se o usuário está na lista
onList = False

#Modo rápido é usado para adicionar itens na lista sem precisar confirmar a cada item
#É possível escolher entre o modo normal e o modo rápido no menu principal
modoRapido = False
#Mensagem para mostrar se o modo rápido esta ativado ou desativado
modo = "Desativado"

#Carregar o ficheiro salvo no .json
def Carregar():
    try:
        #Abrir o arquivo .json para ler o seu conteúdo
        with open("Lista.json", mode="r", encoding="utf-8") as carregar:
            #Carregar o conteúdo do .json para o ficheiro
            return json.load(carregar)
    except FileNotFoundError:
        return {}

#Carregar o ficheiro ao entrar
ficheiro = Carregar()

#Função para salvar o ficheiro no .json
def Salvar():
    #Abrir o arquivo .json para escrever nele
    with open("Lista.json", mode="w", encoding="utf-8") as salvar:
        #Escrever tudo que estiver no ficheiro no arquivo .json
        json.dump(ficheiro, salvar, indent=4, ensure_ascii=False)

def LimparConsole():
    #Limpar o console usando comandos para diferentes sistemas
    os.system("cls" if os.name == "nt" else "clear") 

def Opcoes():
    print("-========== MENU ==========-")
    print("f = Criar um ficheiro")
    print("l = Abrir a lista\n ")
    if modoRapido:
        modo = "Ativado"
    else:
        modo = "Desativado"
    print(f"ar = Ativar/Desativar modo rápido [{modo}]")
    print("a = Adicionar item na lista")
    print("m = Modificar um item da lista\n ")
    print("r = Remover item da lista")
    print("d = Deletar lista do ficheiro")
    print("e = Esvaziar a lista inteira\n ")
    print("t = Gerar um arquivo .txt do ficheiro")
    print("s = Sair")
    print("-==========================-")
   
def Dicionario():
    if ficheiro:
        print("========== Ficheiro ===========")
        #Enumerar cada lista do ficheiro para deixar bonito e organizado
        for indice, item in enumerate(ficheiro, start=1):
            print(f"{indice}. {item}")
        print("===============================")
        if onList: 
            try:
                list_num = int(input("Digite o número da lista para abri-la: "))
                #Mostrar a lista pelo número digitado pelo usuário
                if (list_num > len(ficheiro) or list_num < 0):
                    LimparConsole()
                    print("Lista não encontrada")
                else:
                    LimparConsole()
                    Lista(list_num)
                input("Pressione 'ENTER' para voltar para o menu")
            except ValueError, IndexError:
                print("Digite apenas o número da lista para abri-la")
                time.sleep(1.5)
    else:
        print("========== Ficheiro ===========")
        print("             Vazio             ")
        print("===============================")
        if onList:
            input("Pressione 'ENTER' para voltar para o menu")

def Lista(lista_num):
    #Todos os nomes das listas que estão no ficheiro
    nomes_listas = list(ficheiro.keys())
    #Encontra e escolhe a lista pelo número dela usando o número digitado
    lista_escolhida = nomes_listas[lista_num - 1]
    
    #Mostrar a lista apenas quando tiver pelo menos 1 lista dentro dela
    if len(ficheiro[lista_escolhida]) > 0:
        print(f"Lista de '{lista_escolhida}'")
        print("============ Lista ============")
        #Enumerar cada item da lista para deixar bonito e organizado
        for indice, item in enumerate(ficheiro[lista_escolhida], start=1):
            print(f"{indice}. {item}")
        print("===============================")
        #Mostar o total de itens que contem na lista escolhida
        print(f"Total de itens: {len(ficheiro[lista_escolhida])}")
    else:
        print(f"Lista de '{lista_escolhida}'")
        print("============ Lista ============")
        print("             Vazia             ")
        print("===============================")

def Criarficheiro():
    LimparConsole()
    while(True):
        Dicionario()
        novo_ficheiro = input("Digite o nome da nova lista: ")
        #Evita lista com nomes vazios
        if novo_ficheiro.strip() == "":
            LimparConsole()
            print("Não é possível ter uma lista sem nome")
            time.sleep(1.5)
        #Evita listas com o mesmo nome
        elif novo_ficheiro in ficheiro:
            LimparConsole()
            print("Não é possível ter duas listas com o mesmo nome")
            time.sleep(1.5)
        #Caso esteja tudo certo a lista será criada
        else:
            LimparConsole()
            #Criando a lista dentro do ficheiro
            ficheiro[novo_ficheiro] = []
            Dicionario()
            Salvar()
            
        print("c = Continuar")
        print("enter = Voltar")
        key = input().lower()

        #Se o usuário escolher não continuar ele voltará para o menu principal
        if key not in ["c", "f"]:
            break

        else:
            LimparConsole()
            
def Adicionar():
    LimparConsole()
    while(True):
        Dicionario()
        try:
            lista_numero = int(input("Digite o número da lista para abri-la: "))
            LimparConsole()
            try:
                #Todos os nomes das lista dentro do ficheiro
                nomes_listas = list(ficheiro.keys())
                #Buscar a lista usando o numero que foi digitado
                nome_escolhido = nomes_listas[lista_numero - 1]
                
                #Caso o modo rapido não esteja ativado ele seguirá normalmente
                if modoRapido == False:
                    Lista(lista_numero)
                    itens = input(f"Digite o nome do item para adicionar na lista '{nome_escolhido}': ")
                    #Evitar items vazios na lista
                    if itens.strip() == "":
                        LimparConsole()
                        print("Não é possível ter um item vazio na lista")
                    else:
                        LimparConsole()
                        #Criar o item dentro da lista
                        ficheiro[nome_escolhido].append(itens)
                        Lista(lista_numero)
                        Salvar()
                        
                #Se o modo rápido estiver ativado
                else:
                    while(True):
                        LimparConsole()
                        Lista(lista_numero)
                        print(f"Digite o nome do item para adicionar na lista '{nome_escolhido}': ")
                        print("Para sair apenas aperte 'ENTER'")
                        itens = input()
                        #Item vazio é usado para o usuário sair do loop de adicionar itens
                        #Esse método é usado para o modo rápido para que o usário não tenho que confirmar sempre que adicionar um item
                        if itens.strip() == "":
                            break
                        else:
                            #Criar itens dentro da lista
                            ficheiro[nome_escolhido].append(itens)
                            Salvar()
                
                LimparConsole()
                print("c = Continuar")
                print("enter = Voltar")
                key = input().lower()
                
                if key not in ["c", "a"]:
                    break
                
                else:
                    LimparConsole()
            except ValueError, IndexError:
                print("Lista não encontrada")
                time.sleep(1)
        except ValueError, IndexError:
            print("Digite apenas o número da lista para abri-la")
            time.sleep(1.5)
            break

def Modificar():
    LimparConsole()
    while(True):
        if ficheiro:
            Dicionario()
            try:
                list_num = int(input("Digite o número da lista para abri-la: "))
                LimparConsole()
                nomes_listas = list(ficheiro.keys())
                lista_escolhida = nomes_listas[list_num - 1]
                Lista(list_num)
                try:
                    item_num = int(input("Digite o número do item para editar: "))
                    #A index do item é o numero do item menos 1
                    #(A lista dos itens começa no 1 porém a lista do python começa no 0)
                    item = item_num - 1
                    
                    #Usuário não encontra o item caso não exista o número do item na lista
                    if item >= len(ficheiro[lista_escolhida]) or item < 0:
                        LimparConsole()
                        print("Item não encontrado")
                        time.sleep(1.5)
                    
                    else:
                        LimparConsole()
                        print(f"Editando o item '{ficheiro[lista_escolhida][item]}'")
                        nome = input("Digite o novo nome para esse item: ")
                        #Evita que o novo nome seja vazio
                        if nome.strip() == "":
                            print("Não é possível ter um item vazio na lista")    

                        else:
                            LimparConsole()
                            
                            print(f"'{ficheiro[lista_escolhida][item]}' agora é '{nome}'")
                            #Substitui o nome antigo do item para o novo
                            ficheiro[lista_escolhida][item] = nome
                            Salvar()
                            print("c = Continuar modificando")
                            print("enter = Voltar")
                            key = input().lower()
                            
                            if key not in ["c", "m"]:
                                break
                            
                            else:
                                LimparConsole()
                                continue
                except ValueError, IndexError:
                    LimparConsole()
                    print("Digite apenas o número do item da lista")
                    time.sleep(2)
                    break
            except ValueError, IndexError:
                LimparConsole()
                print("Digite apenas o número da lista para abri-la")
                time.sleep(2)
                break
        else:
            print("A lista está vazia")
            print("Não é possível edita-la")
            time.sleep(1.5)
            break
            
def AbrirLista():
    LimparConsole()
    Dicionario()

def Remover():
    LimparConsole()
    while(True):
        if ficheiro:
            Dicionario()
            try:
                list_num = int(input("Digite o número da lista para abri-la: "))
                LimparConsole()
                Lista(list_num)
                try:
                    #Busca todos os nomes da lista
                    nomes_lista = list(ficheiro.keys())
                    #Escolhe a lista de acordo com o número digitado
                    lista_escolhida = nomes_lista[list_num - 1]
                    item_num = int(input("Digite o número do item para ser removido: "))
                    #Cálculo para pegar o item na lista correta
                    item = item_num - 1
                    
                    #Evita o erro de escolher o número de um item que não existe na lista
                    if item >= len(ficheiro[lista_escolhida]) or item < 0:
                        LimparConsole()
                        print("Item não encontrado")
                        time.sleep(1.5)
                        break
                    
                    else:
                        LimparConsole()
                        print(f"{ficheiro[lista_escolhida][item]} foi removido(a) da lista")
                        #Deleta o item na lista escolhida
                        del ficheiro[lista_escolhida][item]
                        Salvar()
                        time.sleep(1.5)
                
                except ValueError, IndexError:
                    LimparConsole()
                    print("Digite apenas o número do item para ser removido")
                    time.sleep(1.5)
                    break
                    
                LimparConsole()
                #Mostrar os itens restantes da lista
                print("Itens restantes na: ")
                Lista(list_num)
                print("c = Continuar removendo")
                print("enter = Voltar")
                key = input().lower()
                
                if key not in ["c", "r"]:
                    break
                
                else:
                    LimparConsole()
                    continue
                
            except ValueError, IndexError:
                LimparConsole()
                print("Digite apenas o número da lista para abri-la")
                time.sleep(2)
                break
        else:
            print("Não é possível remover itens da lista")
            print("A lista está vazia")
            time.sleep(2)
            break
            
def DeletarLista():
    LimparConsole()
    #Evitar de deletar a lista caso o ficheiro estiver vazio
    if len(ficheiro) == 0:
        print("Não tem nenhum lista para ser deletada")
        time.sleep(1)
    else:
        try:
            Dicionario()
            num_list = int(input("Digite o número da lista para deletar: "))
            #Encontra os nomes das listas que estão no ficheiro
            nomes_lista = list(ficheiro.keys())
            #Escolhe a lista com o número digitado
            lista_escolhida = nomes_lista[num_list - 1]
            #Evitar o erro de colocar um número da lista que não está no ficheiro
            if num_list > len(ficheiro) or num_list < 0:
                LimparConsole()
                print("Lista não encontrada")
                time.sleep(1.5)
            else:
                LimparConsole()
                print(f"Deletando a lista '{lista_escolhida}', confirmar?")
                print("s = Sim")
                print("n = Não (Voltar)")
                confirm = input().lower()
                if confirm == "s":
                    LimparConsole()
                    print(f"'{lista_escolhida}' foi deletado com sucesso!")
                    #Deletar a lista inteira do ficheiro
                    del ficheiro[lista_escolhida]
                    Salvar()
                    time.sleep(1.5)
                else:
                    print("Voltando...")
                    time.sleep(1)
        
        except ValueError, IndexError:
            print("Digite apenas o número da lista")
            time.sleep(1)
    
def Esvaziar():
    LimparConsole()
    Dicionario()
    try:
        num_list = int(input("Digite o número da lista para limpar: "))
        #Econtrar todos os nomes da lista que estiver no ficheiro
        nomes_lista = list(ficheiro.keys())
        #Buscar a lista escolhida pelo número digitado
        lista_escolhida = nomes_lista[num_list - 1]
        
        #Evitar o erro de buscar por uma lista usando um número que não existe no ficheiro
        if(num_list > len(ficheiro) or num_list < 0):
            LimparConsole()
            print("Lista não encontrada")
            time.sleep(1)
        else:
            LimparConsole()
            Lista(num_list)
            print(f"Tem certeza que quer esvaziar a lista '{lista_escolhida}' inteira?")
            print("s = Sim")
            print("n = Não (voltar)")

            key = input().lower()
            if (key == "s"):
                #Esvaziar a lista escolhida inteira
                ficheiro[lista_escolhida].clear()
                print("Lista esvaziada com sucesso")
                Salvar()
                time.sleep(1)
                
            else:
                print("Voltando...")
                time.sleep(1)
                
    except ValueError, IndexError:
        LimparConsole()
        print("Digite apenas o número da lista")
        time.sleep(1)

def GerarTxt():
    LimparConsole()
    try:
        #Cria um arquivo .txt
        with open("ficheiro.txt", mode="w", encoding="utf-8") as file:
            #Escreve e enumera cada item do ficheiro no arquivo .txt
            for key, itens in ficheiro.items():
                #A lista e o seus itens são escritos na mesma linha organizadamente
                file.write(f"{key}: {itens}\n")
                #Espaçamento depois da linha de cada lista
                file.write(" \n")
        print("Aquivo de texto criado com sucesso")
        time.sleep(1.5)
    except FileNotFoundError:
        print("Não é possivel criar o arquivo")
        time.sleep(1.5)

def Sair():
    LimparConsole()
    print("Saindo...")
    Salvar()

#Aqui é onde o usuário vai escolher para onde ir
while(True): 
    #Inserir aqui as letras das páginas para abrir
    key = ""
    LimparConsole()
    Opcoes()
    #Evitar letras maiúsculas
    key = input().lower()
        
    if (key == "a"):
        onList = False
        Adicionar()
        
    elif (key == "ar"):
        modoRapido = not modoRapido

    elif (key == "f"):
        onList = False
        Criarficheiro()
        
    elif (key == "m"):
        onList = False
        Modificar()
        
    elif (key == "l"):
        onList = True
        AbrirLista()
        
    elif (key == "r"):
        onList = False
        Remover()
        
    elif (key == "d"):
        onList = False
        DeletarLista()
            
    elif (key == "e"):
        onList = False
        Esvaziar()
    
    elif (key == "t"):
        onList = False
        GerarTxt()
        
    elif (key == "s"):
        Sair()
        break
    
    else:
        print("Página não encontrada! Digite novamente.")
        time.sleep(1)
        continue