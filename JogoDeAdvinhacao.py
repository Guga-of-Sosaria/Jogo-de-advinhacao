from collections import deque
import time

#Classe que representará o nó
class Node:
    def __init__(self, question=None, answer=None):
        self.question = question
        self.answer = answer
        self.yes = None
        self.no = None

#Função para percorrer a árvore em dfs
def dfs(node):
    #Termina a função se não houver mais nenhum nó a ser percorrido
    if node is None:
        return
    
    #Printa o valor contido no nó
    print(node.question) if node.question != None else print(node.answer)
    #Percorre recursivamente o nó da esquerda (o nó "sim")
    dfs(node.yes)
    #Percorre recursivamente o nó da direita (o nó "não")
    dfs(node.no)

#Função para percorrer a árvore em bfs
def bfs(root):
    if root is None:
        return
    #Cria a fila de nós
    queue = deque([root])
    while queue:
        #Remove o nó da frente da fila
        node = queue.popleft()
        #Printa o valor contido no nó
        print(node.question) if node.question != None else print(node.answer)

        #Insere o nó da esquerda na fila
        if node.yes:
            queue.append(node.yes)
        #Insere o nó da direita na fila
        if node.no:
            queue.append(node.no)

#Função para rodar o jogo de advinhação
def RodarJogo(root):
    #Inicializa a variável currentNode para a raiz da árvore
    currentNode = root

    #O loop garante que o jogo rode até que uma resposta seja encorntrada
    #(nesse caso, um nó cujo o valor de answer não seja None)
    while currentNode.answer == None:
        #Faz a pergunta ao usuário
        userInput = None
        #Esse loop roda até o usuário fazer uma escolha válida
        while True: 
            userInput = input(f"{currentNode.question} (y/n)")
            if userInput.upper() == 'Y':
                #Se o usuário responder sim a pergunta, vai para o nó da esquerda  
                currentNode = currentNode.yes
                break
            elif userInput.upper() == 'N':
                #Caso o usuário responda não, vai para o nó da direita
                currentNode = currentNode.no
                break
            else:
                #Se o usuário responder com algo que não seja "y" ou "n",
                #exibe mensagem de erro
                print("Alternativa inválida!")
    #Printa a resposta ao usuário
    print(f"O seu pokémon é o {currentNode.answer}") 

#Montando a árvore
raiz = Node(question="O seu pokémon é do tipo elétrico?")
raiz.yes = Node(question="O seu pokémon é da região de Kanto?")
raiz.yes.yes = Node(answer="Pikachu")
raiz.yes.no = Node(answer="Rotom")
raiz.no = Node(question="O seu pokémon é um lendário?")
raiz.no.yes = Node(answer="Mewtwo")
raiz.no.no = Node(answer="Charizard")

#Roda o jogo de advinhação
RodarJogo(raiz)

print()

#Percorre a árvore com dfs e calcula o tempo de execução
print("=============PERCORRENDO A ÁRVORE COM O DFS...===================")
inicio = time.time()
dfs(raiz)
fim = time.time()
tempoDFS = fim - inicio
print("Pronto!")

print()

#Percorre a árvore com bfs e calcula o tempo de execução
print("=============PERCORRENDO A ÁRVORE COM O BFS...===================")
inicio = time.time()
bfs(raiz)
fim = time.time()
tempoBFS = fim - inicio
print("Pronto!")

#Mostra os tempos de execução de cada algorítimo
print(f"Tempo de execução do DFS: {tempoDFS}")
print(f"Tempo de execução do BFS: {tempoBFS}")
