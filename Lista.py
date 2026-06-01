import os
import time
import json

"""
[X] Editar item
    Alterar o nome de um item que já está na lista.

[X] Salvar lista em arquivo
    Fazer os itens continuarem salvos mesmo depois de fechar o programa.

[X] Contador de itens
    Mostrar algo como: “Total de itens: 7”.

[X] Sistema de múltiplas listas
    Uma lista para compras, outra para estudos, outra para projetos.

[X] Modo rápido
    Adicionar vários itens de uma vez, sem precisar confirmar a cada item.

[ ] Exportar lista
    Gerar um arquivo .txt, .csv ou .json.
"""

onList = False
modoRapido = False

modo = "Desativado"

def Carregar():
    try:
        with open("Lista.json", mode="r", encoding="utf-8") as carregar:
            return json.load(carregar)
    except FileNotFoundError:
        return {}
    
ficheiro = Carregar()

def Salvar():
    with open("Lista.json", mode="w", encoding="utf-8") as salvar:
        json.dump(ficheiro, salvar, indent=4, ensure_ascii=False)

def LimparConsole():
    os.system("cls" if os.name == "nt" else "clear") 

def Opcoes():
    print("-========== MENU ==========-")
    print("f = Criar um ficheiro")
    print("l = Abrir a lista")
    print("")
    if modoRapido:
        modo = "Ativado"
    else:
        modo = "Desativado"
    print(f"ar = Ativar/Desativar modo rápido [{modo}]")
    print("a = Adicionar item na lista")
    print("m = Modificar um item da lista")
    print("")
    print("r = Remover item da lista")
    print("d = Deletar lista do ficheiro")
    print("e = Esvaziar a lista inteira")
    print("")
    print("s = Sair")
    print("-==========================-")
    
def Dicionario():
    if ficheiro:
        print("========== Ficheiro ===========")
        for indice, item in enumerate(ficheiro, start=1):
            print(f"{indice}. {item}")
        print("===============================")
        if onList: 
            try:
                key_lista = int(input("Digite o número da lista para abri-la: "))
                if (key_lista > len(ficheiro) or key_lista < 0):
                    LimparConsole()
                    print("Lista não encontrada")
                else:
                    LimparConsole()
                    Lista(key_lista)
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
    nomes_listas = list(ficheiro.keys())
    lista_escolhida = nomes_listas[lista_num - 1]
    
    if len(ficheiro[lista_escolhida]) > 0:
        print(f"Lista de '{lista_escolhida}'")
        print("============ Lista ============")
        for indice, item in enumerate(ficheiro[lista_escolhida], start=1):
            print(f"{indice}. {item}")
        print("===============================")
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
        if novo_ficheiro.strip() == "":
            LimparConsole()
            print("Não é possível ter uma lista sem nome")
            time.sleep(1.5)
        elif novo_ficheiro in ficheiro:
            LimparConsole()
            print("Não é possível ter duas listas com o mesmo nome")
            time.sleep(1.5)
        else:
            LimparConsole()
            ficheiro[novo_ficheiro] = []
            Dicionario()
            Salvar()
            
        print("c = Continuar")
        print("enter = Voltar")
        key = input().lower()

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
                nomes_listas = list(ficheiro.keys())
                nome_escolhido = nomes_listas[lista_numero - 1]
                if modoRapido == False:
                    Lista(lista_numero)
                    itens = input(f"Digite o nome do item para adicionar na lista '{nome_escolhido}': ")
                    if itens.strip() == "":
                        LimparConsole()
                        print("Não é possível ter um item vazio na lista")
                    else:
                        LimparConsole()
                        ficheiro[nome_escolhido].append(itens)
                        Lista(lista_numero)
                        Salvar()
                else:
                    while(True):
                        LimparConsole()
                        Lista(lista_numero)
                        print(f"Digite o nome do item para adicionar na lista '{nome_escolhido}': ")
                        print("Para sair apenas aperte 'ENTER'")
                        itens = input()
                        if itens.strip() == "":
                            break
                        else:
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
                key_lista = int(input("Digite o número da lista para abri-la: "))
                LimparConsole()
                nomes_listas = list(ficheiro.keys())
                lista_escolhida = nomes_listas[key_lista - 1]
                Lista(key_lista)
                try:
                    num = int(input("Digite o número do item para editar: "))
                    item = num - 1
                    
                    if item >= len(ficheiro[lista_escolhida]) or item < 0:
                        LimparConsole()
                        print("Item não encontrado")
                        time.sleep(1.5)
                    
                    else:
                        LimparConsole()
                        print(f"Editando o item '{ficheiro[lista_escolhida][item]}'")
                        nome = input("Digite o novo nome para esse item: ")
                        if nome.strip() == "":
                            print("Não é possível ter um item vazio na lista")    

                        else:
                            LimparConsole()
                            
                            print(f"'{ficheiro[lista_escolhida][item]}' agora é '{nome}'")
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
                key_lista = int(input("Digite o número da lista para abri-la: "))
                LimparConsole()
                Lista(key_lista)
                try:
                    nomes_lista = list(ficheiro.keys())
                    lista_escolhida = nomes_lista[key_lista - 1]
                    item_num = int(input("Digite o número do item para ser removido: "))
                    item = item_num - 1
                    
                    if item >= len(ficheiro[lista_escolhida]) or item < 0:
                        LimparConsole()
                        print("Item não encontrado")
                        time.sleep(1.5)
                        break
                    
                    else:
                        LimparConsole()
                        print(f"{ficheiro[lista_escolhida][item]} foi removido(a) da lista")
                        del ficheiro[lista_escolhida][item]
                        Salvar()
                        time.sleep(1.5)
                
                except ValueError, IndexError:
                    LimparConsole()
                    print("Digite apenas o número do item para ser removido")
                    time.sleep(1.5)
                    break
                    
                LimparConsole()
                print("Itens restantes na: ")
                Lista(key_lista)
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
    if len(ficheiro) == 0:
        print("Não tem nenhum lista para ser deletada")
        time.sleep(1)
    else:
        try:
            Dicionario()
            num_list = int(input("Digite o número da lista para deletar: "))
            nomes_lista = list(ficheiro.keys())
            lista_escolhida = nomes_lista[num_list - 1]
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
        nomes_lista = list(ficheiro.keys())
        lista_escolhida = nomes_lista[num_list - 1]
        
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
                
def Sair():
    LimparConsole()
    print("Saindo...")
    Salvar()
    
while(True): 
    key = ""
    LimparConsole()
    Opcoes()
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
        
    elif (key == "s"):
        Sair()
        break
    
    else:
        print("Página não encontrada! Digite novamente.")
        time.sleep(1)
        continue