#ARVORE BINÁRIA DE BUSCA.


#CLASSE NÓ
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.data)

#CLASSE ÁRVORE BINÁRIA     
class Btree:
    def __init__(self, data=None):
        if data:
            node = Node(data)
            self.root = node
        else:
            self.root = None
            
            
#PERCURSO PRE ORDEM //   
    def pre_ordem(self, node=None):
        if node is None:
            node = self.root
        print(node, end=' ')
        if node.left:
            self.pre_ordem(node.left)
        if node.right:
            self.pre_ordem(node.right)

#PERCURSO EM ORDEM // DA ESQUERDA PRA DIREITA
    def em_ordem_trav(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.em_ordem_trav(node.left)
        print(node, end=' ')
        if node.right:
            self.em_ordem_trav(node.right)
            
#PERCURSO DE PÓS ORDEM // DA ULTIMA FOLHA PARA RAIZ (ESQUERDA PARA DIREITA)
    def pos_ordem(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.pos_ordem(node.left)
        if node.right:
            self.pos_ordem(node.right)
        print(node, end=' ')
        
#PERCURSO PARA ALTURA // PERCORRE PELO NÓ PARA SABER A ALTURA DA ARVORE
    def height(self, node=None):
        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)
        if hright > hleft:
            return hright + 1
        return hleft + 1


#CLASSE BUSCA NA ÁRVORE BINÁRIA.
class Binarysearchtree(Btree):
    def insert(self, value):
        parent = None
        x = self.root
        while(x):
            parent = x
            if value < x.data:
                x = x.left
            else:
                x = x.right
        if parent is None:
            self.root = Node(value)
        elif value < parent.value:
            parent.left = Node(value)
        else:
            parent.right = Node(value)
    

    
if __name__ == "__main__":
    tree = Btree()
    
    n1 = Node('B')
    n2 = Node('E')
    n3 = Node('A')
    n4 = Node('T')
    n5 = Node('R')
    n6 = Node('I')
    n7 = Node('C')
    n8 = Node('Y')

    n8.left = n6 
    n8.right = n7 
    n6.left = n4 
    n6.right = n5 
    n4.left = n3 
    n3.left = n1 
    n3.right = n2
    tree.root = n8 #RAIZ
    
    
    tree.pos_ordem()
    print('<----- POS ORDEM')
    tree.em_ordem_trav()
    print('<----- EM ORDEM')
    tree.pre_ordem()
    print('<----- PRE ORDEM')
    print('altura: ',tree.height())
    