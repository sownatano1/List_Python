import os
import time

""""
[X] Editar item
    Alterar o nome de um item que já está na lista.

[ ] Salvar lista em arquivo
    Fazer os itens continuarem salvos mesmo depois de fechar o programa.

[X] Contador de itens
    Mostrar algo como: “Total de itens: 7”.

[ ] Sistema de múltiplas listas
    Uma lista para compras, outra para estudos, outra para projetos.

[ ] Modo rápido
    Adicionar vários itens de uma vez, sem precisar confirmar a cada item.

[ ] Exportar lista
    Gerar um arquivo .txt, .csv ou .json.

"""

lista = []
key = ""

def LimparConsole():
    os.system("cls" if os.name == "nt" else "clear") 

def Opcoes():
    print("-========== MENU ==========-")
    print("f = Criar ou deletar um fichário")
    print("a = Adicionar item na lista")
    print("m = Modificar um item da lista")
    print("l = Abrir a lista")
    print("r = Remover item da lista")
    print("e = Esvaziar a lista inteira")
    print("s = Sair")
    print("-==========================-")
    
def Lista():
    if lista:
        print("============ Lista ============")
        for indice, item in enumerate(lista, start=1):
            print(f"{indice}. {item}")
        print("===============================")
    else:
        print("============ Lista ============")
        print("             Vazia             ")
        print("===============================")

def Ficheiro():
    print("a")

def Adicionar():
    LimparConsole()
    while(True):
        itens = input("Digite o item para adicionar na lista: ")
        if itens.strip() == "":
            print("Não é possível ter um item vazio na lista")
        else:
            lista.append(itens)
            
        print("c = Continuar")
        print("enter = Voltar")
        key = input().lower()
        
        if key not in ["c", "a"]:
            break
        
        else:
            LimparConsole()
            
def Modificar():
    LimparConsole()
    while(True):
        if lista:
            Lista()
            try:
                num = int(input("Digite o número do item para editar: "))
                item = num - 1
                
                if item >= len(lista) or item < 0:
                    LimparConsole()
                    print("Item não encontrado")
                    time.sleep(1.5)
                
                else:
                    LimparConsole()
                    print(f"Editando o item '{lista[item]}'")
                    nome = input("Digite o novo nome para esse item: ")
                    if nome.strip() == "":
                        print("Não é possivel ter um item vazio na lista")    

                    else:
                        LimparConsole()
                        lista.pop(item)
                        lista.insert(item, nome)
                        Lista()
                    
                        print("c = Continuar modificando")
                        print("enter = Voltar")
                        key = input().lower()
                        
                        if key not in ["c", "m"]:
                            break
                        
                        else:
                            LimparConsole()
                            continue
            except ValueError:
                LimparConsole()
                print("Digite apenas o número do item da lista")
                time.sleep(2)
                break
        else:
            print("A lista está vazia")
            print("Não é possivel editar-la")
            time.sleep(1.5)
            break
            
def AbrirLista():
    LimparConsole()
    Lista()
    print(f"Total de itens: {len(lista)}")
    input("Pressione 'ENTER' para voltar para o menu")

def Remover():
    LimparConsole()
    while(True):
        if lista:
            Lista()
            try:
                item_num = int(input("Digite o número do item para ser removido: "))
                item = item_num - 1
                
                if item >= len(lista) or item < 0:
                    LimparConsole()
                    print("Item não encontrado")
                    time.sleep(1.5)
                
                else:
                    LimparConsole()
                    print(f"{lista[item]} foi removido(a) da lista")
                    lista.remove(lista[item])
                    time.sleep(1.5)
            
            except ValueError:
                LimparConsole()
                print("Digite apenas o número do item para ser removido")
                time.sleep(1.5)
                
            LimparConsole()
            print("        Itens restantes        ")
            Lista()
            print("c = Continuar removendo")
            print("enter = Voltar")
            key = input().lower()
            
            if key not in ["c", "r"]:
                break
            
            else:
                LimparConsole()
                continue
        else:
            print("Não é possível remover itens da lista")
            print("A lista está vazia")
            time.sleep(2)
            break
            
def Esvaziar():
    LimparConsole()
    Lista()
    print("Tem certeza que quer apagar a lista inteira?")
    print("s = Sim")
    print("n = Não (voltar)")
    
    key = input().lower()
    if (key == "s"):
        lista.clear()
        print("Lista apagada com sucesso")
        time.sleep(1)
        
    elif (key == "n"):
        print("Voltando...")
        time.sleep(1)
        
    else:
        print("Opção não encontrada!")
        time.sleep(1)
            
def Sair():
    LimparConsole()
    print("Saindo...")
    
while(True): 
    key = ""
    LimparConsole()
    Opcoes()
    key = input().lower()
        
    if (key == "a"):
        Adicionar()

    elif (key == "f"):
        Ficheiro()
        
    elif (key == "m"):
        Modificar()
        
    elif (key == "l"):
        AbrirLista()
        
    elif (key == "r"):
        Remover()
            
    elif (key == "e"):
        Esvaziar()
        
    elif (key == "s"):
        Sair()
        break
    
    else:
        print("Página não encontrada! Digite novamente.")
        time.sleep(1)
        continue